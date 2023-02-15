from time import *
from gpiozero import *
from signal import pause


print("one button, blink by default, stop when pressed")

led = LED(21)
btn = Button(20)

def pressed():
  print('pressed')
  led.off()

def released():
  print('released')
  led.blink(0.5, 0.5)


released()
btn.when_pressed = pressed
btn.when_released = released

pause()
