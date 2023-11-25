from application import db

class User(db.Model):
   # model attributes
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(255), unique=True)
   username = db.Column(db.String(40), unique=True)