from src.domain.use_cases import FindUserInterface
from src.domain.model import User
from src.data.interfaces import UserRepositoryInterface
from typing import Type,List,Dict



class FindUser(FindUserInterface):
    """Clas to define use case Find User"""
    def __init__(self,user_repository:Type[UserRepositoryInterface]) -> None:
        self.user_repository=user_repository

    def by_id(self,user_id)->Dict[bool,List[User]]:
        """:param - user_id: id of the user
        return user by id"""

        response=None
        validate_entry=isinstance(user_id,int)

        if validate_entry:
            response=self.user_repository.select_user(user_id=user_id)

        return{'Success':validate_entry,'Data':response}
    
    def by_name(self,name:str)->Dict[bool,List[User]]:
        """ params: name: name of the user
            return dict[bool,list[user]]
        """
        response=None
        validate_entry=isinstance(name,str)

        if validate_entry:
            response=self.user_repository.select_user(name=name)

        return{'Success':validate_entry,'Data':response}
    
    def by_id_and_name(self,user_id:int,name:str)->Dict[bool,List[User]]:
        """ -params: name: name of the user
            -parms:  user_id: if of the user
            return dict[bool,list[user]]
        """
        response=None
        validate_entry=isinstance(name,str) and isinstance(user_id,int)

        if validate_entry:
            response=self.user_repository.select_user(name=name,user_id=user_id)

        return{'Success':validate_entry,'Data':response}
    
        