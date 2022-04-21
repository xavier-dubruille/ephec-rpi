from flask import Flask,redirect
import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs

app = Flask('xa')

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p><a href=/on>led</a>"


def turn_led7_on_off():
    GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
    GPIO.setwarnings(False) #On désactive les messages d'alerte
    
    LED = 7 #Définit le numéro du port GPIO qui alimente la led
    
    GPIO.setup(LED, GPIO.OUT) #Active le contrôle du GPIO
    
    state = GPIO.input(LED) #Lit l'état actuel du GPIO, vrai si allumé, faux si éteint
    
    if state : #Si GPIO allumé
        GPIO.output(LED, GPIO.LOW) #On l’éteint
    else : #Sinon
        GPIO.output(LED, GPIO.HIGH) #On l'allume


@app.route("/on")
def led():
    print('turn on/off led 7')
    
    turn_led7_on_off()
    return redirect('/')

@app.route("/redirect")
def rdirect():
    print('rrreeeedirect')
    return redirect('/')

app.run(host='0.0.0.0', port=80)

