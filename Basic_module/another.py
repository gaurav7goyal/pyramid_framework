# another.py
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='goodbye')
def goodbye(request):
    return Response('Goodbye world!')

@view_config(route_name='home')
def hello_world(request):
    return Response('Hello world!')

def includeme(config): # <-- previously named moreconfiguration
    config.add_route('goodbye', '/goodbye')
    config.add_route('home', '/')
    config.scan()
