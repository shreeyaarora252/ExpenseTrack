from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.sms_mod import SMS
from app import db

sms_bp = Blueprint('sms', __name__)

@sms_bp.route('/receive', methods=['POST'])
@jwt_required()  # Validates the JWT token
def receive_sms():
    current_user = get_jwt_identity()  # Extracts user identity from the token

    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"message": "Message field is required"}), 400

    sms = SMS(user_id=current_user, message=message)
    db.session.add(sms)
    db.session.commit()

    return jsonify({"message": "SMS received and processed successfully"}), 200
