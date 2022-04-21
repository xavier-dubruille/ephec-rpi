from flask import Flask

app = Flask('xa')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><a href=/on>led</a>"


@app.route("/on")
def led():
    return "led (virtualy) on :D "

app.run(host='0.0.0.0', port=80)

