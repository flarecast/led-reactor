from reactor import Reactor
import RPi.GPIO as GPIO
import time

class LEDReactor(Reactor):
    event_kinds = {"input"}
    # TODO: Move this to XML
    GPIO_OUT = 4

    def __init__(self):
        Reactor.__init__(self)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LEDReactor.GPIO_OUT, GPIO.OUT)

    def react(self, alert):
        GPIO.output(LEDReactor.GPIO_OUT, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(LEDReactor.GPIO_OUT, GPIO.LOW)
