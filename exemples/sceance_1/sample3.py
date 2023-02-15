from time import *
from gpiozero import *
from signal import pause


print("two buttons: one to turn on, one to turn off")

led = LED(21)
btn1 = Button(20)
btn2 = Button(16)

def pressed1():
  print('button 1 pressed')
  led.off()

def pressed2():
  print('button 2 pressed')
  led.on()


btn1.when_pressed = pressed1
btn2.when_pressed = pressed2

pause()
