---
name: Bitcoin Core (Linux)
description: Exécutez votre propre nœud avec Bitcoin core sous Linux
---

![cover](assets/cover.webp)


## Exécuter son propre nœud avec Bitcoin core


Introduction à Bitcoin et au concept de nœud, complétée par un guide d'installation complet sur Linux.


L'un des aspects les plus intéressants de Bitcoin est la possibilité d'exécuter soi-même le programme, et donc de participer à un niveau granulaire au réseau et à la vérification de la transaction publique Ledger.


Bitcoin, en tant que projet open-source, est disponible gratuitement et distribué publiquement depuis 2009. Près de 17 ans après sa création, Bitcoin est aujourd'hui un réseau monétaire numérique robuste et imparable, bénéficiant d'un puissant effet de réseau organique. Pour ses efforts et sa vision, Satoshi Nakamoto mérite notre gratitude. À propos, nous hébergeons le livre blanc Bitcoin ici sur Agora 256 (note : également sur l'université).


### Devenir sa propre banque


Gérer son propre nœud est devenu essentiel pour les adeptes de l'éthique Bitcoin. Sans demander la permission à personne, il est possible de télécharger le Blockchain depuis le début et de vérifier ainsi toutes les transactions de A à Z selon le protocole Bitcoin.


Le programme comprend également son propre Wallet. Ainsi, nous contrôlons les transactions que nous envoyons au reste du réseau, sans intermédiaire ni tiers. Vous êtes votre propre banque.


Le reste de cet article est donc un guide pour installer Bitcoin core - la version la plus utilisée du logiciel Bitcoin - spécifiquement sur les distributions Linux compatibles avec Debian telles qu'Ubuntu et Pop!OS. Suivez ce guide pour faire un pas de plus vers votre souveraineté individuelle.


## Guide d'installation du Bitcoin core pour Debian/Ubuntu


**Prérequis**


- Minimum 6GB de stockage de données (nœud pruned) - 1TB de stockage de données (Full node)
- Attendez-vous à ce que le téléchargement du bloc initial (IBD) prenne au moins 24 heures. Cette opération est obligatoire même pour un nœud pruned.
- Prévoir ~600GB de bande passante pour l'IBD, même pour un nœud pruned.


**Note:💡** les commandes suivantes sont prédéfinies pour Bitcoin core version 24.1.


### Téléchargement et vérification des fichiers



- [Télécharger](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, ainsi que les fichiers `SHA256SUMS` et `SHA256SUMS.asc` (vous devez évidemment télécharger la dernière version du logiciel).



- Ouvrez un terminal dans le répertoire où se trouvent les fichiers téléchargés. Exemple : `cd ~/Downloads/`.



- Vérifiez que la somme de contrôle du fichier de version est listée dans le fichier de somme de contrôle en utilisant la commande `sha256sum --ignore-missing --check SHA256SUMS`.



- La sortie de cette commande devrait inclure le nom du fichier de la version téléchargée suivi de `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installez git en utilisant la commande `sudo apt install git`. Ensuite, clonez le dépôt contenant les clés PGP des signataires de Bitcoin core en utilisant la commande `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importer les clés PGP de tous les signataires en utilisant la commande `gpg --import guix.sigs/builder-keys/*`



- Vérifiez que le fichier de checksum est signé avec les clés PGP des signataires en utilisant la commande `gpg --verify SHA256SUMS.asc`.



Chaque signature valide affichera une ligne commençant par : `gpg : Good signature` et une autre ligne se terminant par : `Empreinte de la clé primaire : 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (exemple de l'empreinte de la clé PGP de Pieter Wuille).


**Note💡:** il n'est pas nécessaire que toutes les clés de signature renvoient un "OK". En fait, une seule peut être nécessaire. Il appartient à l'utilisateur de déterminer son propre seuil de validation pour la vérification PGP.


Vous pouvez ignorer les avertissements :



- `Cette clé n'est pas certifiée par une signature de confiance!`



- rien n'indique que la signature appartient au propriétaire


### Installation de l'interface graphique Bitcoin core Interface



- Dans le terminal, toujours dans le répertoire où se trouve le fichier de la version Bitcoin core, utilisez la commande `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` pour extraire les fichiers contenus dans l'archive.



- Installez les fichiers extraits précédemment en utilisant la commande `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Installez les dépendances nécessaires en utilisant la commande `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Lancez _bitcoin-qt_ (Bitcoin core graphique Interface) en utilisant la commande `Bitcoin-qt`.



- Pour choisir un nœud pruned, cochez _Limit Blockchain storage_ et configurez la limite de données à stocker :


![welcome](assets/fr/02.webp)


### Conclusion de la partie 1 : Guide d'installation


Une fois la Bitcoin core installée, il est recommandé de la laisser fonctionner autant que possible pour contribuer au réseau Bitcoin en vérifiant les transactions et en transmettant les nouveaux blocs à d'autres pairs.


Toutefois, l'exécution et la synchronisation intermittentes de votre nœud, ne serait-ce que pour valider les transactions reçues et envoyées, restent une bonne pratique.


![Creation wallet](assets/fr/03.webp)


## Configuration de Tor pour un nœud Bitcoin core


**Note💡:** ce guide est conçu pour Bitcoin core 24.0.1 sur les distributions Linux compatibles Ubuntu/Debian.


### Installation et configuration de Tor pour Bitcoin core


Tout d'abord, nous devons installer le service Tor (The Onion Router), un réseau utilisé pour les communications anonymes, qui nous permettra d'anonymiser nos interactions avec le réseau Bitcoin. Pour une introduction aux outils de protection de la vie privée en ligne, dont Tor, reportez-vous à notre article sur ce sujet.


Pour installer Tor, ouvrez un terminal et entrez `sudo apt -y install tor`. Une fois l'installation terminée, le service sera normalement lancé automatiquement en arrière-plan. Vérifiez qu'il fonctionne correctement avec la commande `sudo systemctl status tor`. La réponse devrait être `Active : active (exited)`. Appuyez sur `Ctrl+C` pour quitter cette fonction.


**Dans tous les cas, vous pouvez utiliser les commandes suivantes dans le terminal pour démarrer, arrêter ou redémarrer Tor :


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Ensuite, lançons le Bitcoin core graphique Interface avec la commande `Bitcoin-qt`. Ensuite, activez la fonction automatique du logiciel pour router nos connexions à travers un proxy Tor : _Paramètres > Réseau_, et de là, cochez _Connecter à travers un proxy SOCKS5 (proxy par défaut)_ ainsi que _Utiliser un proxy SOCKS5 séparé pour atteindre des pairs via les services d'oignon Tor_.


![option](assets/fr/04.webp)


Bitcoin core détecte automatiquement si Tor est installé et, si c'est le cas, crée par défaut des connexions sortantes vers d'autres nœuds utilisant également Tor, en plus des connexions vers des nœuds utilisant des réseaux IPv4/IPv6 (clearnet).


**Note💡:** pour changer la langue d'affichage en français, allez dans l'onglet Affichage dans Paramètres.


### Configuration avancée de Tor (en option)


Il est possible de configurer le Bitcoin core pour qu'il n'utilise que le réseau Tor pour se connecter avec des pairs, optimisant ainsi l'anonymat de notre nœud. Comme il n'y a pas de fonctionnalité intégrée pour cela dans le Interface graphique, nous devrons créer manuellement un fichier de configuration. Allez dans Settings, puis dans Options.


![option 2](assets/fr/05.webp)


Ici, cliquez sur _Ouvrir le fichier de configuration_. Une fois dans le fichier texte `Bitcoin.conf`, ajoutez simplement la ligne `onlynet=onion` et sauvegardez le fichier. Vous devez redémarrer Bitcoin core pour que cette commande prenne effet.


Nous configurerons ensuite le service Tor pour que Bitcoin core puisse recevoir des connexions entrantes via un proxy, ce qui permettra à d'autres nœuds du réseau d'utiliser notre nœud pour télécharger les données de Blockchain sans compromettre la sécurité de notre machine.


Dans le terminal, entrez `sudo nano /etc/tor/torrc` pour accéder au fichier de configuration du service Tor. Dans ce fichier, cherchez la ligne `#ControlPort 9051` et supprimez le `#` pour l'activer. Maintenant, ajoutez deux nouvelles lignes au fichier :


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Pour quitter le fichier tout en le sauvegardant, appuyez sur `Ctrl+X > Y > Enter`. De retour dans le terminal, redémarrez Tor en entrant la commande `sudo systemctl restart tor`.


Avec cette configuration, Bitcoin core pourra établir des connexions entrantes et sortantes avec d'autres nœuds du réseau uniquement à travers le réseau Tor (Onion). Pour le confirmer, cliquez sur l'onglet _Window_, puis _Peers_.


![Nodes Window](assets/fr/06.webp)


### Ressources complémentaires


En fin de compte, utiliser uniquement le réseau Tor (`onlynet=onion`) pourrait vous rendre vulnérable à un Sybil Attack. C'est pourquoi certains recommandent de maintenir une configuration multi-réseaux pour atténuer ce type de risque. De plus, toutes les connexions IPv4/IPv6 seront routées à travers le proxy Tor une fois qu'il sera configuré, comme indiqué précédemment.


Alternativement, pour rester uniquement sur le réseau Tor et atténuer le risque d'une Sybil Attack, vous pouvez ajouter la Address d'un autre noeud de confiance à votre fichier `Bitcoin.conf` en ajoutant la ligne `addnode=adresse_de_confiance.onion`. Vous pouvez ajouter cette ligne plusieurs fois si vous voulez vous connecter à plusieurs nœuds de confiance.


Pour voir les journaux de votre noeud Bitcoin spécifiquement liés à son interaction avec Tor, ajoutez `debug=tor` à votre fichier `Bitcoin.conf`. Vous aurez alors des informations pertinentes sur Tor dans votre journal de débogage, que vous pouvez visualiser dans la fenêtre _Information_ avec le bouton _Fichier de débogage_. Il est aussi possible de voir ces logs directement dans le terminal avec la commande `bitcoind -debug=tor`.


**Tip💡:** voici quelques liens intéressants :


- [Page wiki expliquant Tor et sa relation avec Bitcoin] (https://en.Bitcoin.it/wiki/Tor)
- [Générateur de fichier de configuration Bitcoin core par Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Guide de configuration de Tor par Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Comme toujours, si vous avez des questions, n'hésitez pas à les partager avec la communauté Agora256. Nous apprenons ensemble pour être meilleurs demain qu'aujourd'hui !