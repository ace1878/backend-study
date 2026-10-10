from fastapi import FastAPI, Path, HTTPException

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

@app.get("/double/{number}")
def double_number(number: int = Path(ge=1, le=100)):
    return {"result": number * 2}

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return {
    "id": 1,
    "title": "My first post",
    "content": "Hello, FastAPI!"
}