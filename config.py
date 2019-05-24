import sys
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


class Config:
    """App base configuration"""

    DEBUG = False
    TESTING = False
    FLASK_ENV = getenv('FLASK_ENV', 'production')
    PORT = getenv('PORT', 5000)
    SWAGGER_URL = '/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = getenv(
        'DATABASE_URI',
        'postgresql://localhost/flight_booking')


class StagingConfig(Config):
    """App staging configuration"""

    pass


class ProductionConfig(Config):
    """App production configuration"""

    pass


class DevelopmentConfig(Config):
    """App development configuration"""

    DEBUG = True


class TestingConfig(Config):
    """App testing configuration"""

    DEBUG = True
    TESTING = True
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI',
        'postgresql://localhost/flight_booking_test')


config = {
    "staging": StagingConfig,
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}

AppConfig = TestingConfig if 'pytest' in sys.modules else config.get(
    getenv('FLASK_ENV'), 'development')

