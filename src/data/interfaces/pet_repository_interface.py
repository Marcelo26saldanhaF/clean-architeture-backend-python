from abc import ABC,abstractmethod
from src.domain.model import Pet
from typing import List

class PetRepositoryInterface(ABC):
    """interface for pet repository"""
    @abstractmethod
    def insert_pet(self,name:str,specie:str,age:int,user_id:int)->Pet:
        """abstract method"""
        raise Exception('Method not implemented')
    
    @abstractmethod
    def select_pet(self,pet_id:int=None,user_id:int=None)->List[Pet]:
        """abstract method"""
        raise Exception('Method not implemented')
