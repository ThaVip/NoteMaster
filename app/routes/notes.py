# app/routes/notes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Note, User

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_identity = get_jwt_identity()
    user = User.query.filter_by(email=user_identity['email']).first()

    note = Note(title=title, content=content, author=user)
    db.session.add(note)
    db.session.commit()

    return jsonify({"message": "Note created successfully"}), 201

@notes_bp.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(email=user_identity['email']).first()
    notes = Note.query.filter_by(author=user).all()

    return jsonify([{
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "date_posted": note.date_posted
    } for note in notes]), 200
