'''
Purpose: User Register Module Define
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
	'''
	User Register Table  Sachema Define.
	'''
	__tablename__='UserProfile'
	id=Column(Integer,primary_key=True)
	name=Column(String)
	lastName=Column(String)
	email=Column(String(50),unique=True,nullable=False)
	mobileNo=Column(mysql.BIGINT)
	address=Column(String)
	user_Type=Column(String)
	createdAt=Column(DateTime, default=func.now())
	updated_at =Column(DateTime, default=func.now(), onupdate=func.now())
	UniqueConstraint('email')

class RegisterUser(object):
	'''
	Register user data fatch and add to database

	'''
	def __init__(self,request,appstruct):
		self.request=request
		self.appstruct=appstruct

	def set_register_user_data(self):
		'''
		set register user detail in UserProfile table
		'''
		dbsession=self.request.dbsession
		add_user=UserProfile()
		#setattr set (object,key,value) for UserProfile class
		for key ,value in self.appstruct.items():
			setattr(add_user,key,value)
		dbsession.add(add_user)

