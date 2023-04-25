from faker import Faker
from src.domain.model import User

fake=Faker()


def mock_users():
    return User(id=fake.random_number(digits=5),
                name=fake.name(),
                password=fake.password()
                )

