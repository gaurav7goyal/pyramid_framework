from pyramid.view import view_config
from pyramid.response import Response

class model(object):

	def __init__(self,request):
		pass

	###model#######
	@view_config(route_name='name')
	def hello_world(request):
	    return Response('gaurav goyal!')

	def includeme(config):
		config.add_route('name','/name')
		config.add_view(hello_world, route_name='name')