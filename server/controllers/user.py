from flask import Blueprint, request

from data.models.user import User

user_controller = Blueprint('user_controller', __name__, url_prefix='/user')

# REST CRUD controller for user
@user_controller.route('', methods=['POST'])
def create_user():
    username = request.args.get('username')
    password = request.args.get('password')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    # Generate ID
    generated_id = 0

    user = User(generated_id, username, password, first_name, last_name)
    return f"Creating user {username}..."

@user_controller.route('', methods=['GET'])
def get_users():
    return "Getting users ..."

@user_controller.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return f"Getting user {user_id} ..."

@user_controller.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return f"Deleting user {user_id} ..."
