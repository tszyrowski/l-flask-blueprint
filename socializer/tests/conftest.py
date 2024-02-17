import os
import pytest
from application import create_app, db as database
from test_settings import SQLALCHEMY_DATABASE_URI

DB_LOCATION = SQLALCHEMY_DATABASE_URI.replace('sqlite:///', '')

@pytest.fixture(scope='session')
def app():
    # Ensure the directory for the SQLite database exists
    print(f"DB_LOCATION: {DB_LOCATION}") 
    os.makedirs(os.path.dirname(DB_LOCATION), exist_ok=True)
    app = create_app(config_filename='../test_settings.py')
    with app.app_context():
        yield app


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
def session(db, app):
    """Creates a new database session for a test."""
    # Start a transaction
    connection = db.engine.connect()
    transaction = connection.begin()

    # Bind the session to the connection
    db.session.bind = connection

    # This ensures that db.session uses the transaction
    @app.before_request
    def override_session():
        db.session.begin_nested()

    yield db.session

    # After each test, rollback the transaction
    db.session.rollback()
    connection.close()
    db.session.remove()