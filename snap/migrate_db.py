"""After changes in DB schema the DB need to be migrated

In this case the _password was added:
sqlite> .tables
user
sqlite> .schema user
CREATE TABLE user (
        id INTEGER NOT NULL, 
        email VARCHAR(255), 
        username VARCHAR(40), 
        PRIMARY KEY (id), 
        UNIQUE (email), 
        UNIQUE (username)
);
"""
from flask_migrate import Migrate, init, migrate, upgrade
from application import app, db  # Ensure these are imported correctly
from application.users.models import User  # Import your models

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        # Initialize the migration repository (only needed once)
        init(directory='migrations', multidb=False)

        # Create a new migration (only needed when models change)
        migrate(directory='migrations', message='New migration', sql=False, head='head', splice=False, branch_label=None, version_path=None, rev_id=None)

        # Apply the migration
        upgrade(directory='migrations', revision='head', sql=False, tag=None)
