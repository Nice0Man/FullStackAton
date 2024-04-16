# src/api/v1/__init__.py

from fastapi import FastAPI

app = FastAPI(title="Resume-API")


@app.get("/")
def hello():
    return {"message": "Hello, World!"}
