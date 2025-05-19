from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer , String




class DbUser(Base): 
    __tablename__ ='user'
    Id = Column(Integer , primary_key=True , index= True )
    Username = Column(String)
    Email = Column(String)
    Password = Column(String)

