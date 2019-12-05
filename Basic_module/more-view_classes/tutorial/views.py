from pyramid.view import view_config
from pyramid.view import view_defaults


# First view, available at http://localhost:6543/
@view_config(route_name='home', renderer='default_home.pt')
def home(request):
    return {'name': 'Home View'}


# /howdy
# @view_config(route_name='hello', renderer='home.pt')
# def hello(request):
#     return {'name': 'Hello View'}

@view_config(route_name='myname', renderer='default_home.pt')
def name(request):
	return {'name': 'gaurav'}


@view_defaults(route_name='hello')
class TutorialViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'

    @property
    def full_name(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return first + ' ' + last

  

    # Retrieving /howdy/first/last the first time
    @view_config(renderer='hello.pt')
    def hello(self):
        return {'page_title': 'Hello View'}

    # Posting to /howdy/first/last via the "Edit" submit button
    @view_config(request_method='POST', renderer='edit.pt')
    def edit(self):
        new_name = self.request.params['new_name']
        return {'page_title': 'Edit View', 'new_name': new_name}

    # Posting to /howdy/first/last via the "Delete" submit button
    @view_config(request_method='POST', request_param='form.delete',
                 renderer='delete.pt')
    def delete(self):
        print ('Deleted')
        return {'page_title': 'Delete View'}