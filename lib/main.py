# Write your solution here ✍️
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"detail" :"Ready, Set, Go"}