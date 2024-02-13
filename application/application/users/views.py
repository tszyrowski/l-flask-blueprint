from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/')
def index():
    return "This is the users index", 200

@users.route('/me')
def me():
    return "This is my page", 200