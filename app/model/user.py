from datetime import date

from sqlalchemy import (Column, String, Date, Integer)
from sqlalchemy.orm import relationship

from app.config import BASE


class User(BASE):
    __tablename__: str = "User"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50))
    document: str = Column(String(11))
    user: str = Column(String(50))
    create_at: date = Column(Date())
    password: str = Column(String(50))
    deposit = relationship('deposit', back_populates='User')
