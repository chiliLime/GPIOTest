import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel numbering scheme
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 18 as an output
GPIO.setup(18, GPIO.OUT)

# Set GPIO pin 18 to HIGH
GPIO.output(18, GPIO.HIGH)

# Leave it on for 10 seconds
time.sleep(10)

# Reset the pin to low and clean up GPIO
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()

