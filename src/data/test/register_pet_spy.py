from typing import Dict,List
from src.domain.model import Pet,User
from src.domain.test import mock_pets,mock_users


class RegisterPetSpy:
    """Class to tet use case register pet"""

    def __init__(self,pet_repository_spy:any,find_user_spy:any) -> None:
        self.pet_repository_spy=pet_repository_spy
        self.find_user_spy=find_user_spy
        self.registry_params={}
        
    
    def registry(self,name:str,specie:str,user_information:Dict[int,str],age:int=None)->Dict[bool,Pet]:

        self.registry_params['name']=name
        self.registry_params['specie']=specie
        self.registry_params['user_information']=user_information
        self.registry_params['age']=age
        
        response=None
        validate_enrty=isinstance(name,str) and isinstance(specie,str)
        user=self.__find_user_information(user_information) # implementanto esse metodo ele tem qe retornar uma lista
        checker= validate_enrty and user['Success']

        if checker:
            response=mock_pets()
            
        return {'Success':checker,'Data':response} 
        
    
    def __find_user_information(self,user_information:Dict[int,str])->Dict[bool,list[User]]:
        user_found=None

        user_params=user_information.keys()

        if "user_name" in user_params and "user_id" in user_params:
            user_found={'Success':True,'Data':mock_users()}

        elif "user_name" in user_params and "user_id" not in user_params:
            user_found={'Success':True,'Data':mock_users()}

        elif "user_name" not in user_params and "user_id" in user_params:
            user_found={'Success':True,'Data':mock_users()}

        else:
            return {'Success':False,'Data':None}

        return user_found