from fastapi import FastAPI
appp = FastAPI()
@appp.get("/")
def index():
    return {"message": "Hello ibrahim"}