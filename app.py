from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, Backend!"}

@app.get("/status")
def get_status():
    return{"status": "running", "message": "Server is working!"}

@app.get("/hello/{name}")
def greet(name: str):
    return{"message": f"Hello, {name}!"}