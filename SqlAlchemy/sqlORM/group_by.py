
'''
purpose:- data find by group by fillter in mssql database table
database:-test
table:-t1
colom name:-id
'''

import sys
import configparser
import sqlalchemy
import pyodbc

from sqlalchemy import create_engine,MetaData,select
from sqlalchemy import inspect
from sqlalchemy.engine import reflection
from sqlalchemy import func 



engine = create_engine('mssql+pyodbc://SA:Gaurav@mssql@0.0.0.0:1433/test?driver=ODBC+Driver+17+for+SQL+Server')
#insp = reflection.Inspector.from_engine(engine)
conn = engine.connect()

metadata = MetaData()
#print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
#print(metadata.tables)



ex_table = metadata.tables['t1']
print(ex_table)


select_st = select([ex_table.c.id,func.count()]).group_by(ex_table.c.id).having(func.count() > 1)

res = conn.execute(select_st)
for _row in res:
    print(_row)
