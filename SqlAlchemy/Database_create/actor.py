'''
# coding=utf-8
	actors table model define
'''

from sqlalchemy import Column, String, Integer, Date

from base import Base


class Actor(Base):
	'''
	actors table create in test databases
	'''
	__tablename__ = 'actors'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	birthday = Column(Date)

	def __init__(self, name, birthday):
		self.name = name
		self.birthday = birthday
