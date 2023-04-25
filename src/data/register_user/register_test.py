from .register import RegisterUser
from faker import Faker
from src.infra.test import UserRepositorySpy

faker=Faker()


def test_register():
    """ Test register """
    user_repo_spy=UserRepositorySpy()
    register_user=RegisterUser(user_repository=user_repo_spy)

    attributes={
        "name":faker.name(),
        "password":faker.password()
    }

    response=register_user.register(name=attributes['name'],password=attributes['password'])

    # testing input

    assert user_repo_spy.insert_user_parms['name']== attributes['name']
    assert user_repo_spy.insert_user_parms['password']==attributes['password']
    

    #testing output
    
    assert response['Success'] is True
    assert response['Data']

def test_register_fail():
    """ Test register fail """
    user_repo_spy=UserRepositorySpy()
    register_user=RegisterUser(user_repository=user_repo_spy)

    attributes={
        "name":faker.random_number(digits=2), # colocando number no lugar da str para ver a estrutura bloquenate ira bloquear 
        "password":faker.password()
    }

    response=register_user.register(name=attributes['name'],password=attributes['password'])
    print(response)
    # testing input
    assert user_repo_spy.insert_user_parms=={}
    #testing output
    
    assert response['Success'] is False
    assert response['Data'] is None

    