from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.user import User

user_bp = Blueprint("users", __name__)
user_api = Api(user_bp)


class UserAPI(Resource):
    def get(self):
        # Modify the logic for user authentication
        username = request.args.get("username")
        password = request.args.get("password")
        user = db.session.query(User).filter_by(username=username, password=password).first()
        if user:
            return user.to_dict()
        return {"message": "Invalid username or password"}, 401

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        parser.add_argument("password", required=True, type=str)
        args = parser.parse_args()

        user = User(username=args["username"], password=args["password"])
        try:
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"Server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("username", required=True, type=str)
        parser.add_argument("password", required=True, type=str)
        args = parser.parse_args()

        try:
            user = db.session.query(User).get(args["id"])
            if user:
                user.username = args["username"]
                user.password = args["password"]
                db.session.commit()
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"Server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            user = db.session.query(User).get(args["id"])
            if user:
                db.session.delete(user)
                db.session.commit()
                return user.to_dict()
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"Server error: {e}"}, 500


class UserListAPI(Resource):
    def get(self):
        users = db.session.query(User).all()
        return [user.to_dict() for user in users]

    def delete(self):
        try:
            db.session.query(User).delete()
            db.session.commit()
            return []
        except Exception as e:
            db.session.rollback()
            return {"message": f"Server error: {e}"}, 500


user_api.add_resource(UserAPI, "/login")
user_api.add_resource(UserListAPI, "/userList")