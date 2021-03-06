############################
# Multi Motor test, Fardin
# Status: 
############################
import RPi.GPIO as gpio
import time

## Initialize pins
# Enables
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) # ENB
    gpio.setup(16, gpio.OUT) # ENA

	# Left wheel
    gpio.setup(27, gpio.OUT) # IN3
    gpio.setup(22, gpio.OUT) # IN4

	#Right wheel
    gpio.setup(20, gpio.OUT) # IN1
    gpio.setup(21, gpio.OUT) # IN2

    
def reverse(t = 1):
    """
    Default to 5 seconds of travel
    unless specified otherwise
    """
    init()
    
    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA
    
    gpio.output(20, False)
    gpio.output(21, True)
    gpio.output(22, True)
    gpio.output(27, False)
    
    time.sleep(t)
    
    gpio.cleanup() 
    
def forward(t = 1):
    init()
    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA

    gpio.output(20, True)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, True)
    
    time.sleep(t)
    
    gpio.cleanup()
    
def turn_right(t = 0.5):
    init()
    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA

    gpio.output(20, True)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, False)
    
    time.sleep(t)
    
    gpio.cleanup()
    
def turn_left(t = 0.5):
    init()
    gpio.output(17, True) # ENB
    gpio.output(16, False) # ENA

    gpio.output(20, False)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, True)
    
    time.sleep(t)
    
    gpio.cleanup()
    
if __name__ == '__main__':

    while True:
    
        x,_t = input('Enter direction: ').split()
        _t = float(_t)

        if x == 'f':
            forward(t = _t)
        elif x == 'b':
            reverse(t = _t)
        elif x == 'r':
            turn_right(t = _t)
        elif x == 'l':
            turn_left(t = _t)
        else:
            print('Ending test')
            break
