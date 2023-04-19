from src.infra.config import DBConnectionHanddler
from src.infra.entites import User

class Fakerepository:
    """somenthing"""

    @classmethod
    def insert_user(cls):
        with DBConnectionHanddler() as db_conn:
            try:
                new_user=User(name="programador",password="lhama")
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except Exception as e:
                print(e)
                db_conn.session.rollback()
            finally:
                db_conn.session.close()