from flask import Flask, jsonify,request,flash
from dotenv import load_dotenv
import requests
import secrets
import os
from utils.conection_db import condb 
from utils.encrip_pass import verify_pass

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/login", methods=['POST'])
def index():
    data = request.get_json()
    username = data['usuario']
    password = data['password']
    cursor = condb.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,) )
    result = cursor.fetchone()
    print(result)
    cursor.close()
    if result != None :
        if verify_pass(bytes(result[2], 'utf-8'),password):
            return jsonify({'message': 'Registro valido', 'usuario': username, 'roll' :result[3]})
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'})
    else:
        return jsonify({'message': 'Usuario o contraseña incorrectos'})
    
@app.route('/', methods=['POST'])
def ppp():
    return "hello word"

if __name__ == "__main__":
    app.run(port=os.getenv('PORTLOGINSERVICE'),
             debug=True)