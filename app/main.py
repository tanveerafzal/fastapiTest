from fastapi import FastAPI
from app.multiply_script import multiply

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render!"}


@router.get("/multiply")
def multiply_route(a: int, b: int):
    return {"result": multiply(a, b)}
