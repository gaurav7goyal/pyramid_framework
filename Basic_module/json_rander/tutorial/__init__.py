from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.add_route('myname','/name')
    config.add_route('name_json', '/name.json')
    config.scan('.views')
    return config.make_wsgi_app()