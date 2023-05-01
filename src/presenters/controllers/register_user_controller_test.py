from faker import Faker
from .register_user_controller import RegisterUserController
from src.presenters.helpers import HttpRequest
from src.data.test import RegisterUserSpy
from src.data.test import RegisterUserSpy

fake=Faker()
register_user_controller=RegisterUserController(register_user_case=RegisterUserSpy(repository_use=None))

def test_register_user_controller_route():
    """test method route of register user controller"""
    http_request=HttpRequest(
        body={
        "name":fake.name(),
        "password":fake.password()
        }
    )

    response=register_user_controller.route(http_request)


    assert response.status_code==200
    assert response.body

def test_register_user_controller_route_fail_error_422():
    """test method route of register user controller fail and generate error 422"""
    http_request=HttpRequest(
        body={
        # "name":fake.random_number(digits=4),
        "password":fake.password()
        }
    )

    response=register_user_controller.route(http_request)
    
    assert response.status_code==422
    assert "error" in response.body

def test_register_user_controller_route_fail_error_400():
    """test method route of register user controller fail and generate error 400"""
    http_request=HttpRequest(
        body={
        # "name":fake.random_number(digits=4),
        # "password":fake.password()
        }
    )

    response=register_user_controller.route(http_request)
    
    assert response.status_code==400
    assert "error" in response.body