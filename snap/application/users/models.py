import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from application import db, flask_bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    _password = db.Column("password", db.String(60))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User {!r}>'.format(self.username)
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        """Bcrypt the password on assignment"""
        self._password = flask_bcrypt.generate_password_hash(password)
