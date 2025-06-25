from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Greeting API!"}


@app.get("/greet/")
def greet(name: Optional[str] = "Guest"):
    return {"greeting": f"Hello, {name}!"}
