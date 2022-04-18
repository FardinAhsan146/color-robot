#################
# Ultra sonic sensor test script by Fardin
# Used to test the functionanlity of the us sensors
# seems to work within 10% worst case error.
# Testing status = PASS
#################

import RPi.GPIO as GPIO
import time
 
# Setting to board mode
GPIO.setmode(GPIO.BCM)
 
# pin configuration
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # Send pulses 0.01 ms
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    # Initialize time counters
    start_time,stop_time = time.time(),time.time()
 
    # sent time
    while not GPIO.input(GPIO_ECHO):
        start_time = time.time()
 
    # arrival time
    while GPIO.input(GPIO_ECHO):
        stop_time = time.time()
 
    # delta time
    time_elapsed = stop_time - start_time

    # (34300 cm/s)/2 -> speed of sound
    return (time_elapsed * 34300) / 2
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print(f"Measured Distance = {dist:0.1f} cm")
            time.sleep(1)
 
    # To exit test script
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
