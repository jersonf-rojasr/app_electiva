import pytest
from main import app as app_operations

@pytest.fixture()
def app():
    yield app_operations

@pytest.fixture()
def client(app):
    return app.test_client()
