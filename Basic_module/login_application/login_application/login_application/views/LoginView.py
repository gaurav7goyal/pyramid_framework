'''
purpose: login view deifne
'''
import colander
import deform
from pyramid.view import view_config
from pyramid.response import Response

from .. import models

class LoginFormSchema(colander.MappingSchema):
	'''
	login  form schema define
	'''
	email =  colander.SchemaNode(
		colander.Str(),
		title='Email',
		validator=colander.All(colander.Email()),
		widget=deform.widget.TextInputWidget(size=40, maxlength=260, type='email', placeholder="youremail@example.com"),
		description="The email address under which you have your account.")
	password = colander.SchemaNode(
		colander.String(),
		validator=colander.Length(min=5, max=100),
    	widget=deform.widget.PasswordWidget(),
   		description='Enter a password')
		


class LoginView(object):
	def __init__(self, request):
		self.request = request
	
	@property
	def login_form(self):
		schema = LoginFormSchema()
		b = deform.Button(name='submit', title="Submit", css_class="btn-block  btn-primary btn-pg")
		return deform.Form(schema, buttons=(b, ))

	@property
	def reqts(self):
		return self.login_form.get_widget_resources()


	@view_config(route_name='login', renderer='../templates/logintemplate.jinja2')
	def login_view(self):
		rendered_form = self.login_form.render()
		if 'submit' in self.request.params:
				controls = self.request.POST.items()
				try:
					appstruct = self.login_form.validate(controls)
				except deform.ValidationFailure as e:
					return dict(rendered_form=e.render())

		
		return locals()