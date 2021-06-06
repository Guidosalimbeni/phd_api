from transformers import pipeline, set_seed
from flask import Flask, jsonify, request
from flask_restful import Resource

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

class TextGenerationGpt2(Resource):
    def post(self):
        #Step 1 get the posted data
        postedData = request.get_json()
        text = postedData["user_text"]
        
        chat_list = generator(str(text), max_length=30, num_return_sequences=2) 
        chat = chat_list[0]
        retJson = {
            "status":200,
            "ratio": chat,
            "msg":"text generated successfully"
        }

        return jsonify(retJson)
