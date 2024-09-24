#!/usr/bin/env python3

import os

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Mission, Planet, Scientist, db
from werkzeug.exceptions import NotFound

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db, render_as_batch=True)

Api.error_router = lambda self, router, error: router(error)
api = Api(app)

db.init_app(app)

class Scientists(Resource):
    def get(self):
        scientists = Scientist.query.all()
        sc_dicts = [scientist.to_dict(rules=("-missions",)) for scientist in scientists]
        return make_response(sc_dicts, 200)
    
    def post(self):
        req_json = request.get_json()
        try:
            sci = Scientist(**req_json)
        except Exception as e:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(sci)
        db.session.commit()
        return make_response(sci.to_dict(), 201)
    
class ScientistById(Resource):
    def get(self, id):
        sci = Scientist.query.get(id)
        if not sci:
            raise NotFound
        return make_response(sci.to_dict(), 200)
    
    def patch(self, id):
        sci = Scientist.query.get(id)
        if not sci:
            raise NotFound
        req_json = request.get_json()
        try:
            for field, value in req_json.items():
                setattr(sci, field, value)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
    
        db.session.commit()
        return make_response(sci.to_dict(), 202)

    
    def delete(self, id):
        sci = Scientist.query.get(id)
        if not sci:
            raise NotFound
        db.session.delete(sci)
        db.session.commit()
        return make_response({}, 204)
    
class Planets(Resource):
    def get(self):
        planets = Planet.query.all()
        return make_response([p.to_dict(rules=("-missions",)) for p in planets], 200)
    
class Missions(Resource):
    def post(self):
        req_json = request.get_json()
        try:
            mis = Mission(**req_json)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(mis)
        db.session.commit()
        return make_response(mis.to_dict(), 201)
        
    
api.add_resource(Scientists, '/scientists')
api.add_resource(ScientistById, '/scientists/<int:id>')
api.add_resource(Planets, "/planets")
api.add_resource(Missions, "/missions")

@app.errorhandler(NotFound)
def handle_404(exception):
    # path = request.path
    # cleaned_path = ''.join(char for char in path if char.isalpha())[:-1]
    # response = make_response({"error": f"{cleaned_path.title()} not found"}, 404)
    print(exception)
    response = make_response({"error": f"{request.path.rstrip('1234567890/s').lstrip('/').title()} not found"})
    return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)
