# FAST API POST PUT REQUEST LAB
### setup 

Fork and clone this repo, then navigate into the cloned folder 

spawn a virtual environment `pipenv shell`

install relevant dependencies `pipenv install`

Here's the directory structure for our application
```
├── alembic
├── lib
│   ├── test
|   |   |──test_main.py
|   |   |
│   │── employee.py
│   ├── main.py
├── Pipfile
├── Pipfile.lock
|── README.md

```
Similar to the Previous GET Lab you will be working with data concerning Employees
The Employee Model has been created and is available  in the models directory under the lib folder, ceate and run your migrations.  

Inside the lib folder you will find a file `main.py` where you are expected to write your solution. 

The Schema for the Employee Model you will be working with is similar to the one from the GET request Lab.

```
id: Integer
last_name -> String 
firs_tname -> String 
email -> String 
age -> Integer
gender -> String
phone_number -> Integer 
salary -> Integer
designation -> String
```
Create a corresponding Pydantic class called `EmployeeSchema` for the model and use it to annotate your endpoints as per the return type.   
Add validation to your employee fields as follows. 
`last_name and first_name should include at least 2 characters` 
`email should be valid` 
`Gender should be Male or Female`   
`Age should be greater than 18`  
`Salary should be between 30,000 - 200,000` 

Implement the following endpoints and the required functionality.

- `POST /add_employee`: creates a new Employee Instance when supplied with an JSON Object of the employee data, It should also respond with the appropriate status code
    - implement an error handler for a non existent entry in the database which should yield the appropriate status code and the message "Employee already exists"
- `PUT  '/employees/full_update/:id`: updates all the details of employee with the corresponding id,
it should respond with appropriate status code.


To run your server run `uvicorn lib.main:app` 
or `uvicorn lib.main:app --reload` to enable reloading on file changes 

To test your solution run ` pytest `

## Resources 

[POST  Requests With FastAPI](https://fastapi.tiangolo.com/tutorial/body/)   
[PUT REquest With FastAPi](https://fastapi.tiangolo.com/tutorial/body-updates/)    
[Error Handling in FastAPI](https://fastapi.tiangolo.com/tutorial/handling-errors/)    
 

