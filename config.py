import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mssql+pyodbc://admin:admin@DESKTOP-V7D56HF\SQLEXPRESS/testSadygFour?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False