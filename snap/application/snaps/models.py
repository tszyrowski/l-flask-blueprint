import datetime
import hashlib
import uuid

from sqlalchemy import orm, event

from application import db


class Snap(db.Model):

    # The primary key for each snap record
    id = db.Column(db.Integer, primary_key=True)

    # The name of the file; dows not need to be unique
    name = db.Column(db.String(128))

    # The extension of the file used for syntax highlighting
    extension = db.Column(db.String(12))

    # The content of the Snap
    content = db.Column(db.Text())

    # The unique, un-guessable IF of the file
    uuid = db.Column(
        db.String(36), unique=True, default=lambda: str(uuid.uuid4())
    )
    hash_key = db.Column(db.String(40), unique=True)

    # The date/time when snap was created
    created_on = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, index=True
    )

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", backref=db.backref("naps", lazy="dynamic"))

    def __repr__(self):
        return "<Snap {!r}>".format(self.id)
    
    @orm.reconstructor
    def init_on_load(self):
        """Called when loading instance from the database, the same as init"""
        if not self.hash_key:
            self.hash_key = self.content_hash()

    def content_hash(self):
        """sets context-sensitive default function"""
        if self.content and self.created_on:
            return hashlib.sha1(
                (self.content + str(self.created_on)).encode("utf-8")
            ).hexdigest()
        else:
            return None

    def __init__(self, name, extension, content, user_id):
        self.name = name
        self.extension = extension
        self.content = content
        self.user_id = user_id
        self.created_on = datetime.datetime.utcnow()
        self.hash_key = self.content_hash()

@event.listens_for(Snap, "before_insert")
def receive_before_insert(mapper, connection, target):
    if not target.hash_key:
        target.hash_key = target.content_hash()
