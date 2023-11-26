from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from application.users.models import User
from application import flask_bcrypt


users = Blueprint('users', __name__, template_folder='../templates')

class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password',  validators=[DataRequired(), Length(min=6)])

    @users.route('/login', methods=['GET', 'POST'])
    def login():
        """Login page for users."""
        if current_user.is_authenticated:
            return redirect(url_for("users.index"))
    
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()

            if user and flask_bcrypt.check_password_hash(
                    user.password,
                    form.password.data
                    # request.form['password']
                ):
                login_user(user, remember=True)
                flash("Logged in successfully.")
                # return redirect(request.args.get("next") or url_for("snaps.listing"))
                return redirect(url_for("users.index"))
            else:
                flash("That username or password is not correct.")
        return render_template("users/login.html", form=form)
    
    @users.route('/logout', methods=['GET'])
    def logout():
        """Logout the current user."""
        logout_user()
        flash("You have been logged out.")
        # return redirect(url_for('snaps.listing'))
        return redirect(url_for('users.login'))
    
    @users.route('/index', methods=['GET'])
    def index():
        """User index page."""
        return render_template('users/index.html')