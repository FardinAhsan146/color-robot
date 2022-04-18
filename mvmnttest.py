############################
# Multi Motor test, Fardin
# Status: 
############################
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

## Initialize pins
# Enables
gpio.setup(17, gpio.OUT) # ENB
gpio.setup(16, gpio.OUT) # ENA

# Left wheel
gpio.setup(27, gpio.OUT) # IN3
gpio.setup(22, gpio.OUT) # IN4

#Right wheel
gpio.setup(20, gpio.OUT) # IN1
gpio.setup(21, gpio.OUT) # IN2

    
def forward(t = 5):
    """
    Default to 5 seconds of travel
    unless specified otherwise
    """
    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA
    
    gpio.output(20, False)
    gpio.output(21, True)
    gpio.output(22, True)
    gpio.output(27, False)
    
    time.sleep(t)
    
    gpio.cleanup() 
    
def reverse(t = 5):

    gpio.output(17, True) # ENB
    gpio.output(16, True) # ENA

    gpio.output(20, True)
    gpio.output(21, False)
    gpio.output(22, True)
    gpio.output(27, False)
    
    time.sleep(t)
    
    gpio.cleanup()
    
def turn_left(t = 5):

    gpio.output(17, False) # ENB
    gpio.output(16, True) # ENA

    gpio.output(20, True)
    gpio.output(21, False)
    gpio.output(22, False)
    gpio.output(27, False)
    
    time.sleep(t)
    
    gpio.cleanup()
    
def turn_right(t = 5):

    gpio.output(17, True) # ENB
    gpio.output(16, False) # ENA

    gpio.output(20, False)
    gpio.output(21, False)
    gpio.output(22, True)
    gpio.output(27, False)
    
    time.sleep(t)
    
    gpio.cleanup()
    
if __name__ == '__main__':

    while True:
    
        x = input('Enter direction: ')
        
        if x == 'f':
            forward()
        elif x == 'b':
            reverse()
        elif x == 'r':
            right_turn()
        elif x == 'l':
            turn_left()
        else:
            print('Ending test')
            gpio.cleanup()
            break
            
    
