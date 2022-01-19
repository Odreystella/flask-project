from flask import Flask
from flask_restx import Api

from healthcare.controller import StatisticsView, ConceptInfoView


app = Flask(__name__)
api = Api(app)

api.add_resource(StatisticsView, "/statistics")
api.add_resource(ConceptInfoView, "/concept")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
