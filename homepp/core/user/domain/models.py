# from typing import Optional
# from dataclasses import dataclass, field
#
# from homepp.core.common.types.user import UserId, Username, Email
#
#
# @dataclass
# class User:
#     id: Optional[UserId] = field(init=False, default=None)
#     username: Username
#     email: Email
#     hashed_password: str

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    controller_id = Column(Integer, ForeignKey("controllers.id"))
    controller = relationship("Controller", back_populates="users")


class Controller(Base):
    __tablename__ = 'controllers'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    hardware_key = Column(String, nullable=False)
    users = relationship("User", back_populates="Controller")
