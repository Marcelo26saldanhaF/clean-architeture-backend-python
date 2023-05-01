from typing import Dict
from src.domain.model import User
from src.domain.test import mock_users



class RegisterUserSpy:
    """class to simulation use case Register Use"""

    def __init__(self,repository_use:any) -> None:
        self.repository_use_params={}

    def register(self, name:str, password: str) -> Dict[bool, User]:
        """test Register user use case
        :param - name: person name
                - password: password of the person
        : return - Dictionary with information about the process
        """
        self.repository_use_params['name']=name
        self.repository_use_params['password']=password
        response=None

        validate_entry = isinstance(name,str) and isinstance(password,str)
        if validate_entry:
            response=mock_users()

        return {"Success":validate_entry,"Data":response}