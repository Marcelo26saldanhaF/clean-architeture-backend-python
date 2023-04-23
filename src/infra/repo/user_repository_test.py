from faker import Faker
from src.infra.config import DBConnectionHanddler
from .user_repository import User_repository
from sqlalchemy import text
from src.infra.entites import User as UserModel

db_conn=DBConnectionHanddler()
db_conn.get_engine()
faker=Faker()
user_repo=User_repository()

def test_insert_user():
    """must insert a new user a database"""
    name=faker.name()
    password=faker.password()
    new_user=user_repo.insert_user(name=name,password=password)
    with db_conn as conn:
        query_user=conn.session.execute(text(f'SELECT * FROM users WHERE ID={new_user.id};')).first()
        conn.session.execute(text(f'DELETE FROM users WHERE ID={new_user.id};')) # boa pratica pois não popula o db com testes

    assert new_user.id==query_user.id
    assert new_user.name==query_user.name

def test_select_user():
    """select  a user in database by id or name"""
    name=faker.name()
    password=faker.password()
    id=faker.random_number(digits=5)
    new_user=UserModel(id=id,name=name,password=password)
    new_user.gen_hash()
    with db_conn as conn:
            conn.session.execute(text("INSERT INTO users(id,name,password) VALUES (:id,:name,:password);"),{'id':new_user.id,'name':new_user.name,'password':new_user.password})
            conn.session.commit()

    get_user_by_id=user_repo.select_user(user_id=new_user.id)
    get_user_by_name=user_repo.select_user(name=new_user.name)
    get_user_by_id_and_name=user_repo.select_user(user_id=new_user.id,name=new_user.name)

    assert new_user in get_user_by_id
    assert new_user in get_user_by_name
    assert new_user in get_user_by_id_and_name

