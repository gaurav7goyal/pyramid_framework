'''
purpose:- from package dict 
'''
from .register_form import RegisterForm

def includeme(config):
    """
    Initialize the form  for a Pyramid app.

    Activate this setup using ``config.include('login_application.models')``.

    """    