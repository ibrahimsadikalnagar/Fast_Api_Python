from fastapi import APIRouter
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)
@router.post("/")
def post_Data():
    pass