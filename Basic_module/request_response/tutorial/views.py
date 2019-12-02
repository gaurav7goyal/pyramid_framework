from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import (
    view_config,
    view_defaults
    )



@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return HTTPFound(location='/name')

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}

    @view_config(route_name='myname')
    def name(self):
        name = self.request.params.get('name', 'No Name Provided')
        body = 'URL %s with name: %s' % (self.request.url, name)
        # return Response(
        #     content_type='text/plain',
        #     body=body
        # )
        return {'name': name }