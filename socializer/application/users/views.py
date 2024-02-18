from flask import Blueprint, render_template, redirect, url_for, flash, g
from flask_login import login_user, logout_user

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from application.users.models import User
from application import db, flask_bcrypt_instance

users = Blueprint('users', __name__, template_folder="templates")


class LoginForm(FlaskForm):
    """Basic login form and validation"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])


class CreateUserForm(FlaskForm):
    """Basic user creation form and validation"""

    email = StringField('Email', validators=[DataRequired(), Length(min=6)])
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=3)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6)]
    )


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = CreateUserForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash('User successfully created')
        login_user(user, remember=True)
        return redirect(url_for('users.login'))

    return render_template('users/signup.html', form=form)

@users.route('/', methods=['GET'])
def index():
    return render_template('users/index.html')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if hasattr(g, 'user') and g.user.is_authenticated:
        return redirect(url_for('users.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        if not user or not flask_bcrypt_instance.check_password_hash(
            user.password, form.password.data
        ):
            flash('Invalid username or password')
            return redirect(url_for('users.login'))

        login_user(user, remember=True)
        return redirect(url_for('users.index'))
    
    return render_template('users/login.html', form=form)

@users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('users.login'))
