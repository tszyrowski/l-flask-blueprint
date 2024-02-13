import datetime
from application import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

from application.posts.models import Post

__all__ = ['followers', 'User']

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model):

    # The primary key of the User model is the id column, which is an integer.
    id = db.Column(db.Integer, primary_key=True)
    # The unique email address of the user.
    email = db.Column(db.String(255), unique=True, nullable=False)
    # The unique username of the user.
    username = db.Column(db.String(40), unique=True, nullable=False)
    # The hashed password of the user.
    _password = db.Column("password", db.String(255))
    # The date and time the user was created.
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    followed = db.relationship(
        "User",
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(id==followers.c.user_id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return f"<User {self.username}>"
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    def unfollow(self, user):
        if not self.is_following(user):
            return False
        self.followed.remove(user)
        return self
    
    def follow(self, user):
        if self.is_following(user):
            return False
        self.followed.append(user)
        return self
    
    def is_following(self, user):
        followed = self.followed.filter(followers.c.user_id == user.id)
        return followed.count() > 0
    
    def newsfeed(self):
        """Return all posts from users that this user follows."""
        join_condition = followers.c.user_id == Post.user_id
        filter_condition = followers.c.follower_id == self.id
        ordering = Post.created_on.desc()

        return Post.query.join(
            followers, join_condition).filter(
                filter_condition).order_by(ordering)