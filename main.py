############################
# Main Script, Robotics Final Project
# "Color sensing" Robot
# By Fardin 
############################
import RPi.GPIO as gpio
import sshkeyboard
import time

## Initialize pins
# Enables
def init():
    """
    Initialize pins, motors 
    """
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) # ENB (Motor driver)
    gpio.setup(16, gpio.OUT) # ENA

	# Left wheel
    gpio.setup(27, gpio.OUT) # IN3
    gpio.setup(22, gpio.OUT) # IN4

	#Right wheel
    gpio.setup(20, gpio.OUT) # IN1
    gpio.setup(21, gpio.OUT) # IN2
    
def init_magnet():
    # Magnet init
    gpio.setmode(gpio.BCM)
    gpio.setup(19,gpio.OUT) # ENA (Magnet driver)
    gpio.setup(6,gpio.OUT) #IN1
    gpio.setup(26,gpio.OUT) #IN2
    

def reverse():
    """
    Travel until specified otherwise!
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
    
# def magnet_on():
    # """
    # Create a massive amount 
    # of magnetic field
    # """
    # gpio.cleanup()
    # init()
    
    # gpio.output(19, True)
    # print('Magnet ON')
    # gpio.output(6,gpio.HIGH)
    # gpio.output(26,gpio.LOW)
    
# def magnet_off():
    # """
    # Trust Flyback diode 
    # """
    # init()
    # print('Magnet OFF')
    # gpio.cleanup()

def clean_all():
    gpio.cleanup()

def clean_motor():
    gpio.cleanup((17,16,27,22,20,21))

def release(x):    
    """
    Clear gpio class method
    on keystroke release
    """
    if x == 'm':
        clean_motor()
    elif x in ('w','a','s','d'):
        clean_motor()
    else:
        clean_all()
        


def press(x):
    """
    Program press NOT TAP
    actions on key stroke
    """

    # Wheel controls
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
    elif x == 'm':
        clean_motor()
        init_magnet()
    elif x == 'f':
        clean_all()
    else:
        gpio.cleanup()
        print('Ending test')
        return None

if __name__ == '__main__':

    while True:
        sshkeyboard.listen_keyboard(on_press = press
        ,on_release = release)

