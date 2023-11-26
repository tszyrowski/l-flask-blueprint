from flask import Blueprint, render_template, url_for, redirect, current_app, flash
from flask_wtf import FlaskForm
from flask_login import login_required, current_user

from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

from sqlalchemy import exc

from .models import Snap
from application import db

snaps = Blueprint('snaps', __name__, template_folder='../templates')

class SnapForm(FlaskForm):
    """Form for creating new snap"""

    name = StringField('name', validators=[DataRequired()])
    extension = StringField('extension', validators=[DataRequired()])
    content = StringField('content', widget=TextArea(), validators=[DataRequired()])


@snaps.route('/', methods=['GET'])
def listing():
    """List all snaps."""
    snaps = Snap.query.order_by(Snap.created_on.desc()).limit(20).all()
    return render_template('snaps/index.html', snaps=snaps)

@snaps.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add a new snap."""
    form = SnapForm()
    if form.validate_on_submit():
        user_id = current_user.id

        snap = Snap(
            user_id=user_id,
            name=form.name.data,
            content=form.content.data,
            extension=form.extension.data
        )
        db.session.add(snap)
        try:
            db.session.commit()
            flash("Snap added successfully.")
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            flash("Somehting went worng\nError: {}".format(e))
    else:
        return render_template("snaps/add.html", form=form)
    
    return redirect(url_for("snaps.listing"))
