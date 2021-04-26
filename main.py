from flask import render_template, Blueprint, request, abort, jsonify
from . import db
from .models import Feedback

main = Blueprint('main', __name__)


@main.route('/')
def root():
    return render_template('index.html')