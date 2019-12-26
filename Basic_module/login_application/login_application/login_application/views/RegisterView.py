'''
create a register view
'''
import colander
import deform

from pyramid.view import view_config
from pyramid.response import Response


from ..models import UserProfile,RegisterUser
from ..form import ValidateRegistrationForm

class RegisterFormSchema(colander.MappingSchema):
	'''
	register form schema define using colander schema pacakge
	'''
	

	name = colander.SchemaNode(
		colander.String(),
		title='First Name'
		)
	lastName = colander.SchemaNode(
		colander.String(),
		title='Last Name'
		)
	email =  colander.SchemaNode(
		colander.String(),
		title='Email',
		validator=colander.All(colander.Email(),ValidateRegistrationForm.uniqe_email_validate),
		widget=deform.widget.TextInputWidget( type='email', placeholder="youremail@example.com"),
		)
	password = colander.SchemaNode(
		colander.String(),
		validator=colander.Length(min=5, max=100),
		widget=deform.widget.CheckedPasswordWidget(redisplay=True),
		)
	# repassword = colander.SchemaNode(
	#   colander.String(),
	#   validator=colander.Length(min=5, max=100),
	#   widget=deform.widget.CheckedPasswordWidget(placeholder='Re password'),
	#   )






class RegisterView(object):
	def __init__(self, request):
		self.request = request
	
	@property
	def register_form(self):
		schema = RegisterFormSchema().bind(request=self.request)
		b = deform.Button(name='submit', title="Submit", css_class="btn-block  btn-primary btn-pg")
		return deform.Form(schema, buttons=(b, ))

	@property
	def reqts(self):
		return self.register_form.get_widget_resources()

	@view_config(route_name='register', renderer='../templates/registertemplate.jinja2')
	def register_view(self):
		rendered_form = self.register_form.render()
		if self.request.method == "POST":

			controls = self.request.POST.items()
			try:
				self.register_form.validate(controls)
				self.register_form.save(dbsession)				
			except deform.ValidationFailure as e:
				return dict(rendered_form=e.render())
					
			print(appstruct)

		return dict(rendered_form=rendered_form)