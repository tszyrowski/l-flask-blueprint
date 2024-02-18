from application import db, create_app
from application.users.models import User
from application.posts.models import Post

app = create_app()

# Push an application context
with app.app_context():
    # Now you can safely call functions that require the application context
    db.create_all()