import platform

import cherrypy

class LedWebService(object):
    exposed = True

    def __init__(self):
        if platform.machine() == "armv6l":
            from ledGpio import LedGpio
            self.led = LedGpio()
        else:
            from ledEmulator import LedEmulator
            self.led = LedEmulator()

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        if self.led.state() is False:
            return "off"
        else:
            return "on"

    def POST(self, state="off"):
        if state.lower() == "on":
            self.led.on()
        else:
            self.led.off()

        return str(self.led.state()).lower()

#    def PUT(self, another_string):
#        cherrypy.session['mystring'] = another_string

#    def DELETE(self):
#        cherrypy.session.pop('mystring', None)
