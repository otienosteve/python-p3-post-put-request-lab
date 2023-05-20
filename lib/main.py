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
    class Config:
        orm_mode = True


# @app.get('/')
# def root() -> None: 
#     return {'success' : "root"}

# 👍 🤔 😕
@app.post('/add_employee', status_code=201)
def add_employee(payload: EmployeeSchema) -> None:
    
    emp = Employee(**dict(payload))
    session.add(emp)
    session.commit()

    return payload