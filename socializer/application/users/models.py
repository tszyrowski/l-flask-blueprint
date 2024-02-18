import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from application import db, flask_bcrypt_instance
from application import user_followed
from application.posts.models import Post

__all__ = ["followers", "User"]

followers = db.Table(
    "followers",
    db.Column(
        "follower_id", db.Integer, db.ForeignKey("user.id"), primary_key=True
    ),
    db.Column(
        "user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True
    )
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(40), unique=True)
    _password = db.Column("password", db.String(60))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    followed = db.relationship(
        "User",
        secondary=followers,
        primaryjoin=(id==followers.c.follower_id),
        secondaryjoin=(id==followers.c.user_id),
        backref=db.backref("followers", lazy="dynamic"),
        lazy="dynamic"
    )

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
        self._password = flask_bcrypt_instance.generate_password_hash(password)

    def unfollow(self, user):
        """Unfollow the given user
        
        :return false if user was not followed
            otherwise:
                remove user from the followed list and return
                current object to be committed to the session
        """
        if not self.is_following(user):
            return False
        self.followed.remove(user)
        return self
    
    def follow(self, user):
        """Follow given user
        return false if user was already followed
        """
        if self.is_following(user):
            return False
        self.followed.append(user)

        # Emit a signal that the user was followed
        user_followed.send(self)

        return self
    
    def is_following(self, user):
        """Returns true if current_user following user, false otherwise"""
        followed = self.followed.filter(followers.c.user_id == user.id)
        return followed.count() > 0
    
    def newsfeed(self):
        """Return all posts from users that this user follows."""
        join_condition = followers.c.user_id == Post.user_id
        filter_condition = followers.c.follower_id == self.id
        ordering = Post.created_at.desc()

        return Post.query.join(
            followers, join_condition
        ).filter(filter_condition).order_by(ordering)