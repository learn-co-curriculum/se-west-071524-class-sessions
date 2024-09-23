from datetime import datetime

import ipdb
from flask import Flask, abort, jsonify, make_response, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Cheese, Producer, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


class Producers(Resource):
    def get(self):
        producers = Producer.query.all()
        prod_dicts = [prod.to_dict(rules=("-cheeses",)) for prod in producers]
        return make_response(prod_dicts, 200)


class ProducerByID(Resource):
    def get(self, id):
        producer = Producer.query.filter(Producer.id == id).first()
        if not producer:
            return make_response({"error": "Resource not found"}, 404)
        return make_response(producer.to_dict(), 200)

    def delete(self, id):
        producer = Producer.query.filter(Producer.id == id).first()
        if not producer:
            return make_response({"error": "Resource not found"}, 404)
        db.session.delete(producer)
        db.session.commit()
        return make_response("", 204)


class Cheeses(Resource):
    def post(self):
        req_dict = request.get_json()
        # ipdb.set_trace()
        try:
            format = "%Y-%m-%d"
            req_dict["production_date"] = datetime.strptime(
                req_dict["production_date"], format
            )
            new_cheese = Cheese(**req_dict)
        except ValueError as e:
            # abort(422, e.args[0])
            return make_response({"errors": ["validation errors"]}, 422)
        db.session.add(new_cheese)
        db.session.commit()
        return make_response(
            new_cheese.to_dict(
                rules=(
                    "-producer.founding_year",
                    "-producer.id",
                    "-producer.image",
                    "-producer.operation_size",
                    "-producer.region",
                )
            ),
            200,
        )


class CheeseByID(Resource):
    def patch(self, id):
        cheese = Cheese.query.get(id)
        if not cheese:
            return make_response({"errors": ["validation errors"]}, 422)
        req_json = request.get_json()
        for attr, value in req_json.items():
            if attr == "production_date":
                value = datetime.strptime(value, "%Y-%m-%d")
            setattr(cheese, attr, value)
        db.session.add(cheese)
        db.session.commit()
        return make_response(cheese.to_dict(rules=("-producer",)), 202)

    def delete(self, id):
        cheese = Cheese.query.get(id)
        if not cheese:
            return make_response({"error": "Resource not found"}, 404)
        db.session.delete(cheese)
        db.session.commit()
        return make_response("", 204)


api.add_resource(Producers, "/producers")
api.add_resource(ProducerByID, "/producers/<int:id>")
api.add_resource(Cheeses, "/cheeses")
api.add_resource(CheeseByID, "/cheeses/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
