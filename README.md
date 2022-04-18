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


Il est possible de partager une connexion, de modifier la configuration du Microtik et/ou du RPi, mais ça peut prendre beaucoup de temps (et pas d'aide ne sera fournie)

#### Autre Passwords
* wifi (si il y en a) : `ephecephec` (n'hésitez pas à le changer)
* interface d'administration du Mikrotik : `ephec`  (il n'est normalement pas nécessaire d'y accéder)



## Déroulement des séances
### Séance 1
Intro au Python, au Raspberry Pi. Allumage d'une led ainsi d'une utilisation d'un bouton poussoir.



(Je ne met pas de ressources d'exemple, car une simple recherche donne que des ressources intéressantes)


Note: la librairie utilisé fût RPi.GPIO, mais on ne continuera pas avec.

### Séance 2 (jeudi 21 avril)
* (Utilisation des Microtik )
* La librairie RPi.GPIO est abandonnée au profit de gpiozero: Expérimentation avec une led et un bouton
* Intro à Flask: création d'un serveur Web.
* Quelques nouveaux Capteurs sont introduit
    * encodeur rotatif (difficultée 2/3)
    * capteurs proximité (difficultée 1/3)
    * buzzer (difficultée 1.5/3)
    * capteurs température (difficultée 3/3)
    * Et d'autres ...


Une grande difficultée de cette séance est de devoir gérer le serveur Web en même temps, ce qui implique que la partie 'electronique' du code ne peux pas bloquer la partie Web...


Note: il n'y a pas que la difficulté de 'faire marcher' le capteur, il y a aussi la difficulté lié à votre senario, ex: une led n'est pas compliqué, mais afficher un nombre en binaire l'est plus... Un bouton n'est pas compliqué, mais une mini calculatrice l'est plus,... 

* introduction au grand concours

### Séance 3
- travail sur votre projet
- plus de capteurs pour les intéressés

### Séance 4
- Présentation
- Jury

