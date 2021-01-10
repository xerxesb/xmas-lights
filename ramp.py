import math
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

# GPIO.output(7, GPIO.HIGH)
# GPIO.output(5, GPIO.LOW)

def fade_pwm(pwm):
    for i in range(0, 100000):
        x = abs(math.sin(i/100)) * 100
        pwm.ChangeDutyCycle(x)
        time.sleep(0.05)



# pwm7 = GPIO.PWM(7, 1000)
# pwm7.start(0)
# fade_pwm(pwm7)
# 
# GPIO.cleanup()
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(5, GPIO.OUT)

pwm5 = GPIO.PWM(5, 500)
pwm5.start(0)
fade_pwm(pwm5)

GPIO.cleanup()

