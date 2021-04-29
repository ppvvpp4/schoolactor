from flask import render_template, Blueprint, request, abort, jsonify
from . import db
from .models import Feedback

main = Blueprint('main', __name__)


@main.route('/')
def root():
    return render_template('index.html')

@main.route('/send_request', methods=['POST'])
def send_request():
    try:
        data = request.get_json()
        
        name = data['name']
        email = data['email']
        phone = data['phone']
        question = data['question']
    except Exception:
        return abort(400)

    try:
        f = Feedback(name = name,
                     email = email, 
                     phone = phone, 
                     question = question)
        db.session.add(f)
        db.session.commit()
        return jsonify(
                       { 'status' : 1 }
                      )
    except Exception:
        return abort(500)
    
    

