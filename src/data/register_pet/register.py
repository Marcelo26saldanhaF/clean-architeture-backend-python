from src.domain.use_cases import RegisterPetInterface
from src.data.find_user import FindUser
from typing import Type,Dict,List
from src.data.interfaces import PetRepositoryInterface
from src.domain.model import Pet,User

class RegisterPet(RegisterPetInterface):
    """Class to define use case RegisterPet"""

    def __init__(self,pet_repository:Type[PetRepositoryInterface],find_user:type[FindUser]) -> None:
        self.pet_repository=pet_repository
        self.find_user=find_user

    def registry(self,name:str,specie:str,user_infromation:Dict[int,str],age:int=None)->Dict[bool,Pet]:
        """Register Pet
        :params - name : pet name
                - specie : type of specie
                - age : age of the pet
                - user_information : dictionary with user_id and|or user_name
        :return - Dictionary with informatios of the process
        """
        response=None
        #validate entry and tryng to find an user
        validate_entry=isinstance(name,str) and isinstance(specie,str)
        user=self.__find_user_information(user_infromation)
        checker=validate_entry and user['Success'] 

        if checker:
            response=self.pet_repository.insert_pet(name=name,specie=specie,age=age,user_id=user_infromation['user_id'])
            return {'Success':checker,'Data':response}

        return{'Success':checker,'Data':None}


    def __find_user_information(self,user_information:Dict[int,str])->Dict[bool,List[User]]:
        """Check user info and select user
        :params - user_information : dictionary with user_id and|or user_name
        :return - dictionary with the response of find_use case
        """
        user_found=None
        user_params=user_information.keys()
        if "user_id" in user_params and "user_name" in user_params:
            user_found=self.find_user.by_id_and_name(user_id=user_information['user_id'],name=user_information['user_name'])

        elif "user_id" not in user_params and "user_name" in user_params:
            user_found=self.find_user.by_name(name=user_information["user_name"])

        elif "user_id" in user_params and "user_name" not in user_params:
            user_found=self.find_user.by_id(user_id=user_information['user_id'])
        
        else:
            return {'Success':False,'Data':None}

        return user_found