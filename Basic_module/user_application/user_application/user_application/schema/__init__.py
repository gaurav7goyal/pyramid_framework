'''
Purpose:- colander schema or say user form schema init dict
'''

from .register_form_schema import RegistrationForm


def includeme(config):
    """
    Initialize the form  for a Pyramid app.

    Activate this setup using ``config.include('login_application.models')``.

    """    