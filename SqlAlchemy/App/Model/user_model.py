'''
purpose: create a user table in database
'''
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import Base
from sqlalchemy import Column, String, Integer

class User(Base):

    __tablename__ ='users'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    addresses = relationship("Address", back_populates='user',
                    cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)




class Address(Base):

    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
    	return "<Address(email_address='%s')>" % self.email_address

# User.addresses = relationship(
#     "Address", order_by=Address.id, back_populates="user")