from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

###model#######

def hello_world(request):
    return Response('gaurav!')

def city_name(request):
	return Response('delhi!')


if __name__ == '__main__':
    with Configurator() as config:
		###controller############
        config.add_route('hello', '/hello')
		###########view###############
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6544, app)
    server.serve_forever()
