import datetime
from application import db

__all__ = ['Post']

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())

    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)

    # USer id that created the post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.id}>"