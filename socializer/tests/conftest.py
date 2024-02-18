import os
import pytest
from application import create_app, db as database
from test_settings import SQLALCHEMY_DATABASE_URI

DB_LOCATION = SQLALCHEMY_DATABASE_URI.replace('sqlite:///', '')

@pytest.fixture(scope='session')
def app():
    print(f"DB_LOCATION: {DB_LOCATION}") 
    os.makedirs(os.path.dirname(DB_LOCATION), exist_ok=True)
    app = create_app(config_filename='../test_settings.py')
    with app.app_context():
        yield app

@pytest.fixture(scope='function')
def client(app):
    """Create and configure a new app instance for each test."""
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(DB_LOCATION):
        os.unlink(DB_LOCATION)

    database.app = app
    database.create_all()

    def teardown():
        database.drop_all()
        os.unlink(DB_LOCATION)
    
    request.addfinalizer(teardown)
    return database

@pytest.fixture(scope='function')
def session(db):
    """Provide a transactional scope around a series of DB operations."""
    connection = db.engine.connect()
    transaction = connection.begin()
    yield db.session  # default Flask-SQLAlchemy session
    transaction.rollback()
    connection.close()
    db.session.remove()