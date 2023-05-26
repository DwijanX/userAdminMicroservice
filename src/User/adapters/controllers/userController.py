# app/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from application.Services.userService import UserService
from adapters.DTO.userDTO import UserDTO

userBP = Blueprint('user', __name__)

@userBP.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    userDto=UserDTO(data['username'],data['email'],data['password'])
    user_service = UserService()  
    user = user_service.createUser(userDto)

    if user:
        response = {
            'message': 'User created successfully',
            'userID': user.userID,
            'username': user.username,
            'email': user.email
        }
        return jsonify(response), 201
    else:
        return jsonify({'message': 'Failed to create user'}), 500

@userBP.route('/users/<int:user_id>', methods=['GET'])
def get_user(userID):
    user_service = UserService()  
    userDto=UserDTO(userID)

    user = user_service.getUser(userDto)

    if user:
        response = {
            'userID': user.userID,
            'username': user.username,
            'email': user.email
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@userBP.route('/users/<int:user_id>', methods=['PUT'])
def update_user(userID):
    data = request.get_json()
    userDto=UserDTO(userID,data['username'],data['email'],data['password'])

    user_service = UserService()  # Instancia del servicio de usuario
    user = user_service.updateUser(userDto)

    if user:
        response = {
            'message': 'User updated successfully',
            'userID': user.userID,
            'username': user.username,
            'email': user.email
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@userBP.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(userID):
    user_service = UserService() 
    userDto=UserDTO(userID)
    user_service.deleteUser(userDto)
    return jsonify({'message': 'User deleted successfully'}), 200