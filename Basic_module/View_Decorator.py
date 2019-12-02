from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import my_View

###model#######
@view_config(route_name='hello')
def hello_world(request):
    return Response('gaurav!')
@view_config(route_name='city')
def city_name(request):
	return Response('delhi!')


if __name__ == '__main__':
	with Configurator() as config:
		config.add_route('hello','/')
		config.add_route('city','/city')
		config.include(my_View.model)
		config.scan()
		app=config.make_wsgi_app()
	server=make_server('0.0.0.0',6544,app)
	server.serve_forever()


