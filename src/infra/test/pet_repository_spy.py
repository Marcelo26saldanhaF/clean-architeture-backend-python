from src.domain.model import Pet
from typing import List
from src.domain.test import mock_pets



class PetRepositorySpy:

    def __init__(self) -> None:
        self.insert_pet_params={}
        self.select_pet_params={}
    
    def insert_pet(self,name:str,specie:str,user_id:int,age:int=None,):
        """this method is use to test"""
        self.insert_pet_params['name']=name
        self.insert_pet_params['specie']=specie
        self.insert_pet_params['user_id']=user_id
        self.insert_pet_params['age']=age

        return mock_pets()
    
    def select_pet(self,user_id:int=None,pet_id:int=None)->List[Pet]:
        """this method is use to test """
        self.select_pet_params['pet_id']=pet_id
        self.select_pet_params['user_id']=user_id

        return [mock_pets()]