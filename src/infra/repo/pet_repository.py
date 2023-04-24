from src.infra.entites import Pets as PetsModel
from src.domain.model import Pet
from src.infra.config import DBConnectionHanddler
from typing import List
from sqlalchemy import select,and_
from src.data.interfaces import PetRepositoryInterface

class Pet_repository(PetRepositoryInterface):
    """class to manager pets"""

    @classmethod
    def insert_pet(cls,name:str,specie:str,age:int,user_id:int)->Pet:
        """insert a new pet"""
        with DBConnectionHanddler() as db_conn:
            try:
                new_pet=PetsModel(name=name,specie=specie,age=age,user_id=user_id)
                db_conn.session.add(new_pet)
                db_conn.session.commit()
                return Pet(
                    id=new_pet.id,
                    age=new_pet.age,
                    name=new_pet.name,
                    specie=new_pet.specie,
                    user_id=new_pet.user_id
                           )
            except Exception as e:
                print(e)
                db_conn.session.rollback()
            finally:
                db_conn.session.close() 
        return None
    
    @classmethod
    def select_pet(cls,pet_id:int=None,user_id:int=None)->List[Pet]:
        """select a pet by pet_id or user_id"""
        with DBConnectionHanddler() as db_conn:
            try:
                query_data=None
                if pet_id and not user_id:
                    stm=select(PetsModel).where(PetsModel.id==pet_id)
                    data=db_conn.session.scalar(stm)
                    query_data=[data]

                elif user_id and not pet_id:
                    stm=select(PetsModel).where(PetsModel.user_id==user_id)
                    data=db_conn.session.scalars(stm).all()
                    query_data=data

                elif pet_id and user_id:
                    stm=select(PetsModel).where(and_(PetsModel.id==pet_id,PetsModel.user_id==user_id))
                    data=db_conn.session.scalars(stm).all()
                    query_data=data
                
                return query_data
            
            except Exception as e:
                db_conn.session.rollback()
                print(e)
            finally:
                db_conn.session.close()

            return None