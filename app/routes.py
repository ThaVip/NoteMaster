from flask import request, jsonify, session
from app import app, db
from app.models import User, Note
from flask_bcrypt import generate_password_hash, check_password_hash

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({"message": "Logged in successfully"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    new_note = Note(title=data['title'], content=data['content'], user_id=session['user_id'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "Note created successfully"}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{"title": note.title, "content": note.content} for note in notes]), 200

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    note = Note.query.get(id)
    if note and note.user_id == session['user_id']:
        note.title = data['title']
        note.content = data['content']
        db.session.commit()
        return jsonify({"message": "Note updated successfully"}), 200
    return jsonify({"message": "Note not found or unauthorized"}), 404
