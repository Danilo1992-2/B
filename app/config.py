from model.entity import entity
from sqlalchemy import create_engine

CON_STRING: str = "root:shaman@localhost:3306/contas"

ENGINE = create_engine("mysql+pymysql://" + CON_STRING)
entity.BASE.metadata.create_all(ENGINE)
