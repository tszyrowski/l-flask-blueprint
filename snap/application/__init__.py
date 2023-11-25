from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)

from application.users import models as user_models
from application.users.views import users

@login_manager.user_loader
def load_user(user_id):
    return user_models.user_models.query.get(user_id)