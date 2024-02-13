from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)

    # app.config.from_object('settings')

    db.init_app(app)
    bcrypt.init_app(app)

    return app
