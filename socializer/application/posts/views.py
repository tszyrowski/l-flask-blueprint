from flask import Blueprint, render_template, redirect, url_for, flash, request, g, current_app

from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from sqlalchemy import exc

from application.posts.models import Post
from application import db

posts = Blueprint("posts", __name__, template_folder="templates")

class CreatePostForm(FlaskForm):
    """Basic post creation form and validation"""
    content = StringField('Content', widget=TextArea(), validators=[DataRequired()])

@posts.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        user_id = current_user.id

        post = Post(content=form.content.data, user_id=user_id)
        try:
            db.session.add(post)
            db.session.commit()
            flash('Post successfully created')
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            current_app.logger.error("Post creation failed: %s", e)
            flash('Post creation failed')

    else:
        return render_template('posts/add.html', form=form)

    return redirect(url_for('users.index'))  
        