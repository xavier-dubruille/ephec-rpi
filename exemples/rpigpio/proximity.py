#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PIN = 7 

GPIO.setup(PIN, GPIO.IN) 

while True:
    print(str(GPIO.input(PIN)))
    time.sleep(0.3) 
