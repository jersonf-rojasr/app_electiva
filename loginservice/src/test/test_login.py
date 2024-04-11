from flask import jsonify,json

"""def test_login(app,client):
    response =  client.post('/')
    assert response.status_code == 200"""

def test_login(client):
    response = client.post('/login', json={
        "usuario": "test",
        "password": "test"
    })
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    data = response.json  # Sin paréntesis después de json
    assert 'usuario' in data
    assert 'roll' in data

def test_login_fail(client):
    response = client.post('/login', json={
        "usuario": "test",
        "password": "teeeee"
    })
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    data = response.json  # Sin paréntesis después de json
    assert 'message' in data