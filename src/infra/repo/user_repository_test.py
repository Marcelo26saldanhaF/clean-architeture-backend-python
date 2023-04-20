from user_repository import User_repository
from faker import Faker

faker=Faker()
user_repo=User_repository()

def test_insert_user():
    """must insert a new user a database"""
    name=faker.name()
    password=faker.password()

    user_repo.insert_user(name=name,password=password)