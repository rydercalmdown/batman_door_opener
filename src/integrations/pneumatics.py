import RPi.GPIO as GPIO
import time


PIN_EXTEND = 23
PIN_RETRACT = 24


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_EXTEND, GPIO.OUT)
    GPIO.setup(PIN_RETRACT, GPIO.OUT)


def shutdown():
    GPIO.cleanup()


def activate(delay=1):
    print('extending')
    GPIO.output(PIN_EXTEND, GPIO.HIGH)
    time.sleep(delay)
    print('retracting')
    GPIO.output(PIN_EXTEND, GPIO.LOW)
    GPIO.output(PIN_RETRACT, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(PIN_RETRACT, GPIO.LOW)


setup()
