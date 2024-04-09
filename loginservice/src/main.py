from flask import Flask, jsonify,request
from dotenv import load_dotenv
import requests
import secrets
import os
from db import usuarios


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')


@app.route("/login", methods=['GET','POST'])
def index():
    data = request.get_json()
    print(data['usuario'])
    for ele in usuarios:
        print(ele)
        if data['usuario'] == ele['usuario'] :
            print(ele)
            env_session = {'usuario' : data['usuario'], 'token': secrets.token_hex()}
            return jsonify(env_session)
    return jsonify({
        'message': 'user not found'
            })
    
if __name__ == "__main__":
    app.run(port=os.getenv('PORTLOGINSERVICE'),
             debug=True)