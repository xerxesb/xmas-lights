ENABLE_GPIO = False

import math
import time
import os
from rich.console import Console

if (ENABLE_GPIO):
    import RPi.GPIO as GPIO

console = Console()

def print_set1_on():
    os.system('clear')
    console.print("\r*     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *", style='bold blue')

def print_set2_on():
    os.system('clear')
    console.print("\r   *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *", style='bold blue')

def set1_on():
    print_set1_on()
    if (ENABLE_GPIO):
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)

def set2_on():
    print_set2_on()
    if (ENABLE_GPIO):
        GPIO.output(7, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)

def get_delay(x):
    if x < 50:
        delay = 0.1 
    elif x > 90:
        delay = 0.5
    else:
        delay = 0.2 

    return delay

if (ENABLE_GPIO):
    # GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)

x = 0
while True:
    x = x + 1
    delay = get_delay(x)
    set1_on()
    time.sleep(delay)
    set2_on()
    time.sleep(delay)

    if x > 100:
        x = 0

if (ENABLE_GPIO):
    GPIO.cleanup()

