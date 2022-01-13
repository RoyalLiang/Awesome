import os

SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "sqlite:///../dev.db",
    )
DEBUG = True

ENV = 'dev'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ECHO = True
