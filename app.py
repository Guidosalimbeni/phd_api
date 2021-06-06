from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
# from nlp.similarity import Detect
# from nlp.gpt_generation import TextGenerationGpt2


app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        
        retJson = {
            "status":200,
            "ratio": "Hello World",
            "msg":"text generated successfully"
        }

        return jsonify(retJson)

# api.add_resource(Detect, '/detect')
api.add_resource(Hello, '/')
# api.add_resource(TextGenerationGpt2, '/generate')

app.run(port=5000)