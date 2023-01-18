from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.calculators import Calculator

calculator_bp = Blueprint("calculators", __name__)
calculator_api = Api(calculator_bp)


class CalculatorAPI(Resource):
    def get(self, id):
        calculator = db.session.query(Calculator).get(id)
        if calculator:
            return calculator.to_dict()
        return {"message": "calculator not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("expression", required=True, type=str)
        parser.add_argument("output", required=True, type=str)
        args = parser.parse_args()

        calculator = Calculator(args["expression"],args["output"])
        try:
            db.session.add(calculator)
            db.session.commit()
            return calculator.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("expression", required=True, type=str)
        parser.add_argument("output", required=True, type=str)
        args = parser.parse_args()

        try:
            calculator = db.session.query(Calculator).get(args["id"])
            if calculator:
                calculator.expression = args["expression"]
                db.session.commit()
            else:
                return {"message": "calculator not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            calculator = db.session.query(Calculator).get(args["id"])
            if calculator:
                db.session.delete(calculator)
                db.session.commit()
                return calculator.to_dict()
            else:
                return {"message": "calculator not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class CalculatorListAPI(Resource):
    def get(self):
        calculators = db.session.query(Calculator).all()
        return [calculator.to_dict() for calculator in calculators]


calculator_api.add_resource(CalculatorAPI, "/calculator")
calculator_api.add_resource(CalculatorListAPI, "/calculatorList")
