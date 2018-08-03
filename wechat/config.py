import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@host:port/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost:3306/wechat'


class ProductConfig(Config):
    pass

