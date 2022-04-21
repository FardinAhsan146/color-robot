############################
# Multi Motor test -- input, Fardin
# Status: 
############################
import RPi.GPIO as gpio
import sshkeyboard
import time

## Initialize pins
# Enables
def init():
    """
    Initialize pins
    """
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) # ENB
    gpio.setup(16, gpio.OUT) # ENA

	# Left wheel
    gpio.setup(27, gpio.OUT) # IN3
    gpio.setup(22, gpio.OUT) # IN4

	#Right wheel
    gpio.setup(20, gpio.OUT) # IN1
    gpio.setup(21, gpio.OUT) # IN2
    
    
def reverse():
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

    
def forward():
    init()
    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA

    gpio.output(20, True)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, True)

    
def turn_right():
    init()
    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA

    gpio.output(20, True)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, False)
   
    

    
def turn_left():
    init()
    gpio.output(17, True) # ENB
    gpio.output(16, False) # ENA

    gpio.output(20, False)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, True)

def release(x):    
    gpio.cleanup()

def press(x):
    if x == 'w':
        print('Going forward')
        forward()
    elif x == 's':
        print('Going backwards')
        reverse()
    elif x == 'd':
        print('Turning right')
        turn_right()
    elif x == 'a':
        print('Turning left')
        turn_left()
    else:
        gpio.cleanup()
        print('Ending test')
        return None

if __name__ == '__main__':

    while True:
        sshkeyboard.listen_keyboard(on_press = press
        ,on_release = release)

