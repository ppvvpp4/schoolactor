from flask import Blueprint, flash, render_template, redirect, url_for, session, request, abort
from flask_login import login_user, logout_user
from flask_login.utils import login_required
from werkzeug.security import check_password_hash
from . import db 
from .models import User

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login_get():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    try:

        login = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(login=str(login)).first()
        if not check_password_hash(user.password, password):
            return redirect(url_for('auth.login_get'))
        else:
            session['user'] = user.login
            login_user(user, remember=True)
            return redirect(url_for('admin.adminpanel'))
    except Exception:
        return abort(400)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.root'))
