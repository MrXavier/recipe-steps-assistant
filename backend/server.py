from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai
import os

import openai_utils
import pandas
import numpy as np
import service

app = Flask(__name__)
cors = CORS(app, support_credentials=True)

openai.api_key = os.environ["OPENAI_API_KEY"]
model_gpt_4="gpt-4" 
model_gpt_3_5_turbo="gpt-3.5-turbo" 

@app.route('/')
def home():
    return 'Home Page Route'

@app.route('/about')
def about():
    return 'About Page Route'

@app.route('/completion', methods=['POST'])
@cross_origin(supports_credentials=True)
def completion():
    data = request.get_json()
    response = service.handle_completion(data)
    return jsonify({'completion': response})


if __name__ == '__main__':
    app.run(debug=True)
