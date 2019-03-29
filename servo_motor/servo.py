import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep      # Importing sleep from time library to add delay in code
import keyboard

servo_pin = 21      # Initializing the GPIO 21 for servo motor

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin

p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
p.start(2.5) 

def right():
	p.ChangeDutyCycle(0.5)
	
def left():
	p.ChangeDutyCycle(0.5)


try:
	while 1:                    # Loop will run forever
		if keyboard.is_pressed('d'): right()
			
		if keyboard.is_pressed('q'): left()
			
#		p.ChangeDutyCycle(0.5)  # Move servo to 0 degrees
#		sleep(1)                # Delay of 1 sec
#		p.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
#		sleep(1)                
#		p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
#		sleep(1)

		
# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	pass   # Go to next line

GPIO.cleanup()              # Make all GPIO pins LOW