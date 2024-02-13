import os
import pytest
from application import create_app, db as database

DB_LOCATION = 'sqlite:///tmp/test_app.db'

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app(config='test_settings')
    return app

@pytest.fixture(scope='session')
def db(app, request):
    """Session wide test database."""
    database.app = app
    database.create_all()

    def teardown():
        database.drop_all()
        os.unlink(DB_LOCATION)

    request.addfinalizer(teardown)
    return database

@pytest.fixture(scope='function')
def session(db, request):
    
    sesssion = db.create_scoped_session()
    db.session = sesssion

    def teardown():
        sesssion.remove()

    request.addfinalizer(teardown)
    return sesssion