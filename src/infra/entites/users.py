from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config import Base


class User(Base):
    """User Entity"""
    __tablename__="users"
    id=Column(Integer(),primary_key=True,autoincrement=True)
    name=Column(String(),nullable=False,unique=True)
    password=Column(String(),nullable=False)
    id_pet=relationship("Pets")


    def __repr__(self)->str:
        return f'User [name={self.name}]'