import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)
GPIO.output(5, GPIO.LOW)

time.sleep(10)

print("Swap")

GPIO.output(7, GPIO.LOW)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)

time.sleep(10)

GPIO.cleanup()

