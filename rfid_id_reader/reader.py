import RPi.GPIO as GPIO
import SimpleMFRC522
from time import sleep
import subprocess
import webbrowser

reader = SimpleMFRC522.SimpleMFRC522()

file = open("ID.txt", "a")

def slow_type(message):
    for character in message:
        print(character, end="")
        sleep(0.01)
    print("\n")

slow_type("Hold a tag near the reader")

try:
    while True:
        id, text = reader.read()
        print(id)
        file.write(str(id) + "\n")
        sleep(0.1)
        if id == 303135970126:
            slow_type("Bienvenue Anthony Amar. \n Laissez-moi ouvrir pour vous le navigateur internet avec votre site préféré")
            webbrowser.open_new("https://bison-ville-texas.herokuapp.com/")
            sleep(0.2)
        else:
            print(id)
        
            
        
except KeyboardInterrupt:
    print("cleaning up :-)")
    GPIO.cleanup()
    file.close()



