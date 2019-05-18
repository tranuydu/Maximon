import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,help="Please enter username")
    parser.add_argument('password', type=str, required=True,help="Please enter password")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_name(data['username']):
            return {'message': 'User exists'}, 400

        user = UserModel(data['username'], data['password'])

        user.insert()

        return {'message': 'User created'}, 201


class UserList(Resource):
    @jwt_required()
    def get(self):
        return UserModel.getUsers()
