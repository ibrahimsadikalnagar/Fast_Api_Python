
from fastapi import FastAPI
from db.database import engine, Base
from routers import blog_get
from routers import blog_post

from routers import user
import db.models  # this registers your models with SQLAlchemy

app = FastAPI()


# Include routers
app.include_router(user.router)
app.include_router(blog_post.router)
app.include_router(blog_get.router)

# Create all tables
Base.metadata.create_all(engine)

@app.get("/")
def simple():
    return {"message": "Hello api"}
