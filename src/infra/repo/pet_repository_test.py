from src.infra.entites import Pets as PetsModel
from src.infra.entites.pets import AnimalTypes
from src.infra.config import DBConnectionHanddler
from .pet_repository import Pet_repository
from faker import Faker
from sqlalchemy import text

db_conn=DBConnectionHanddler()
db_conn.get_engine()
fake=Faker()
pet_repo=Pet_repository()

def test_insert_pet():
    """must insert a new pet in the table"""
    name=fake.name()
    specie="FISH"
    age=fake.random_number(digits=1)
    user_id=fake.random_number(digits=1)

    new_pet=pet_repo.insert_pet(name=name,specie=specie,age=age,user_id=user_id)
    
    with db_conn as conn:
        query_pet=conn.session.execute(text('SELECT * FROM pets WHERE ID= :id;'),{'id':new_pet.id}).first()
        conn.session.execute(text('DELETE FROM pets WHERE ID= :id;'),{'id':new_pet.id})

    assert new_pet.__eq__(query_pet)

def test_select_pet():
    pet_id=fake.random_number(digits=3)
    name=fake.name()
    age=fake.random_number(digits=1)
    specie='DOG'
    user_id=fake.random_number(digits=5)
    specie_mok=AnimalTypes('dog')
    new_pet=PetsModel(id=pet_id,name=name,age=age,specie=specie_mok,user_id=user_id)
    
    with db_conn as conn:
        conn.session.execute(text('INSERT INTO pets(id,name,age,specie,user_id) VALUES(:id,:name,:age,:specie,:user_id);'),\
                     {'id':pet_id,'name':name,'age':age,'specie':specie,'user_id':user_id})
        conn.session.commit()
        

    pet_select_from_database_by_pet_id=pet_repo.select_pet(pet_id=pet_id)
    pet_select_from_database_by_user_id=pet_repo.select_pet(user_id=user_id)
    pet_select_from_database_by_pet_id_and_user_id=pet_repo.select_pet(pet_id=pet_id,user_id=user_id)

    assert new_pet in pet_select_from_database_by_pet_id
    assert new_pet in pet_select_from_database_by_user_id
    assert new_pet in pet_select_from_database_by_pet_id_and_user_id

