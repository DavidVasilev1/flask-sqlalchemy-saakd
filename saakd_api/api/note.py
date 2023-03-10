from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.notes import Notes

note_bp = Blueprint("note", __name__)
note_api = Api(note_bp)


class NoteAPI(Resource):
    def get(self):
        id = request.args.get("id")
        note = db.session.query(Notes).get(id)
        if note:
            return note.to_dict()
        return {"message": "note not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True, type=str)
        parser.add_argument("subject", required=True, type=str)
        args = parser.parse_args()

        note = Notes(args["text"], args["subject"])
        try:
            db.session.add(note)
            db.session.commit()
            return note.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("text", required=True, type=str)
        args = parser.parse_args()

        try:
            note = db.session.query(Notes).get(args["id"])
            if note:
                note.text = args["text"]
                db.session.commit()
            else:
                return {"message": "note not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("text", required=True, type=str)
        parser.add_argument("subject", required=True, type=str)
        args = parser.parse_args()

        try:
            note = db.session.query(Notes).get(
                args["id"], args["text"], args["subject"])
            if note:
                db.session.delete(note)
                db.session.commit()
                return note.to_dict()
            else:
                return {"message": "note not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class NoteListAPI(Resource):
    def get(self):
        notes = db.session.query(Notes).all()
        return [note.to_dict() for note in notes]

    def delete(self):
        try:
            db.session.query(Notes).delete()
            db.session.commit()
            return []
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


note_api.add_resource(NoteAPI, "/note")
note_api.add_resource(NoteListAPI, "/noteList")
