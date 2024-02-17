import os

# Get the directory where the settings.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use os.path.join to construct the database file path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DEBUG = True
TESTING = False
