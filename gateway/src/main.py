from flask import Flask,jsonify,request,render_template
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/", methods=['GET','POST'])
def gateway():
    api_login = 'http://localhost:5100/login'
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        data = {
            'usuario' : nombre,
            'password' : password
        }
        try:
            response = requests.post(api_login, json=data)
            if response.status_code == 200:
                respuesta = response.json()
                return jsonify(respuesta)
            else:
                return 'Error al enviar los datos al otro microservicio', 500
        except requests.exceptions.RequestException as e:
        # Capturar excepciones si la solicitud falla
            return jsonify({'error': 'El servicio está fuera de servicio'}), 503
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.run(port=os.getenv('PORTGATEWAY'),
            debug=True)