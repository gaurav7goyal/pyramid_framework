'''
purpose:- data find by group by fillter in mssql database table
database:-test
table:-t1
colom name:-id
'''

import pyodbc

from sqlalchemy import create_engine,MetaData,select,Table
from sqlalchemy import inspect
from sqlalchemy.engine import reflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import func 



engine = create_engine('mssql+pyodbc://SA:Gaurav@mssql@0.0.0.0:1433/test?driver=ODBC+Driver+17+for+SQL+Server')
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
#print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
#print(metadata.tables)

# Get Table
ex_table = metadata.tables['t1']
print(ex_table)



select_st=session.query(ex_table).count()
print(select_st)

group_by=session.query(ex_table.c.id).group_by(ex_table.c.id).having(func.count() > 1)
print(group_by.all())



select_st1=session.query(ex_table).where(ex_table.c.id==1)
print(select_st1.all())
# query='id'
# filter_colomname=session.query(ex_table).filter(ex_table.c.like("%" +query+ "%"))
# print(filter_colomname)
