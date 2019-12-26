'''
# coding=utf-8
	test database connection
	https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc

engine = create_engine('mssql+pyodbc://SA:Gaurav@mssql@0.0.0.0:1433/test?driver=ODBC+Driver+17+for+SQL+Server',echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()