from flask import Flask,jsonify,request,render_template,flash,redirect,url_for,session
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
app.config.update(PERMANENT_SESSION_LIFETIME=60)

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

@app.route('/home')
def home():
    if 'username' in session : 
        usename = session['username']
        print(usename)
        return render_template('menu.html', username = usename)
    else:
        return redirect(url_for('gateway'))


if __name__ == "__main__":
    app.run(port=os.getenv('PORTGATEWAY'),
            debug=True)