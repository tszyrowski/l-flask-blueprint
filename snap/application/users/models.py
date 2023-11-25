import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from application import db, flask_bcrypt


class User(db.Model):

    # The primary key for each user record.
    id = db.Column(db.Integer, primary_key=True)

    # The unique email for each user record.
    email = db.Column(db.String(255), unique=True)

    # The unique username for each record.
    username = db.Column(db.String(40), unique=True)

    # The hashed password for the user
    _password = db.Column(db.String(60))

    # The date/time that the user account was created on.
    created_on = db.Column(db.DateTime, 
        default=datetime.datetime.utcnow)

    @hybrid_property
    def password(self):
        """Get the hashed password."""
        return self._password
    
    @password.setter
    def password(self, password):
        """Set the password."""
        self._password = flask_bcrypt.generate_password_hash(password)


    def __repr__(self):
        return '<User {!r}>'.format(self.username)

    def is_authenticated(self):
        """All our registered users are authenticated."""
        return True

    def is_active(self):
        """All our users are active."""
        return True

    def is_anonymous(self):
        """We don)::f):lf):users are authenticated."""
        return False

    def get_id(self):
        """Get the user ID as a Unicode string."""
        return str(self.id)