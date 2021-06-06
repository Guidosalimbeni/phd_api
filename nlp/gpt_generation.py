from transformers import pipeline, set_seed
from flask import Flask, jsonify, request
from flask_restful import Resource
import random


generator = pipeline('text-generation', model='gpt2')
set_seed(42)

class TextGenerationGpt2(Resource):
    def post(self):
        #Step 1 get the posted data
        postedData = request.get_json()
        text = postedData["user_text"]
        number = 3
        chat_list = generator(str(text), max_length=30, num_return_sequences=number) 
        chat = chat_list[random.randint(0,number)]["generated_text"]
        chat = chat.replace(text, "")
        chats = chat.split(".")
        chats_2 = []
        for sent in chats:
            if len(sent) > 0:
                chats_2.append(sent)
        chat = chats_2[0]
        chat = chat.replace(".", "")
        chat = chat + "."
        if chat[0] == " ":
            chat = chat[1:]
        retJson = {
            "status":200,
            "ratio": chat,
            "msg":"text generated successfully"
        }

        return jsonify(retJson)
