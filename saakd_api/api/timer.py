from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.timers import Timer

timer_bp = Blueprint("timers", __name__)
timer_api = Api(timer_bp)


class TimerAPI(Resource):
    def get(self):
        id = request.args.get("id")
        timer = db.session.query(Timer).get(id)
        if timer:
            return timer.to_dict()
        return {"message": "todo not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("tasks", required=True, type=str)
        parser.add_argument("TimeExpected", required=False, type=str)
        parser.add_argument("storedtime", required=False, type=int)

        args = parser.parse_args()

        timer = Timer(args["tasks"], args["TimeExpected"], args["storedtime"])
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
        parser.add_argument("completed", required=True, type=int)
        args = parser.parse_args()

        try:
            timer = db.session.query(Timer).get(args["id"])
            if timer:
                timer.completed = args["completed"]
                db.session.commit()
                return timer.to_dict()
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


# from flask import Blueprint, request
# from flask_restful import Api, Resource, reqparse
# from .. import db
# from ..model.timers import Timer

# timer_bp = Blueprint("timer", __name__)
# timer_api = Api(timer_bp)


# class TimerAPI(Resource):
#     def get(self):
#         id = request.args.get("id")
#         timer = db.session.query(Timer).get(id)
#         if timer:
#             return timer.to_dict()
#         return {"message": "timer not found"}, 404

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("tasks", required=True, type=str)
#         parser.add_argument("TimeExpected", required=False, type=str)
#         parser.add_argument("storedtime", required=False, type=int)

#         args = parser.parse_args()

#         timer = Timer(args["tasks"], args["TimeExpected"], args["storedtime"])
#         try:
#             db.session.add(timer)
#             db.session.commit()
#             return timer.to_dict(), 201
#         except Exception as e:
#             db.session.rollback()
#             return {"message": f"server error: {e}"}, 500

#     def put(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("id", required=True, type=int)
#         args = parser.parse_args()

#         try:
#             timer = db.session.query(Timer).get(args["id"])
#             if timer:
#                 # timer.started = False
#                 db.session.commit()
#             else:
#                 return {"message": "timer not found"}, 404
#         except Exception as e:
#             db.session.rollback()
#             return {"message": f"server error: {e}"}, 500

#     def delete(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("id", required=True, type=int)
#         args = parser.parse_args()

#         try:
#             timer = db.session.query(Timer).get(args["id"])
#             if timer:
#                 db.session.delete(timer)
#                 db.session.commit()
#                 return timer.to_dict()
#             else:
#                 return {"message": "todo not found"}, 404
#         except Exception as e:
#             db.session.rollback()
#             return {"message": f"server error: {e}"}, 500


# class TimerListAPI(Resource):
#     def get(self):
#         timers = db.session.query(Timer).all()
#         return [timer.to_dict() for timer in timers]


# timer_api.add_resource(TimerAPI, "/timer")
# timer_api.add_resource(TimerListAPI, "/timerList")
