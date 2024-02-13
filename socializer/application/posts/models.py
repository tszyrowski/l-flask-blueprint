from application import db
import datetime

__all__ = ['Post']

class Post(db.Model):
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)