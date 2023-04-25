"""aqui é o caso de uso de verdade"""
from src.domain.use_cases import RegisterUserInterface
from typing import Type,Dict
from src.data.interfaces import UserRepositoryInterface
from src.domain.model import User

class RegisterUser(RegisterUserInterface):
    """Cllass to define use case: Register User"""

    def __init__(self,user_repository:Type[UserRepositoryInterface]) -> None:
        self.user_repository=user_repository

    def register(self, name:str, password: str) -> Dict[bool, User]:
        """ Register user use case
            :param - name: person name
                   - password: password of the person
            : return - Dictionary with information about the process
        """
        response=None
        
        validate_entry = isinstance(name,str) and isinstance(password,str)
        if validate_entry:
            response=self.user_repository.insert_user(name,password)

        return {"Success":validate_entry,"Data":response}