import os


class Config(object):
    ENV = os.environ['ENV']
    CSRF_ENABLED = True
    SECRET_KEY = "this_is_a_secret_key"

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/trailperf"

class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = "mongodb://datascrum.org:27017/trailperf"
