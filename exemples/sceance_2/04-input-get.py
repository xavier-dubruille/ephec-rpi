from flask import Flask, request
from gpiozero import *

led = PWMLED(21, frequency=2000)
app = Flask(__name__)

@app.route('/')
def index():
    light = request.args.get('light')
    setIntensity(light)
    return f"""
<!DOCTYPE html>
<html>
<body>

<h1>Controlez l'intensité de la led</h1>

<form action="/" method="get">
  <input type="range" value={light} name="light" min="0" max="100">
  <input type="submit" value="Go">
</form>

</body>
</html>
"""


def setIntensity(light):
    print(f'Requested light is {light}')
    if(light):
        led.value = int(light)/100

app.run(host='0.0.0.0', port=80, debug=True)
