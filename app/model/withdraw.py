from datetime import date

from sqlalchemy import (Column, Date, Integer,
                        Float, ForeignKey)
from sqlalchemy.orm import relationship

from app.config import BASE


class Withdraw(BASE):
    __tablename__: str = "withdraw"
    id: str = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: date = Column(Date())
    month: int = Column(Integer())
    user_id: int = Column(Integer(), ForeignKey('User.id'))
    user = relationship('User', back_populates='withdraw')
