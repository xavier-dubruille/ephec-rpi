# ephec-rpi

Vous trouverez ici des exemples ainsi que certaines informations utiles pour les ateliers Raspberry Pi en première TI à l'Ephec.

## Configurations réseau
Les Raspberry Pi ont un numéro(unique) sur leur carte SD, ce numéro défini leur IP(Statique) et leur Hostname:
* Leur IP est: `192.168.20.[numero_unique] / 24`
* Leur hostname est: `pi[numero_unique]`.
* Leur username est: `pi`
* Leur password est: `ephec` (vous pouvez le changer)

Une fois votre Raspberry allumé et branché avec un câble réseau (dans votre ordi ou dans le switch), vous pouvez vous y connecter (en ssh), soit:
* en spécifiant juste son hostname (dans l'outil utilisé pour s'y connecter) ex: ssh pi@pi10 (il se connectera en IPv6 en utilisant le protocole de neighbours discovery)
* en vous connectant au wifi du Mikotik puis en utilisant l'ipv4 du Raspberry Pi (il y a un DHCP sur l'interface du wifi, donc il n'y a rien à faire)
* en configurant une IP statique sur votre ordinateur (si vous êtes en câblé) pour être dans le même sous réseauque votre Raspberry Pi) puis utilisez l'ipv4 du RPi.

#### Accès internet : 
la GW des Raspberry Pi est `192.168.20.254` . Lorsque celui si sera branché sur le même réseau qu'une GW avec cette IP, alors il aura accès à internet. 


En théorie, il est possible de partager une connexion internet avec le RPi (en modifiant la configuration du Mikrotik et/ou du RPi), mais ça peut prendre beaucoup de temps/chippotage (et pas d'aide ne sera fournie).

#### Autre Passwords
* wifi (si il y en a) : `ephecephec` (n'hésitez pas à le changer)
* interface d'administration du Mikrotik : `ephec`  (il n'est normalement pas nécessaire d'y accéder)


## Choses à upgrader/installer sur le raspberry pi
```
sudo su
apt update
apt dist-upgrade
apt install python-pip python3-pigpio tmux vim bpython
pip install Flask
```

## Note sur les cartes SD
Il y a deux type de cartes: des cartes avec des numéro inférieur à 50 et d'autre suppérieur à 50 (entre 90 et 99 pour être exact).
* Les inférieures à 50 sont nouvelles et fiable.  
* Les suppérieur à 50 ne sont **ABSOLUMENT PAS** fiable. Ca ne devrait pas vous empêcher d'utiliser le raspberry pi (quoi que il pourrait être plus lent), mais ne l'utilisez pas pour installer des choses dessus (car il est probable que vos modifications ne s'enregistre pas réelement sur la carte et que tous disparaisse après un reboot)


## Déroulement des séances
### Séance 1
Intro au Python, au Raspberry Pi. Allumage d'une led ainsi d'une utilisation d'un bouton poussoir.



(Je ne met pas de ressources d'exemple, car une simple recherche donne que des ressources intéressantes)


Note: la librairie utilisé fût RPi.GPIO, mais on ne continuera pas avec.

### Séance 2 (jeudi 21 avril)
* (Utilisation des Microtik )
* La librairie RPi.GPIO est abandonnée au profit de gpiozero (https://gpiozero.readthedocs.io/en/stable/)
* Quelque notions théorique sur les rpi et l'electronique
* Installation de certaines chose sur votre Rpi (tel que Flask)
* Experimentation électronique avec "GPIO Zero"
* Intro à Flask: création d'un serveur Web.
* Quelques nouveaux Capteurs sont introduit
    * codeur rotatif 
    * capteurs proximité 
    * servo moteur
    * buzzer 
    * capteurs température (à confirmer)
    * Et d'autres ...


Note :  Il était prévu de mettre ici des exemple d'utilisation de la librairie 'gpio zero', mais les exemples officiel sont très bien fait (avec des couleur et des shéma) ===> aller donc plutot là-bas: https://gpiozero.readthedocs.io/en/stable/recipes.html


Note : Une difficultée de cette séance est de devoir gérer le serveur Web en même temps, ce qui implique que la partie 'electronique' du code ne peux pas bloquer la partie Web...


Note: il n'y a pas que la difficulté de 'faire marcher' le capteur, il y a aussi la difficulté lié à votre senario, ex: une led n'est pas compliqué, mais afficher un nombre en binaire l'est plus... Un bouton n'est pas compliqué, mais une mini calculatrice l'est plus,... 

* introduction au concour

### Séance 3
- travail sur votre projet
- plus de capteurs pour les intéressés

### Séance 4
- Présentation
- Jury


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
