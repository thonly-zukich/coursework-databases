from flask import jsonify, request, abort
from services.user_service import (
    get_all_users,
    get_user_by_id,
    create_new_user,
    update_user_data,
    delete_user_data
)

def get_users():
    users = get_all_users()
    return jsonify(users), 200

def get_user(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user), 200

def create_user():
    data = request.get_json()
    if not data or not "username" in data or not "email" in data:
        abort(400, description="Missing required fields: username or email")
    new_user = create_new_user(data)
    return jsonify(new_user), 201

def update_user(user_id):
    data = request.get_json()
    updated_user = update_user_data(user_id, data)
    if not updated_user:
        abort(404, description="User not found")
    return jsonify(updated_user), 200

def delete_user(user_id):
    success = delete_user_data(user_id)
    if not success:
        abort(404, description="User not found")
    return jsonify({"message": "User deleted successfully"}), 200
