from flask import Flask,jsonify,request,render_template,flash,redirect,url_for,session
import requests
from dotenv import load_dotenv
import os
from utils.createjson import createjson 

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
app.config.update(PERMANENT_SESSION_LIFETIME=240)

@app.route("/", methods=['GET','POST'])
def gateway():
    loginservice = os.getenv('LOGINSERVICE')
    portloginservice = os.getenv('PORTLOGINSERVICE')
    api_login = f'http://{loginservice}:{portloginservice}/login'
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        data = {
            'usuario' : nombre,
            'password' : password
        }
        try:
            response = requests.post(api_login, json=data)
            respuesta = response.json()
            print(respuesta, "esto es de aca")
            if response.status_code == 200:
                if 'usuario' in respuesta:
                    session['username'] = [respuesta['usuario'],respuesta['roll']]
                    session.permanent = True
                    return redirect(url_for('home'))  
                else:
                    flash(f"{respuesta['message']}")
                    return redirect(url_for('gateway'))
            else:
                return 'Error al enviar los datos al otro microservicio', 500
        except requests.exceptions.RequestException as e:
        # Capturar excepciones si la solicitud falla
            return jsonify({'error': 'El servicio está fuera de servicio'}), 503
    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def home():
    operationservice = os.getenv('OPERATIONSSERVICE')
    portoperationservice = os.getenv('PORTOPERATIONSSERVICE')
    api_operatios = f'http://{operationservice}:{portoperationservice}/createoperations'
    print(api_operatios)
    if 'username' in session : 
        usename = session['username']
        usr = usename[1]
        if request.method == 'POST':
            respuesta = request.form
            respues = createjson(respuesta)
            json = { 'usuario' : f'{usr}', 'productos' : respues }
            print(json)
            try:
                response = requests.post(api_operatios, json=json)
                print(response)
                respuesta = response.json()
                if response.status_code == 200:
                    flash(f"{respuesta['message']}")
                    return redirect(url_for('home'))  
                else:
                    flash(f"{respuesta['message']}")
                    return redirect(url_for('home')) 
            except requests.exceptions.RequestException as e:
            # Capturar excepciones si la solicitud falla
                return jsonify({'error': 'El servicio está fuera de servicio'}), 503
        return render_template('menu.html', username = usename)
    else:
        return redirect(url_for('gateway'))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.getenv('PORTGATEWAY'),
            debug=True)