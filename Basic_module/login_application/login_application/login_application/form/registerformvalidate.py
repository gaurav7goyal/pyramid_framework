'''
Purpose: Registation form validation define
'''
from deform import Form
import colander
from ..models import UserProfile


class ValidateRegistrationForm:
    '''
    Registration form custom validate fun define 
    '''
   
    def uniqe_email_validate(node,value):
        '''
        Custom schema level validation code.
        email already use in database
        '''
        request = node.bindings["request"]
        dbsession = request.dbsession
        if dbsession.query(UserProfile).filter_by(email=value).first():
            raise colander.Invalid(node, "Email address already taken")

   
   def save(self, dbsession):
        user_profile = UserProfile()
        user
        dbsession.add(user_profile)
        