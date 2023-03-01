from flask import Flask, redirect
from gpiozero import *

app = Flask(__name__)
led = LED(21)

@app.route('/')
def index():
    # note: les 3 guillemets permetent de définir une chaine de charactère multi-ligne
    return """
<!DOCTYPE html>
<html>
<head>
<style>
.button {
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 50px;
  transition-duration: 0.4s;
  cursor: pointer;
  color: black;
  border: 2px solid #4CAF50;
}

.button:hover {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<body>

<h1>Controle une LED</h1>

<a href="/led" class="button">On / Off</a>

</body>
</html>
"""


@app.route('/led')
def led_page():
    print('leeeeddd')
    led.toggle()
    return redirect('/')


app.run(host='0.0.0.0', port=80, debug=True)
