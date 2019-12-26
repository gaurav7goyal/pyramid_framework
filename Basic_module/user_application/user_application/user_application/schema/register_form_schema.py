'''
purpose:- create Register form colander schema with pre define some validation
'''
import colander
import deform

class RegistrationForm(colander.MappingSchema):
	'''
	Registration from schema
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
		validator=colander.All(colander.Email()),
		widget=deform.widget.TextInputWidget( type='email', placeholder="youremail@example.com"),
		)
	password = colander.SchemaNode(
		colander.String(),
		validator=colander.Length(min=5, max=100),
		widget=deform.widget.CheckedPasswordWidget(redisplay=True),
		)