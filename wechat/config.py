import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@host:port/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    TURING_APIKEY = "----get turing123----"
    TURING_USERID = "turing123 account"

    WECHAT_APPID = 'wechat public account'
    WECHAT_APPSECRET = 'get secret'

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost:3306/wechat'


class ProductConfig(Config):
    pass

