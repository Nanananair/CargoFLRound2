from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from .models import base
from dotenv import load_dotenv

load_dotenv()

db_string = "postgresql://{0}:{1}@{2}:{3}/{4}".format(os.getenv('DB_USER'), os.getenv(
    'DB_PASSWORD'), os.getenv('DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME'))




db = create_engine(db_string)

base.metadata.create_all(db)

def recreate_database():
    base.metadata.drop_all(db)
    base.metadata.create_all(db)

# recreate_database()

class SessionHelper():
    __session_object = None

    def __init__(self) -> None:
        self.Session = sessionmaker(bind=db)

    def get_session(self):
        if not self.__session_object:
            self.__session_object = self.Session()
        return self.__session_object

    def close_session(self):
        if self.__session_object:
            self.__session_object.close()
            self.__session_object = None