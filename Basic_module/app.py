from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config



if __name__ == '__main__':
    config = Configurator()
    config.include('another')  # <-- changed
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5050, app)
    server.serve_forever()
