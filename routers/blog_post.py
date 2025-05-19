from fastapi import APIRouter
from pydantic import BaseModel 
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title : str
    content : str
    nb_comments : int 
    published : Optional[bool]

@router.post("/{id}")
def post_Data(blog : BlogModel , id : int , version = 1 ):
    return {'data':blog , 'id': id }

def requestt():
    return "Hello to every one i am independency"