from flask import Flask

# D'abord on crée notre application Flask (vous n'avez rien à changer)
app = Flask(__name__)

# puis on va l'utiliser pour "créer" des routes, en associant une route (ex "/youpie")
# à la méthode python qui sera appelé quand quelqu'un ira sur cette route.
#
# La route '/' est la route correspondant à la racine du site,
# Pour y acceder (à adapter), on peut taper dans un navigateur 192.168.20.105:8000
# (Pour connaitre l'ip de votre raspberry, vous pouvez taper 'ip a')
@app.route('/')
def index():
    return '<h1>Bienvenue sur la page principale</h1>'


# Pour aller sur cette route ('/hello'), il suffit d'aller sur 192.168.20.206:8000/hello
@app.route('/hello')
def hello():
    return 'Vous voici sur la page <b>hello</b>'


# Cette ligne va lancer flask sur le host et le port demandé
# (gardez le host a 0.0.0.0, c'est plus simple)
# mettez le port que vous voulez. Le 80 est particulièrement sympa car, étant celui par
# default pour une page web: vos visiteurs ne devront plus spécifier de port...
# Par contre, vous devrez lancer votre application en root en mettant 'sudo' devant votre commande
#  ==> sudo python intro.py
app.run(host='0.0.0.0', port=8000)
