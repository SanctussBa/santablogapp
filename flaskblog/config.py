import os


basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    ENV = ''
    if ENV == 'dev':
        DEBUG = True
        # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        SECRET_KEY = 'mysecret'
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:berzone@localhost/blogdata'
    else:
        DEBUG = False
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        DEBUG = False
        SECRET_KEY = 'mysecret'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
