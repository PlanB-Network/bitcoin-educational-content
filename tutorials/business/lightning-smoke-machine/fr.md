---
name: Lightning Smoke Machine
description: Déclenchez une machine à fumée avec un paiement Lightning via ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)

## Introduction

Transforme une machine à fumée classique en dispositif payable en Bitcoin via Lightning Network. Chaque paiement déclenche automatiquement un jet de fumée !

- Niveau : Intermédiaire
- Temps estimé : 2-3 heures
- Cas d'usage : Événements Bitcoin, performances artistiques, démos Lightning, effets scéniques automatisés

## Prérequis

### Connaissances

 - Bases en électronique (câblage, relais)
 - Soudure (ou utilisation de connecteurs Dupont)
 - Notions de configuration réseau (WiFi, WebSocket)

### Comptes nécessaires

- BTCPay Server : Instance fonctionnelle (self-hosted ou hébergée)
- Blink Wallet : Compte + accès API

### Accès

- Accès admin à BTCPay Server
- Connexion WiFi pour l'ESP32

## Matériel nécessaire

### Hardware - Composants électroniques 

- 1 Microcontrôleur - ESP32-WROOM-32 
*L'ESP32-WROOM-32 est un microcontrôleur WiFi/Bluetooth compact et peu coûteux qui permet de connecter des appareils électroniques à Internet et de les contrôler à distance.*

![ESP32](assets/fr/1.webp)

- 1 Module relais - 5V avec optocoupleur
*Un relais, c'est comme un interrupteur que l'ESP32 peut actionner pour allumer ou éteindre la machine à fumée.*

![relay](assets/fr/2.webp)

- ~10 Câbles Dupont - Mâle/Mâle et Mâle/Female

![dupont-cables](assets/fr/3.webp)

- 1 Alimentation pour l'ESP32 - 5V USB ou batterie Li-Po

![battery](assets/fr/4.webp)

- 1 Cable micro-USB - connexion entre l'ESP32 et son alimentation

![micro-usb-cables](assets/fr/5.webp)

- 1 Machine à fumée 220V avec télécommande à pile 12V

![remote-and-smoke-machine](assets/fr/6.webp)

- 1 bouteille de liquide compatible avec votre machine à fumée

### Hardware - Outils 

- Fer à souder + étain (si soudure)
- Tournevis
- Multimètre (recommandé)

### Logiciels

- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Navigateur web compatible WebSerial (Chrome/Edge/Brave)
- BTCPay Server configuré. Pour plus d'informations sur la création d'une instance BTCPay Server, rendez-vous sur ce tutoriel : https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Architecture du système

![architecture-lightning-smoke-machine](assets/fr/7.webp)

---


**⚠️** **AVERTISSEMENT SÉCURITÉ - LIRE AVANT DE CONTINUER** **⚠️** 

Ce projet implique une machine à fumée branchée sur **secteur 220V**. Une erreur de manipulation peut provoquer une **électrocution mortelle** ou un **incendie**.

**Règles non négociables :**

1. **Débranchez TOUJOURS la machine à fumée du secteur** avant d'ouvrir la télécommande ou de toucher au câblage
2. **Retirez la pile de la télécommande** avant toute manipulation (risque de court-circuit et de dommage aux composants)
3. **Vérifiez l'isolation de toutes vos connexions** avant de rebrancher quoi que ce soit
4. **Ne rebranchez jamais le 220V** tant que le boîtier de la télécommande n'est pas refermé et sécurisé

Si vous n'êtes pas à l'aise avec ces manipulations, faites-vous accompagner par quelqu'un qui a l'expérience.

---

## PARTIE 1 : Montage Hardware

### Étape 1 : Préparation de la télécommande

Objectif : Connecter le relais au bouton ON/OFF de la télécommande
1. Ouvrir la télécommande 
    - Identifier le bouton ON/OFF
    - Dévisser le boîtier pour ouvrir la télécommande 
2. Repérer les connexions
	- Localisez les bornes + et - du bouton 
	- Testez la continuité au multimètre (optionnel)

![smoke-machine-remote](assets/fr/8.webp)

3. Câblage du bouton (soudure ou connecteurs)
    - Souder un câble noir sur la borne - du bouton
    - Souder un câble rouge sur la borne + commune

![smoke-machine-remote](assets/fr/9.webp)

### Étape 2 : Connexion au module relais

**Rappel : Terminologie du relais**

| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Câblage de la télécommande vers le module relais :**
- Fil noir du bouton ON/OFF **→** NO (Normally Open)
- Fil rouge (commun) **→** COM (Common)

**Logique :** 
Quand l'ESP32 active le relais, il relie COM et NO, ça revient exactement à appuyer sur le bouton de la télécommande. 
Quand l'ESP32 coupe le relais, COM et NO se séparent, ça revient à relâcher le bouton. 

![remote-relay](assets/fr/10.webp)

### Étape 3 : Connexion de l'ESP32 au module relais

**Schéma de câblage :**

| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |
**Vérification :**
- VCC et GND bien connectés (polarité)
- GPIO 21 utilisé pour le signal de commande 
- Pas de court-circuit visible 

![relay-esp32](assets/fr/11.webp)

**Checkpoint Hardware**
Avant de passer au logiciel, vérifiez : 
- Télécommande câblée correctement 
- Module relais connecté à l'ESP32
- Pas de fils dénudés touchant d'autres composants
- 220V toujours débranchés

![relay-esp32](assets/fr/12.webp)



---


## PARTIE 2 : Configuration Logicielle

Nous prendrons *Blink* comme exemple, mais *BTCPay Server* propose également *Strike, Breez et Boltz* si vous préférez une autre option. 

### Étape 1 : Plugins, Installation *BitcoinSwitch* + *Blink

1 - Rendez-vous sur votre instance *BTCPay Server* avec un compte admin

2 - Créer votre premier store

3 - Dans la partie gauche de *BTCPay Server*, faire défiler jusqu'en bas et aller dans *"Manage Plugins"*

![btcpay-plugins](assets/fr/13.webp)

4 - Nous allons installer le plugins *BitcoinSwitch* ainsi que *Blink* 

![btcpay-plugins](assets/fr/14.webp)

5 - Faire dérouler la liste des plugins et cliquer sur *"Install"* : *BitcoinSwitch et Blink* (ou le wallet disponible de votre choix)

![btcpay-plugins](assets/fr/15.webp)

6 - Une fois l'installation faite, redémarrer *BTCPay Server* et attendre 1 minute que l'instance redémarre

![btcpay-plugins](assets/fr/16.webp)

7 - Lorsque vous retournez dans *"Manage plugins"*, vérifiez que les deux plugins ont bien été installés

![btcpay-plugins](assets/fr/17.webp)

### Étape 2 : Backend : Configuration *BTCPay Server + Blink*

**1 - Créer un wallet *Blink***
- Rendez-vous sur https://www.blink.sv
- Créez votre compte. Pour ça, vous pouvez vous référer au tutoriel : 

[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)

**2 - Générer un clé API *Blink***
- Accédez à l'interface API : **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** et connectez vous avec le même compte que lors de la création de votre wallet *Blink*

![blink-api](assets/fr/18.webp)
   
   - Une fois connecter, aller dans l'onglet *API Keys* 

![blink-api](assets/fr/19.webp)
   
   - Cliquez sur *" + "* en haut à droite pour accéder à la configuration de votre API Key

![blink-api](assets/fr/20.webp)
   
   - Donnez un nom à votre API Key et laissez les paramètres par défaut. Puis, à la troisième étape notez précieusement votre API Key, vous ne la verrez qu'une seule fois : `blink_mZ5KxxxxxxxxxxxxxxxNbmX` 

  ![blink-api](assets/fr/21.webp)

   - Une fois créée, vous devez la voir apparaître dans votre liste d'API Key active. 

![blink-api](assets/fr/22.webp)

**3 - Connecter *Blink* à *BTCPay Server***
- Ouvrez votre *BTCPay Server*
- Naviguez vers : *Wallet* **→** *Lightning*

![btcpay-server](assets/fr/23.webp)

- Cliquez sur *Use a custom node*
- Collez la chaîne de connexion suivante : 

```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```

**⚠️** **Important** : 
- Ne modifiez pas la première partie : `type=blink;server=https://api.blink.sv/graphql`;
- Remplacez uniquement : 
    - api-key= *par votre clé API Blink*
    - wallet-id= *par votre ID de wallet Blink*
- Cliquez ensuite sur *Test connexion*, puis sur *Save*

![btcpay-server](assets/fr/24.webp)
 
 - Vérifiez que la connexion est établie (statut vert)

![btcpay-server](assets/fr/25.webp)

**4 - Créer un Point of Sale (PoS)**
- Dans BTCPay Server, allez dans l'onglet *Plugins* et cliquez sur *Point of sale*

![btcpay-server](assets/fr/26.webp)

- Donner un nom à votre PoS et cliquer sur *Create*

![btcpay-server](assets/fr/27.webp)

- Configuration du PoS :
    - Choose a point of sale style = *Print display*
    - Currency = *SATS*
    - Cliquez sur *SAVE*

![btcpay-server](assets/fr/28.webp)

- Configuration du produit :
    - Supprimer tous les produit présents par défaut
    - Cliquez ensuite sur *add item*

![btcpay-server](assets/fr/29.webp)

![btcpay-server](assets/fr/30.webp)

- Configurez le produit : 
    - Title : *smoke-machine*
    - Price : *10 sats*
    - Bitcoin switch GPIO : 21
    - Bitcoin switch duration (en millisecondes) : 5000
    - Cliquez sur *Close* puis sur *Save* pour enregistrer le nouveau produit

![btcpay-server](assets/fr/31.webp)

### Étape 3 : Firmware : Flashage de l'ESP32

**1 - Accéder au site de flashage**
- Rendez-vous sur : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)

![bitcoinswitch-lnbits](assets/fr/32.webp)

**2 - Flasher le firmware BitcoinSwitch**
- Branchez l'ESP32 à votre ordinateur avec votre câble USB/Micro-USB
- Puis, cliquez sur *Connect to Device*
- Une fenêtre s'ouvre, sélectionnez le port USB de votre ESP32, puis cliquez sur *Connect* 

![bitcoinswitch-lnbits](assets/fr/33.webp)
   
- Une fois votre ESP32 connecté, nous allons y flasher le firmware BitcoinSwitch. Dans la section *T-Display*, cliquez sur *Upload Firmware* de la dernière version disponible (actuellement : *bitcoinSwitch T-Display v1.0.1*)

![bitcoinswitch-lnbits](assets/fr/34.webp)

- Patientez pendant l'upload, le processus est terminé lorsque les logs affichent *"Leaving..."*
 ![bitcoinswitch-lnbits](assets/fr/35.webp)
   
- Débranchez l'ESP32

**3 - Vérification de l’installation du firmware BitcoinSwitch**
- Rechargez la page : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Rebranchez l'ESP32 à votre ordinateur avec votre câble USB/Micro-USB
- Puis, cliquez sur *Connect to device
- Sélectionnez le Port USB de votre ESP32, puis cliquez sur *Connect* comme nous l’avons vu précédemment
- Une fois connecté, appuyez sur le bouton **RESET** de l'ESP32
- Vérifiez dans les logs que les dernières lignes affichent :

``` 
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```

(C'est normal, ça signifie qu'il n'y a pas encore de config, mais que le firmware à bien été installé)

![bitcoinswitch-lnbits](assets/fr/36.webp)

**4 - Générer l'URL WebSocket LNURL**

Format final attendu :

```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```

Étapes de génération :
- Ouvrez votre instanceBTCPay Server, puis allez dans le PoS que nous avons créé ultérieurement.
- Cliquez ensuite sur “View”, pour ouvrir votre PoS dans le navigateur

![btcpay-server-https](assets/fr/37.webp)

- Copiez l'URL de la page, exemple : 	 

![btcpay-server-https](assets/fr/38.webp)

Décortiquons cette URL :

```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```

- `XXXXv` → le domaine de votre instance BTCPay Server
- `46XXXXXXXXXXXXXXXXXXXXwFB` → l'identifiant unique de votre PoS
- `/pos` → indique qu'il s'agit d'un Point of Sale

Transformez-la :
- Remplacez `https://` par `wss://`
- Ajoutez `/bitcoinswitch` à la fin

Résultat :

```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```

Gardez bien cette URL pour la suite de la configuration, c'est elle qui permettra à votre ESP32 de communiquer en temps réel avec BTCPay Server. Le protocole WebSocket (`wss://`) établit une connexion permanente entre les deux : dès qu'un paiement Lightning est confirmé sur votre PoS, BTCPay envoie instantanément l'information à l'ESP32, qui peut alors déclencher votre machine à fumée.

**5 - Configurer le WiFi et le WebSocket**
- Retournez sur la page : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) avec votre ESP32 connecté
- Allez dans la partie *Configure Device* → *Wifi Settings*

Renseignez :
- WiFi SSID : le nom de votre réseau WiFi
- WiFi Password : le mot de passe de votre WiFi

![bitcoinswitch-lnbits](assets/fr/39.webp)

- Dans la section *LNbits Device URL*, collez l'URL WebSocket créé à l'étape précédente
- Cliquez sur *Upload config*

![bitcoinswitch-lnbits](assets/fr/40.webp)

- Attendez la fin de l'upload, les logs doivent afficher les paramètres que vous venez d'entrer (SSID, mot de passe et URL WebSocket)

![bitcoinswitch-lnbits](assets/fr/41.webp)

- Attendez pendant que l'ESP32 établit la connexion WebSocket. Vous devriez voir apparaître : 

```
WiFi connection established!

[WebSocket] Connected to url: ...
```

![bitcoinswitch-lnbits](assets/fr/42.webp)

- Vous pouvez maintenant débrancher l'ESP32

---
## Checkpoint Logiciel

Avant le test final, vérifiez :

-  Blink connecté à BTCPay
-  PoS créé avec au moins 1 item
-  ESP32 flashé avec BitcoinSwitch
-  WiFi configuré sur l'ESP32
-  WebSocket URL correcte
-  Logs ESP32 sans erreur

---

## Test et Débogage

### Test final complet

1. Branchez la smoke machine (220V) et allumez-la
2. Alimentez l'ESP32 (batterie ou USB)
3. Ouvrez votre BTCPay PoS dans votre navigateur
4. Scannez l'item "smoke-machine"
5. Payez via un wallet Lightning (Blink ou autre wallet)
6. Observez :
	- Le relais clique (son audible et la LED du relais s’allume)
	- La smoke machine s'active
	- Fumée générée !

### Problèmes féquents et solutions

| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Ressources

### Liens utiles

- BitcoinSwitch Firmware : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)

### Communauté & Support

- **BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Mattermost officiel
- **BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- **LNbits** : [t.me/lnbits](https://t.me/lnbits) - Telegram officiel, communauté active
- **BitcoinSwitch (bugs firmware)** : [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)

### Code source

- Code source du firmware BitcoinSwitch : [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)

---

**⚡** Stack sats, make smoke, have fun, stay humble! **⚡**
