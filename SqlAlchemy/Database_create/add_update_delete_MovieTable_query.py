'''
purpose: add update and delete database value using sql alchemy ORM model in movie table
'''

from datetime import date
from base import Session, engine, Base
from movie import Movie


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
SESSION = Session()


#add row in movie table
DDL = Movie('HP', date(2000, 12, 5))
SESSION.add(DDL)

# #update date for movie title HP
# movie_name = session.query(Movie).filter_by(title='HP').first()
# movie_name.title="hello page"
# session.dirty

# session.rollback()

# 10 - commit and close session
SESSION.commit()
SESSION.close()
