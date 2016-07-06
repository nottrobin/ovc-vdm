# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Option, Command
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.sql import exists
from sqlalchemy import or_, exc
from mapper import Mapper
import email.utils as eut
import datetime
from datetime import timedelta, date
import requests
import os
import json
from models import *
import re
from urlparse import urlparse
import ast
import gc
from app import app, db
import time
from utils import send_mail
import sendgrid

from flask.ext.cache import Cache

cache = Cache()


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)



manager.add_command('db', MigrateCommand)


@manager.command
def flush_releases():
    #TODO: APPLIQUER CASCADE LORS DE LA CREATION DES RELEASES
    try:
        db.session.query(Release).delete() 
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        send_mail("SQLAlchemy error during operation flush_releases", repr(e))


@manager.command
def test_emails():

    send_mail("Test send mail function", "This is a test!")

@manager.command
def update_sources():
    #TODO : Delete sources that have been removed from config
    #TODO : Mettre un parametre --force pour forcer la mise a jour des données quoiqu'il arrive.

    start = datetime.now() 
    try:
        for config_source in  app.config["DATA_SOURCES"]:
            db_source =  db.session.query(Source).filter(Source.url == config_source["url"]).scalar()
            if db_source == None:
                db_source = Source(config_source) 
                db.session.add(db_source) 
            else:
                db_source.name = config_source["name"]
                db_source.mapper = config_source["mapper"]
                db_source.type = config_source["type"]
            db_source.last_update =  start.strftime("%Y-%m-%d %H:%M:%S")
            db.session.commit()

        db.session.query(Source).filter(Source.last_update < start - timedelta(minutes=15)).delete()
        db.session.commit()


    except exc.SQLAlchemyError as e:  
        db.session.rollback()
        send_mail("SQLAlchemy error during operation update_sources", repr(e))


def compute_supplier_size():
    
    records = db.session.query(Release.supplier_id.label('supplier_id'), func.sum(Release.value).label('total_value'))      
    records = records.group_by('1')

    for r in records:
        record = r._asdict()
        size = 1

        #Assign supplier to the correct bucket
        for i, val in enumerate(app.config["SUPPLIER_SIZE"]):
            if record["total_value"] >= val:
                size = i + 1

        supplier = db.session.query(Supplier).filter(Supplier.id == record["supplier_id"]).one()
        supplier.size = size


    db.session.commit()


@manager.command
def update_releases(forced=False):
    '''Uses the sources list in DB to search for contracts'''
    sources =  db.session.query(Source).all()
    updated_sources = 0

    for source in sources:
        print source.url
        if re.match("^http", source.url):
            #TODO: With the fixture we are not testing this part which is fairly sensitive
            r = requests.head(source.url)

            #If Last-Modified not avaiable, we always process
            now = datetime.now()
            source_update = now
            if 'Last-Modified' in r.headers:
                source_update = datetime(*eut.parsedate(r.headers['Last-Modified'])[:6])

            if forced or source_update >= source.last_retrieve :
                load_source(source)
                updated_sources += 1
        else:
            load_source(source)
            updated_sources += 1

    if updated_sources > 0:
        compute_supplier_size()

    #Let's flush the cache
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})
    with app.app_context():
        cache.clear()

       

@manager.command
def load_source(source, action='load'):


    if source != None:
        db.session.query(Release).filter(Release.source_id == source.id).delete() 

    error_hash = {}
    mapper = Mapper(source)
    for release, error in  mapper.to_ocds():
        if error != None:
            if error[0] not in error_hash:
                error_hash[error[0]] = []
            error_hash[error[0]].append(error[1])
        else:
            load_ocds(release, type='dict', source=source)


    if len(error_hash) > 0:
        message = "Erreurs lors du chargement du fichier %s \n\n" % (source.url)
        message += "\n".join(["Erreur: %s pour les lignes: %s" % (error_type, lines) for error_type, lines in error_hash.items()])

        send_mail("Vue sur les contrats - Error when loading file", message)    

    else: 

        send_mail("Vue sur les contrats - Succès du chargement du fichier : %s" % (source.url), "")

    source.last_retrieve = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.session.commit()


        
@manager.command
def load_ocds(release, type='path', source=None):

    try:

        the_release= Release(release)
        
        the_release.source_id = source.id

        the_buyer =  db.session.query(Buyer).filter(Buyer.name== release["buyer"]["name"]).scalar()
        if the_buyer == None:
            the_buyer = Buyer(release["buyer"]) 
            db.session.add(the_buyer)
            db.session.flush()     

        the_supplier =  db.session.query(Supplier).filter(Supplier.slug == slugify(release["awards"][0]["suppliers"][0]["name"], to_lower=True)).scalar()
        if the_supplier == None:
            the_supplier = Supplier(release["awards"][0]["suppliers"][0]) 
            db.session.add(the_supplier)
            db.session.flush()
    

        the_release.supplier_id = the_supplier.id

        the_release.buyer_id = the_buyer.id
        db.session.add(the_release)

        
        db.session.flush()
        


    except exc.SQLAlchemyError as e:  
        #If we have a SQLAlchemy error here, we can assume it's serious so we rollback...
        db.session.rollback()
        send_mail("SQLAlchemy error during operation load_ocds", repr(e))


@manager.command
def generate_stats():

    total = 0
    from_app = 0
    path = dict()
    args = dict()
    referrers = dict()

    today = date.today( )
    today_midnight = str(today) + " 00:00:00"
    yesterday = today - timedelta(days=1)
    yesterday_midnight = str(yesterday) + " 00:00:00"

    dailies =  db.session.query(DailyStat).filter(DailyStat.datetime >= yesterday_midnight).filter(DailyStat.datetime < today_midnight)

    for daily in dailies:

        total += 1

        if daily.path not in path:
            path[daily.path] = 0
        path[daily.path] += 1

        if daily.referrer != None:
            parsed_uri = urlparse(daily.referrer)
            domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)

            if domain ==  app.config['URL_ROOT']:
                from_app += 1
            else:
                if daily.referrer not in referrers:
                    referrers[daily.referrer] = 0
                referrers[daily.referrer] += 1

        for (key, value) in daily.args.iteritems():
            if key not in args:
                args[key] = dict()
            if value not in args[key]:
                args[key][value] = 0

            args[key][value] += 1

    stat = Stat()

    stat.date = yesterday
    stat.total_counts = total
    stat.referrers = referrers
    stat.counts_app = from_app
    stat.path = path
    stat.args =  args


    try:
        db.session.add(stat)
        db.session.commit()
    except exc.SQLAlchemyError as e:  
        db.session.rollback()
        send_mail("SQLAlchemy error during operation generate_stats", repr(e))        



@manager.command
def send_stats(delta_days = 31):
    daily_stats = db.session.query(Stat).filter(Stat.date >= (datetime.today() - timedelta(days=delta_days)))

    msg = 'Date\t\tTotal\tVenant de l\'application\n'
    for stat in daily_stats:
        msg += "%s\t%s\t%s\n" % (stat.date, stat.total_counts, stat.counts_app)

    send_mail("OVC - Statistiques API", msg)


 

if __name__ == '__main__':
    manager.run()
