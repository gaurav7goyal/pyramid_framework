'''
Purpose: commit session in database file
'''
from connection import Session, engine, Base
from user_model import User,Address



#  generate database schema
Base.metadata.create_all(engine)

#  create a new session
session = Session()

# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

jack = User(name='amit', fullname='Jack Bean', nickname='gjffdd')
jack.addresses = [ Address(email_address='amit@google.com'),
                 	Address(email_address='amit@yahoo.com')]

#add user table and address table with user id
gaurav=User(name='gaurav',fullname='gaurav goyal', nickname='gg')
gaurav.addresses=[Address(email_address='gaurav@gmail.com')]

#session.add(jack)
session.commit()
session.close()