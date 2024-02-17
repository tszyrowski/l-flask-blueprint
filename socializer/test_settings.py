import os

# Get the directory where the settings.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use os.path.join to construct the database file path
test_db_path = os.path.join(BASE_DIR, 'tests', 'test_app.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + test_db_path
DEBUG = True
TESTING = True
