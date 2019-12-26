'''
# coding=utf-8
    Movie  table model define
'''

from sqlalchemy import Column, String, Integer, Date
from connection import Base
class Movie(Base):
    '''
    create movie table in test database.
    '''
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

class Wikipages(Base):
    __tablename__ = 'wikipages'
    uid = Column(Integer, mssql_identity_start=100,primary_key=True)
    title = Column(String)
    body = Column(String)
