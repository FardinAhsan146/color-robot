import RPi.GPIO as GPIO
import time
import colorsys

NUM_CYCLES = 10 # number of measurements to perform to determine colour

S0 = 4      # S0 colour sensor
S1 = 5      # S1 colour sensor
S2 = 23     # 20 colour sensor
S3 = 24     # S3 colour sensor
Out = 25    # Out colour sensor

# setup GPIO pins (inputs/outputs)

GPIO.setmode(GPIO.BCM)

GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(Out, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#####################################################

# pin reading sequence for Red, Green, Blue measurements [S2, S3]
pin_reading_seq = [[GPIO.LOW, GPIO.LOW], [GPIO.HIGH, GPIO.HIGH], [GPIO.LOW, GPIO.HIGH], [GPIO.HIGH, GPIO.LOW]]

RGBW = [0, 0, 0, 0] # Initialize empty array to hold Red, Green, Blue & White colour sensor readings

# Set colour frequency scaling to 2% / 12 kHz
GPIO.output(S0, GPIO.LOW)
GPIO.output(S1, GPIO.HIGH)

colour_names = ['Red', 'Green', 'Blue', 'White']


def read_color():
    """
    Function descrition:
        Reads the Red, Green, Blue & White colour components from the TCS3200 colour sensor,
        converts the RGB colour into the HSV colour space, determines the colour name from the Hue value,
        and displays all of the above information on the OLED screen.
    Arguments:
        None
    Returns:
        -color_str (String with the colour name)
        -HSV_Val (list with Hue, Saturation and Value components respectively)
    """

    for idx, pin_states in enumerate(pin_reading_seq):
        # Select colour filter
        GPIO.output(S2, pin_states[0])
        GPIO.output(S3, pin_states[1])
        ##############################
        time.sleep(0.01)

        start = time.time() # start timing measurement to time pulse length

        # Wait until the NUM_cycles pulses have been counted
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(Out, GPIO.FALLING)
        ####################################################

        duration = time.time() - start # calculate duration of pulses
        RGBW[idx] = ((NUM_CYCLES / duration) / 10000) *255 # compute Red, Green and White colour components and scale to 0-255

    # Scale Red, Green & Blue components with respect to the White/Brightness reading
    RGBW[0] = (RGBW[0] /RGBW[3]) 
    RGBW[1] = (RGBW[1] / RGBW[3])
    RGBW[2] = (RGBW[2] / RGBW[3])
    #################################################################################

    HSV_val = colorsys.rgb_to_hsv(RGBW[0], RGBW[1], RGBW[2]) # Convert RGB colour readings into HSV colour space
    
    color_str = ""
    
    # Convert Red, Green & Blue values to rounded percentages
    R_perc = round(RGBW[0]*100)
    G_perc = round(RGBW[1]*100)
    B_perc = round(RGBW[2]*100)
    #########################################################

    hue_deg = round(HSV_val[0]*360) # Convert Hue to rounded degrees

    # Convert value and saturation to rounded percentages
    val_perc = round(HSV_val[1]*100)
    sat_perc = round(HSV_val[2]*100)
    #####################################################

 
    # Determine colour based on hue parameter
    if sat_perc < 35:
        color_str = "Black/Dark"
    elif hue_deg > 357 or hue_deg < 10:
        color_str = "ORANGE"
    elif hue_deg > 10 and hue_deg < 40:
        color_str = "YELLOW"
    elif hue_deg > 45 and hue_deg < 160:
        color_str = "GREEN"
    elif hue_deg > 210 and hue_deg < 270:
        color_str = "BLUE"
    elif hue_deg > 270 and hue_deg < 330:
        color_str ="PURPLE"
    elif hue_deg > 340 and hue_deg < 356:
        color_str = "RED"
    else:
        color_str = "No valid color detected"
    #########################################



    return color_str, HSV_val

print("Whadda you see?")
print("===============")

if __name__ == '__main__':

    while True:
        color_str, HSV_val = read_color() # Read and display colour name and values

        print("Detected color: {}".format(color_str))