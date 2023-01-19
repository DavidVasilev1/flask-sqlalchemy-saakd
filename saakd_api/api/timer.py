from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.timers import Timer

timer_bp = Blueprint("timer", __name__)
timer_api = Api(timer_bp)


class TimerAPI(Resource):
    def get(self, id):
        timer = db.session.query(Timer).get(id)
        if timer:
            return timer.to_dict()
        return {"message": "timer not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("task", required=True, type=str)
        parser.add_argument("expectedtime", required=False, type=int)
        args = parser.parse_args()

        timer = Timer(args["task"],  args["expectedtime"])
        try:
            db.session.add(timer)
            db.session.commit()
            return timer.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            timer = db.session.query(Timer).get(args["id"])
            if timer:
                timer.completed = True
                db.session.commit()
            else:
                return {"message": "timer not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            timer = db.session.query(Timer).get(args["id"])
            if timer:
                db.session.delete(timer)
                db.session.commit()
                return timer.to_dict()
            else:
                return {"message": "todo not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class TimerListAPI(Resource):
    def get(self):
        timers = db.session.query(Timer).all()
        return [timer.to_dict() for timer in timers]


timer_api.add_resource(TimerAPI, "/timer")
timer_api.add_resource(TimerListAPI, "/timerList")
