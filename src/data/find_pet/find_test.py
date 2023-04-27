from .find import FindPet
from faker import Faker
from src.infra.test import PetRepositorySpy

pet_repository_spy=PetRepositorySpy()
find_pet=FindPet(pet_repository=pet_repository_spy)
fake=Faker()

def test_find_pet_by_pet_id():
    attributes={
        "pet_id":fake.random_number(digits=3)
    }
       
    
    response=find_pet.by_pet_id(pet_id=attributes["pet_id"])

    assert pet_repository_spy.select_pet_params['pet_id']==attributes['pet_id']

    assert response['Success'] is True
    assert response['Data']

def test_find_pet_by_user_id():
    
    attributes={
        "user_id":fake.random_number(digits=5)
    }
       
    
    response=find_pet.by_user_id(user_id=attributes['user_id'])

    assert pet_repository_spy.select_pet_params['user_id']==attributes['user_id']

    assert response['Success'] is True
    assert response['Data']

def test_find_pet_by_pet_id_and_user_id():
    
    attributes={
        "pet_id":fake.random_number(digits=3),
        "user_id":fake.random_number(digits=5)
    }
       
    
    response=find_pet.by_pet_id_and_user_id(user_id=attributes['user_id'],pet_id=attributes['pet_id'])

    assert pet_repository_spy.select_pet_params['pet_id']==attributes['pet_id'] and pet_repository_spy.select_pet_params['user_id']==attributes['user_id']

    assert response['Success'] is True
    assert response['Data']
