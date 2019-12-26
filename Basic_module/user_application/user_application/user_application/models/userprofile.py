'''
Purpose: User Profile Module Define
'''
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    UniqueConstraint,
    DateTime
)
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func

from .meta import Base


class UserProfile(Base):
    __tablename__ = 'UserProfile'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastName = Column(String)
    email = Column(String(50), unique=True, nullable=False)
    mobileNo = Column(mysql.BIGINT)
    address = Column(String)
    password = Column(String(25), nullable=False)
    user_Type = Column(String)
    createdAt = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    UniqueConstraint('email')
