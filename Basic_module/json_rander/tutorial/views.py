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
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}

    @view_config(route_name='myname')
    @view_config(route_name='name_json', renderer='json')
    ##name is calling html templete
    ## name and last is calling json object
    def name(self):
    	return {'name': 'Hello Gaurav','last':'Goyal'}