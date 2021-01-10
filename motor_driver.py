from time import sleep
import RPi.GPIO as gpio

EN = 21
DIR = 20
STEP = 16
CW = 1
CCW = 0

class motor_driver:

    def __init__(self):
        #gpio.setmode(gpio.BCM)
        gpio.setup(DIR, gpio.OUT)
        gpio.setup(STEP, gpio.OUT)
        gpio.output(DIR, CW)

    def motor_run(self, time, ticks, direction):

        gpio.output(DIR, direction)
        for x in range(ticks):
            gpio.output(STEP, gpio.LOW)
            sleep(time)
            gpio.output(STEP, gpio.HIGH)
            sleep(time)


"""
# Main body of code
try:
    while True:
        sleep(1)
        gpio.output(DIR, CW)
        for x in range(400):
            gpio.output(STEP, gpio.HIGH)
            sleep(.0005)
            gpio.output(STEP, gpio.LOW)
            sleep(.0005)

        sleep(1)
        gpio.output(DIR, CCW)
        for x in range(400):
            gpio.output(STEP, gpio.HIGH)
            sleep(.0010)
            gpio.output(STEP, gpio.LOW)
            sleep(.0010)




except KeyboardInterrupt:  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
"""