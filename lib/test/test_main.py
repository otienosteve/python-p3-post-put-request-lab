import pytest 
from fastapi.testclient import TestClient
from main import app 
from models.employee import session, Employee

exist_data = {
"id": 1,
"first_name": "Cosmas",
"last_name": "Light",
"email": "Clight@jigsy.com",
"age": 20,
"gender": "Male",
"phone_number": 6469701273,
"salary": 521396,
"designation": "Cook"
}
new_data =  {
"id": 109,
"first_name": "Purity",
"last_name": "Edwards",
"email": "Pedwars@jigsy.com",
"age": 38,
"gender": "Female",
"phone_number": 6469701273,
"salary": 121396,
"designation": "Surveyor"
}
@pytest.fixture
def Client():
    return TestClient(app)

@pytest.fixture(scope='session')
def employee():

    yield new_data
    session.query(Employee).filter_by(id=707).delete()
    
@pytest.fixture
def employee_set_unset():
      return TestClient(app)

@pytest.fixture(scope='session')
def employee():
    create = Employee(**dict(exist_data))
    session.add(create)
    session.commit()
    yield exist_data
    session.query(Employee).filter_by(id=109).delete()

def test_root(Client):
    res=Client.get('/')
    assert res.json() == {'success' : "root"}

def test_post(Client, employee):
    res = Client.post('/add_employee', headers={'content-type':'application/json' ,'accept':'application/json'} ,json=new_data)
    added = session.query(Employee).filter_by(id=employee['id']).first()
    assert added, f"Post Operation unsuccessful" 

def test_existing_item(Client):
    res = Client.post('/',headers={'content-type':'application/json' ,'accept':'application/json'},json=exist_data)
    assert res.status_code == 404
    assert res.json() == {"detail" : "Employee Already Exists"}


