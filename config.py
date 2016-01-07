import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x99\xda?\x15\xdd\x99\xfc\xed\x10\xe5\xf1Zw\xf4|\x8d\xb5\x8f\xd0\xffO`\xdal'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print SQLALCHEMY_DATABASE_URI


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
