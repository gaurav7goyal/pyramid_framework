import colander
import deform.widget

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

users = {
    '101': dict(uid='101',firstName='gaurav',lastName='goyal',age='22'),
    '102': dict(uid='102',firstName='saurav',lastName='goyal',age='21'),
    '103': dict(uid='103',firstName='sachin',lastName='goyal',age='20')
}


class LoginPage(colander.MappingSchema):
    firstName = colander.SchemaNode(colander.String())
    lastName  = colander.SchemaNode(colander.String())
    age       = colander.SchemaNode(colander.String())
    # body = colander.SchemaNode(
    #     colander.String(),
    #     widget=deform.widget.RichTextWidget()
    # )


class UserViews(object):
    def __init__(self, request):
        self.request = request

    @property
    def user_form(self):
        schema = LoginPage()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        return self.user_form.get_widget_resources()

    @view_config(route_name='user_view', renderer='user_view.pt')
    def user_view(self):
        return dict(users=users.values())

    @view_config(route_name='user_add',
                 renderer='userdetails_addedit.pt')
    def userdetail_add(self):
        form = self.user_form.render()
        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.user_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(form=e.render())
                

            # Form is valid, make a new identifier and add to list
            last_uid = int(sorted(users.keys())[-1])
            new_uid = str(last_uid + 1)
            users[new_uid] = dict(
                uid=new_uid, 
                firstName=appstruct['firstName'],
                lastName=appstruct['lastName'],
                age=appstruct['age'],
               
            )
            # Now visit new page
            url = self.request.route_url('userpage_view', uid=new_uid)
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='userpage_view', renderer='userpage_view.pt')
    def userpage_view(self):
        uid = self.request.matchdict['uid']
        user = users[uid]
        return dict(user=user)

    @view_config(route_name='user_edit',
                 renderer='userdetails_addedit.pt')
    def userpage_edit(self):
        uid = self.request.matchdict['uid']
        user = users[uid]

        user_form = self.user_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = user_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(page=user, form=e.render())

            # Change the content and redirect to the view
            user['firstName']=appstruct['firstName'],
            user['lastName']=appstruct['lastName'],
            user['age']=appstruct['age']

            url = self.request.route_url('userpage_view',
                                         uid=user['uid'])
            return HTTPFound(url)

        form = user_form.render(user)

        return dict(page=user, form=form)