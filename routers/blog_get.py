from routers.blog_post import requestt
from fastapi import APIRouter , status , Response , Depends
from enum import Enum
from typing import Optional

router = APIRouter(
     prefix='/blog',
     tags=['blog']
)

@router.get("/tasks")
def get_another_Method():
    return {"Hello with tasks "}
@router.get("/tasks/todo")
def get_another_return():
    return {
        "message " : "I started to get what i am doing i am start to now fast today "
        }

# @app.post("/")
# def get_method_Post():
#     return {"i am post it and i want to see how is it "}
@router.get("/blog/all")
def GetAll():
    return {"message" :" i am modee and i want vahsa  "}

class blogType(str , Enum):
        short = "short"
        long = "long"
        howto = "howto"
        mybrother ="ismail"

@router.get("/taskss/{type}" 
         
          )
def UseGetEnum(type :blogType  ):
     return {"message":f"Hello Enum:{type}"}

@router.get("/get")
def putPerameter(pages = 1, numberPages: Optional[int] = None):
     return {"message" : f"the total pages is {pages} and you are in number {numberPages}"}


@router.get("/try/{id}/comment/{commit_Id}")
def get_all_blog(id: int , commit_Id : int , valid : bool = True , username :Optional[str] = None):
     return {"message":f"id : {id} , commit_Id : {commit_Id} , valid : {valid} , username : {username}"}


@router.get("/ismail/{id}" , status_code= status.HTTP_102_PROCESSING , 
           tags= ['isn' ,'YTy'] ,
          summary="this is to try summary"
          , description="i want to try also the description of the parameters" )
def GetIsmailId(id : int , response : Response , requestt: dict = Depends(requestt)):
    if id > 5 : 
        response.status_code = status.HTTP_404_NOT_FOUND
        return {f"Id  {id} is not found" ,"Req: : {requestt}"}
    else: 
         response.status_code = status.HTTP_200_OK
         return {f"id {id} is found"}


