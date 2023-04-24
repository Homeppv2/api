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

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
