from flask import render_template, Blueprint, abort, redirect, url_for, request
from flask_login.utils import login_required
from sqlalchemy import text
from . import db
from .models import Feedback, User
from werkzeug.security import generate_password_hash

admin = Blueprint('admin', __name__)


@login_required
@admin.route('/admin')
def adminpanel():
    questions = Feedback.query.order_by(text('id desc')).all()
    return render_template('admin.html', data = questions)


@admin.route('/start')
def first_start():
    if len(User.query.all()) <= 0:
        return render_template('start.html')
    else:
        return abort(404)

@admin.route('/start', methods=['POST'])
def first_start_post():
    if len(User.query.all())<= 0:
        login = request.form['login']
        password = request.form['password']

        newuser = User(login = login, password = generate_password_hash(password))
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('auth.login_get'))
    else:
        return abort(404)