from config import DBConnectionHanddler
from src.infra.entites import User

class User_repository:
    """ clss to manage user"""
    @classmethod
    def insert_user(cls,name:str,password:str):
        """insert a  new user on databese"""
        with DBConnectionHanddler() as db_conn:
            try:
                new_user=User(name=name,password=password)
                new_user.gen_hash()
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except Exception as e:
                print(e)
                db_conn.session.rollback()
            finally:
                db_conn.session.close()