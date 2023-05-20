import pytest 
from fastapi.testclient import TestClient
from main import app 



@pytest.fixture
def Client():
    return TestClient(app)

def test_root(Client):
    res=Client.get('/')
    assert res.json() == {'success' : "root"}