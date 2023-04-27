from typing import Dict,List
from src.domain.test import mock_users
from src.domain.model import User


class FindUserSpy:
    """class to test """
    def __init__(self,user_repository:any) -> None:
        self.user_repository=user_repository 
        self.by_id_param={}
        self.by_name_param={}
        self.by_id_and_name_param={}

    def by_id(self,user_id)->Dict[bool,List[User]]:
        """method to test"""
        self.by_id_param['user_id']=user_id
        response=None
        validate_entry=isinstance(user_id,int)

        if validate_entry:
            response=[mock_users()]
            
        return{'Success':validate_entry,'Data':response}
    
    def by_name(self,name:str)->Dict[bool,List[User]]:
        """method to test """
        self.by_name_param['user_name']=name
        response=None
        validate_entry=isinstance(name,str)

        if validate_entry:
            response=[mock_users()]

        return{'Success':validate_entry,'Data':response}
    
    def by_id_and_name(self,user_id:int,name:str)->Dict[bool,List[User]]:
        """ method to test"""
        self.by_id_and_name_param['user_id']=user_id
        self.by_id_and_name_param['user_name']=name
        response=None
        validate_entry=isinstance(name,str) and isinstance(user_id,int)

        if validate_entry:
            response=[mock_users()]
        return{'Success':validate_entry,'Data':response}