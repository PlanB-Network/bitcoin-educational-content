---
name: Ashigaru Terminal
description: Utiliser Ashigaru sur desktop pour faire des coinjoins
---

![cover](assets/cover.webp)

Ashigaru Terminal est la version desktop de l'applciaiton mobile Ashigaru, qui s’inscrit dans la continuité du travail initié par Samourai Wallet, dont elle reprend les principes fondamentaux : self-custody et outils pour préserver sa confidentialité. Ce logiciel spécifiquement Ashigaru Terminal sur dekstop est un fork de Sparrow Server, adapté et optimisé pour une intégration complète avec l’écosystème Whirlpool, le protocole de coinjoin ZeroLink développé initialement par les équipes de Samourai.

Ashigaru Terminal fonctionne depuis une interface en ligne de commande et peut être déployé sur un ordinateur classique ou bien sur un serveur. Il permet d’interagir directement avec Whirlpool afin d’initier des "Tx0", de gérer les comptes "Deposit", "Premix", "Postmix" et "Badbank", et de procéder à des remixages automatiques pour renforcer la confidentialité de vos pièces.

Donc pour faire simple, Ashigaru Terminal va surtout vous être utile si vous souhaitez faire des coinjoins avec Whirlpool.

Dans ce premier tutoriel, je vais vous guider dans l'installation et la prise en main d'Ashigaru Terminal, puis, dans un second tutoriel plus avancé, nous verrons comment faire des coinjoins.

## 1. Installer Ashigaru Terminal

Pour installer Ashigaru Terminal, vous aurez besoin de Tor Browser, car les binaires ne sont distribués que via Tor. Si vous ne l'avez pas encore, [installez le sur votre machine](https://www.torproject.org/download/).

### 1.1. Télécharger Ashigaru Terminal

Sur Tor Browser, rendez-vous ensuite [sur la page de realese de leur dépot Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) pour télécharger la dernioère version en fonciton de votre système d'exploitation.

```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```

01

Téléchargez les 2 fichiers suivants correspondant à votre système d’exploitation :
- Le binaire (par exemple `ashigaru_terminal_v1.0.0_amd64.deb`, `.dmg` ou `.zip`)
- Le fichier de hachages signés : `ashigaru_terminal_v1.0.0_signed_hashes.txt`

### 1.2. Vérifier Ashigaru Terminal

Avant de lancer le logiciel sur votre appareil, nous allons vérifier son authenticité et son intégrité. Cette étape est très importante, car elle vous permet d'éviter d'installer un logiciel frauduleux qui pourrait voler vos bitcoins ou infecter votre machine.

Ouvrez un nouvel onglet dans Tor Browser et accédez à [l’outil de vérification Keybase](https://keybase.io/verify). Collez dans le champ prévu le contenu du fichier `.txt` téléchargé que vous venez de télécharger, puis cliquez sur le bouton `Verify`.

02

Pour diversifier les sources, vous pouvez vérifier que ce message est bien le même que sur le site clearnet `ashigaru.rs` dans la section `/download`.

03

Si la signature est authentique, Keybase affichera un message confirmant que le fichier a bien été signé par les développeurs d’Ashigaru.

04

Vous pouvez également cliquer sur le profil `ashigarudev` indiqué par Keybase et vérifier que l’empreinte de leur clé correspond exactement à : `A138 06B1 FA2A 676B`.

05

En revanche, si une erreur apparaît à cette étape, cela signifie que la signature n’est pas valide. Dans ce cas, **n’installez pas le logiciel téléchargé**. Reprenez la procédure depuis le début ou demandez de l’aide à la communauté avant de poursuivre.

Keybase vous a fourni le hachage de l’application. Nous allons maintenant vérifier que le hachage du fichier `.deb`, `.zip` ou `.dmg` que vous avez téléchargé correspond bien à celui vérifié sur Keybase. Pour cela, rendez-vous sur le site [HASH FILE ONLINE](https://hash-file.online/).

Cliquez sur le bouton `BROWSE...` et sélectionnez le fichier `.deb`, `.zip` ou `.dmg` téléchargé à l’étape 1.1. Choisissez ensuite la fonction de hachage `SHA-256`, puis cliquez sur `CALCULATE HASH` pour calculer le hachage de votre fichier.

06

Le site vous affichera le hachage de votre binaire. Comparez-le à celui que vous avez vérifié sur Keybase.io. Si les deux hachages sont identiques, la vérification d’authenticité et d’intégrité est réussie. Vous pouvez alors procéder à l’installation du logiciel.

07

### 1.3 Lancer Ashigaru Terminal

- **Debian / Ubuntu**

Pour installer le logiciel, exécutez la commande :

```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```

Modifiez la commande en fonciton de la evrsion téléchargée.

Vérifiez ensuite l’installation :

```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```

Puis lancez le logiciel :

```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```

- **Windows**

Faites un clic droit sur le dossier `.zip` téléchargé et vérifié, puis cliquez sur `Extract All...`.

Il vous suffit ensuite de double cliquer sur le logiciel `Ashigaru-terminal.exe` pour lancer le logiciel.

08

## 2. Prendre en main Ashigaru Terminal

Ashigaru Terminal est un logiciel en TUI (*Text-based User Interface*). Autrement dit, c'est une interface minimaliste dans un terminal sur laquelle vous pouvez intéragir avec des menus, des raccourcis clavier, mais sans environnement graphique.

09

Pour utiliser ce logiciel c'est assez simple, vous pouvez utiliser les flèches vers le bas et vers le haut de votre clavier pour vous déplacer dans l'interface, et utiliser la touche `Enter` pour confirmer un choix.

## 3. Connecter son nœud à Ashigaru Terminal

Par défaut, Ashigaru Terminal va se connecter à un serveur Electrum public. Cela pose évidemment des risques en termes de confidentialité et d'indépendance, c'est pourquoi nous allons directement nous connecter à notre propre Electrum Server.

Pour ce faire, rendez-vous dans le menu `Preferences > Server`.

10

Cliquez sur le bouton `< Edit >`.

11

Sélectionnez `Private Electrum Server`, puis `<Continue>`.

12

