from .find import FindUser
from  src.infra.test import UserRepositorySpy
from faker import Faker

user_repository_spy=UserRepositorySpy()
find_user=FindUser(user_repository=user_repository_spy)
fake=Faker()

def test_find_user_by_id():
    name=fake.name()
    user_id=fake.random_number(digits=3)

    attributes={
        'name':name,
        'user_id':user_id
    }
    response=find_user.by_id(user_id=attributes['user_id'])

    assert response['Success'] is True
    assert response['Data']

def test_find_user_by_name():
    name=fake.name()
    user_id=fake.random_number(digits=3)
    attributes={
        'name':name,
        'user_id':user_id
    }
    response=find_user.by_name(name=attributes['name'])
    
    assert response['Success'] is True
    assert response['Data']

def test_find_user_by_name_by_id():
    name=fake.name()
    user_id=fake.random_number(digits=3)
    attributes={
        'name':name,
        'user_id':user_id
    }
    response= find_user.by_id_and_name(user_id=attributes['user_id'],name=attributes['name']) 

    assert response['Success'] is True
    assert response['Data']



def test_find_user_by_id_fail():
    name=fake.random_number(digits=3)
    user_id=fake.name()
    #estou invertando os valores de id para string e o nmae para int , para testar os validadores 

    attributes={
        'name':name,
        'user_id':user_id
    }

    response= find_user.by_id(user_id=user_id)

    assert response['Success'] is False
    assert response['Data'] is None

def test_find_user_by_name_fail():
    
    name=fake.random_number(digits=3)
    user_id=fake.name()
    #estou invertando os valores de id para string e o nmae para int , para testar os validadores 

    attributes={
        'name':name,
        'user_id':user_id
    }
    response=find_user.by_name(name=name)
     
    assert response['Success'] is False
    assert response['Data'] is None

    
def test_find_user_by_id_and_name_fail():
    
    name=fake.random_number(digits=3)
    user_id=fake.name()
    #estou invertando os valores de id para string e o nmae para int , para testar os validadores 

    attributes={
        'name':name,
        'user_id':user_id
    }
    response= find_user.by_id_and_name(user_id=user_id,name=name)
    assert response['Success'] is False
    assert response['Data'] is None

