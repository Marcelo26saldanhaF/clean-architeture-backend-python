from sqlalchemy import Column,Integer,String,ForeignKey,Enum
from src.infra.config import Base
import enum

class AnimalTypes(enum.Enum):
    """Defining Animals Types"""
    DOG="dog"
    CAT="cat"
    FISH="fish"
    TURTLUE="turtlue"

class Pets(Base):
    """Pets Entity"""
    __tablename__="pets"
    id=Column(Integer(),primary_key=True,autoincrement=True)
    name=Column(String(20),nullable=False,unique=True)
    specie=Column(Enum(AnimalTypes),nullable=False)
    age=Column(Integer())
    user_id=Column(Integer(),ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f'Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]'