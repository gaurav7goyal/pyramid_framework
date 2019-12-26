from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    lastName= Column(String)

