from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Table
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()


class Page(Base):
    __tablename__ = 'wikipages'
    uid = Column(Integer, mssql_identity_start=100,primary_key=True)
    title = Column(Text)
    body = Column(Text)

class Mytable(Base):
    __tablename__ = 'test'
    id = Column(Integer,primary_key=True)
    name =Column (Text)

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass