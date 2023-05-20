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
# 👍 🤔 😕 🤗 ✍️
@app.post('/add_employee', status_code=201)
def add_employee(payload: EmployeeSchema) -> None:
    emp = session.query(Employee).filter_by(id=payload.id).first()
    if emp:
        raise HTTPException(status_code=401, detail='Employee Already Exists' )
    else:
        newemp = Employee(**dict(payload))
        session.add(newemp)
        session.commit()

    return payload

@app.put("/employees/updateall/{employee_id}", status_code=202)
def update_all(employee_id: int, payload: EmployeeSchema) ->EmployeeSchema:
    emp = session.query(Employee).filter_by(id=employee_id).first()
    for key, value in emp:
        setattr(emp, key, value)
    session.commit()



