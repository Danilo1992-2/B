from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

CON_STRING: str = "shaman@localhost:3306/Byru"
BASE = declarative_base()


class conn:
    def __init__(self) -> create_engine:
        self.engine = create_engine("mysql+pymysql://root:" + CON_STRING)

    def create_tables(self) -> None:
        BASE.metadata.create_all(self.engine)


conection = conn()
conection.create_tables()
