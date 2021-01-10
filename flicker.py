import math
import RPi.GPIO as GPIO
import time

def set1_on():
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)

def set2_on():
    GPIO.output(7, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)

# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

x = 0
for i in range(1):
    x = x + 0.1
    delay = abs(math.sin(x))
    set1_on()
    time.sleep(delay)
    set2_on()
    time.sleep(delay)

GPIO.cleanup()

