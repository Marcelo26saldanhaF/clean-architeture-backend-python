from abc import ABC,abstractmethod
from src.domain.model import User
from typing import Dict

class RegisterUserInterface(ABC):
    """Interface to register use case"""
    @abstractmethod
    def register(self,name:str,password:str)->Dict[bool,User]:
        """ Case """
        raise Exception("Must implement method")