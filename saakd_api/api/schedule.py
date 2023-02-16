from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.schedules import Schedule

schedule_bp = Blueprint("schedule", __name__)
schedule_api = Api(schedule_bp)


class ScheduleAPI(Resource):
    def get(self):
        id = request.args.get("id")
        schedule = db.session.query(Schedule).get(id)
        if schedule:
            return schedule.to_dict()
        return {"message": "schedule not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("period", required=True, type=int)
        parser.add_argument("class1", required=False, type=str)
        parser.add_argument("classNumber", required=False, type=str)
        parser.add_argument("startTime", required=False, type=str)
        parser.add_argument("endTime", required=False, type=str)
        
        args = parser.parse_args()

        schedule = Schedule(args["period"], args["class1"], args["classNumber"], args["startTime"], args["endTime"])
        try:
            db.session.add(schedule)
            db.session.commit()
            return schedule.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            schedule = db.session.query(Schedule).get(args["id"])
            if schedule:
                schedule.started = False
                db.session.commit()
            else:
                return {"message": "schedule not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            schedule = db.session.query(Schedule).get(args["id"])
            if schedule:
                db.session.delete(schedule)
                db.session.commit()
                return schedule.to_dict()
            else:
                return {"message": "schedule not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class ScheduleListAPI(Resource):
    def get(self):
        schedules = db.session.query(Schedule).all()
        return [schedule.to_dict() for schedule in schedules]


schedule_api.add_resource(ScheduleAPI, "/schedule")
schedule_api.add_resource(ScheduleListAPI, "/scheduleList")
