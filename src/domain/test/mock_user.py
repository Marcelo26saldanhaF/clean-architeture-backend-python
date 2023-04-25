from faker import Faker
from src.domain.model import User

fake=Faker()

def mock_users(name,password):
    return User(id=fake.random_number(digits=5),
                name=name,
                password=password
                )

