---
name: Neutrino
description: Guide d'installation du LND Neutrino
---
![image](assets/cover.webp)


## Configuration du Raspberry Pi avec LND


### 1. Télécharger Raspberry Pi OS Lite


Les instructions pour télécharger et installer l'image sur une carte micro SD sous Windows, Mac et Linux se trouvent sur [cette page](https://www.raspberrypi.org/software/operating-systems/).


### 2. Formater la carte SD


Utilisez Raspberry Pi Imager ou balenaEtcher.


**Note:** Le symbole `$` est utilisé comme invite et permet à l'utilisateur de saisir des instructions dans le terminal. Ces instructions seront ensuite interprétées par bash sous Linux. Le symbole `#`, placé au début d'une ligne, indique que ce qui suit est un commentaire.


### 3. Activer SSH


Avant de démarrer le Raspberry Pi avec la carte SD formatée, il faut d’abord l'insérer dans un ordinateur afin d’y créer deux fichiers nécessaires qui nous permettront de nous connecter à distance. Grâce à la commande `touch`, on crée un fichier vide dans la partition /boot, ce qui permet d’activer la connexion SSH dès le premier démarrage du Raspberry Pi.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Créer un fichier pour la connexion Wi-Fi


Avec la commande nano, nous créons le fichier `wpa_supplicant.conf` et l’ouvrons directement pour l'éditer. Dans ce fichier, il suffit copier la configuration wifi, en copiant le texte entre START et END, puis de remplacer le SSID et le mot de passe du wifi auquel vous voulez vous connecter.


```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
ssid="MyNetworkSSID"
psk="password"
}
------ END -------
```


### 5. Connexion


Ensuite, insérez la carte SD dans le Raspberry Pi, puis connectez-le à l'alimentation pour lancer le système d'exploitation. Il faut ensuite l'identifier sur le réseau, grâce au protocole mDNS, il portera généralement le nom raspberrypi.local. Nous pouvons maintenant tenter de nous connecter via SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Si cela ne fonctionne pas, nous devons vérifier le réseau. Commençons par identifier l'address IP à laquelle nous sommes connectés.


```
$ ifconfig
```


Par exemple, s'il s'agit de 192.168.0.0, utilisez nmap pour trouver le Pi.


```
nmap -v 192.168.0.0/24
```


Si nous découvrons une nouvelle address IP sur notre réseau, nous pouvons nous y connecter via SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Configurer le Pi


```
$ sudo raspi-config
```


- Sélectionnez l'option (1) et modifiez le mot de passe de l'utilisateur pi.
- Choisissez l'option (8) pour mettre à jour l'outil de configuration à la dernière version
- Sélectionnez l'option (4) pour sélectionner notre fuseau horaire
- Choisissez l'option (7) pour étendre le système de fichiers
- Finition


### 7. Mettre à jour le système d'exploitation


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Ajouter l'utilisateur Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Sécuriser l'IPR


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


### 10. Installer Go


Si vous n'utilisez pas de raspberry pi, téléchargez go for your architecture [ici](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Compilation et installation de LND


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


### 12. Créer le fichier conf de LND


Créer le fichier de configuration LND, avec l'utilisateur 'Bitcoin'


```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```


```
[Application Options]
# enable spontaneous payments
accept-keysend=1

# Public name of the node
alias=YOUR_ALIAS
# Public color in hexadecimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```


### 13. LND service autostart


Pour que LND se lance automatiquement au démarrage du Raspberry Pi, nous devons créer un fichier .service dans systemd. Si nous sommes connectés en tant qu'utilisateur Bitcoin et que nous souhaitons revenir à l'utilisateur pi, il suffit de taper 'exit'.


```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```


```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Service execution
###################

ExecStart=/usr/local/bin/lnd


# Process management
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Directory creation and permissions
####################################

# Run as bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```


```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```


Nous pouvons consulter les journaux en exécutant la commande journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Maintenant nous commençons LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Ajouter des fonds au nœud


```
$ lncli newaddress p2wkh
```

Vous pouvez maintenant envoyer des BTC à l’adresse fournie par LND.


avec cette commande, vous pouvez vérifier le solde :


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Une fois la transaction confirmée, nous pouvons ouvrir un canal. Si vous ne savez pas avec quel nœud ouvrir le canal, vous pouvez aller sur 1ml.com et choisir un nœud.


Ouvrir une connexion à un nœud :


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Ouvrez ensuite un canal :


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Vérifiez nos fonds :


```
$ lncli walletbalance
$ lncli channelbalance
```


Nous pouvons voir les canaux en attente et les canaux actifs :


```
$ lncli pendingchannels
$ lncli listchannels
```


Pour payer un éclair Invoice :


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Pour recevoir un paiement, créez une Invoice pour un montant spécifique :


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Pour consulter des informations sur mon nœud :


```
$ lncli getinfo
```


La liste complète des commandes peut être consultée en exécutant simplement la commande lncli :


```
$ lncli
```


Enfin, pour faire des appels à l'API LND :


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Fin du guide !
