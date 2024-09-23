from flask import Flask, jsonify, make_response, request
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


api.add_resource(Producers, "/producers")
api.add_resource(ProducerByID, "/producers/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
