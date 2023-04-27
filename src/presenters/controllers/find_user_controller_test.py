from .find_user_controller import FindUserController
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from faker import Faker
from src.presenters.helpers import HttpRequest

fake=Faker()
find_user_spy=FindUserSpy(UserRepositorySpy())
find_user_controller=FindUserController(find_user_spy)

def test_handle():
    """testing handle method"""
    http_request=HttpRequest(
        query={"user_id":fake.random_number(digits=5),"user_name":fake.name()}
    )

    response=find_user_controller.handle(http_request)
    # testing input
    assert find_user_spy.by_id_and_name_param['user_id']==http_request.query['user_id']

    assert find_user_spy.by_id_and_name_param['user_name']==http_request.query['user_name']

def test_handle_fail_error_422():
    """testing handle in error case"""

    http_request=HttpRequest(
        query={"user":fake.random_number(digits=5),"user":fake.name()}
    )

    response=find_user_controller.handle(http_request)
    assert response.status_code==422
    assert  "error" in response.body

def test_handle_fail_error_400():
    """testing handle in error case"""
    # no caso da query for passada sem parametros    
    http_request=HttpRequest(
        query={}
    )
    response=find_user_controller.handle(http_request)
    assert response.status_code==400
    assert "error" in response.body
