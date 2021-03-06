# -*- coding: utf-8 -*-
import collections
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SENDMAIL = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    if 'EMAIL_CREDENTIALS' in os.environ:
        EMAIL_CREDENTIALS = os.environ['EMAIL_CREDENTIALS']
    
    SMTP_SERVER = 'smtp.sendgrid.net'
    EMAIL_SENDER = 'envoidemasse@ville.montreal.qc.ca'
    ADMINS = ['donneesouvertes@ville.montreal.qc.ca']

    URL_ROOT = 'http//localhost'
    OCID_PREFIX = 'ocds-a1234567-mt-'

    CACHE_DURATION = 86400
    STATS_LOG = 'stats/log.out'

    FTS_LANG = 'french'
    START_HIGHLIGHT = "<em>"
    END_HIGHLIGHT = "</em>"

    DATA_SOURCES = [
        {
            'name': 'Fonctionnaires',
            'mapper': 'field_mapper_fonc_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv',
            'type': 'contract'
        }, 
        {
            'name': 'Conseil municipal',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/5cf0220b-c149-43c4-ac23-758c55648584/resource/1e5ab066-f560-4b4f-8f12-991de39df134/download/contratsconseilmunicipal.csv',
            'type': 'contract'
        },
        {
            'name': 'Comité exécutif',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/72083af8-83f8-41c1-823b-1cae5e76ff9a/resource/4b2d8744-a257-4102-8897-95a30a20de34/download/contratscomiteexecutif.csv',
            'type': 'contract'
        },        
        {
            'name': 'Conseil d\'agglomération',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/5cf0220b-c149-43c4-ac23-758c55648584/resource/7cf955d0-a3e6-4e94-8c24-9b0a4f7c0408/download/contratsconseilagglomeration.csv',
            'type': 'contract'
        },
        {
            'name': 'Conseil municipal',
            'mapper': 'field_mapper_subvention_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/c792de47-9cc2-4d91-ba66-ca8d2b8d74ab/resource/ee49851f-0e05-4311-be89-93dca5202f0f/download/subventionsconseilmunicipal.csv',
            'type': 'subvention'
        },
        {
            'name': 'Conseil d\'agglomération',
            'mapper': 'field_mapper_subvention_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/c792de47-9cc2-4d91-ba66-ca8d2b8d74ab/resource/81d15b7e-df33-47ec-9515-bb0eff10b0a7/download/subventionsconseilagglomeration.csv',
            'type': 'subvention'
        },                
        {
            'name': 'Comité exécutif',
            'mapper': 'field_mapper_subvention_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/f85037d6-e443-436c-9411-4c9fc41409ab/resource/2a8befdf-57c5-40ef-a0a6-ba38777ed131/download/subventionscomiteexecutif.csv',
            'type': 'subvention'
        },        
    ]

    SUPPLIER_SIZE = [0, 1000000, 10000000]

    AGG_ACTIVITIES = 4


    ACTIVITY_COLOR_CODE = collections.OrderedDict([
        ("Arrondissements", "#DDA2A2"),
        ("Communications et relations publiques", "#A8657E"),
        ("Développement économique", "#A165A9"),
        ("Environnement", "#61BFC8"),
        ("Foncier", "#B6A2CE"),
        ("Gestion de l'information" , "#E1C6A0"),
        ("Immeubles et terrains" , "#DFB2A1"),
        ("Infrastructures" , "#33577B"),
        ("Juridique", "#7264AC"),
        ("Organisation et administration" , "#3884AF"),
        ("Ressources financières", "#619CC6"),
        ("Ressources humaines", "#637EBE"),
        ("Ressources matérielles et services", "#A2B1CC"),
        ("Sécurité publique", "#B6A2CE"),
        ("Sports, loisirs, culture et développement social" , "#7DBB92"),
        ("Transport" , "#57A9B7"),
        ("Urbanisme et habitation", "#A2CBCB"),        
        ("Autres" , "#E3D7A0")

    ])

    SERVICE_TO_ACTIVITY = {
        # NO SEMI_COLUMN - PAS DE POINT-VIRGULE
        "ARRONDISSEMENT DE VILLERAY-SAINT-MICHEL-PARC-EXTENSION" : ["Arrondissements"],
        "ARRONDISSEMENT DE VILLE-MARIE": ["Arrondissements"],
        "ARRONDISSEMENT DE MONTRÉAL-NORD": ["Arrondissements"],
        "ARRONDISSEMENT DE MERCIER-HOCHELAGA-MAISONNEUVE": ["Arrondissements"],
        "ARRONDISSEMENT DE L’ÎLE-BIZARD–STE-GENEVIÈVE": ["Arrondissements"],
        "ARRONDISSEMENT DE LASALLE": ["Arrondissements"],
        "ARRONDISSEMENT DE LACHINE": ["Arrondissements"],
        "ARRONDISSEMENT DE SAINT-LAURENT": ["Arrondissements"],
        "ARRONDISSEMENT DE SAINT-LÉONARD": ["Arrondissements"],
        "ARRONDISSEMENT DE ROSEMONT-LA PETITE-PATRIE": ["Arrondissements"],
        "ARRONDISSEMENT DU PLATEAU-MONT-ROYAL": ["Arrondissements"],
        "ARRONDISSEMENT DE PIERREFONDS-ROXBORO": ["Arrondissements"],
        "ARRONDISSEMENT D'OUTREMONT": ["Arrondissements"],
        "ARRONDISSEMENT DU SUD-OUEST": ["Arrondissements"],
        "ARRONDISSEMENT DE RIVIÈRE-DES-PRAIRIES–POINTE-AUX-TREMBLES": ["Arrondissements"],
        "ARRONDISSEMENT DE CÔTE-DES-NEIGES - NOTRE-DAME-DE-GRÂCE": ["Arrondissements"],
        "ARRONDISSEMENT D'AHUNTSIC-CARTIERVILLE": ["Arrondissements"],
        "ARRONDISSEMENT D'ANJOU": ["Arrondissements"],
        "ARRONDISSEMENT DE VERDUN": ["Arrondissements"],
        "BUREAU DE L’OMBUDSMAN" :["Organisation et administration"],
        "BUREAU DU VÉRIFICATEUR GÉNÉRAL" :["Organisation et administration"],
        "BUREAU DE L'INSPECTEUR GÉNÉRAL" :["Organisation et administration"],
        "BUREAU DE LA VILLE INTELLIGENTE ET NUMÉRIQUE": ["Organisation et administration"],
        "COMMISSION DES SERVICES ÉLECTRIQUES DE MONTRÉAL" : ["Organisation et administration"],
        "COMMISSION DE LA FONCTION PUBLIQUE DE MONTRÉAL": ["Organisation et administration"],
        "DIRECTION GÉNÉRALE" : ["Organisation et administration"],
        "SERVICE DE LA MISE EN VALEUR DU TERRITOIRE" : ["Urbanisme et habitation"],
        "SERVICE DU DÉVELOPPEMENT ÉCONOMIQUE" : ["Développement économique"],
        "SERVICE DU MATÉRIEL ROULANT ET DES ATELIERS" : ["Ressources matérielles et services"],
        "SERVICE DES TECHNOLOGIES DE L'INFORMATION" : ["Gestion de l'information"],
        "SERVICE DES RESSOURCES HUMAINES" : ["Ressources humaines"],
        "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT-ROYAL": ["Sports, loisirs, culture et développement social"],
        "SERVICE DES ESPACES POUR LA VIE":  ["Sports, loisirs, culture et développement social"],
        "SERVICE DES AFFAIRES JURIDIQUES ET DE L'ÉVALUATION FONCIÈRE" : ["Juridique", "Foncier"],
        "SERVICE DE POLICE DE LA VILLE DE MONTRÉAL": ["Sécurité publique"],
        "SERVICE DE L'EAU" : ["Infrastructures"],
        "SERVICE DES INFRASTRUCTURES, DE LA VOIRIE ET DES TRANSPORTS" : ["Infrastructures"],
        "SERVICE DE LA GESTION ET DE LA PLANIFICATION IMMOBILIÈRE": ["Immeubles et terrains"],
        "SERVICE DE LA DIVERSITÉ SOCIALE ET DES SPORTS": ["Sports, loisirs, culture et développement social"],
        "SERVICE DE LA CONCERTATION DES ARRONDISSEMENTS ET RESSOURCES MATÉRIELLES": ["Organisation et administration"],
        "SERVICE DE L'APPROVISIONNEMENT" : ["Ressources matérielles et services"],
        "SERVICE DE L'ENVIRONNEMENT"  : ["Environnement"],
        "SERVICE DE L'ÉVALUATION FONCIÈRE" : ["Foncier"],
        "SERVICE DE LA CONCERTATION DES ARRONDISSEMENTS" : ["Organisation et administration"],
        "SERVICE DE LA CULTURE" : ["Sports, loisirs, culture et développement social"],
        "SERVICE DE LA PERFORMANCE ORGANISATIONNELLE" : ["Organisation et administration"],
        "SERVICE DE LA QUALITÉ DE VIE" : ["Sports, loisirs, culture et développement social"],
        "SERVICE DE SÉCURITÉ INCENDIE DE MONTRÉAL" : ["Sécurité publique"],
        "SERVICE DES AFFAIRES INSTITUTIONNELLES" : ["Organisation et administration"],
        "SERVICE DES AFFAIRES JURIDIQUES" : ["Juridique"],
        "SERVICE DES COMMUNICATIONS" : ["Communications et relations publiques"],
        "SERVICE DES FINANCES" : ["Ressources financières"],
        "SERVICE DES INFRASTRUCTURES, DU TRANSPORT ET DE L'ENVIRONNEMENT" : ["Transport","Environnement"],
        "SERVICE DU CAPITAL HUMAIN ET DES COMMUNICATIONS" : ["Ressources humaines", "Communications et relations publiques"],
        "SERVICE DU CONTRÔLEUR GÉNÉRAL" : ["Organisation et administration"],
        "SERVICE DU GREFFE" : ["Gestion de l'information"],
        "SERVICE DES INFRASTRUCTURES, DE LA VOIRIE ET DES TRANSPORTS" : ["Infrastructures"],
        "SERVICE DE LA CONCERTATION DES ARRONDISSEMENTS ET RESSOURCES MATÉRIELLES": ["Organisation et administration"],
        "SOCIÉTÉ DU PARC JEAN-DRAPEAU" : ["Sports, loisirs, culture et développement social"],
    }

    SERVICE_AGGREGATOR = {
        "AHUNTSIC-CARTIERVILLE" : "ARRONDISSEMENT D'AHUNTSIC-CARTIERVILLE",
        "ANJOU" : "ARRONDISSEMENT D'ANJOU",
        "ARRONDISSEMENT DE CÔTE-DES-NEIGES-NOTRE-DAME-DE-GRÂCE" : "ARRONDISSEMENT DE CÔTE-DES-NEIGES - NOTRE-DAME-DE-GRÂCE",
        "CÔTE-DES-NEIGES–NOTRE-DAME-DE-GRÂCE" : "ARRONDISSEMENT DE CÔTE-DES-NEIGES - NOTRE-DAME-DE-GRÂCE",
        "ARRONDISSEMENT DE RIVIÈRE-DES-PRAIRIES-POINTE-AUX-TREMBLES" : "ARRONDISSEMENT DE RIVIÈRE-DES-PRAIRIES–POINTE-AUX-TREMBLES",
        "RIVIÈRE-DES-PRAIRIES–POINTE-AUX-TREMBLES" : "ARRONDISSEMENT DE RIVIÈRE-DES-PRAIRIES–POINTE-AUX-TREMBLES",
        "ARRONDISSEMENT LE SUD-OUEST" : "ARRONDISSEMENT DU SUD-OUEST",
        "SUD-OUEST" : "ARRONDISSEMENT DU SUD-OUEST",
        "BUREAU DU VÉRIFICATEUR" : "BUREAU DU VÉRIFICATEUR GÉNÉRAL",
        "COMMISSION DES SERVICES ÉLECTRIQUES" : "COMMISSION DES SERVICES ÉLECTRIQUES DE MONTRÉAL",
        "LACHINE" : "ARRONDISSEMENT DE LACHINE",
        "LASALLE" : "ARRONDISSEMENT DE LASALLE",
        "L’ÎLE-BIZARD–STE-GENEVIÈVE" : "ARRONDISSEMENT DE L’ÎLE-BIZARD–STE-GENEVIÈVE",
        "MERCIER–HOCHELAGA-MAISONNEUVE" : "ARRONDISSEMENT DE MERCIER-HOCHELAGA-MAISONNEUVE",
        "MONTRÉAL-NORD" : "ARRONDISSEMENT DE MONTRÉAL-NORD",
        "OMBUDSMAN DE MONTRÉAL" : "BUREAU DE L’OMBUDSMAN",
        "OUTREMONT" : "ARRONDISSEMENT D'OUTREMONT",
        "PIERREFONDS–ROXBORO" : "ARRONDISSEMENT DE PIERREFONDS-ROXBORO",
        "PLATEAU-MONT-ROYAL" : "ARRONDISSEMENT DU PLATEAU-MONT-ROYAL",
        "ROSEMONT–LA PETITE-PATRIE" : "ARRONDISSEMENT DE ROSEMONT-LA PETITE-PATRIE",
        "SAINT-LAURENT" : "ARRONDISSEMENT DE SAINT-LAURENT",
        "SAINT-LÉONARD" : "ARRONDISSEMENT DE SAINT-LÉONARD",
        "SERVICE DE CONCERTATION DES ARRONDISSEMENTS ET DES RESSOURCES MATÉRIELLES" : "SERVICE DE LA CONCERTATION DES ARRONDISSEMENTS ET RESSOURCES MATÉRIELLES",
        "SERVICE DE LA DIVERSITÉ SOCIALE\nET DES SPORTS" : "SERVICE DE LA DIVERSITÉ SOCIALE ET DES SPORTS",
        "SERVICE DE LA GESTION ET PLANIFICATION IMMOBILIÈRE" : "SERVICE DE LA GESTION ET DE LA PLANIFICATION IMMOBILIÈRE",
        "SERVICE DE L’EAU" : "SERVICE DE L'EAU",
        "SERVICE DE POLICE" : "SERVICE DE POLICE DE LA VILLE DE MONTRÉAL",
        "SERVICE DE POLICE DE MONTRÉAL" : "SERVICE DE POLICE DE LA VILLE DE MONTRÉAL",
        "SERVICE DES AFFAIRES JURIDIQUES ET DE L’ÉVALUATION FONCIÈRE" : "SERVICE DES AFFAIRES JURIDIQUES ET DE L'ÉVALUATION FONCIÈRE",
        "SERVICES DES AFFAIRES JURIDIQUES ET DE L'ÉVALUATION FONCIÈRE" : "SERVICE DES AFFAIRES JURIDIQUES ET DE L'ÉVALUATION FONCIÈRE",
        "SERVICES DES AFFAIRES JURIDIQUES ET ÉVALUATION FONCIÈRE" : "SERVICE DES AFFAIRES JURIDIQUES ET DE L'ÉVALUATION FONCIÈRE",
        "SERVICE DE L'ESPACE POUR LA VIE" : "SERVICE DES ESPACES POUR LA VIE",
        "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT ROYAL" : "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT-ROYAL",
        "SERVICE DES GRANDS PARCS, VERDISSEMENT ET DU MONT-ROYAL" : "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT-ROYAL",
        "SERVICE DES GRANDS PARCS, VERDISSEMENT ET MONT ROYAL" : "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT-ROYAL",
        "SERVICE DES GRANDS PARCS_VERDISSEMENT ET DU MONT-ROYAL": "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT-ROYAL",
        "SERVICE DES INFRASTRUCTURES, VOIRIE ET TRANSPORTS" : "SERVICE DES INFRASTRUCTURES, DE LA VOIRIE ET DES TRANSPORTS",
        "SERVICE DES INFRASTRUCTURES_VOIRIE ET TRANSPORTS" : "SERVICE DES INFRASTRUCTURES, DE LA VOIRIE ET DES TRANSPORTS",
        "RESSOURCES HUMAINES" : "SERVICE DES RESSOURCES HUMAINES",
        "SERVICE DES TECHNOLOGIES DE L’INFORMATION" : "SERVICE DES TECHNOLOGIES DE L'INFORMATION",
        "SERVICES DES TECHNOLOGIES DE L'INFORMATION" : "SERVICE DES TECHNOLOGIES DE L'INFORMATION",
        "SERVICE DU MATERIEL ROULANT ET ATELIERS" : "SERVICE DU MATÉRIEL ROULANT ET DES ATELIERS",
        "SERVICE DU MATÉRIEL ROULANT ET DES ATELIER" : "SERVICE DU MATÉRIEL ROULANT ET DES ATELIERS",
        "VERDUN" : "ARRONDISSEMENT DE VERDUN",
        "VILLE-MARIE" : "ARRONDISSEMENT DE VILLE-MARIE",
        "VILLERAY–ST-MICHEL–PARC-EXTENSION" : "ARRONDISSEMENT DE VILLERAY-SAINT-MICHEL-PARC-EXTENSION",
        "SERVICE DE DÉVELOPPEMENT ÉCONOMIQUE" : "SERVICE DU DÉVELOPPEMENT ÉCONOMIQUE",
        "SERVICE MISE EN VALEUR DU TERRITOIRE" : "SERVICE DE LA MISE EN VALEUR DU TERRITOIRE",
        "FACTURATION PÉRIODIQUE À RÉPARTIR SELION UTILISATION" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "FACTURATION PÉRIODIQUE À RÉPARTIR SELON CONSOMMATION" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "FACTURATION PÉRIODIQUE À RÉPARTIR SELON UTILISATEURS" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "FACTURATION PÉRIODIQUE À RÉPARTIR SELON UTILISATION" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "FACTURATION PÉRIODIQUE À RÉPARTIR SELON UTILISATON" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "FACTURÉ SELON SITE" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "À REDISTRIBUER SELON UTILISATEURS" : "FACTURATION PÉRIODIQUE À RÉPARTIR",
        "SERA RÉPARTI ENTRE LES UTILISATEURS" : "FACTURATION PÉRIODIQUE À RÉPARTIR"

    }


class ProductionConfig(Config):
    DEBUG = False
    SENDMAIL = True
    URL_ROOT = 'https://ovc-prod.herokuapp.com'
    ADMINS = ['donneesouvertes@ville.montreal.qc.ca']
    FTS_LANG = 'fr'

class StagingConfig(Config):
    URL_ROOT = 'https://ovc-stage.herokuapp.com'
    SENDMAIL = True
    DEVELOPMENT = False
    DEBUG = False

class DevelopmentConfig(Config):
    URL_ROOT = 'http://localhost:5000'
    DEVELOPMENT = True
    DEBUG = True
    

class TestingConfig(Config):
    TESTING = True
    SUPPLIER_SIZE = [0, 100000, 10000000]

    DATA_SOURCES = [
        {
            'name': 'Conseil Municipal',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'fixtures/contracts.csv',
            'type': 'contract'
        },
         {
            'name': 'Conseil Municipal',
            'mapper': 'field_mapper_subvention_mtl',
            'url': 'fixtures/subventions.csv',
            'type': 'subvention'
        },       
    ]
