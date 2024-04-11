import pytest
from main import app as app_login

@pytest.fixture()
def app():
    yield app_login

@pytest.fixture()
def client(app):
    return app.test_client()
