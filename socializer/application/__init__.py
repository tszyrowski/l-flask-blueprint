from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
flask_bcrypt_instance = Bcrypt()

def create_app(config_filename=None):
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)
    else:
        # Default configuration, useful for development
        app.config.from_object('settings')

    db.init_app(app)
    flask_bcrypt_instance.init_app(app)

    return app
