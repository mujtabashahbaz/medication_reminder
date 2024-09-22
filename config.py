# Configuration file for database, etc.
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///medications.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
