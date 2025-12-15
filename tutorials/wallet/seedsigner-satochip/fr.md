---
name: Satochip x SeedSigner
description: Comment utiliser un Satochip avec son SeedSigner ?
---

![cover](assets/cover.webp)

*Merci à [Crypto Guide](https://www.youtube.com/@CryptoGuide/) pour son fork du firmware SeedSigner permettant la prise en charge des smartcards, que nous allons utiliser dans ce tutoriel.*

---

Le Satochip est un hardware wallet au format carte à puce, doté d’un élément sécurisé certifié EAL6+, l’un des standards de sécurité les plus élevés. Il est conçu et produit par l’entreprise belge du même nom : Satochip.

Proposée à un prix d’environ 25 €, le Satochip se distingue de la concurrence par son excellent rapport qualité-prix. Grâce à sa puce sécurisée, elle offre une résistance face aux attaques physiques. De plus, le code source de son applet est entièrement open-source, sous licence *AGPLv3*.

En revanche, son format impose certaines limites fonctionnelles. Le principal inconvénient du Satochip réside dans l’absence d’écran intégré : l’utilisateur doit alors signer ses transactions à l’aveugle, en se fiant uniquement à l’affichage de son ordinateur.

Pour pallier cette faiblesse, une configuration particulièrement intéressante consiste à l’utiliser conjointement avec un SeedSigner. Dans ce setup, la communication ne s’effectue plus directement entre l’ordinateur et le Satochip, mais passe par des échanges de QR codes entre l’ordinateur et le SeedSigner. Le SeedSigner agit alors comme un écran de confiance : il affiche les informations à signer, tandis que la signature elle-même est réalisée par le Satochip. Contrairement à une utilisation classique du SeedSigner (ou même à son utilisation combinée avec un Seedkeeper), la seed n’est jamais chargée dans le SeedSigner. Celui-ci devient donc l'écran du Satochip, et élimine les risques liés au fait de signer à l’aveugle.

Si l’on prend le problème dans l'autre sens, l’utilisation du SeedSigner avec un Satochip comble une lacune majeure du SeedSigner : la possibilité de stocker et d'utiliser la seed au sein d’un élément sécurisé.

Selon moi, cette configuration présente plusieurs avantages par rapport aux hardware wallets classiques :
- Elle est plutôt économique : le Satochip coûte environ 25 €, et, puisque l’applet est open-source, il est possible de l’installer soi-même sur une smartcard vierge. Il faut ensuite ajouter le coût des composants du SeedSigner et de l’extension pour lire les smartcards : en fonction d'où vous achetez ce matériel, le total devrait se situer entre 70 € et 100 €.
- Tous les logiciels impliqués dans le setup sont open-source : le firmware du SeedSigner et l’applet du Satochip.
- Vous bénéficiez d’un élément sécurisé certifié.
- La configuration peut être réalisée intégralement en DIY, sans recours à du matériel explicitement destiné à une utilisation de Bitcoin, ce qui peut permettre une forme de déni plausible et de résistance à certaines menaces externes (y compris, selon le pays, des pressions étatiques). Cela constitue aussi une solution intéressante si l’accès aux hardware wallets commerciaux est restreint ou impossible dans votre région.


## 1. Matériel nécessaire

Pour réaliser ce setup, vous aurez besoin des éléments suivants :  
- Le matériel habituel nécessaire à un SeedSigner classique :
	- un Raspberry Pi Zero avec broches GPIO,
	- un écran Waveshare 1.3",
	- une caméra compatible,
	- une carte microSD.

![Image](assets/fr/01.webp)

- Le kit d’extension pour SeedSigner, disponible [sur la boutique officielle de Satochip](https://satochip.io/product/seedsigner-extension-kit/), qui permet de lire et d’écrire sur une smartcard directement depuis votre SeedSigner. Une autre option consiste à utiliser [un lecteur de carte à puce externe](https://satochip.io/product/chip-card-reader/), pouvant être connecté par câble à un port Micro-USB du Raspberry Pi. Toutefois, je n'ai pas testé cette solution de mon côté ;
- [Un Satochip](https://satochip.io/product/satochip/), ou à défaut une [smartcard vierge](https://satochip.io/product/card-for-diy-project/) sur laquelle vous installerez l’applet du Satochip (le kit d’extension vendu par Satochip inclut déjà une smartcard vierge). Le kit d'extension proposé par Satochip prend également en charge le format [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Vous pouvez donc opter pour ce format si vous le préférez.

![Image](assets/fr/02.webp)

Pour plus de détails sur le matériel requis pour assembler un SeedSigner, je vous invite à consulter la partie 1 de cet autre tutoriel :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Installer le firmware

Pour utiliser votre SeedSigner avec un Satochip, il est nécessaire d’installer un firmware alternatif, différent de celui du SeedSigner original, afin d’avoir la prise en charge de la lecture des cartes à puce. Pour cela, [je vous recommande d’utiliser le fork de "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Téléchargez [la dernière version de l’image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) correspondant au modèle de Raspberry Pi que vous utilisez.

![Image](assets/fr/03.webp)

Si vous ne l'avez pas encore, téléchargez le logiciel [Balena Etcher](https://etcher.balena.io/), puis procédez comme suit :
- Insérez la carte microSD dans votre ordinateur ;
- Lancez Etcher ;
- Sélectionnez le fichier `.zip` que vous venez de télécharger ;
- Choisissez la carte microSD comme cible ;
- Cliquez sur `Flash!`.

![Image](assets/fr/04.webp)

Patientez jusqu’à la fin du processus : votre microSD est désormais prête à l’emploi. Vous pouvez à présent passer à l’assemblage de votre appareil.

Pour plus de détails concernant l’installation du firmware et la vérification du logiciel (étape que je vous recommande vivement de faire), consultez le tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Assembler le lecteur de smartcard

Commencez par installer la caméra sur le Raspberry Pi Zero en l’insérant délicatement dans la broche prévue à cet effet, puis verrouillez-la avec la languette noire. Placez ensuite le Pi au fond du boîtier en veillant à bien aligner les ports avec les ouvertures correspondantes.

![Image](assets/fr/05.webp)

Fixez ensuite le lecteur de carte à puce sur les broches GPIO du Raspberry Pi Zero.

![Image](assets/fr/06.webp)

Glissez le cache en plastique sur le lecteur de carte à puce jusqu’à ce qu’il soit correctement positionné.

![Image](assets/fr/07.webp)

Ajoutez ensuite l’écran sur les broches GPIO de l’extension.

![Image](assets/fr/08.webp)

Insérez enfin la carte microSD contenant le firmware dans le port latéral du Raspberry Pi Zero.

![Image](assets/fr/09.webp)

Vous pouvez désormais brancher votre SeedSigner soit via le port Micro-USB du Raspberry Pi Zero, soit via le port USB-C de l’extension. Les deux options fonctionnent. Attendez quelques secondes le temps du démarrage, puis vous devriez voir apparaître l’écran d’accueil.

![Image](assets/fr/10.webp)

Pour plus de détails sur le paramétrage initial de votre SeedSigner, je vous recommande de consulter la partie 4 du tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flasher une smartcard avec l’applet Satochip (optionnel)

Si vous possédez déjà un Satochip, vous pouvez passer cette étape et aller directement à l’étape 4. Dans cette section, nous allons voir comment installer l’applet du Satochip sur une smartcard vierge (méthode DIY). L'applet, c'est simplement un petit programme exécuté sur la carte à puce qui va nous permettre de gérer des fonctions spécifiques.

Pour commencer, ouvrez le menu `Tools > Smartcard Tools` sur votre SeedSigner.

![Image](assets/fr/11.webp)

Sélectionnez ensuite `DIY Tools > Install Applet`.

![Image](assets/fr/12.webp)

Insérez votre smartcard dans le lecteur du SeedSigner, puce orientée vers le bas, puis choisissez l’applet `Satochip`.

![Image](assets/fr/13.webp)

Patientez pendant l’installation : le processus peut durer quelques dizaines de secondes.

![Image](assets/fr/14.webp)

Une fois l’applet installée avec succès, vous pouvez passer à l’étape 4.

![Image](assets/fr/15.webp)


## 5. Création et sauvegarde de la seed

### 5.1. Générer la seed

À présent que tout votre matériel est prêt et que les logiciels fonctionnent correctement, vous pouvez procéder à la création de votre portefeuille Bitcoin. Pour cela, branchez votre SeedSigner, puis générez votre seed comme avec un SeedSigner classique, soit par un lancer de dés, soit en prenant une photo :
- Accédez au menu `Tools > Camera / Dice Rolls` ;
- Suivez ensuite le processus de génération de l’entropie selon la méthode choisie ;
- Sauvegardez enfin la seed sur un support physique et vérifiez soigneusement cette sauvegarde.

![Image](assets/fr/16.webp)

Si vous souhaitez consulter le détail de cette procédure, je vous invite à suivre la partie 5 de ce tutoriel :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Sauvegarder la seed sur un Seedkeeper

Une fois la seed générée, c’est le seul moment où elle réside dans la mémoire vive du SeedSigner. Dans mon cas, je souhaite la sauvegarder sur un [Seedkeeper](https://satochip.io/product/seedkeeper/), un autre produit de Satochip conçu pour stocker des secrets. J’utiliserai ce dispositif comme solution de dernier recours, en cas de perte de mon Satochip.

La stratégie de sauvegarde choisie ici dépend de vos préférences, mais il est impératif de disposer d’au moins une copie de votre phrase mnémonique, que ce soit sur un support physique (papier ou métal) ou, comme ici, dans un Seedkeeper. Vous pouvez également multiplier les sauvegardes selon vos besoins. Pour plus d'informations sur les stratégies de sauvegarde de portefeuille, je vous suggère de lire ce tutoriel :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pour sauvegarder votre seed sur un Seedkeeper, rendez-vous directement dans le menu `Backup Seed`.

![Image](assets/fr/17.webp)

Insérez ensuite votre Seedkeeper dans le lecteur de carte à puce, puis sélectionnez `To SeedKeeper`.

![Image](assets/fr/18.webp)

Entrez votre code PIN pour le déverrouiller.

![Image](assets/fr/19.webp)

Choisissez un `Label` afin d’identifier facilement vos différents secrets enregistrés sur le Seedkeeper. Vous pouvez, par exemple, conserver simplement l’empreinte du portefeuille ou indiquer explicitement `Seed`. Le choix dépend de votre préférence et de vos risques.

![Image](assets/fr/20.webp)

Si votre stratégie de sauvegarde repose uniquement sur ce Seedkeeper, je vous recommande vivement d’effectuer un test de récupération à vide dès maintenant, puis de comparer les empreintes pour vérifier que la sauvegarde est bien fonctionnelle.

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Concernant le choix du code PIN du Seedkeeper, il doit être aussi long et aléatoire que possible, afin de prévenir toute tentative de brute force en cas de compromission physique de la carte. Veillez également à conserver une copie de secours de ce code PIN, stockée à un endroit distinct du Seedkeeper. Sans ce code PIN, il vous sera impossible d’accéder à la phrase mnémonique stockée dans le Seedkeeper, et vos bitcoins seraient alors définitivement perdus.

### 5.3. Sauvegarder la seed sur le Satochip

Maintenant que votre portefeuille a été généré, sauvegardé et vérifié, nous allons le transférer sur le Satochip. Pour cela, veillez à ce que la seed soit bien chargée dans la mémoire vive du SeedSigner. Rendez-vous ensuite dans le menu `Tools > Smartcard Tools > Satochip Functions`.

![Image](assets/fr/21.webp)

Insérez votre Satochip dans le lecteur de carte à puce, puis sélectionnez `Initialise with Seed`.

![Image](assets/fr/22.webp)

Le dispositif vous demande d’indiquer le code PIN du Satochip ; comme la carte est neuve et non initialisée, aucun PIN n’existe encore. Saisissez donc un code quelconque pour passer cette étape (elle n’est pas bloquante).

![Image](assets/fr/23.webp)

Le SeedSigner détecte que votre Satochip n’a pas été initialisé. Cliquez sur `I Understand` pour confirmer.

![Image](assets/fr/24.webp)

Vous pourrez alors définir le code PIN du Satochip, entre 4 et 16 caractères. Pour renforcer la sécurité de votre portefeuille, privilégiez un code long et aléatoire : c’est la seule protection contre les accès physiques à votre phrase mnémonique.

Pensez à sauvegarder ce code PIN dès sa création, soit dans un gestionnaire de mots de passe sécurisé, soit sur un support physique, selon votre stratégie personnelle. Dans ce dernier cas, veillez à ne jamais stocker le support contenant le PIN au même endroit que votre Satochip, sans quoi la protection deviendrait inutile. Il est important de disposer d’une copie de secours : **sans ce code PIN, vous ne pourrez plus accéder à votre seed, et vos bitcoins seraient définitivement perdus**.

![Image](assets/fr/25.webp)

Le SeedSigner vous demande ensuite quelle seed importer dans le Satochip. Sélectionnez celle dont l’empreinte correspond au portefeuille que vous venez tout juste de créer.

![Image](assets/fr/26.webp)

Votre seed est désormais importée dans le Satochip.

![Image](assets/fr/27.webp)

Vous pouvez à présent éteindre votre SeedSigner.

Si vous souhaitez utiliser une passphrase BIP39 pour renforcer la sécurité de votre portefeuille, vous pouvez consulter la partie 6 de ce tutoriel :

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Importer le wallet dans Sparrow

Maintenant que votre portefeuille est fonctionnel, nous allons importer ses informations publiques (le "*keystore*") dans Sparrow Wallet ou dans un autre logiciel de gestion de portefeuille. Ce logiciel servira à créer, diffuser et suivre vos transactions. En revanche, il ne pourra pas les signer, car seules le Satochip (et vos éventuelles sauvegardes) détiennent les clés privées nécessaires à cette opération.

### 6.1 Préparation du SeedSigner et du Satochip

Insérez la carte microSD contenant le système d’exploitation, puis allumez votre SeedSigner. Pour l’instant, celui-ci ne peut rien faire, car il ne connaît pas encore votre seed. Il faut donc commencer par insérer le Satochip dans le lecteur de carte à puce, puisque c’est lui qui détient cette seed.

Depuis l’écran d’accueil, accédez au menu `Tools > Smartcard Tools > Satochip Functions`.

![Image](assets/fr/28.webp)

Cliquez ensuite sur `Export Xpub`.

![Image](assets/fr/29.webp)

Choisissez le type de portefeuille. Dans notre cas, il s’agit d’un portefeuille simple : sélectionnez donc `Single Sig`.

![Image](assets/fr/30.webp)

Vient ensuite le choix du standard de script. Choisissez le plus récent : `Native SegWit`.

![Image](assets/fr/31.webp)

Enfin, sélectionnez le `Coordinator`, c’est-à-dire le logiciel de gestion de portefeuille que vous souhaitez utiliser. Ici, nous utiliserons Sparrow Wallet.

![Image](assets/fr/32.webp)

Un message d’avertissement s’affiche : c’est tout à fait normal. La clé publique étendue (`xpub`) permet de visualiser l’ensemble des adresses dérivées de votre seed (sur le premier compte). Elle ne donne toutefois aucun accès à vos fonds : sa divulgation compromettrait votre vie privée, mais pas la sécurité de vos bitcoins. En d’autres termes, elle permet d’observer vos soldes, mais pas de les dépenser.

Cliquez sur `I Understand`.

![Image](assets/fr/33.webp)

Saisissez ensuite le code PIN de votre Satochip pour le déverrouiller. Il s’agit du code que vous aviez défini et sauvegardé à l’étape 5.

![Image](assets/fr/34.webp)

Cliquez enfin sur `Export Xpub` si les informations affichées vous conviennent.

![Image](assets/fr/35.webp)

Le SeedSigner génère alors votre xpub sous la forme d’un QR code dynamique, contenant toutes les données nécessaires à la gestion de votre portefeuille dans Sparrow Wallet. Vous pouvez ajuster la luminosité de l’écran à l’aide du joystick afin de faciliter le scan du QR code.

### 6.2 Importer un nouveau portefeuille dans Sparrow Wallet

Assurez-vous que le logiciel Sparrow Wallet est installé sur votre ordinateur. Si vous ne savez pas comment le télécharger, vérifier son authenticité et l’installer correctement, consultez notre tutoriel complet à ce sujet :

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Sur votre ordinateur, ouvrez Sparrow Wallet, puis dans la barre de menu, cliquez sur `File → Import Wallet`.

![Image](assets/fr/36.webp)

Faites défiler la liste jusqu’à l’option `SeedSigner`, puis sélectionnez `Scan...`. Votre webcam s’activera : scannez alors le QR code dynamique affiché sur l’écran de votre SeedSigner.

![Image](assets/fr/37.webp)

Attribuez un nom à votre portefeuille, puis cliquez sur `Create Wallet`. Sparrow vous demandera ensuite de définir un mot de passe pour verrouiller l’accès local à ce portefeuille. Choisissez un mot de passe fort : il protège vos données dans Sparrow (clés publiques, adresses, labels et historique des transactions). Ce mot de passe n’est toutefois pas nécessaire pour restaurer le portefeuille dans le futur : seule votre phrase mnémonique (et éventuellement votre passphrase) le sera.

Je vous recommande de sauvegarder ce mot de passe dans un gestionnaire de mots de passe, afin d’éviter de le perdre.

![Image](assets/fr/38.webp)

Votre keystore a été importé avec succès.

![Image](assets/fr/39.webp)

Vérifiez maintenant que la `Master fingerprint` affichée dans Sparrow Wallet correspond bien à celle relevée précédemment sur votre SeedSigner.

Le SeedSigner vous demandera ensuite de scanner une adresse de réception aléatoire depuis votre portefeuille Sparrow afin de confirmer la validité de l’importation.

![Image](assets/fr/40.webp)

Votre Satochip (via le SeedSigner) et Sparrow Wallet sont désormais connectés de manière sécurisée. Sparrow sert d’interface de gestion complète, tandis que le Satochip demeure le seul appareil capable de signer vos transactions. Vous êtes à présent prêt à recevoir et à envoyer des bitcoins dans une configuration totalement air-gapped.

![Image](assets/fr/41.webp)

## 7. Recevoir et envoyer des bitcoins

Votre Satochip et Sparrow Wallet sont désormais configurés pour fonctionner ensemble. Dans cette section, nous allons détailler pas à pas comment recevoir puis envoyer des bitcoins dans ce mode d'utilisation.

### 7.1 Recevoir des bitcoins

#### 7.1.1 Génération d’une adresse de réception

Sur votre ordinateur, ouvrez Sparrow Wallet et déverrouillez votre portefeuille `Satochip-SeedSigner` à l’aide de votre mot de passe. Vérifiez que le logiciel est bien connecté à un serveur (indicateur en bas à droite). Puis, dans la barre latérale, cliquez sur `Receive`.

![Image](assets/fr/42.webp)

Une nouvelle adresse Bitcoin apparaît. Vous y trouverez :
* L’adresse au format texte (commençant par `bc1q…` si vous utilisez P2WPKH, comme dans cet exemple) ;
* Le QR code associé ;
* Un champ `Label`, utile pour la traçabilité de vos transactions.

Je vous recommande fortement d’ajouter un label à chaque réception de bitcoins dans votre portefeuille. Cela vous aidera à identifier facilement la provenance de chaque UTXO et à mieux gérer votre confidentialité. Pour aller plus loin sur ce sujet important, consultez la formation dédiée sur Plan ₿ Academy :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Pour ajouter un label, saisissez simplement un nom dans le champ `Label`, puis validez.

Par exemple :

```txt
Label : Sale of the Raspberry Pi Zero
```

Votre adresse est désormais associée à ce label dans toutes les sections de Sparrow.

![Image](assets/fr/43.webp)

#### 7.1.2 Vérification de l’adresse sur le SeedSigner

Avant de communiquer votre adresse de réception au payeur, il est important de vérifier qu’elle appartient bien à votre seed. Cette étape garantit que votre Satochip pourra ensuite signer les transactions associées à cette adresse. Elle prévient également les attaques potentielles où Sparrow afficherait une adresse frauduleuse. Gardez à l’esprit que Sparrow s’exécute sur un environnement non sécurisé (votre ordinateur), dont la surface d’attaque est bien plus importante que celle de votre Satochip, qui est totalement isolé. C’est pourquoi vous ne devez jamais faire confiance aveuglément aux adresses affichées dans Sparrow avant de les vérifier sur votre hardware wallet.

Dans Sparrow, cliquez sur le QR code de l’adresse pour l’agrandir : il s’affichera alors en plein écran.

![Image](assets/fr/44.webp)

Sur votre SeedSigner, insérez le Satochip dans le lecteur, puis depuis le menu principal, sélectionnez `Scan`. Scannez le QR code affiché sur votre ordinateur, puis choisissez `Use Satochip card`.

![Image](assets/fr/45.webp)

Confirmez ensuite le type de script utilisé (ici, `Native SegWit`), saisissez le code PIN du Satochip pour le déverrouiller, puis validez les informations relatives à la `xpub`.

![Image](assets/fr/46.webp)

Si l’adresse scannée correspond bien à celle dérivée de votre seed, le SeedSigner affichera le message : `Address Verified`.

![Image](assets/fr/47.webp)

Vous pouvez alors être certain que l’adresse appartient bien à votre portefeuille.

#### 7.1.3 Réception des fonds

Vous pouvez désormais transmettre cette adresse sous forme de texte ou via son QR code à la personne ou au service qui doit vous envoyer des sats. Une fois la transaction diffusée sur le réseau, elle s’affichera dans l’onglet `Transactions` de Sparrow Wallet.

![Image](assets/fr/48.webp)

### 7.2 Envoyer des bitcoins

L’envoi de bitcoins avec la configuration Satochip-SeedSigner s’effectue en 3 étapes :
- La création de la transaction dans Sparrow ;
- La signature de cette transaction sur le Satochip, via le SeedSigner ;
- Enfin, la diffusion de la transaction sur le réseau depuis Sparrow.

Tous les échanges entre les deux appareils se déroulent exclusivement par le biais de QR codes.

#### 7.2.1 Créer la transaction dans Sparrow

Dans Sparrow Wallet, vous pouvez créer une transaction en cliquant sur l’onglet `Send` dans la barre latérale gauche. Cependant, je préfère utiliser l’onglet `UTXOs`, qui permet de pratiquer le *Coin Control*. Cette méthode offre un contrôle précis sur les UTXOs dépensés, afin de limiter les informations révélées lors de vos transactions.

Dans l’onglet `UTXOs`, sélectionnez les pièces que vous souhaitez dépenser, puis cliquez sur `Send Selected`.

![Image](assets/fr/49.webp)

Remplissez ensuite les champs de la transaction :
- Dans `Pay to`, collez l’adresse du destinataire ou scannez son QR code à l’aide de l’icône d’appareil photo ;
- Dans `Label`, ajoutez une étiquette pour tracer cette dépense ;
- Dans `Amount`, indiquez le montant à envoyer ;
- Choisissez enfin le taux de frais selon les conditions actuelles du réseau (vous pouvez consulter les estimations sur [mempool.space](https://mempool.space/)).

Une fois tous les champs complétés, relisez attentivement les informations, puis cliquez sur `Create Transaction >>`.

![Image](assets/fr/50.webp)

Vérifiez une dernière fois les détails de la transaction pour vous assurer de leur exactitude, puis cliquez sur `Finalize Transaction for Signing`.

![Image](assets/fr/51.webp)

La transaction est désormais prête, mais elle n’a pas encore été signée. Pour afficher la [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) sous forme de QR code, cliquez sur `Show QR`.

![Image](assets/fr/52.webp)

#### 7.2.2 Signer la transaction avec le Satochip

Allumez votre SeedSigner et insérez votre Satochip comme d'habitude. Depuis l’écran d’accueil, sélectionnez `Scan`, puis scannez le QR code affiché sur Sparrow.

![Image](assets/fr/53.webp)

Choisissez l’option `Use Satochip card`.

![Image](assets/fr/54.webp)

Saisissez votre code PIN pour déverrouiller la smartcard.

![Image](assets/fr/55.webp)

Le SeedSigner détecte qu’il s’agit d’une PSBT et affiche un résumé de la transaction :
   * Le montant envoyé,
   * Les adresses de destination,
   * Les frais de transaction associés.

Cliquez sur `Review Details` et examinez minutieusement toutes les informations directement sur l’écran du SeedSigner. Les points les plus importants à vérifier sont les montants envoyés, les adresses de destination et le montant des frais de transaction.

![Image](assets/fr/56.webp)

Si tout est conforme, sélectionnez `Approve PSBT` pour signer la transaction à l’aide du Satochip.

![Image](assets/fr/57.webp)

Une fois la signature terminée, le SeedSigner génère un nouveau QR code contenant la transaction signée, prêt à être scanné par Sparrow.

#### 7.2.3 Diffuser la transaction depuis Sparrow

La transaction étant désormais signée et valide, il reste à la diffuser sur le réseau Bitcoin afin qu’un mineur puisse l’inclure dans un bloc. Dans Sparrow, cliquez sur `Scan QR`.

![Image](assets/fr/58.webp)

Présentez à la webcam le QR code affiché sur votre SeedSigner (celui contenant la transaction signée). Sparrow affichera alors l’ensemble des détails de la transaction. Vérifiez une dernière fois l’exactitude de toutes les informations, puis cliquez sur `Broadcast Transaction` pour la diffuser sur le réseau Bitcoin.

![Image](assets/fr/59.webp)

Votre transaction est maintenant transmise au réseau. Vous pouvez suivre ses confirmations dans l’onglet `Transactions` de Sparrow Wallet.

![Image](assets/fr/60.webp)

## 8. Récupérer son portefeuille

Comme nous l’avons vu dans les sections précédentes, selon votre stratégie de sécurisation, il existe plusieurs manières de sauvegarder votre phrase de récupération en complément de votre Satochip :
- En utilisant un *SeedQR* classique avec le SeedSigner ;
- En notant la phrase mnémonique sur un support physique ;
- Ou encore en la stockant sur un Seedkeeper, comme expliqué dans la partie 5.2.

Dans tous les cas, 2 situations principales peuvent se présenter et nécessitent une intervention de votre part : la perte du Satochip ou la perte du SeedSigner. Examinons ensemble comment réagir dans chacun de ces scénarios.

### 8.1. Récupérer son portefeuille avec le Satochip

Si vous avez toujours votre Satochip mais que votre SeedSigner est cassé ou perdu, la situation est assez simple à gérer, puisque votre portefeuille est toujours présent dans le Satochip.

La meilleure option consiste à recommander les composants nécessaires et reconstruire un nouveau SeedSigner à partir de zéro. Comme il s’agit d’un appareil "*stateless*", peu importe que vous utilisiez le même ou un autre SeedSigner : dès lors que vous pouvez y insérer votre Satochip, tout fonctionnera normalement.

Si vous ne souhaitez pas en reconstruire un, vous pouvez également utiliser votre Satochip de manière classique, c’est-à-dire directement depuis votre ordinateur, sans passer par le SeedSigner. Cette méthode fonctionne parfaitement, mais elle réduit considérablement la sécurité de votre portefeuille Bitcoin : vous perdez l’isolation "*air-gapped*" et devez désormais signer à l’aveugle, puisque le SeedSigner jouait le rôle d’écran de confiance. Cela peut néanmoins constituer une solution temporaire en cas d’urgence ou d’impossibilité de reconstruire un SeedSigner.

Pour procéder ainsi, munissez-vous d’un lecteur de carte à puce ou NFC en USB. Ouvrez ensuite dans Sparrow le portefeuille que vous souhaitez restaurer, puis rendez-vous dans l’onglet `Settings` et cliquez sur `Replace`.

![Image](assets/fr/61.webp)

Insérez votre Satochip dans le lecteur de carte à puce connecté à l’ordinateur, puis cliquez sur `Import` à côté de `Satochip`.

![Image](assets/fr/62.webp)

Saisissez enfin le code PIN de votre smartcard pour la déverrouiller. Vous pourrez alors accéder à votre portefeuille, créer des transactions et les signer directement à l’aide du Satochip branché.

### 8.2. Récupérer son portefeuille avec le SeedSigner

L’autre cas de figure, plus délicat à gérer, est celui où vous perdez l’accès à votre Satochip contenant la seed : qu’il soit cassé, perdu, volé, ou que vous ayez oublié son code PIN. Si votre Satochip a été volé ou égaré, il est fortement recommandé, une fois l’accès à vos fonds rétabli, de transférer immédiatement vos bitcoins vers un tout nouveau portefeuille, généré avec une seed différente. Cela garantit qu’un éventuel attaquant ne puisse jamais accéder à vos sats.

Pour retrouver l’accès à votre portefeuille et déplacer vos fonds, il vous suffit de charger votre seed dans le SeedSigner. Selon le support de sauvegarde que vous avez utilisé, plusieurs options s’offrent à vous :

- Entrer manuellement votre phrase mnémonique en vous rendant dans le menu `Seeds > Enter 12-word seed`.

![Image](assets/fr/63.webp)

- Scanner votre *SeedQR* en cliquant sur le bouton `Scan` depuis la page d’accueil.

![Image](assets/fr/64.webp)

- Ou bien charger votre seed depuis un Seedkeeper, via le menu `Seeds > From SeedKeeper` (c’est la méthode que j’utilise dans ce tutoriel). Il vous faudra simplement saisir le code PIN du Seedkeeper et sélectionner le secret à utiliser comme seed sur le SeedSigner.

![Image](assets/fr/65.webp)

Une fois la seed chargée dans le SeedSigner, quelle que soit la méthode, vous pourrez signer une ou plusieurs transactions de balayage afin de déplacer vos bitcoins vers un nouveau portefeuille non compromis. Pour savoir comment effectuer cette opération, consultez la partie 7.2 du tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Vous savez désormais comment utiliser le Satochip pour gérer votre portefeuille Bitcoin de manière sécurisée en combinaison avec le SeedSigner.

Si ce setup vous a convaincu, n’hésitez pas à soutenir les projets qui le rendent possible :  
- En achetant votre matériel directement [sur le site de Satochip](https://satochip.io/shop/) ;
- En effectuant [un don au projet SeedSigner](https://seedsigner.com/donate/) ;
- En vous abonnant à [la chaîne YouTube de Crypto Guide](https://www.youtube.com/@CryptoGuide/), tenue par la personne qui maintient le dépôt GitHub hébergeant le firmware modifié que nous avons utilisé dans ce tutoriel.
