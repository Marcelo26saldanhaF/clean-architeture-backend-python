from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHanddler:
    """ sqlalchemy dtabase connection """
    
    def __init__(self) -> None:
        self.__connection_string="sqlite:///storage.db"
        self.session=None

    def get_engine(self):
        """return connect engine
            :param - None
            : return - engine conection to database
        """
        engine=create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        engine=create_engine(self.__connection_string)
        session_maker=sessionmaker()
        self.session=session_maker(bind=engine)
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.session.close()