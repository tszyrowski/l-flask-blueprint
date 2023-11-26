from application import app, db
from application.users.models import User

user = User(username="test1", password="mypassword", email="test1@email.com")
print(user.password)

with app.app_context():
    db.session.add(user)
    db.session.commit()