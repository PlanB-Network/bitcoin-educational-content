---
name: Neutrino
description: Guide d'installation de LND Neutrino
---

# Configuration de Raspberry Pi avec LND

1. Télécharger Raspberry Pi OS Lite

Téléchargez Raspberry Pi OS Lite à partir de [cette page](https://www.raspberrypi.org/software/operating-systems/). Les instructions pour télécharger et installer l'image sur une carte micro SD sont disponibles pour Windows, Mac et Linux.

2. Formater la carte SD

Formatez la carte SD avec Raspberry Pi Imager ou balenaEtcher.

> NOTE: Le symbole `$` est utilisé comme invite et permet à l'utilisateur de saisir des commandes sur l'ordinateur. Les commandes seront interprétées par bash sous Linux. Le symbole `#` au début d'une ligne indique que le texte qui suit est un commentaire.

3. Activer SSH

Avant de démarrer Raspberry Pi avec la carte mémoire formatée, insérez-la dans un ordinateur et créez deux fichiers qui nous permettront de nous connecter à distance. Utilisez la commande `touch` pour créer un fichier vide dans la partition /boot. Cela activera la connexion SSH lors du premier démarrage de la carte SD nouvellement formatée.

```
# NOTE: Si la microSD est montée sur /media/microSD, la commande
# devrait être $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4.- Utilisez la commande nano pour créer le fichier wpa_supplicant.conf et commencez à l'éditer directement. Dans ce fichier, copiez la configuration du wifi en copiant le texte entre DÉBUT et FIN, puis modifiez le SSID et le mot de passe du wifi auquel vous souhaitez vous connecter.

```
$ nano /boot/wpa_supplicant.conf

------ DÉBUT -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ FIN -------
```

5.- Insérez ensuite la carte SD dans Raspberry Pi et connectez la rpi à une source d'alimentation pour démarrer le système d'exploitation. Vous devrez la trouver sur le réseau, probablement le protocole mDNS lui attribuera le nom raspberrypi.local sur le réseau. Essayons de nous connecter via SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Si cela ne fonctionne pas, vous devrez trouver le réseau. Trouvons l'adresse IP à laquelle nous sommes connectés.

```
$ ifconfig
```

Si par exemple, c'est 192.168.0.0, utilisez nmap pour trouver la rpi.

```
nmap -v 192.168.0.0/24
```

Supposons que nous trouvions une nouvelle IP sur notre réseau, 192.168.0.30.

Connectez-vous via SSH.

```
$ ssh pi@192.168.0.30
password: raspberry
```

6.- Configurez la rpi

```
$ sudo raspi-config
```

- Sélectionnez l'option (1) et changez le mot de passe de l'utilisateur pi'
- Nous sélectionnons l'option (8) pour mettre à jour l'outil de configuration vers la dernière version
- Nous sélectionnons l'option (4) pour sélectionner notre fuseau horaire
- Nous sélectionnons l'option (7) puis "Expand filesystem"
- Terminé

  7.- Nous mettons à jour le système d'exploitation

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Nous ajoutons l'utilisateur bitcoin

```
$ sudo adduser bitcoin
```

9.- Nous sécurisons la rpi

```
$ sudo apt install ufw
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'allow SSH from LAN'
$ sudo ufw allow 9735 comment 'allow Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- Nous installons go: si vous n'utilisez pas un raspberry pi, téléchargez go pour votre architecture ici (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # doit afficher le message suivant 'go version go1.13.5 linux/arm'
```

11.- Nous compilons et installons lnd

```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli version 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```

12.- Nous créons le fichier de configuration de lnd, cela doit être fait avec l'utilisateur 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# permet les paiements spontanés
accept-keysend=1

# Nom public du nœud
alias=TU_ALIAS
# Couleur publique en hexadécimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# Socket gRPC
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Pour que LND démarre après le démarrage de la rpi, nous devons créer le fichier .service dans systemd
'Si nous sommes connectés en tant qu'utilisateur bitcoin et que nous voulons revenir à l'utilisateur pi, il suffit d'écrire "exit"

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Exécution du service
###################

ExecStart=/usr/local/bin/lnd


# Gestion des processus
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Création de répertoires et permissions
####################################

# Exécuter en tant que bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Mesures de renforcement de la sécurité
####################

# Fournir un /tmp et /var/tmp privés.
PrivateTmp=true

# Monter /usr, /boot/ et /etc en lecture seule pour le processus.
ProtectSystem=full

# Interdire au processus et à tous ses enfants d'acquérir
# de nouveaux privilèges via execve().
NoNewPrivileges=true

# Utiliser un nouvel espace de noms /dev peuplé uniquement de pseudo-périphériques API
# tels que /dev/null, /dev/zero et /dev/random.
PrivateDevices=true

# Refuser la création de mappages de mémoire modifiables et exécutables.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Nous pouvons voir les journaux en exécutant la commande journalctl

```
$ sudo journalctl -f -u lnd
```

14. Maintenant, nous lançons lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Ajouter des fonds à notre nœud

```
$ lncli newaddress p2wkh
```

Envoyer des bitcoins à l'adresse renvoyée par lnd

Pour vérifier le solde

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Une fois la transaction confirmée, nous pouvons ouvrir un canal. Si vous ne savez pas encore avec quel nœud ouvrir le canal, vous pouvez aller sur 1ml.com et choisir un nœud.

Nous établissons une connexion avec un nœud :

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Ensuite, nous ouvrons un canal

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Nous vérifions nos fonds

```
$ lncli walletbalance
$ lncli channelbalance
```

Nous pouvons voir les canaux en attente et actifs

```
$ lncli pendingchannels
$ lncli listchannels
```

Pour payer une facture lightning

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Pour recevoir un paiement, je crée une facture pour un montant spécifique

````
$ lncli addinvoice --memo 'mi primer pago en LN' --amt 100```
````

Pour voir des informations sur mon nœud

```
$ lncli getinfo
```

La liste complète des commandes peut être consultée en exécutant simplement lncli

```
$ lncli
```

Enfin, pour effectuer des appels à l'API de lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> FIN
