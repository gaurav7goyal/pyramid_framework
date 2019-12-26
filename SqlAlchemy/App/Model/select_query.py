'''
Purpose: Join Query
'''
from connection import Session, engine, Base
from user_model import User,Address
from sqlalchemy.sql import func

session=Session()
amit=session.query(User).filter_by(name='amit').one()


session.delete(amit)
amit=session.query(User).filter_by(name='amit').count()
print('jack persernt',amit)
user_date=session.query(User,Address).filter(User.id==Address.user_id).\
							filter(Address.email_address=='jack@google.com').all()

for user ,address in user_date:
	print(user)
	print(address)

# using join operation
user_details=session.query(User).join(Address).all()
for user in user_details:
	print(user)


stmt = session.query(Address.user_id, func.count('*').\
        label('address_count')).\
        group_by(Address.user_id).subquery()

for u, count in session.query(User, stmt.c.address_count).\
    outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
    print(u, count)

session.close()