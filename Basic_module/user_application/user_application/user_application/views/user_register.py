'''
purpose: user Registration View
'''
class UserRegister(object):
	'''
	User Registration View
	'''
	def __init__(self,request):
		self.request=request

	@view_config(route_name='register', renderer='../templates/registertemplate.jinja2')
	def registration(self):
		#check request iis post
		if self.request.method == "POST":
			'''
			form validate call and save tha data
			if exception genrate the trigger the exception
			if form submit the render to sussess page
			write code here
			'''
			pass
		# check request is get
		else:
			'''
			rander the same registration page
			write code here
			'''
			pass
