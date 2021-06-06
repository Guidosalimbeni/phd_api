# from flask import Flask, jsonify, request
# from flask_restful import Resource

# class Detect(Resource):
#     def post(self):
#         #Step 1 get the posted data
#         postedData = request.get_json()
#         text1 = postedData["text1"]
#         text2 = postedData["text2"]


#         #Calculate edit distance between text1, text2
#         import spacy
#         nlp = spacy.load('en_core_web_sm')
#         text1 = nlp(text1)
#         text2 = nlp(text2)

#         ratio = text1.similarity(text2)

#         retJson = {
#             "status":200,
#             "ratio": ratio,
#             "msg":"Similarity score calculated successfully"
#         }


#         return jsonify(retJson)