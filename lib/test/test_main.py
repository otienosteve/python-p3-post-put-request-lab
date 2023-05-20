import pytest 
from fastapi.testclient import TestClient
from main import app 
from models.employee import session, Employee
from sqlalchemy import  delete

# Post setup teardown
@pytest.fixture(scope='function')
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
    emp = session.query(Employee).filter_by(id=707).first()
    session.delete(emp)
    session.commit()

# Existing data Post setup teardown
@pytest.fixture
def Client():
    return TestClient(app)


@pytest.fixture(scope='session')
def employee_set_unset():
    create = Employee(**dict(exist_data))
    session.add(create)
    session.commit()
    yield {
"id": 109,
"first_name": "Cosmas",
"last_name": "Light",
"email": "Clight@jigsy.com",
"age": 20,
"gender": "Male",
"phone_number": 6469701273,
"salary": 521396,
"designation": "Cook"
}
    emp = session.query(Employee).filter_by(id=707).first()
    session.delete(emp)
    session.commit()

# Post tests
def test_post(Client, employee): 
    res = Client.post('/add_employee', headers={"content-type":"application/json"} ,json=employee)
    assert res.json() == employee
   
    assert res.status_code == 201, 'Output Correct status Code {res.status_code}'

# existing post data test
def test_existing_item(Client):
    res = Client.post('/add_employee',headers={'content-type':'application/json' ,'accept':'application/json'}, json=exist_data)
    assert res.json()== {"status_code": 400, "detail":"Employee Already Exists", "headers":"content-type: application/json"}
    assert res.status_code == 400 , f'Failed to return status code'




