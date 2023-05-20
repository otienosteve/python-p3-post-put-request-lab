import pytest 
from fastapi.testclient import TestClient
from main import app 
from models.employee import session, Employee



@pytest.fixture
def Client():
    return TestClient(app)

@pytest.fixture(scope='session')
def employee():

    yield {
"id": 707,
"first_name": "Purity",
"last_name": "Edwards",
"email": "Pedwars@jigsy.com",
"age": 38,
"gender": "Female",
"phone_number": 6469701273,
"salary": 121396,
"designation": "Surveyor"
}
    

def test_root(Client):
    res=Client.get('/')
    assert res.json() == {'success' : "root"}

def test_post(Client, employee):
    res = Client.post('/add_employee', headers={'content-type':'application/json' ,'accept':'application/json'} ,json=employee)
    added = session.query(Employee).filter_by(id=employee['id']).first()
    assert added, f"Post Operation unsuccessful" 
    session.query(Employee).filter_by(id=707).delete()

