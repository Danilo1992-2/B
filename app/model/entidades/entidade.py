from datetime import date
from sqlalchemy.orm import declarative_base
from sqlalchemy import (Column, String, Date, Integer, ForeignKey, Float)
from sqlalchemy.orm import relationship

BASE = declarative_base()


class User(BASE):
    __tablename__: str = "user"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50))
    document: str = Column(String(11))
    user: str = Column(String(50))
    create_at: date = Column(Date())
    password: str = Column(String(50))
    deposit = relationship('deposit', back_populates='user')


class Deposit(BASE):
    __tablename__: str = "deposit"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: date = Column(Date())
    month: int = Column(Integer())
    user_id: int = Column(Integer())
    user_id: int = Column(Integer(), ForeignKey('user.id'))
    user = relationship('user', back_populates='deposit')


class Withdraw(BASE):
    __tablename__: str = "withdraw"
    id: str = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: date = Column(Date())
    month: int = Column(Integer())
    user_id: int = Column(Integer(), ForeignKey('user.id'))
    user = relationship('user', back_populates='withdraw')
