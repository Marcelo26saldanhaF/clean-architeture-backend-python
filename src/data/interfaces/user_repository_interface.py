from abc import ABC,abstractmethod
from src.domain.model import User
from typing import List

class UserRepositoryInterface(ABC):
    """interface for pet repository"""
    @abstractmethod
    def insert_user(self,name:str,password:str)->User:
        """abstract method"""       
        raise Exception('Method not implemented')
    
    @abstractmethod
    def select_user(self,user_id:int=None,name:str=None)->List[User]:        
        """abstract method"""
        raise Exception('Method not implemented')