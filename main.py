from fastapi import FastAPI 

app = FastAPI()
@app.get("/")
def simple():
    return {"message Hello api"}

