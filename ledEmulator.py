
class LedEmulator(object):
    def __init__(self, initstate=False):
        self._state = initstate

    def state(self):
        return self._state

    def on(self):
        self._state = True

    def off(self):
        self._state = False
