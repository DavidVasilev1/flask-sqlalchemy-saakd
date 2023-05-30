from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.players import Player

# Change variable name and API name and prefix
player_api = Blueprint('player_api', __name__,
                   url_prefix='/api/players')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(player_api)

class PlayerAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data from json body '''
            body = request.get_json()
            
            ''' Sanitizing '''
            # check name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # check uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # get info from request body
            password = body.get('password')
            tokens = body.get('tokens')

            ''' #1: Key code block, setup USER OBJECT '''
            newPlayer = Player(
                    name=name, 
                    uid=uid,
                    tokens=tokens,
                    )
            
            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                newPlayer.set_password(password)            
            
            ''' #2: Key Code block to add user to database '''
            # create player in database
            player = newPlayer.create()
            # if successful, it will return the new json object that is added
            if player:
                return jsonify(player.read())
            # incase of failure, it will return an error
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            players = Player.query.all()    # read/extract all users from database
            json_ready = [player.read() for player in players]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Update(Resource):
        def put(self):
            body = request.get_json() # get the body of the request
            uidFromBody = body.get('uid') # get the UID (Know what to reference)
            data = body.get('data') # get what needs to be updated
            user = Player.query.filter_by(_uid = uidFromBody).first() # get the user (using the uid in this case)
            user.update(data)
            return f"{user.read()} Updated"

    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            uidFromBody = body.get('uid')
            user = Player.query.filter_by(_uid = uidFromBody).first() # get the user that needs to be deleted
            user.delete()
            return f"{user.read()} Has been deleted"

    class _Security(Resource):

        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Get Data '''
            uid = body.get('uid')
            if uid is None or len(uid) < 1:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 400
            password = body.get('password')
            
            ''' Find user '''
            user = Player.query.filter_by(_uid=uid).first()
            if user is None or not user.is_password(password):
                return {'message': f"Invalid user id or password"}, 400
            
            ''' authenticated user '''
            return jsonify(user.read())

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Update, '/update')
    api.add_resource(_Security, '/authenticate') 