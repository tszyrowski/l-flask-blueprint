from application import app, db
from application.users.models import User

user = User(username="test", password="mypassword", email="test@email.com")
print(user.password)

with app.app_context():
    db.session.add(user)
    db.session.commit()