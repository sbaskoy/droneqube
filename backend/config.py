class Config(object):
    # secrets
    SECRET_KEY = 'droneqube_secret_key'
    JWT_SECRET_KEY = "droneqube_jwr_secret_key"
    # database
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
