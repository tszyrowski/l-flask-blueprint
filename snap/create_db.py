from application import app, db
from application.users.models import User

with app.app_context():
    db.create_all()