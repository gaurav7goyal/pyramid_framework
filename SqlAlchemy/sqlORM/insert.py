'''
'''

from movie import Movie ,Wikipages
from connection import Session, engine, Base

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

#print(dir(session.query(Wikipages)))
rows = session.query(Wikipages).group_by(Wikipages.uid)

print(rows)