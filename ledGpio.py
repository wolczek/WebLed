import RPi.GPIO as GPIO

#GPIO.cleanup()

class LedGpio(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)

    def state(self):
        return True if GPIO.input(18) == 1 else False

    def on(self):
        GPIO.output(18, True)

    def off(self):
        GPIO.output(18, False)
