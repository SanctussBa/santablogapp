import os


basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    ENV = ''
    if ENV == 'dev':
        DEBUG = True
        SECRET_KEY = ' ' #Need to add
        SQLALCHEMY_DATABASE_URI = 'postgresql://server_name:password@localhost/table_name' #need to change
    else:
        DEBUG = False
        SECRET_KEY = os.urandom(32)
        app.config['SECRET_KEY'] = SECRET_KEY
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


    SQLALCHEMY_TRACK_MODIFICATIONS = False
