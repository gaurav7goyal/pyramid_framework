'''
Purpose: select query in orm model in movie table
'''

# 1 - imports
from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date
from sqlalchemy.orm import aliased 
from sqlalchemy import and_ , or_ ,text,func

# 2 - extract a session
session = Session()

#3 alising colom name in sql orm model
Movie_Name = aliased(Movie, name='Movie_Name')
movie=session.query(Movie_Name).all()
for movie_title in movie:
	print(movie_title.title)


'''
Basic operations with Query include issuing LIMIT and OFFSET, most conveniently 
using Python array slices and typically in conjunction with ORDER BY:
limit start with 0
'''
for movie in session.query(Movie).order_by(Movie.id)[0:4]:
	print(movie.id,'movie_title',movie.title)

'''
multipal where clause condition: and  
type 1 : using use  and_ ()
type2 : or send multiple expressions to .filter()
type 3: or chain multiple filter()/filter_by() calls
'''
and_clause_Data = session.query(Movie_Name).filter(and_(Movie_Name.title == 'HP', Movie_Name.id==14))

for data in and_clause_Data:
	print('id',data.id,'Movie Name',data.title)

'''
where clause use or opertaor
using or_()
'''
Or_clause_Data = session.query(Movie_Name).filter(or_(Movie_Name.title == 'DDl', Movie_Name.id==14))

for data in Or_clause_Data:
	print('id',data.id,'Movie Name',data.title)



'''
count the query result
Query includes a convenience method for counting called count():
'''
#select count * from table 
count=session.query(Movie_Name).count()
print('count query',count)

#func count
count_id=session.query(func.count(Movie_Name.id)).scalar()
print('count id',count_id)

#group by count find .
count_name_groupby=session.query(func.count(Movie_Name.title), Movie_Name.title).group_by(Movie_Name.title).all()
for count in count_name_groupby:
	print('count title',count)




'''
like : case senstive
Ilike: case Insenstive lower c
'''
like_data=session.query(Movie_Name).filter(Movie_Name.title.like('%h%')).count()
ilike_data=session.query(Movie_Name).filter(Movie_Name.title.ilike('%h%')).count()
#print('like query',like_data)
#print('ilike query',ilike_data)


'''
Textual SQL
'''
for data_sql in session.query(Movie_Name).filter(text("id<14")).all():
	print('Movie title',data_sql.title)

for data_sql in session.query(Movie_Name).filter(text("id=14")).all():
	print('Movie title',data_sql.title)

for data_sql in session.query(Movie_Name).filter(text("title='HP'")).all():
	print('Movie title',data_sql.title)

'''
using param parameter pass
'''
param_data=session.query(Movie_Name).filter(text("id<:value and title=:name")).\
    params(value=14, name='DDl').order_by(Movie_Name.id).one()
print("param_query",data.title)