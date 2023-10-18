from datetime import date

from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Date, Integer,
                        Float, ForeignKey)

from app.config import BASE


class Deposit(BASE):
    __tablename__: str = "deposit"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: date = Column(Date())
    month: int = Column(Integer())
    user_id: int = Column(Integer())
    user_id: int = Column(Integer(), ForeignKey('User.id'))
    user = relationship('User', back_populates='deposit')
