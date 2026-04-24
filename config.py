import os
import logging

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'SQLite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'A83H5HA3290FJS490SGE'
    SQLALCHEMY_ECHO = False