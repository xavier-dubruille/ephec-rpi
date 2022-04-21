from threading import Event
from colorzero import Color
from gpiozero import RotaryEncoder, RGBLED, Button
import time

rotor = RotaryEncoder(17, 27, wrap=True, max_steps=360)

while True:
    time.sleep(0.5)
    print(str(rotor.steps))
