from abc import ABC,abstractclassmethod
from src.domain.model import User
from typing import List,Dict



class FindUserInterface(ABC):
    """Abstract class to use case"""

    @abstractclassmethod
    def by_id(cls,user_id:int)->Dict[bool,List[User]]:
        """ Specific case """
        raise Exception("Method must be implemented ")
    
    @abstractclassmethod
    def by_name(cls,name:str,)->Dict[bool,List[User]]:
        """Specif case"""
        raise Exception("Method must be implemented")
    

    @abstractclassmethod
    def by_id_and_name(cls,user_id:int,name:str)->Dict[bool,List[User]]:
        """Specif case"""
        raise Exception("Method must be implemented")