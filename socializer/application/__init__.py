from blinker import Namespace
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
flask_bcrypt_instance = Bcrypt()
login_manager = LoginManager()

socializer_signals = Namespace()
user_followed = socializer_signals.signal('user-followed')

from application.signal_handlers import connect_handlers
connect_handlers()

def create_app(config_filename=None):
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)
    else:
        # Default configuration, useful for development
        app.config.from_object('settings')

    db.init_app(app)
    flask_bcrypt_instance.init_app(app)
    login_manager.init_app(app)

    from application.users.views import users
    app.register_blueprint(users, url_prefix="/users")

    from application.users.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))    

    return app
