from time import *
from gpiozero import *
from signal import pause

print("One button to turn on or off")

led = LED(21)
btn = Button(20, bounce_time=None)

while True:
  print('turn on')
  led.on()
  sleep(0.2) # to avoid bouncing
  btn.wait_for_press()
  print('turn off')
  led.off()
  sleep(0.2) # to avoid bouncing
  btn.wait_for_press()
