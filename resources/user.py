# File Name: user.py
# Original Author: Jesse Malinen/blank-py
# Description: User class definition

# imports
from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.user import User

class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()
        
        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')
        
        if User.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST
        
        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST
        
        password = password
        
        user = User(
            username=username,
            email=email,
            password=password
        )
        
        user.save()
        
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        
        return data, HTTPStatus.CREATED
    