from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.nhl import Player

player_bp = Blueprint("players", __name__)
player_api = Api(player_bp)


class PlayerAPI(Resource):
    def get(self):
        id = request.args.get("id")
        player = db.session.query(player).get(id)
        if player:
            return player.to_dict()
        return {"message": "player not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("SOG", required=True, type=str)
        parser.add_argument("Min", required=True, type=str)
        parser.add_argument("Points", required=True, type=str)
        parser.add_argument("Name", required=True, type=str)
        args = parser.parse_args()

        player = player(args["SOG"], args["Min"], args["Points"], args["Name"])
        try:
            db.session.add(player)
            db.session.commit()
            return player.to_dict(), 201
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
            player = db.session.query(player).get(args["id"])
            if player:
                player.SOG = args["SOG"]
                player.Min = args["Min"]
                player.Points = args["Points"]
                player.Name = args["Name"]
                db.session.commit()
            else:
                return {"message": "player not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            player = db.session.query(player).get(args["id"])
            if player:
                db.session.delete(player)
                db.session.commit()
                return player.to_dict()
            else:
                return {"message": "player not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class playerListAPI(Resource):
    def get(self):
        players = db.session.query(Player).all()
        return [player.to_dict() for player in players]

    def delete(self):
        try:
            db.session.query(Player).delete()
            db.session.commit()
            return []
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


player_api.add_resource(PlayerAPI, "/player")
player_api.add_resource(playerListAPI, "/playerList")
