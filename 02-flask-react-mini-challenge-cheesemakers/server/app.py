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
        prod_dicts = [prod.to_dict() for prod in producers]
        return make_response(prod_dicts, 200)


api.add_resource(Producers, "/producers")


@app.route("/")
def index():
    response = make_response({"message": "Hello Fromagers!"}, 200)
    return response


if __name__ == "__main__":
    app.run(port=5555, debug=True)
