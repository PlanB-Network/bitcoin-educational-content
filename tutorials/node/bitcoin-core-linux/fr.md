# Faire tourner son propre nœud avec Bitcoin Core

Introduction à Bitcoin et au concept de nœud, complémenter d'un guide complet d'installation sur Linux.

_**Ce tutoriel vous est offert par WINTER ☩ HODLER via l'initiative Agora256. Merci de les soutenirs et bravo pour leur travail**_

L'une des propositions les plus enivrantes de Bitcoin est de pouvoir exécuter le programme soi-même, et ainsi de participer à un niveau granulaire au réseau et à la vérification du registre public des transactions.

Bitcoin, un projet à code-source libre, est distribué publiquement et disponible gratuitement depuis 2009. Près de 15 ans après son apparition, Bitcoin est aujourd'hui un réseau monétaire numérique étoffé et inarrêtable, bénéficiant d'un effet de réseau organique puissant. Pour ses efforts et sa vision, Satoshi Nakamoto mérite notre gratitude. D'ailleurs, nous hébergeons le livre blanc de Bitcoin ici sur Agora 256 (note: également sur l'université).

## Devenir sa propre banque

Faire tourner son propre nœud devient un incontournable pour les adhérents à l'axiome Bitcoin. Sans demander la permission à quiconque, il est possible de télécharger la chaîne de blocs depuis le début et ainsi de vérifier toutes les transactions de A à Z selon le protocole Bitcoin.

Le programme contient également son portefeuille. Ainsi, nous avons le contrôle sur les transactions que nous émettons au reste du réseau, sans intermédiaire ou tierce partie. Vous êtes votre propre banque.

La suite de cet article se veut donc un guide d'installation de Bitcoin Core — la version logicielle Bitcoin la plus répandue — spécifiquement sur distributions Linux compatibles avec Debian, telles que Ubuntu et Pop!/\_OS. Suivez ce guide pour faire un pas de plus vers votre souveraineté de l'individu.

## Guide d'installation de Bitcoin Core sur Debian/Ubuntu

    Prérequis

    - 6GB minimum de stockage de données (nœud élagué/pruned node) — 1TB de stockage de données (nœud complet/full node)

    - Prévoir au moins 24 heures pour la complétion du IBD (Initial Block Download ou Chargement Initial des Blocs). Cette opération est obligatoire même pour un nœud élagué.

    - Prévoir ~600GB de bande passante pour le IBD, même pour un nœud élagué.


    💡 Les commandes suivantes sont prédéfinies pour la version 24.1 de Bitcoin Core.

## Téléchargement et vérification des fichiers

1. Télécharger bitcoin-24.1-x86_64-linux-gnu.tar.gz, ainsi que les fichiers SHA256SUMS et SHA256SUMS.asc. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Ouvrir un terminal dans le répertoire où se trouve les fichiers téléchargés. Ex.: cd ~/Downloads/.
3. Vérifier que la somme de contrôle (checksum) du fichier de version est bien listée dans le fichier de sommes de contrôle en utilisant la commande sha256sum --ignore-missing --check SHA256SUMS.

4. Le sortant de cette commande devrait inclure le nom du fichier de version téléchargé ainsi que "OK". Ex: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Installer git avec la commande sudo install git. Puis, clôner le repo contenant les clés PGP des signataires de Bitcoin Core en utilisant la commande git clone https://github.com/bitcoin-core/guix.sigs.
6. Importer les clés PGP de tous les signataires avec la commande gpg --import guix.sigs/builder-keys//\*
7. Vérifier que le fichier de sommes de contrôle est bien signé avec les clés PGP des signataires avec la commande gpg --verify SHA256SUMS.asc.

Chaque signature retournera une ligne débutant par : gpg: Good signature et une autre se terminant avec Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (exemple du fingerprint de la clé PGP de Pieter Wuille).

    💡 Il n'est pas nécessaire que l'entièreté des clés de signataires retourne un "OK". En réalité, seulement une pourrait être nécessaire. C'est à l'utilisateur de déterminer son propre seuil de validation par rapport à la vérification via PGP.

    Vous pouvez ignorer les messages WARNING: This key is not certified with a trusted signature!
    There is no indication that the signature belongs to the owner.

## Installation de l'interface graphique de Bitcoin Core

1. Dans le terminal, toujours dans le répertoire où se trouve le fichier de version Bitcoin Core, utiliser la commande tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz pour extraire les fichiers contenu dans l'archive.

2. Installation des fichiers, extraits précédemment, avec la commande sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Installation des dépendances nécessaire avec la commande sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Démarrage de bitcoin-qt (interface graphique de Bitcoin Core) avec la commande bitcoin-qt.

5. Pour choisir un noeud élagué, cocher Limit blockchain storage et configurer la limite de données à stocker :

![welcome](assets/1.jpeg)

## Conclusion de la partie 1 : guide d'installation

Une fois que Bitcoin Core est installé, il est recommandé de le laisser tourner au maximum pour pouvoir faire profiter le réseau Bitcoin de son apport à la vérification des transactions et transmission de nouveaux blocs vers d'autres pairs.

Néanmoins, faire tourner et synchroniser son nœud par intermittence, ne serait-ce que pour valider les transactions reçues ainsi que celles émises, demeure une bonne pratique.

![Creation wallet](assets/2.jpeg)

** Fin de l'articl 1 offert par Agora256 ; lien original: https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/ , nous continuons de suite avec la section 2 **

# Configuration de Tor pour un nœud Bitcoin Core

    💡 Ce guide est conçu pour Bitcoin Core 24.0.1 sur distributions Linux compatibles avec Ubuntu/Debian.

## Installation et configuration de Tor pour Bitcoin Core

D'abord, il nous faut installer le service Tor (The Onion Router), un réseau utilisé pour la communication anonyme, lequel nous permettra d'anonymiser nos intéractions avec le réseau Bitcoin. Pour une introduction aux outils de protection de la vie privée en ligne, incluant Tor, référez-vous à notre article à ce sujet.

Pour installer Tor, ouvrez un terminal et entrez sudo apt -y install tor. Une fois l'installation complétée, le service sera normalement lancé automatiquement en arrière-plan. Vérifiez qu'il tourne bien avec la commande sudo systemctl status tor. Dans la réponse retournée devrait se trouver Active: active (exited). Appuyez sur Ctrl+C pour quitter cette fonction.

    Dans tous les cas vous pouvez utiliser les commandes suivantes dans le terminal pour lancer, arrêter, ou redémarrer Tor :
    sudo systemctl start tor
    sudo systemctl stop tor
    sudo systemctl restart tor

Lançons ensuite l'interface graphique de Bitcoin Core avec la commande bitcoin-qt. Puis, activons la fonctionnalité automatisée du logiciel pour diriger nos connexions via un proxy Tor : Paramètres > Réseau, et de là nous pouvons cocher Se connecter par un mandataire SOCKS5 (mandataire par défaut) ainsi que Utiliser un mandataire SOCKS5 séparé pour atteindre les pairs par les services oignons de Tor.

![option](assets/3.jpeg)

Bitcoin Core détecte automatiquement si Tor est installé et, si c'est le cas, créera par défaut des connexions sortantes (Outbound) vers d'autres nœuds utilisant aussi Tor, en plus des connexions vers des nœuds utilisant les réseaux IPv4/IPv6 (clearnet).

    💡 Pour changer la langue d'affichage au français, rendez vous dans l'onglet Affichage des Paramètres.

## Configuration avancée de Tor (optionnel)

Il est possible de configurer Bitcoin Core pour n'utiliser que le réseau Tor afin de se connecter avec des pairs, optimisant ainsi notre anonymité via notre nœud. Comme il n'existe pas de fonctionnalité à cet effet dans l'interface graphique, nous allons devoir créer manuellement un ficher de configuration. Allez dans Paramètres, puis Options.

![option 2](assets/4.jpeg)

Ici, cliquez sur Ouvrir le fichier de configuration. Une fois dans le fichier texte bitcoin.conf, ajoutez simplement une ligne onlynet=onion et sauvegardez le fichier. Vous devez redémarrer Bitcoin Core pour que cette commande prenne effet.

Nous allons ensuite configurer le service Tor pour que Bitcoin Core puisse recevoir des connexions entrantes via un proxy, permettant ainsi à nos pairs du réseau d'utiliser notre nœud pour télécharger des données de la blockchain sans pour autant compromettre la sécurité de notre machine.

Dans le terminal, entrez sudo nano /etc/tor/torrc pour accéder au fichier de configuration du service Tor. Dans ce fichier, cherchez la ligne #ControlPort 9051 et supprimez le # pour l'activer. Ajoutez maintenant deux nouvelles lignes au fichier : HiddenServiceDir /var/lib/tor/bitcoin-service/ et
HiddenServicePort 8333 127.0.0.1:8334. Pour sortir du fichier tout en le sauvegardant, appuyez sur Ctrl+X > Y > Enter. De retour dans le terminal, redémarrez Tor en entrant la commande sudo systemctl restart tor.

Avec cette configuration, Bitcoin Core pourra désormais établir des connexions entrantes et sortantes avec d'autres pairs du réseau uniquement sur le réseau Tor (Onion). Pour confirmer que c'est bien le cas, appuyez sur l'onglet Fenêtre, puis Pairs.

![Fenetre des noeuds](assets/5.jpeg)

## Ressources supplémentaires

Ultimement, n'utiliser que le réseau Tor (onlynet=onion) pourrait vous rendre vulnérable à une attaque Sybil. C'est pourquoi certains recommandent de préserver une configuration multi-réseau pour palier à ce type de risque. D'ailleurs, toutes les connexions IPv4/IPv6 seront dirigées par le proxy Tor une fois celui-ci configuré, tel qu'indiqué précédemment.

Alternativement, pour demeurer uniquement sur le réseau Tor et mitiger le risque d'attaque Sybil, vous pouvez ajouter l'adresse d'un autre nœud auquel vous faites confiance dans votre fichier bitcoin.conf en ajoutant la ligne addnode=adresse_de_confiance.onion. Il est possible d'ajouter cette ligne à plusieurs reprises si vous désirez vous connecter à plusieurs nœuds de confiance.

Pour consulter les logs de votre nœud Bitcoin en ce qui à trait plus spécifiquement à son intéraction avec Tor, ajoutez debug=tor à votre fichier bitcoin.conf. Vous aurez maintenant les informations pertinentes à Tor dans votre journal de débogage, lequel vous pouvez consulter dans la fenêtre Renseignements, avec le bouton Fichier journal de débogage. Il est également possible de consulter ces logs directement dans le terminal avec la commande bitcoind -debug=tor.

    💡 Quelques liens intéressants:
    Page wiki explicant Tor et sa relation avec Bitcoin
    Générateur de fichier configuration Bitcoin Core par Jameson Lopp
    Guide de configuration Tor par Jon Atack

Comme toujours, si vous avez des questions, n'hésitez pas à les partager à la communauté Agora256, nous apprenons ensemble, pour être meilleur demain que nous ne le sommes aujourd'hui!

** FIN du tutoriel de Agora256; lien original: https://agora256.com/configuration-tor-bitcoin-core/. merci a eux de nous offrir ceci **
