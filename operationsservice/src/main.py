from flask import Flask, jsonify,request,flash
from dotenv import load_dotenv
import os
from utils.conection_db import condb 

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/createoperations", methods=['POST'])
def createoperations():
    data = request.get_json()
    valores_ = data['productos']
    cursor = condb.cursor()
    query = """
        INSERT INTO operaciones (id_operacion, tipo_opereracion, cliente, contenedores, valor, usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
    valores = []
    for i in valores_: 
        valores.append((int(i['id_operacion']), i['tipo_opereracion'], i['cliente'], int(i['contenedores']), int(i['valor']), data['usuario']))
    cursor.executemany(query, valores)
    condb.commit()
    cursor.close()
    return jsonify({ 'message' : 'Operaciones ingresadas con exito'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORTLOGINSERVICE'), debug=True)