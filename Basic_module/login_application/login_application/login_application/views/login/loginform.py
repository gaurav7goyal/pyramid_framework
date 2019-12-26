'''
purpose: login view deifne
'''
from pyramid.view import view_config
from pyramid.response import Response

from .. import models

@view_config(route_name='login', renderer='../templates/login/logintemplate.jinja2')
def login_view(request):
	 return {}