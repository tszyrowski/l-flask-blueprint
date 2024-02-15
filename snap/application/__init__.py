import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate() # for updating the DB schema
login_manager = LoginManager()
login_manager.login_view = 'users.login' 
flask_bcrypt = Bcrypt()


def create_app(config_name=None):
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    db_path = os.path.join(basedir, 'site.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SECRET_KEY'] = "-80:12345678901234567890123456"

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    flask_bcrypt.init_app(app)
    login_manager.init_app(app)

    from application.users import models as user_models
    from application.users.views import users
    from application.snaps.views import snaps
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(snaps, url_prefix="")

    @login_manager.user_loader
    def load_user(user_id):
        return user_models.User.query.get(user_id)
    
    return app
