from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config import Base
from bcrypt import hashpw,checkpw,gensalt

class User(Base):
    """User Entity"""
    __tablename__="users"
    id=Column(Integer(),primary_key=True,autoincrement=True)
    name=Column(String(),nullable=False,unique=True)
    password=Column(String(),nullable=False)
    id_pet=relationship("Pets")

    def gen_hash(self)->None:
        """on the moment then is created a new user also generated a hash"""
        
        self.password=hashpw(self.password.encode('utf-8'),gensalt(10))

    def verify(self,password)->bool:
        """verify the password and return a bool"""
        return checkpw(password,self.password)
    
    def __eq__(self,other)->bool:
        """compare object"""

        if(self.id==other.id and 
           self.name==other.name and 
           self.password==other.password):
            return True
        return False
        


    def __repr__(self)->str:
        return f'User [name={self.name}]'