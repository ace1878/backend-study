from fastapi import FastAPI, Path, HTTPException

app = FastAPI()
posts = [
    {"id": 1, "title": "First post", "content": "Hello, FastAPI!"},
    {"id": 2, "title": "Second post", "content": "Learning backend!"},
    {"id": 3, "title": "Third post", "content": "Python is fun!"}
]

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
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(
        status_code=404,
        detail="Post not found"
    )   

@app.get("/posts")
def get_posts():
    return posts