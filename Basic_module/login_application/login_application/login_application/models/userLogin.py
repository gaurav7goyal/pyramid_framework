'''
Purpose: Create a login Model
'''

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.sql import func

from .meta import Base

class UserLogin(Base):
	'''
	Create a user login table.
	'''
	__tablename__ = 'UserLogin'
	id = Column(Integer, primary_key=True)
	email = Column(String(50), unique=True)
	password = Column(String)
	createdAt = Column(DateTime, default=func.now())
	updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class loginUser():
	'''
	add register user email and password add to login table
	'''