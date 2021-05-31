from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from nlp.similarity import Detect

app = Flask(__name__)
api = Api(app)


api.add_resource(Detect, '/detect')

app.run(port=5000)