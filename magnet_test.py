##################################
# Electro magnet test script, Fardin
# Status: passed
##################################

import RPi.GPIO as GPIO          
import time

GPIO.setmode(GPIO.BCM)

in1, in2, en = 6,26,19

#Set all outputs to 1
for pin in (in1, in2, en):
    GPIO.setup(pin,GPIO.OUT)

print('Starting Magnet test script')

while True:

    x = input('On (n) or off (f) ?')
    if x == 'n':
        GPIO.output(en, True)
        print('going forward')
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        time.sleep(5)
    elif x == 'f':
        GPIO.output(en, False)
        print('going backwards')
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        time.sleep(5)
    else:
        GPIO.cleanup()
        break