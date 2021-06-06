from flask import Flask, request
from flask_restful import Resource, Api, reqparse
# from nlp.similarity import Detect
from nlp.gpt_generation import TextGenerationGpt2

app = Flask(__name__)
api = Api(app)


# api.add_resource(Detect, '/detect')
api.add_resource(TextGenerationGpt2, '/generate')

app.run(port=5000)