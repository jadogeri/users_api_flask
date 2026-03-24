from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from api.extensions import db
from api.models.user import User

# Define the Blueprint
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data or "age" not in data or "fullname" not in data:
        return jsonify({"error": "Missing username or email"}), 400

    new_user = User(age=data["age"], fullname=data["fullname"], username=data['username'], email=data['email'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username or email already exists"}), 409

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.fullname = data.get('fullname', user.fullname)
    try:
        db.session.commit()
        return jsonify({"message": "User updated!"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Update failed: Username or email already exists"}), 409

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted!"})
