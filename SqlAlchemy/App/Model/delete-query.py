'''
cascade delete both table 
'''
from connection import Session, engine, Base
from user_model import User,Address

session=Session()
#get user obj using id
jack = session.query(User).get(10)
print(jack)

#delete one address usign obj
del jack.addresses[1]

query=session.query(Address).filter(
    Address.email_address.in_(['amit@google.com', 'amit@yahoo.com'])
 	).count()
print(query)

session.delete(jack)

user=session.query(User).filter_by(name='amit').count()
print(user)

query=session.query(Address).filter(
    Address.email_address.in_(['amit@google.com', 'amit@yahoo.com'])
 	).count()
print(query)