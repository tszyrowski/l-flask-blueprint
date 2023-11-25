from application import app, db
from application.users.models import User

new_user = User(email="me@email.com", username="me")

with app.app_context():
    db.session.add(new_user)
    db.session.commit()