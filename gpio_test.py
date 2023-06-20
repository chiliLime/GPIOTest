import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel numbering scheme
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 10 as an output
GPIO.setup(10, GPIO.OUT)

# Set GPIO pin 10 to HIGH
GPIO.output(10, GPIO.HIGH)

# Leave it on for 30 seconds
time.sleep(30)

# Reset the pin to low and clean up GPIO
GPIO.output(10, GPIO.LOW)
GPIO.cleanup()

