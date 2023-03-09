# ephec-rpi

Vous trouverez ici des exemples ainsi que certaines informations utiles pour les ateliers Raspberry Pi du projet Transversal (1T Ephec).

## Ressources utiles:
- Formation groupes : http://tiny.cc/transversal1T2023
- Teams (communications lors des séances plus communications informelles): "projet transversal" dans votre Teams
- Mail pour les communications officielles
- Exemples de code/ résolution d'exercices (par Séance + d'autre pas classé): les dossiers 'exemples' et 'exemples_old' de ce repository
- librairie python pour utilisation des gpio: https://gpiozero.readthedocs.io/en/stable/
- Une 'Cheat Sheet' qui n'a peut etre pas été finie/imprimé, mais dont les éléments la constituant se trouvant dans le dossier 'Cheat Sheet' de ce repository.
- intro au python (vous n'aurez pas besoin de grand chose): https://wiki.python.org/moin/BeginnersGuide/Programmers
==> mais beaucoup de choses existe sur internet, n'hésitez pas à chercher

## Configurations réseau
Les Raspberry Pi ont un numéro(unique) sur leur carte SD, ce numéro défini leur Hostname (et, anciennement, leur IPv4 statique):
* ~~Leur IP(pour les cartes configurée pour) est: `192.168.20.[numero_unique] / 24`~~
* Leur hostname est: `pi[numero_unique]`.
* Leur username est: `pi`
* Leur password est: `ephec` (vous pouvez le changer, mais on ne pourra pas vous aider si vous oubliez le nouveau)

Une fois votre Raspberry allumé et branché avec un câble réseau (dans votre ordi ou dans le switch), vous pouvez vous y connecter (en ssh), soit:
* En utilisant juste son hostname: ex: `ssh pi@pi10` (il se connectera en IPv6 en utilisant le protocole de *neighbours discovery*)
* ~~en configurant une IP statique sur votre ordinateur (si vous êtes en câblé) pour être dans le même sous-réseau que votre Raspberry Pi) puis utilisez l'ipv4 du RPi.~~
* Si le routeur + switchs (+ wifi ?) sont déjà en place (à partir du deuxième atelier), il y aura un serveur DHCP (avec un accès internet) et vous pourez aussi (pas obligatoire) utiliser l'IPv4 du Raspberry. Ex: `ssh pi@192.168.20.242` (note: l'ip commencera toujour par *192.168.20._ *)

==> Votre raspberry pi **ET** votre ordinateur doivent être branché sur le routeur/switch. 
Pour trouver l'adresse IP de votre Raspberry Pi, le plus simple, c'est de demander à quelqu'un d'autre (par exemple un autre groupe ? Tant qu'il est branché au switch ...), d'utiliser la méthode 1 pour vous récuperer son IP (note: pour connaitre les addresses IP sur linux, il suffit de taper `ip a`)


Note sur le wifi: **Si** il y a une connection wifi, elle sera probablement pas stable (car beaucoup d'interférences et pas prévue pour supporter beaucoup de connections simultanées) ==>  Evitez donc de l'utiliser autant que possible et, si vous devez l'utiliser, limitez le trafique !   Cette connection wifi peu avoir du sens pour accèder, depuis votre téléphone, à la page web que vous aurez construite ou si **vraiment** vous n'avez **absolument** pas d'autre solution pour brancher votre ordinateur avec un cable.

#### Autre Passwords
* wifi (si il y en a) : `ephecephec`
* interface d'administration du Mikrotik (si on utilise des Mikrotik) : `ephec`  (il n'est normalement pas nécessaire d'y accéder)


## Choses à upgrader/installer sur le raspberry pi (lorsque votre raspberry aura internet ==> à partir de la deuxième séance)
```
sudo su
apt update
apt dist-upgrade -y
apt install -y python3-pip  git tmux vim bpython
pip install Flask
```

## Conseils
- [une fois tmux installé] lancez tmux dés que vous êtes connecté ainsi, si vous perdez la connection, vous pourrez, en vous reconnectant, tapper `tmux a`, et revenir là où vous étiez
- [une fois git installé] vous pouvez faire un `git clone https://github.com/xavier-dubruille/ephec-rpi.git` pour récupérer tout ce repository (ainsi que les exemples)
- les erreurs python sont vite arrivée et la coloration syntaxique est très utile: soit codez sur votre ordinateur (dans un IDE) et copier sur votre raspberry pi (ex: avec nano) ou bien vous pouvez aussi utiliser vim

## Note sur les cartes SD
Les cartes avec un numéro au dessus de 50 (la majorité des cartes cette année) sont plus vielle et un peu moins fiable.  Normalement, ca n'impacte pas la lecture, mais l'écriture (ex: lors d'un reboot, il est possible que vos données n'aient pas persisté) ==> faites donc bien des backups sur votre PC et, au moindre comportement suspect, n'hésitez pas à venir changer votre carte ==> les professeurs ont quelques cartes avec tout le necessaire déjà installé (donc pas la peine de repasser par l'étape précédente)


## Déroulement des séances
### Séance 1 (jeudi 14 février)
Intro au Python, au Raspberry Pi. Allumage d'une led ainsi d'une utilisation d'un bouton poussoir.
Des exemples de code sont disponible dans le directory "exemples par scéance".
Ressource utile: https://gpiozero.readthedocs.io/en/stable/ ( + google ;)

### Séance 2 (jeudi 2 mars)
* (Possible: Utilisation des Microtik )
* Installation de certaines choses sur votre Rpi (tel que Flask)
* Intro à Flask: création d'un serveur Web + un peu plus de Python
* Approfondissement de l'utilisation de gpiozero + quelques notions supplémentaire sur les rpi et l'électronique


Note : Une difficultée de cette séance est de devoir gérer le serveur Web en même temps, ce qui implique que la partie 'electronique' du code ne peux pas bloquer la partie Web...


Note: il n'y a pas que la difficulté de 'faire marcher' le capteur, il y a aussi la difficulté lié à votre senario, ex: une led n'est pas compliqué, mais afficher un nombre en binaire l'est plus... Un bouton n'est pas compliqué, mais une mini calculatrice l'est plus, ... 

### Séance 3 (jeudi 9 mars)
* Quelques nouveaux capteurs sont introduit
    * codeur rotatif 
    * capteurs proximité 
    * servo moteur
    * buzzer 
    * capteurs température (à confirmer)
    * Et d'autres ...
* Définition et travail sur votre projet

### Séance 4 (jeudi 23 mars)
- Travail sur votre projet
- Présentation / Jury


# Capteurs 
Pour la troisième séance, vous avez accès à beaucoup plus de capteur afin de réaliser votre projet.

Parmi les capteurs à disposition, je les mettrais en 3 catégories: 
1. Les "conseillés" ==> ils sont 'relativement' simple, et marchent avec gpiozero (aller voir les exemples et les montage sur le site de gpiozero!)
2. les "challenging" ==> ils sont testé, du code est a disposition, mais gpiozero ne suffira pas, il faudra utiliser 'pythonCircuit', heureusement des cartes SD avec tout installé sont dispo) 
3. les "hardcore" ==> pas de code fourni, probablement qu'ils vous faudra installer des choses supplémentaire et on ne pourra vous fournir qu'une aide limité (en fonction de la disponibilité)

J'en oublie peut-etre, mais voici les capteurs disponible par catégorie:
1. Consseilé :
- Boutton and co  ==> il y a beauchoup de capteurs qui se comportent comme des boutons et sont très simpa à utiliser (genre le tilt sensor)
- LED (notement qq RGB)
- buzzer
- Capteur de lumière
- Capteur de distance
- Capteur de mouvement
- servo moteur
- encodeur rotatif
- relay ?  (pas compliqué, mais necessite un autre appareil à controler)

2. Challenging
- Capteur de températeur et humidité
- Capteur de pression et d'altitude
- Certains autre capteurs fourni dans le boite de découverte de capteurs
- 7 segment unique

3. Hardcore
- Recepteur Infra rouge
- emeteur-recepteur 433 Mhz
- multiple 7-segment
- controleur de moteur
- ... et le reste des capteurs random dispo


## Quelques info sur les capteurs à disposition (note: info pas mise à jour et incomplete)
# Le codeur rotatif
[wikipedia] "Un codeur rotatif ou capteur rotatif est un type de capteur permettant de fournir une information d'angle, en mesurant la rotation effectuée autour d'un axe.

L'information de vitesse peut alors être déduite de la variation de la position par rapport au temps. Plus le codeur rotatif tourne lentement, plus la déduction de vitesse perd en précision."

Les codeurs rotatif disponible ont 4 pin alors que dans l'exemple de 'gpio zero' il n'y en a que 3: c'est parceque ceux-ci ont également un bouton integré: c'est la pin nommée 'sw'.  Les pins nomées 'Data' et 'Clk' peuvent être inter-changé (ca influcera sur quel sens de rotation est concidéré comme le positif.

# Le Servo moteur
Le fil rouge est pour le vcc (en 5v), le brun est le Ground (0v) et le jaune est le signal (celui qui doit aller sur votre GPIO)
Note: il y en a moins disponible

# Le capteur "nivau d'eau/floteur"
Il se comporte comme un button.  Lorsque l'eau soulève le floteur le circuit est fermé.

