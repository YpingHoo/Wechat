import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@host:port/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    TURING_APIKEY = "5efe0411b6504cfab550e7acacee2a41"
    TURING_USERID = "303633"

    WECHAT_APPID = 'wxb8df474148866694'
    WECHAT_APPSECRET = '2a145d6e0fcf9461b7538300cf989927'

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost:3306/wechat'


class ProductConfig(Config):
    pass

