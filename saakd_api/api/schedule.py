# FLASK API FILE

# imports dependencies of program
from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.schedules import Schedule

# setting variables used to store future data
schedule_bp = Blueprint("schedule", __name__)
schedule_api = Api(schedule_bp)

# this class is the resource for the flask API, which allows to user to use methods to store data
class ScheduleAPI(Resource):
    # GET method
    def get(self):
        # requested id turned into variable for later use
        id = request.args.get("id")
        # this looks through the database by id and finds the id that you are requesting
        schedule = db.session.query(Schedule).get(id)
        if schedule:
            # data is sent to the frontend
            return schedule.to_dict()
        # error checking
        return {"message": "schedule not found"}, 404

    # POST method
    def post(self):
        # using parsers to gather and data that is to be posted and validate it's true
        parser = reqparse.RequestParser()
        parser.add_argument("period", required=True, type=int)
        parser.add_argument("class1", required=False, type=str)
        parser.add_argument("classNumber", required=False, type=str)
        parser.add_argument("startTime", required=False, type=str)
        parser.add_argument("endTime", required=False, type=str)
        # variable made to store data
        args = parser.parse_args()
        # variable created to format all data into one place and send to database for logging
        schedule = Schedule(args["period"], args["class1"], args["classNumber"], args["startTime"], args["endTime"])
        try:
            # data is sent to the database for storage
            db.session.add(schedule)
            db.session.commit()
            return schedule.to_dict(), 201
        except Exception as e:
            # error checking
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    # PUT method
    def put(self):
        # parser made to search through all incoming requests
        parser = reqparse.RequestParser()
        # argument expected is set, in this case the id
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            # looks through database, looking for id that needs to be edited
            schedule = db.session.query(Schedule).get(args["id"])
            if schedule:
                # adds in edited data
                db.session.commit()
            else:
                # returns data if id is not found
                return {"message": "schedule not found"}, 404
        except Exception as e:
            # returns data if there's an error in the request
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    # DELETE method
    def delete(self):
        # parser made to search through all incoming requests
        parser = reqparse.RequestParser()
        # argument expected is set, in this case the id
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            # looks through database, looking for id that needs to be deleted
            schedule = db.session.query(Schedule).get(args["id"])
            if schedule:
                # that row with info is deleted
                db.session.delete(schedule)
                db.session.commit()
                return schedule.to_dict()
            else:
                # checks if theres an error with finding the id
                return {"message": "schedule not found"}, 404
        except Exception as e:
            # checks if there's an error with request
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

# new class that includes all data, rather than individual, only has 2 methods
class ScheduleListAPI(Resource):
    # GET method
    def get(self):
        # looks through entire database
        schedules = db.session.query(Schedule).all()
        # pulls all data
        return [schedule.to_dict() for schedule in schedules]

    # DELETE method
    def delete(self):
        try:
            # deletes entire database resource 
            db.session.query(Schedule).delete()
            db.session.commit()
            return []
        except Exception as e:
            # checks for errors in with request
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

# link extensions of each class
schedule_api.add_resource(ScheduleAPI, "/schedule")
schedule_api.add_resource(ScheduleListAPI, "/scheduleList")
