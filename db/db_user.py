
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser

def create_user(db: Session , request : UserBase):
    new_user = DbUser(
        user_name = request.username,
        email = request.email,
        password = hash(request.password)

               )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

