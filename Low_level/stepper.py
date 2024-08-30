import RPi.GPIO as GPIO
import time

# GPIO Pin setup
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200  # Steps per Revolution (360 / 1.8)

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

# Stepper Motor Configuration
step_count = SPR * 16  # Full revolution with microstepping (if MS1, MS2, MS3 are set)
delay = 0.001          # Delay between steps (adjust for speed control)

# Rotate the motor
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

# Change direction and rotate again
GPIO.output(DIR, CCW)
time.sleep(0.5)

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(delay)

# Cleanup GPIO pins
GPIO.cleanup()
