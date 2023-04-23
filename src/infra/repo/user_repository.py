from typing import List
from sqlalchemy import select,and_
from src.infra.config  import DBConnectionHanddler
from src.domain.model import User
from src.infra.entites import User as UserModel


class User_repository:
    """ clss to manage user"""
    
    @classmethod
    def insert_user(cls,name:str,password:str)->User:
        """insert a  new user on databese"""
        with DBConnectionHanddler() as db_conn:
            try:
                new_user=UserModel(name=name,password=password)
                new_user.gen_hash()
                db_conn.session.add(new_user)
                db_conn.session.commit()
                return User(id=new_user.id,name=new_user.name)
            except Exception as e:
                print(e)
                db_conn.session.rollback()
            finally:
                db_conn.session.close()
        return None
    
    @classmethod
    def select_user(cls,user_id:int=None,name:str=None)->List[User]:
        """select user by id or name
            :param  -user_id: id of register
                    -name: User`s name
        """
        with DBConnectionHanddler() as db_conn:
            try:
                query_data=None
                
                if user_id and not name:
                        stm=select(UserModel).where(UserModel.id==user_id)
                        data=db_conn.session.scalar(stm)
                        query_data=[data]

                elif(not user_id and name):
                    with DBConnectionHanddler() as db_conn:
                        stm=select(UserModel).where(UserModel.name==name)
                        data=db_conn.session.scalars(stm).all()
                        query_data=data

                elif (user_id and name):
                    with DBConnectionHanddler() as db_conn:
                        stm=select(UserModel).where(and_(UserModel.id==user_id,UserModel.name==name))
                        data=db_conn.session.scalars(stm).all()
                        query_data=data

            
                return query_data
        
            except Exception as e:
                print(e)
                db_conn.session.rollback()

            finally:
                db_conn.session.close()

            return None

        
            
        


