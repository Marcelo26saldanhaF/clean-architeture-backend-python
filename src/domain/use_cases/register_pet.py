from abc import ABC,abstractclassmethod
from typing import Dict
from src.domain.model import Pet




class RegisterPetInterface(ABC):
    """Interface to FindÈt use case"""
     
    @abstractclassmethod
    def register(cls,name:str,specie:str,user_information:Dict[int,str],age:int=None)->Dict[bool,Pet]:
        """use case"""
        raise Exception("Method must be implented")
    