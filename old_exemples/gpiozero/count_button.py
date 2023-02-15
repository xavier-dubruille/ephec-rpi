#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

channel = 7 

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
def my_callback(chan):
    global count
    count += 1
    print('callback '+str(count))

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)

# OR (same but in two line):
#GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=200)
#GPIO.add_event_callback(channel, my_callback)

while True:
    time.sleep(1)
    print('.')
