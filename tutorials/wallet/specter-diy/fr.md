---
name: Specter DIY
description: Guide d'installation pour Specter DIY
---

![cover](assets/cover.webp)


## Spectre-DIY


> Les cypherpunks écrivent du code. Nous savons que quelqu'un doit écrire un logiciel pour défendre la vie privée, et comme nous ne pouvons pas obtenir la vie privée si nous ne le faisons pas tous, nous allons l'écrire.

*Le manifeste d'un Cypherpunk - Eric Hughes - 9 mars 1993*


L'idée du projet est de construire un matériel wallet à partir de composants disponibles sur le marché.

Bien que nous ayons une carte d'extension qui met tout dans un format agréable et vous aide à éviter toute soudure, nous continuerons à soutenir et à maintenir la compatibilité avec les composants standard.


![image](assets/fr/01.webp)


Nous voulons aussi que le projet reste flexible et qu'il puisse fonctionner avec n'importe quel autre ensemble de composants avec un minimum de changements. Peut-être voulez-vous créer un wallet matériel sur une architecture différente (RISC-V ?), avec un modem audio comme canal de communication - vous devriez pouvoir le faire. Il devrait être facile d'ajouter ou de modifier des fonctionnalités de Specter et nous essayons d'abstraire les modules logiques autant que possible.


Les codes QR sont un moyen par défaut pour Specter de communiquer avec l'hôte. Les codes QR sont très pratiques et permettent à l'utilisateur de contrôler la transmission des données - chaque code QR a une capacité très limitée et la communication se fait de manière unidirectionnelle. De plus, il s'agit d'une communication aérienne - vous n'avez pas besoin de connecter le wallet à l'ordinateur à quelque moment que ce soit.


Pour le stockage des secrets, nous supportons le mode agnostique (wallet oublie tous les secrets lorsqu'il est éteint), le mode téméraire (stocke les secrets dans la mémoire flash du microcontrôleur de l'application) et l'intégration de secure element est à venir.


Nous nous concentrons principalement sur la configuration multi-signature avec d'autres portefeuilles matériels, mais wallet peut également fonctionner en tant que signataire unique. Nous essayons de le rendre compatible avec Bitcoin Core dans la mesure du possible - PSBT pour les transactions non signées, les descripteurs wallet pour l'importation/exportation de portefeuilles multi-signatures. Pour faciliter la communication avec Bitcoin Core, nous travaillons également sur [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - un petit serveur python flask qui communique avec votre nœud Bitcoin Core.


La plupart des microprogrammes sont écrits en MicroPython, ce qui facilite l'audit et la modification du code. Nous utilisons la bibliothèque [secp256k1](https://github.com/bitcoin-core/secp256k1) de Bitcoin Core pour les calculs de courbes elliptiques et la bibliothèque [LittlevGL](https://lvgl.io/) pour l'interface graphique.


## Clause de non-responsabilité


Le projet a considérablement évolué, au point que le niveau de sécurité de Specter-DIY est désormais comparable à celui des portefeuilles matériels commerciaux disponibles sur le marché. Nous avons mis en œuvre un chargeur de démarrage sécurisé qui vérifie les mises à jour du micrologiciel, de sorte que vous pouvez être sûr que seul le micrologiciel signé peut être téléchargé sur l'appareil après l'installation initiale. Toutefois, contrairement aux dispositifs de signature commerciaux, le chargeur de démarrage doit être installé manuellement par l'utilisateur et n'est pas configuré en usine par le vendeur de l'appareil. Il convient donc de redoubler d'attention lors de l'installation initiale du micrologiciel, de s'assurer que les signatures PGP ont été vérifiées et de télécharger le micrologiciel à partir d'un ordinateur sécurisé.


Si quelque chose ne fonctionne pas, ouvrez un problème ici ou posez une question dans notre [groupe Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Liste d'achats pour Specter-DIY


Nous décrivons ici ce qu'il faut acheter, et dans la partie suivante, nous expliquons comment l'assembler et nous donnons quelques informations sur la carte - cavaliers d'alimentation, ports USB, etc.


### Planche de découverte


La partie principale de l'appareil est la carte de développement :



- Carte de développement STM32F469I-DISCO (i.e. de [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) ou [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Câble Mini**USB
- Câble MicroUSB standard pour communiquer par USB


Facultatif mais recommandé :


- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) avec de longs connecteurs comme [ceux-ci](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) ou [ceux-ci](https://www.amazon.com/gp/product/B015KA0RRU/) pour connecter le scanner à la carte (4 connecteurs nécessaires).


Nous travaillons actuellement sur une carte d'extension qui comprend une fente pour carte à puce, un scanner de code QR, une batterie et un boîtier imprimé en 3D, mais elle n'inclut pas la partie principale - la carte de découverte que vous devez commander séparément. De cette manière, l'attaque de la chaîne d'approvisionnement n'est pas un problème puisque les composants critiques pour la sécurité sont achetés dans des magasins d'électronique au hasard.


Vous pouvez commencer à utiliser Specter même sans aucun composant supplémentaire, mais vous pourrez communiquer avec lui par USB ou par l'intermédiaire de l'emplacement de carte SD intégré. L'utilisation de Specter via USB signifie qu'il n'est pas relié à un réseau aérien, ce qui vous fait perdre une propriété de sécurité importante.


### Scanner QR


Pour le scanner de code QR, vous avez plusieurs options.


**Option 1. Recommandé.** Scanner raisonnablement bon de Waveshare (40$)


[Waveshare scanner](https://www.waveshare.com/barcode-scanner-module.htm) - Vous devrez trouver un moyen de le monter correctement, peut-être en utilisant une sorte de bouclier Arduino Prototype et du ruban adhésif.


Aucune soudure n'est nécessaire, mais si vous avez des compétences en soudure, vous pouvez rendre le wallet beaucoup plus beau ;)


**Option 2.** Très bon scanner de Mikroe mais assez cher (150$) :


[Barcode Click](https://www.mikroe.com/barcode-click) + [Adaptateur](https://www.mikroe.com/arduino-uno-click-shield)


**Option 3 : tout autre scanner QR


Vous pouvez trouver des scanners bon marché en Chine. Leur qualité est souvent médiocre, mais vous pouvez tenter votre chance. Peut-être même qu'une ESPcamera ferait l'affaire. Il suffit de connecter l'alimentation, l'UART (broches D0 et D1), et le déclencheur à D5.


**Option 4.** Pas de scanner.


Dans ce cas, vous ne pouvez utiliser Specter qu'avec une carte USB / SD.


A moins que vous ne construisiez votre propre module de communication qui utilise quelque chose d'autre au lieu des codes QR - audiomodem, bluetooth ou autre. Dès qu'il peut être déclenché et envoyer les données en série, vous pouvez faire ce que vous voulez.


### Composants optionnels


Si vous ajoutez un minuscule powerbank ou un chargeur/booster de batterie et d'alimentation, votre wallet devient complètement autonome ;)



## Assemblage de Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Connexion du lecteur de codes-barres Waveshare


Le micrologiciel wallet configurera le scanner pour vous lors de la première utilisation, de sorte qu'aucune préconfiguration manuelle n'est nécessaire.


Voici comment connecter le scanner à la carte :


![image](assets/fr/02.webp)


Pour plus de facilité, vous pouvez acheter un bouclier Arduino Protype et souder et monter le tout dessus (par exemple [celui-ci](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Gestion de l'énergie


Sur la partie supérieure de la carte se trouve un cavalier qui définit l'endroit où la carte sera alimentée. Vous pouvez changer la position du cavalier et sélectionner la source d'alimentation comme l'un des ports USB ou la broche VIN et y connecter une batterie externe (qui doit être de 5V).


### Enceinte pour le bricolage


Consultez le dossier [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Soyez créatifs !


Assemblez votre propre Specter-DIY et envoyez-nous les photos (faites une pull request ou contactez-nous).


Découvrez la [Galerie](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) avec les Spectres assemblés par la communauté !




## Installation du code compilé


Avec le chargeur de démarrage sécurisé, l'installation initiale du micrologiciel est légèrement différente. Les mises à jour sont plus faciles et ne nécessitent pas de connecter le matériel wallet à l'ordinateur.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashing du firmware initial


**Note** Si vous ne voulez pas utiliser les binaires des versions, consultez la [documentation du bootloader](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) qui explique comment compiler et configurer le bootloader pour qu'il utilise vos clés publiques au lieu des nôtres.



- Si vous mettez à jour des versions inférieures à `1.4.0` ou si vous téléchargez le firmware pour la première fois, utilisez le fichier `initial_firmware_<version>.bin` de la page [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Vérifier la signature du fichier `sha256.signed.txt` par rapport à [la clé PGP de Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Vérifier le hachage du fichier `initial_firmware_<version>.bin` par rapport au hachage stocké dans le fichier `sha256.signed.txt`
- Si vous effectuez une mise à jour à partir d'un bootloader vide ou si le message d'erreur du bootloader indique que le micrologiciel n'est pas valide, consultez la section suivante - Flashing du micrologiciel signé Specter.
- Assurez-vous que le cavalier d'alimentation de votre carte de découverte est en position STLK
- Connectez la carte Discovery à votre ordinateur via le câble **miniUSB** situé sur le dessus de la carte.
    - La carte doit apparaître sous la forme d'un disque amovible nommé `DIS_F469NI`.
- Copiez le fichier `initial_firmware_<version>.bin` à la racine du système de fichiers `DIS_F469NI`.
- Lorsque la carte a fini de flasher le firmware, elle se réinitialise et redémarre vers le bootloader. Le bootloader vérifie le micrologiciel et démarre le micrologiciel principal. Si vous voyez un message d'erreur indiquant qu'aucun micrologiciel n'a été trouvé, suivez les instructions de mise à jour et téléchargez le micrologiciel via la carte SD.
- Vous pouvez maintenant placer le cavalier d'alimentation là où vous le souhaitez et alimenter la carte à partir du powerbank ou de la batterie.


Le flashage du firmware initial par copier-coller du fichier `.bin` échoue parfois - souvent à cause du câble, ou si vous connectez l'appareil à travers un hub USB. Dans ce cas, vous pouvez essayer plusieurs fois (cela fonctionne normalement en 2 ou 3 tentatives).


Si cela échoue toujours, vous pouvez utiliser l'outil open-source [stlink](https://github.com/stlink-org/stlink/releases/latest). Installez-le et tapez dans votre terminal : `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Cela fonctionne généralement de manière beaucoup plus fiable.


### Mise à jour du micrologiciel



- Téléchargez le fichier `specter_upgrade_<version>.bin` depuis le site [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Copiez ce fichier binaire à la racine de la carte SD (formatée en FAT, 32 Go maximum)
 - Assurez-vous qu'un seul fichier `specter_upgrade***.bin` se trouve dans le répertoire racine
- Insérez la carte SD dans l'emplacement SD de la carte Discovery et mettez la carte sous tension
- Bootloader flashera le micrologiciel et vous informera lorsque ce sera fait.
- Redémarrez la carte - vous verrez l'interface Specter-DIY, qui vous proposera de sélectionner votre code PIN


Chaque fois qu'une nouvelle version est disponible, il suffit de télécharger le fichier `specter_upgrade_<version>.bin` à partir des versions, de le déposer sur la carte SD et de mettre à jour l'appareil comme dans l'étape précédente. Le Bootloader s'assurera que seul le firmware signé peut être chargé sur la carte.


### Comment connaître la version du micrologiciel


Allez dans le menu `Paramètres de l'appareil` - le numéro de version s'affichera sous le titre de l'écran.


## Utiliser le Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Sécurité de Specter-DIY


### Matériel


L'affichage est contrôlé par l'application MCU.


L'intégration des éléments sécurisés n'est pas encore achevée - pour l'instant, les secrets sont également stockés sur le MCU principal. Mais vous pouvez utiliser le wallet sans stocker le secret - vous devez entrer votre phrase de récupération à chaque fois. Pourquoi se souvenir d'un long passphrase si l'on peut se souvenir de l'ensemble de la mnémonique ?


L'appareil utilise une mémoire flash externe pour stocker certains fichiers (QSPI), mais tous les fichiers utilisateur sont signés par le wallet et vérifiés lors du chargement.


La fonctionnalité de balayage QR se trouve sur un microcontrôleur séparé, de sorte que tout le traitement de l'image se fait en dehors de l'unité MCU critique pour la sécurité. Pour l'instant, l'USB et la carte SD sont toujours gérées par le MCU principal, donc n'utilisez pas la carte SD et l'USB si vous voulez réduire la surface d'attaque.


### Protection par code PIN (authentification de l'utilisateur)


Lors du premier démarrage, un secret unique est généré sur le MCU principal. Ce secret vous permet de vérifier que l'appareil n'a pas été remplacé par un appareil malveillant - lorsque vous entrez le code PIN, vous voyez une liste de mots qui restent inchangés tant que le secret est présent.


Votre code PIN et ce secret unique sont utilisés pour generate une clé de décryptage pour vos clés Bitcoin (si vous les stockez). Ainsi, si l'attaquant est en mesure de contourner l'écran du code PIN, le décryptage échouera quand même.


Si vous avez verrouillé le firmware (TODO : ajouter le lien vers les instructions ici), le secret sera également verrouillé, de sorte que si l'attaquant introduit un firmware différent sur la carte, le secret sera effacé et vous pourrez le reconnaître lorsque vous commencerez à saisir le code PIN - la séquence des mots sera différente.


### Génération de la phrase de récupération


C'est l'une des parties les plus importantes de la wallet - pour sécuriser la clé generate. Pour ce faire, nous utilisons plusieurs sources d'entropie :



- TRNG du microcontrôleur. Propriétaire, certifié et probablement bon, mais nous ne lui faisons pas confiance
- Écran tactile. Chaque fois que vous touchez l'écran, nous mesurons la position et le moment où ce contact s'est produit (en tics de microcontrôleur à 180 MHz).
- Microphones intégrés - pas encore. La carte est équipée de deux microphones, de sorte que le matériel wallet peut vous écouter et mélanger ces données au pool d'entropie.


Toute cette entropie est hachée ensemble et convertie en votre phrase de récupération. L'entropie résultante est toujours meilleure que n'importe laquelle des sources individuelles.


### Logique de haut niveau - portefeuilles


Specter fonctionne comme un stockage de clés. Il contient des clés privées HD qui peuvent être impliquées dans des portefeuilles. Les portefeuilles sont définis par leurs descripteurs. Nous prenons également en charge les miniscripts.


Chaque wallet appartient à un réseau particulier. Cela signifie que si vous avez importé une wallet sur `testnet`, elle ne sera pas disponible sur `mainnet` ou `regtest` - vous devez basculer sur ce réseau et importer la wallet séparément.


### Vérification des transactions


Les règles suivantes s'appliquent aux transactions que wallet signera :



- si des entrées mixtes provenant de différents portefeuilles sont trouvées, l'utilisateur est averti ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- change outputs show the name of the wallet they are sent to
- pour utiliser un multisig ou un miniscript, vous devez d'abord importer le wallet en ajoutant le descripteur wallet (par QR, USB ou carte SD)


## Support des descripteurs


Tous les descripteurs Bitcoin normaux fonctionnent. A part cela, nous avons quelques extensions :


### Branches multiples dans les descripteurs


Pour économiser de l'espace dans les codes QR, nous autorisons l'ajout de descripteurs avec plusieurs branches en une seule fois. Si vous souhaitez utiliser `wpkh(xpub/0/*)` pour les adresses de réception et `wpkh(xpub/1/*)` pour les adresses de modification, vous pouvez les combiner en un seul descripteur : `wpkh(xpub/{0,1}/*)` - le wallet considérera le premier index de la partie `{}` comme la branche pour les adresses de réception et le second comme les adresses de modification.


Vous pouvez également spécifier plus de deux branches, et les index des branches peuvent être différents pour différents cosignataires. Ce descripteur est donc très étrange mais totalement valide :


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Ici, pour recevoir l'adresse numéro 17, le wallet utilisera le script de `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


La seule condition est que le nombre d'index dans tous les ensembles soit le même (3 dans le cas ci-dessus).


### Dérivations par défaut


Si le descripteur contient des clés publiques principales mais ne contient pas de dérivations génériques, la dérivation par défaut `/{0,1}/*` sera ajoutée à toutes les clés étendues dans le descripteur. Si au moins un des xpubs a une dérivation joker, le descripteur ne sera pas modifié.


Le descripteur `wpkh(xpub)` sera converti en `wpkh(xpub/{0,1}/*)`.


### Miniscript


Specter supporte les miniscripts, mais ne supporte pas la compilation de politiques en miniscripts (parce que c'est beaucoup trop cher). Nous effectuons quelques vérifications sur le miniscript, ainsi seuls les scripts `B` sont autorisés au niveau supérieur et tous les arguments dans les sous-miniscripts doivent avoir des propriétés conformes à la [spec](http://bitcoin.sipa.be/miniscript/).


Vous pouvez utiliser [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) pour generate un descripteur d'une politique et l'importer ensuite dans la wallet.


Par exemple, une politique "Je peux dépenser maintenant, ou dans 100 jours ma femme peut dépenser" peut être convertie en wallet de la manière suivante :


Policy : `ou(9@pk(xpubA),and(older(14400),pk(B)))` (ma clé est 9 fois plus probable)


Miniscript : `ou_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor : `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`)


Comme nous n'avons pas de dérivation de type joker, les dérivations par défaut de `/{0,1}/*` seront ajoutées aux xpubs.



---

Licence MIT


Copyright (c) 2019 cryptoadvance


---