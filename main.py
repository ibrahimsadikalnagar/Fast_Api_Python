from fastapi import FastAPI
app = FastAPI()
@app.get("/tasks")
def index():
    return {"message": "Hello ibrahim"}