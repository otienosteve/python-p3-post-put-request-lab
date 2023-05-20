from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from models.employee import session, Employee

app= FastAPI()
class EmployeeSchema(BaseModel):
    id : int
    first_name : str
    last_name : str
    email : str
    age : int
    gender : str
    phone_number : int
    salary : int 
    designation : str


@app.get('/')
def root() -> None: 
    return {'success' : "root"}

# 👍 🤔 😕
@app.post('/add_employee')
def add_employee(payload: EmployeeSchema) -> EmployeeSchema:
    payload = dict(payload)
    exist = session.query(Employee).filter_by(id=payload['id'])
    if exist:
        raise HTTPException(status_code=400, detail="Employee Already Exists")
    emp = Employee(**payload)
    session.add(emp)
    session.commit()

    return payload