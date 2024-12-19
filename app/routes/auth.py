from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db

# Create the blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

# Register route for user registration
@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing required fields"}), 400

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 409

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Create and save a new user object
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Login route
@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing required fields"}), 400

    # Fetch user from the database
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid username or password"}), 401

    # Generate JWT token
    token = create_access_token(identity=user.id)
    return jsonify({"message": "Login successful", "token": token}), 200
