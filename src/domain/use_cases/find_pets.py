from abc import ABC, abstractclassmethod
from src.domain.model import Pet
from typing import List,Dict

class FindPetInterface(ABC):
    """Use case """

    @abstractclassmethod
    def by_pet_id(cls,pet_id:int)->Dict[bool,List[Pet]]:
        """abstract method"""
        raise Exception("The method must be implemented")

    def by_user_id(cls,user_id:int)->Dict[bool,List[Pet]]:
        """abstract method"""
        raise Exception("The method must be implemented")
    
    def by_pet_id_and_user_id(cls,pet_id:int,user_id:int)->Dict[bool,List[Pet]]:
        """abstract method"""
        raise Exception("The method must be implemented")