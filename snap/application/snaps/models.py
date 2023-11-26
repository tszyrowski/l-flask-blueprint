import datetime
import hashlib
from application import db
  

def content_hash(context):
    content = context.current_parameters['content']
    created_on = context.current_parameters['created_on']
    return hashlib.sha1(
        (content + str(created_on)).encode('utf-8')
    ).hexdigest()

class Snap(db.Model):
    
    # The primary key for each snap record.
    id = db.Column(db.Integer, primary_key=True)

    # The name of the files, does not need to be unique.
    name = db.Column(db.String(128))

    # The extension od the file; used for syntax highlighting.
    extension = db.Column(db.String(12))

    # The content of the snap.
    content = db.Column(db.Text())

    # The unique un-guessable ID of the file.
    hash_key = db.Column(db.String(40), unique=True, default=content_hash)

    # The date/time that the snap was created on.
    created_on = db.Column(
        db.DateTime, 
        default=datetime.datetime.utcnow,
        index=True
    )

    # The user this snap belongs to.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('snaps', lazy='dynamic'))

    def __init__(self, user_id, name, content, extension):
        """Initialize a snap."""
        self.user_id = user_id
        self.name = name
        self.content = content
        self.extension = extension
        self.created_on = datetime.datetime.utcnow()

    def __repr__(self):
        return '<Snap {!r}>'.format(self.id)

        
# def content_hash(context):
#     content = context.current_parameters['content']
#     created_on = context.current_parameters['created_on']
#     return hashlib.sha1(
#         (content + str(created_on)).encode('utf-8')
#     ).hexdigest()
