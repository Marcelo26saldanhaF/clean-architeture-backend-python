from faker import Faker
from .register_pet_controller import RegisterPetController
from src.presenters.helpers import HttpRequest
from src.data.test import RegisterPetSpy,FindUserSpy
from src.infra.test import PetRepositorySpy,UserRepositorySpy

fake=Faker()
pet_repository_spy=PetRepositorySpy()
find_user_spy=FindUserSpy(user_repository=UserRepositorySpy())
register_pet_spy=RegisterPetSpy(pet_repository_spy=pet_repository_spy,find_user_spy=find_user_spy)
register_pet_controller=RegisterPetController(register_pet_use_case=register_pet_spy)


def test_register_pet():
    http_request=HttpRequest(
        body={
        "name":fake.name(),
        "specie":"DOG",
        "user_information":{"user_id":fake.random_number(digits=5),"user_name":fake.name()},
        "age":fake.random_number(digits=1)
        }
    )
    
    response=register_pet_controller.route(http_request=http_request)

    assert response.status_code==200
    assert response.body

def test_register_pet_error_422_fail():
    http_request=HttpRequest(
        body={
        "name":fake.name(),
        "specie":"DOG",
        "user_information":{}, #passe user_information em branco
        "age":fake.random_number(digits=1)
        }
    )
    
    response=register_pet_controller.route(http_request=http_request)

    assert response.status_code==422
    assert "error" in response.body


def test_register_pet_error_400_fail():
    http_request=HttpRequest(
         body={
        # "name":fake.name(),
        # "specie":"DOG",
        # "user_information":{}, #passe user_information em branco
        # "age":fake.random_number(digits=1)
        }
    )
    
    response=register_pet_controller.route(http_request=http_request)

    assert response.status_code==400
    assert "error" in response.body