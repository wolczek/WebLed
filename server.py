import os
import os.path
import cherrypy

from ledWebService import LedWebService

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return file('index.html')

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/ledapi': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

    webapp = HelloWorld()
    webapp.ledapi = LedWebService()

    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
    cherrypy.quickstart(webapp, '/', conf)

