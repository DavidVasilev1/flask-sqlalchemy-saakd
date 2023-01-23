from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.todos import Todo

todo_bp = Blueprint("todos", __name__)
todo_api = Api(todo_bp)


class TodoAPI(Resource):
    def get(self):
        id = request.args.get("id")
        todo = db.session.query(Todo).get(id)
        if todo:
            return todo.to_dict()
        return {"message": "todo not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True, type=str)
        args = parser.parse_args()

        todo = Todo(args["text"])
        try:
            db.session.add(todo)
            db.session.commit()
            return todo.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("completed", required=True, type=int)
        args = parser.parse_args()

        try:
            todo = db.session.query(Todo).get(args["id"])
            if todo:
                todo.completed = args["completed"]
                db.session.commit()
            else:
                return {"message": "todo not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            todo = db.session.query(Todo).get(args["id"])
            if todo:
                db.session.delete(todo)
                db.session.commit()
                return todo.to_dict()
            else:
                return {"message": "todo not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class TodoListAPI(Resource):
    def get(self):
        todos = db.session.query(Todo).all()
        return [todo.to_dict() for todo in todos]


todo_api.add_resource(TodoAPI, "/todo")
todo_api.add_resource(TodoListAPI, "/todoList")
