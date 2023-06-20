import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel numbering scheme
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 15 (physical pin 10) as an output
GPIO.setup(15, GPIO.OUT)

# Loop 5 times
for i in range(5):
    # Set GPIO pin 15 to HIGH
    GPIO.output(15, GPIO.HIGH)

    # Leave it on for 3 seconds
    time.sleep(3)

    # Set GPIO pin 15 to LOW
    GPIO.output(15, GPIO.LOW)

    # Leave it off for 3 seconds
    time.sleep(3)

# Clean up GPIO
GPIO.cleanup()
