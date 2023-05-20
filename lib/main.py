from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def root() -> None: 
    return {'success' : "root"}