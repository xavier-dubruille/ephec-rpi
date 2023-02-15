#!/usr/bin/env python3
#-- coding: utf-8 --
from flask import Flask,redirect
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

count = 0
channel = 7 
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def my_callback(chan):
    global count
    count += 1
    print('callback '+str(count))

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)


app = Flask('xa')
@app.route("/")
def hello_world():
    global count
    return f"<p>Hello, World! <br> You have clicked {count} times (<a href='/refresh'> refresh</a> page)'"


@app.route("/refresh")
def rdirect():
    print('rrreeeedirect')
    return redirect('/')

app.run(host='0.0.0.0', port=80)

