# File Name: app.py
# Original Author: Jesse Malinen/blank-py
# Description: Main app script

# imports
from flask import Flask
from flask_restful import Api

from config import Config 
from extensions import db 

from resources.user import UserListResource
from resources.spaces import SpaceListResource, SpaceResource
from resources.reservations import ReservationListResource, ReservationResource


# app definition
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    register_extensions(app)
    register_resources(app)
    
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app)

def register_resources(app):
    api = Api(app)
    
    api.add_resource(UserListResource, '/users')
    api.add_resource(SpaceListResource, '/spaces')
    api.add_resource(SpaceResource, '/spaces/<int:space_id>')
    api.add_resource(ReservationListResource, '/reservations')
    api.add_resource(ReservationResource, '/reservations/<int:reservation_id>')
    
if __name__ == '__main__':
    app = create_app()
    app.run

