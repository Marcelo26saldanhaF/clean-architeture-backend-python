from src.domain.model import User
from src.domain.test import mock_users
from typing import List

class UserRepositorySpy:
    """ spy to user repository """

    def __init__(self) -> None:
        self.insert_user_parms={}
        self.select_user_params={}


    def insert_user(self,name:str,password:str)->User:
        """spy all the attributes"""
        self.insert_user_parms['name']=name
        self.insert_user_parms['password']=password

        return mock_users(name=name,password=password)
    
    def select_user(self,user_id:int=None,name:str=None)->List[User]:
        """spy all the attributes"""
        self.select_user_params['user_id']=user_id
        self.select_user_params['name']=name

        return [mock_users()]