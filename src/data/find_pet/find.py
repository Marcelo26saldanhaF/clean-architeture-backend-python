from src.domain.model import Pet
from src.domain.use_cases import FindPetInterface
from src.data.interfaces import PetRepositoryInterface
from typing import Type,Dict,List


class FindPet(FindPetInterface):
    """Class use case that must select some pet"""

    def __init__(self,pet_repository:Type[PetRepositoryInterface]) -> None:
        self.pet_repository=pet_repository

    def by_pet_id(self,pet_id:int)->Dict[bool,List[Pet]]:
        """select pet by pet_id
        :parmas-pet_id: id of the pet
        return {bool,list[Pet]}
           """
        response=None
        validate_entry=isinstance(pet_id,int)
        if validate_entry:
            response=self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success":validate_entry,"Data":response}
    
    def by_user_id(self,user_id:int)->Dict[bool,List[Pet]]:
        """select pet by user_id
        :parmas-user_id: id of the user
        return {bool,list[Pet]} """

        response=None
        validate_entry=isinstance(user_id,int)
        if validate_entry:
            response=self.pet_repository.select_pet(user_id=user_id)

        return {"Success":validate_entry,"Data":response}
        
    
    def by_pet_id_and_user_id(self,pet_id:int,user_id:int)->Dict[bool,List[Pet]]:
        """select pet by pet_id and user_id
        :parmas - pet_id: id of the pet
                - user_id: id of the user
        return {bool,list[Pet]} """
        
        response=None
        validate_entry=isinstance(pet_id,int) and isinstance(user_id,int)
        if validate_entry:
            response=self.pet_repository.select_pet(pet_id=pet_id,user_id=user_id)

        return {"Success":validate_entry,"Data":response}