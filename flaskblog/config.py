import os


basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    ENV = 'dev'
    if ENV == 'dev':
        DEBUG = True
        # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        SECRET_KEY = 'mysecret'
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:berzone@localhost/blogdata'
    else:
        # POSTGRES = {
        # 'user': 'postgres',
        # 'pw': 'mypassword in postgres',
        # 'db': 'postgres',
        # 'host': 'localhost',
        # 'port': '5432'
        # }
        DEBUG = False
        SECRET_KEY = 'mysecret'
        SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
