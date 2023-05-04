from src.infra.repo import Pet_repository,User_repository
from src.data.register_pet import RegisterPet
from src.data.find_user import FindUser
from src.presenters.controllers import RegisterPetController

def register_pet_composer()->RegisterPetController:
    """..."""

    repository=Pet_repository()
    find_user_case=FindUser(User_repository())
    use_case=RegisterPet(repository,find_user_case)
    register_pet_route=RegisterPetController(use_case)

    return register_pet_route