from flask import Blueprint, request, jsonify, abort
from controllers.user_controller import get_users, create_user, get_user, update_user, delete_user

user_routes = Blueprint('users', __name__)

user_routes.route('/users', methods=['GET'])(get_users)
user_routes.route('/users', methods=['POST'])(create_user)
user_routes.route('/users/<int:user_id>', methods=['GET'])(get_user)
user_routes.route('/users/<int:user_id>', methods=['PUT'])(update_user)
user_routes.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
