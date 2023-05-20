import pytest 
from fastapi.testclient import TestClient
from main import app 
from models.employee import session, Employee

# create client instance
@pytest.fixture
def Client():
    return TestClient(app)

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

exist_data = {
"id": 110,
"first_name": "Cosmas",
"last_name": "Light",
"email": "Clight@jigsy.com",
"age": 20,
"gender": "Male",
"phone_number": 6469701273,
"salary": 521396,
"designation": "Cook"
}
update_data={
"id": 117,
"first_name": "Damian",
"last_name": "Lighter",
"email": "Dlighter@jigsy.com",
"age": 18,
"gender": "Male",
"phone_number": 64654301273,
"salary": 521391236,
"designation": "Waiter"
}

# Existing data Post setup teardown
@pytest.fixture(scope='function')
def exist_data_fix():
    create = Employee(**dict(exist_data))
    session.add(create)
    session.commit()
    yield exist_data
    emp = session.query(Employee).filter_by(id=110).first()
    session.delete(emp)
    session.commit()

# Put request setup teardown
@pytest.fixture(scope='function')
def put_data():
    create = Employee(**dict(update_data))
    session.add(create)
    session.commit()
    yield update_data
    emp = session.query(Employee).filter_by(id=117).first()
    session.delete(emp)
    session.commit()
   
# Post tests
def test_post(Client, employee): 
    res = Client.post('/add_employee', headers={"content-type":"application/json"} ,json=employee)
    assert res.json() == employee
    assert res.status_code == 201, 'Output Correct status Code {res.status_code}'

# existing post data test
def test_existing_item(Client, exist_data_fix):
    res = Client.post('/add_employee',headers={'content-type':'application/json' ,'accept':'application/json'}, json=exist_data_fix)
    assert res.json()== {"detail": "Employee Already Exists"}
    assert res.status_code == 401 , f'Failed to return status code'

def test_put(Client,put_data):
    res = Client.put('/employees/updateall/110', headers={"content-type":"applicatio/json", "accept":"application/json"}, json=put_data)
    res.status_code == 200 , f'Updtae Unsuccessful'
    data = session.query(Employee).filter_by(id=117).first()
    assert data.first_name == 'Damian', f' Unexpected Value {data.first_name}'
    assert data.last_name == 'Lighter', f' Unexpected Value {data.last_name}'
    assert data.email == 'Dlighter@jigsy.com', f' Unexpected Value {data.email}'
    assert data.age == 18, f' Unexpected Value {data.age}'
    assert data.gender == 'Male', f' Unexpected Value {data.gender}'
    assert data.phone_number == 64654301273, f' Unexpected Value {data.phone_number}'
    assert data.designation == 'Waiter', f' Unexpected Value {data.designation}'


    



