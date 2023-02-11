# ephec-rpi

Vous trouverez ici des exemples ainsi que certaines informations utiles pour les ateliers Raspberry Pi du projet Transversal (1T Ephec).

## Ressources utiles:
- Formation groupes : http://tiny.cc/transversal1T2023
- Teams (communications officiel et informel): "projet transversal" dans votre Teams
- Exemples de codes: ce github
- librairie python pour utilisation des gpio: https://gpiozero.readthedocs.io/en/stable/
- intro au python: https://wiki.python.org/moin/BeginnersGuide/Programmers
==> mais beaucoup de choses existe sur internet, n'hésitez pas à chercher

## Configurations réseau
Les Raspberry Pi ont un numéro(unique) sur leur carte SD, ce numéro défini leur IP(Statique) et leur Hostname:
* Leur IP est: `192.168.20.[numero_unique] / 24`
* Leur hostname est: `pi[numero_unique]`.
* Leur username est: `pi`
* Leur password est: `ephec` (vous pouvez le changer, mais on ne pourra pas vous aider si vous oubliez le nouveau)

Une fois votre Raspberry allumé et branché avec un câble réseau (dans votre ordi ou dans le switch), vous pouvez vous y connecter (en ssh), soit:
* en utilisant juste son hostname: ex: ssh pi@pi10 (il se connectera en IPv6 en utilisant le protocole de neighbours discovery)
* en configurant une IP statique sur votre ordinateur (si vous êtes en câblé) pour être dans le même sous réseauque votre Raspberry Pi) puis utilisez l'ipv4 du RPi.
* Si les routeurs (et access point wifi) sont déjà en place (normalement à partir du deuxième atelier), vous aurrez un serveur DHCP et vous pourrez vous y connecter en spéficiant son address IPv4 (plus d'info arriveront lorsque le réseau sera en place)


#### Autre Passwords
* wifi (si il y en a) : `ephecephec` (n'hésitez pas à le changer)
* interface d'administration du Mikrotik (si on utilise des Mikrotik) : `ephec`  (il n'est normalement pas nécessaire d'y accéder)


## Choses à upgrader/installer sur le raspberry pi
```
sudo su
apt update
apt dist-upgrade
apt install python-pip python3-pigpio git tmux vim bpython
pip install Flask
```

## Note sur les cartes SD
Vos cartes sont normalement entre 51 et 80.  Si ce n'est pas le cas, prevenez-nous.
Pour info:
* Les cartes entre 1 et 30 sont des cartes probablement pas vierge, utilisé pour l'année passée
* Les carte entre 90 et 100 sont des cartes en fin de vie qui ne sont **ABSOLUMENT PAS** fiable

Si vous avez des soucis tel que des difficultées à vous connecter ou un système buggé (du, par exemple, à une mauvaise manipulation), un mot de passe oublié, ...  n'hésitez pas venir echanger votre carte.


## Déroulement des séances
### Séance 1 (jeudi 14 février)
Intro au Python, au Raspberry Pi. Allumage d'une led ainsi d'une utilisation d'un bouton poussoir.
Des exemple de code sont disponible dans le directory "exemples par scéance".
Ressource utile: https://gpiozero.readthedocs.io/en/stable/ ( + google ;)

### Séance 2 (jeudi 2 mars)
* (Possible: Utilisation des Microtik )
* Installation de certaines chose sur votre Rpi (tel que Flask)
* Intro à Flask: création d'un serveur Web + un peu plus de Python
* Approfondissement de l'utilisation de gpiozero + quelques notions supplémentaire sur les rpi et l'electronique


Note : Une difficultée de cette séance est de devoir gérer le serveur Web en même temps, ce qui implique que la partie 'electronique' du code ne peux pas bloquer la partie Web...


Note: il n'y a pas que la difficulté de 'faire marcher' le capteur, il y a aussi la difficulté lié à votre senario, ex: une led n'est pas compliqué, mais afficher un nombre en binaire l'est plus... Un bouton n'est pas compliqué, mais une mini calculatrice l'est plus,... 

### Séance 3 (jeudi 9 mars)
* Quelques nouveaux Capteurs sont introduit
    * codeur rotatif 
    * capteurs proximité 
    * servo moteur
    * buzzer 
    * capteurs température (à confirmer)
    * Et d'autres ...
* travail sur votre projet

### Séance 4 (jeudi 23 mars)
- travail de groupe
- Présentation / Jury


## Quelques info sur les capteurs à disposition
# Le codeur rotatif
[wikipedia] "Un codeur rotatif ou capteur rotatif est un type de capteur permettant de fournir une information d'angle, en mesurant la rotation effectuée autour d'un axe.

L'information de vitesse peut alors être déduite de la variation de la position par rapport au temps. Plus le codeur rotatif tourne lentement, plus la déduction de vitesse perd en précision."

Les codeurs rotatif disponible ont 4 pin alors que dans l'exemple de 'gpio zero' il n'y en a que 3: c'est parceque ceux-ci ont également un bouton integré: c'est la pin nommée 'sw'.  Les pins nomées 'Data' et 'Clk' peuvent être inter-changé (ca influcera sur quel sens de rotation est concidéré comme le positif.

# Le Servo moteur
Le fil rouge est pour le vcc (en 5v), le brun est le Ground (0v) et le jaune est le signal (celui qui doit aller sur votre GPIO)
Note: il y en a moins disponible

# Le capteur "nivau d'eau/floteur"
Il se comporte comme un button.  Lorsque l'eau soulève le floteur le circuit est fermé.


## Ressources utile
* https://create.withcode.uk/python/A5  ==> pour tester un code python en ligne (en utlisant RPi.GPIO)
* https://gpiozero.readthedocs.io/en/stable/recipes.html
