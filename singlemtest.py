##################################
# single motor test script, Fardin
# Status: passed
##################################

import RPi.GPIO as GPIO          
import time

GPIO.setmode(GPIO.BCM)

in1, in2, en = 23, 24, 25

#Set all outputs to 1
for pin in (in1, in2, en):
    GPIO.setup(pin,GPIO.OUT)

print('Starting Motor test script)

while True:

    x = input('Enter direction')
    if x == 'f':
        GPIO.output(en, True)
        print('going forward')
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        time.sleep(5)
    elif x == 'b':
        GPIO.output(en, True)
        print('going backwards')
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        time.sleep(5)
    else:
        GPIO.cleanup()
        break