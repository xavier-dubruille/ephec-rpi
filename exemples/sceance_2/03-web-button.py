from flask import Flask
from gpiozero import Button

button = Button(20)

# on crée un tableau avec une seule valeur
count = [42]

app = Flask(__name__)

def increment():
    # on accède à l'indice 0 du tableau, et on l'incrémente de 1
    count[0] +=1

# on choisi la fonction qui est appelée lors d'un press (notez bien qu'il n'y a pas de parentaizes ! )
button.when_pressed = increment

@app.route('/')
def index():
    # le 'f' devant nous permet de mettre des variables (en utilisant {}) dans le texte
    return f"""
<html>
<body>
<script>
  setTimeout(()=> window.location.reload(), 1000)
</script>

  Count = {count[0]}
</body>
</html> """

# notez que si vous laisser le port 80, il faudra le lancer avec sudo
app.run(host='0.0.0.0', port=80, debug=True)
