from application import create_app, db
from application.users.models import User

new_user = User(email="test@example.com", username="test", password="mypassword")
app = create_app()

with app.app_context():
    db.session.add(new_user)
    db.session.commit()