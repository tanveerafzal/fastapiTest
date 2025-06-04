from fastapi import FastAPI
from app.multiply_script import multiply
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render!"}


@app.get("/multiply")
def multiply_route(a: int, b: int):
    return {"result": multiply(a, b)}

@app.get("/wait")
def wait_api():
    time.sleep(60)  # Wait for 60 seconds (synchronous)
    return {"message": "Done waiting for 1 minute"}
    
