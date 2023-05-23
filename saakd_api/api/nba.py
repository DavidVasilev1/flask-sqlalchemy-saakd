from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.nba import Baller

baller_bp = Blueprint("ballers", __name__)
baller_api = Api(baller_bp)


class BallerAPI(Resource):
    def get(self):
        id = request.args.get("id")
        baller = db.session.query(baller).get(id)
        if baller:
            return baller.to_dict()
        return {"message": "baller not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("SOG", required=True, type=str)
        parser.add_argument("Min", required=True, type=str)
        parser.add_argument("Points", required=True, type=str)
        parser.add_argument("Name", required=True, type=str)
        args = parser.parse_args()

        baller = baller(args["SOG"], args["Min"], args["Points"], args["Name"])
        try:
            db.session.add(baller)
            db.session.commit()
            return baller.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("SOG", required=True, type=str)
        parser.add_argument("Min", required=True, type=str)
        parser.add_argument("Points", required=True, type=str)
        parser.add_argument("Name", required=True, type=str)
        args = parser.parse_args()

        try:
            baller = db.session.query(baller).get(args["id"])
            if baller:
                baller.SOG = args["SOG"]
                baller.Min = args["Min"]
                baller.Points = args["Points"]
                baller.Name = args["Name"]
                db.session.commit()
            else:
                return {"message": "baller not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            baller = db.session.query(baller).get(args["id"])
            if baller:
                db.session.delete(baller)
                db.session.commit()
                return baller.to_dict()
            else:
                return {"message": "baller not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class ballerListAPI(Resource):
    def get(self):
        ballers = db.session.query(Baller).all()
        return [baller.to_dict() for baller in ballers]

    def delete(self):
        try:
            db.session.query(Baller).delete()
            db.session.commit()
            return []
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


baller_api.add_resource(BallerAPI, "/baller")
baller_api.add_resource(ballerListAPI, "/ballerList")
