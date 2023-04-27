from faker import Faker
from src.domain.model import Pet

fake=Faker()

def mock_pets():
    specie='DOG'
    return Pet(
            id=fake.random_number(digits=3),
            age=fake.random_number(digits=1),
            name=fake.name(),
            specie=specie,
            user_id=fake.random_number(digits=5)
                    )