import os
from RPi import GPIO
 
os.system('clear') #clear screen, this is just for the OCD purposes
 
step = 5 #linear steps for increasing/decreasing volume
paused = False #paused state
 
#tell to GPIO library to use logical PIN names/numbers, instead of the physical PIN numbers
GPIO.setmode(GPIO.BCM) 
 
#set up the pins we have been using
clk = 17
dt = 18
sw = 27
 
#set up the GPIO events on those pins
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
#get the initial states
counter = 0
clkLastState = GPIO.input(clk)
dtLastState = GPIO.input(dt)
swLastState = GPIO.input(sw)
 
#define functions which will be triggered on pin state changes
def clkClicked(channel):
        global counter
        global step
 
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
 
        if clkState == 0 and dtState == 1:
                counter = counter + step
                print ("Counter ", counter)
 
def dtClicked(channel):
        global counter
        global step
 
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
         
        if clkState == 1 and dtState == 0:
                counter = counter - step
                print ("Counter ", counter)
 
def swClicked(channel):
        global paused
        paused = not paused
        print ("Paused ", paused)             
                 
print ("Initial clk:", clkLastState)
print ("Initial dt:", dtLastState)
print ("Initial sw:", swLastState)
print ("=========================================")
 
#set up the interrupts
GPIO.add_event_detect(clk, GPIO.FALLING, callback=clkClicked, bouncetime=300)
GPIO.add_event_detect(dt, GPIO.FALLING, callback=dtClicked, bouncetime=300)
GPIO.add_event_detect(sw, GPIO.FALLING, callback=swClicked, bouncetime=300)
 
raw_input("Start monitoring input")
 
GPIO.cleanup()
