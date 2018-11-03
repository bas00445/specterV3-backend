import os
# from postgres import DB_URI

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_DATABASE_URI = 'postgres://gkedxhsabubkjq:f8686d5d199ffa209ab2d8aa265f5aec20f19f10d26ce5f20efd2bd9963ce23a@ec2-174-129-236-147.compute-1.amazonaws.com:5432/d8dj0rc7e9duhi'

