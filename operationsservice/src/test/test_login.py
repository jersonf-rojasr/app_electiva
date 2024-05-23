from flask import jsonify,json

def test_operations_add(client):
    response = client.post('/createoperations', json={
    "usuario": "pruebas",
    "productos": [
        {
        "id_operacion": "2332",
        "tipo_opereracion": "importacion",
        "cliente": "dswdas",
        "contenedores": "23",
        "valor": "23323"
        }
    ]
    })
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    data = response.json  # Sin paréntesis después de json
    assert 'message' in data
