from fastapi import FastAPI
from pydantic import BaseModel


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


@app.post('/add_employee')
def add_employee(payload: EmployeeSchema) -> EmployeeSchema:

    return {"detail" :"success"}