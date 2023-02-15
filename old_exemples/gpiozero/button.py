from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def say_held():
    print("Held")

button = Button(2)

button.when_pressed = say_hello
button.when_released = say_goodbye
button.when_held = say_held

pause()
