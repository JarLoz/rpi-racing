import RPi.GPIO as GPIO
import time

CHANNEL = 17;

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN)

previous_input = 1
while True:
	gpio_input = GPIO.input(CHANNEL)
	if(previous_input != gpio_input):
		previous_input = gpio_input
		print("Input changed to " + str(previous_input))
