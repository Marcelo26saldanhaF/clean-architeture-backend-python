from src.data.register_pet import RegisterPet
from src.infra.test import UserRepositorySpy,PetRepositorySpy
from src.data.test import FindUserSpy
from faker import Faker
pet_repository_spy=PetRepositorySpy()
user_repository_spy=UserRepositorySpy()
find_user_spy=FindUserSpy(user_repository_spy)
fake=Faker()
register_pet=RegisterPet(pet_repository=pet_repository_spy,find_user=find_user_spy)

def test_register():
    animal_attributes={
        "name":fake.name(),
        "specie":"DOG",
        "user_information":{"user_id":fake.random_number(digits=5),"user_name":fake.name()},
        "age":fake.random_number(digits=1)
    }

    response=register_pet.registry(name=animal_attributes["name"],specie=animal_attributes["specie"],user_infromation=animal_attributes["user_information"],age=animal_attributes["age"])

    

    assert response['Success'] is True
    assert response['Data']