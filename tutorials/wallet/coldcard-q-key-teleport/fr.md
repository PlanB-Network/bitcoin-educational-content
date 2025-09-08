---
name: COLDCARD Q - Key Teleport
description: Qu'est-ce que la fonctionnalité Key Teleport et comment l'utiliser ?
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)


![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)

Qu'est-ce que la fonctionnalité **Key Teleport** proposée par Coinkite grâce à son appareil flagship ColdCardQ ?

**Key Teleport** permet de transférer de manière sécurisée des données confidentielles entre 2 ColdCardQ. Le canal de transmission n'a même pas besoin d'être chiffré et peut être public.

Cela peut servir à transférer:

- **des seed phrases** (la master seed du ColdCard Q ou les secrets stockés dans le [Seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault) du ColdCardQ).
- **des notes confidentielles et des mots de passe**: ça peut être un secret quelconque ou l'entièreté du répertoire  [Secure Notes & Passwords](https://coldcard.com/docs/secure_notes/) de votre ColdCardQ.
- **un backup de l'entièreté de votre ColdCardQ**: le ColdCardQ qui reçoit ce backup ne doit pas avoir de Master Seed pour que cela fonctionne.
- **des PSBT (*Partially Signed Bitcoin Transactions*) dans le cadre d'un schéma multi signature**.

Cela nécessite d'avoir upgradé le [firmware de votre appareil en version v1.3.2Q](https://coldcard.com/docs/upgrade/) minimum.

## Comment utiliser Key Teleport ?

### 1- Pour transférer tout type de données

Ici on s'intéressera au transfert de seed phrases, de notes, de mots de passe, ou d'un transfert entier du backup d'un ColdCardQ. Le cas des transferts de PSBT pour les transactions multi signatures sera abordé dans un second temps.

#### Préparer l'appareil qui recevra les secrets

Dans le menu **"Advanced / Tools**" de votre ColdCardQ, sélectionnez **"Key Teleport (start)"**.
Sur l'écran suivant, un mot de passe composé de 8 chiffres vous est proposé ici "20420219". il vous faudra communiquer ce mot de passe à l'émetteur. Utilisez par exemple un sms pour transmettre ce mot de passe, ou votre messagerie sécurisée favorite, ou encore un appel vocal.

Ensuite cliquez sur le bouton **"Enter**" de votre ColdCardQ pour passer à l'étape suivante.


![CCQ-key-teleport](assets/fr/01.webp)


Un QR code est généré à l'écran. Vous devrez, là encore, communiquer ce QR code au ColdCardQ "envoyeur". Le plus simple est de le faire via un appel visio.

**ATTENTION ! IL NE FAUT SURTOUT PAS COMMUNIQUER CE QR CODE A TRAVERS LE MÊME CANAL DE TRANSMISSION QUI A SERVI A L'ENVOI DU MOT DE PASSE DE 8 CHIFFRES PRECEDENT**.

![CCQ-key-teleport](assets/fr/02.webp)

*Pour ceux que ça intéresse, essayons de comprendre le mécanisme sous-jacent permettant ce transfert de secrets à travers des canaux non sécurisés.*

*Nous sommes en fait là en train d'initier un transfert de secrets via la méthode Diffie-Hellman, abordée dans le cours BTC204 que je vous mets en dessous.*

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Nous avons pour le moment:*
- *généré une paire de clés éphémères (publique/privée respectivement Ka et ka avec Ka=G.ka, G étant le point générateur de ECDH), ainsi qu'un mot de passe à 8 chiffres*.
- *utilisé ce mot de passe pour chiffrer la clé publique (Ka) via AES-256-CTR, puis transmis ce mot de passe par un canal de communication A au ColdCardQ "envoyeur".*
- *enfin nous avons transmis le paquet chiffré à l'envoyeur via le QR code ci-dessus, par un second canal de communication B différent du 1er*.

#### Préparer l'appareil qui enverra les secrets

Depuis l'appareil envoyeur, cliquez sur le bouton **"QR"** pour scanner le QR code qui vous est transmis par l'appareil receveur, puis entrez le mot de passe à 8 chiffres qui vous a été communiqué à l'étape précédente par un canal séparé. Nous sommes désormais en mesure de commencer l'envoi des données à partir de l'appareil "envoyeur".

**Attention ne vous trompez pas en entrant le mot de passe à 8 chiffres car aucun message d'erreur ne sera affiché et le processus continuera. Cependant le transfert final des données échouera et il vous faudra recommencer**.

![CCQ-key-teleport](assets/fr/03.webp)

 *Pour les plus curieux d'entre vous intéressons nous là encore à ce que nous sommes entrain de réaliser d'un point de vue cryptographique et de transfert de secrets:*
- *nous avons importé les données chiffrées en scannant le QR code de l'appareil receveur*.
- *puis nous les avons déchiffrées en utilisant le mot de passe à 8 chiffres qui nous avait été transmis par un canal secondaire*.
- *nous sommes donc en possession de la clé publique (Ka) générée par le receveur initialement.*
- *Nous générons ensuite sur l'appareil envoyeur une nouvelle paire de clés éphémères (Kb/kb, avec  là encore Kb=G.kb) que nous utilisons pour appliquer ECDH sur Ka. On réalise donc l'opération kb.Ka=Ks , où Ks est appelée **"Session Key"**.* 


Il vous est maintenant demandé de choisir la nature des secrets à transmettre entre les 2 ColdCardQ (notes confidentielles, mot de passe, backup complet, seeds contenues dans votre vault, master seed de l'appareil). 

![CCQ-key-teleport](assets/fr/04.webp)

Ici notre secret sera un message court en choisissant **"Quick Text Message"**. Tapez au clavier votre message (pour nous "PlanB Network rocks") puis pressez **"ENTER"**.
L'appareil génère ensuite un nouveau mot de passe aléatoire appelé **"Teleport Password"** , dans l'exemple "NE XG BT SK".

![CCQ-key-teleport](assets/fr/05.webp)

Pressez **"ENTER"** et un nouveau QR code vous sera présenté. Faites le scanner par l'appareil receveur. Et sur un canal de communication différent, transmettez le **"Teleport Password"** au receveur.

![CCQ-key-teleport](assets/fr/06.webp)

*Là encore pour les curieux, lors de cette étape:*
- *après avoir sélectionné les secrets à transmettre nous générons un nouveau mot de passe aléatoire appelé **"Teleport Password"***.
- *nous chiffrons ensuite les secrets via AES-256-CTR en utilisant la **"Session Key"**, "Ks",  générée lors de l'étape précédente.*
- *on accole en préfixe du paquet déjà chiffré par la **"Session Key"** notre clé publique Kb, puis nous rajoutons une  couche de chiffrement AES-256-CTR supplémentaire avec le **"Teleport Password"**. Le tout est ensuite encodé sous forme de QR code.*


#### Finaliser le transfert de secrets sur l'appareil receveur

Appuyez sur le bouton **"QR"** pour scanner le QR code présenté par l'appareil envoyeur à travers le canal visio. Il vous sera demandé de rentrer votre mot de passe **"Teleport Password"** pour nous "NE XG BT SK". 

![CCQ-key-teleport](assets/fr/07.webp)



Les données sont ensuite déchiffrées et intelligibles pour l'appareil receveur. Le message reçu est bien "PlanB Network rocks". C'est terminé.

![CCQ-key-teleport](assets/fr/08.webp)

*Que s'est-il passé concrètement lors de cette dernière étape :*
- *nous avons déchiffré les données transmises par l'envoyeur en utilisant le **"Teleport Password"**.*
- *nous sommes donc en possession de la clé publique Kb et de notre message secret chiffré par la **"Session Key"**,  "Ks". Mais comment faire puisqu'en tant que receveur on ne connait pas Ks, qui a été créée par l'envoyeur ?*
- *Il nous faut appliquer notre clé privée "ka" de l'étape initiale **"Préparer l'appareil qui recevra les données"** à la clé publique Kb.* 
- *En effet en effectuant le calcul ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks on retrouve Ks. Qu'on utilise enfin pour déchiffrer le message secret.*

### 2- Pour transférer des PSBT pour Multisig (avancé)

Cela présuppose que votre wallet multisig a déjà été créé au préalable et que votre appareil ColdCardQ a déjà été pré-réglé pour être en mesure  de réaliser des transactions multi signatures. Si ce n'est pas le cas des explications sont disponibles [ici](https://coldcard.com/docs/multisig/) sur le site de Coinkite (en anglais).

Petit rappel sur ce qu'est un wallet multi signatures (multisig).

Habituellement pour dépenser les fonds de votre wallet, une seule clé privée est nécessaire pour déverrouiller les UTXOs associés à vos adresses.
Dans le cas d'un wallet multisig, jusqu'à 15 clés privées et donc 15 signatures peuvent être nécessaires pour dépenser les fonds. C'est ce qu'on appelle un portefeuille "M sur N", avec N compris entre 1 et 15 et M le nombre de signatures nécessaires pour que les fonds soient dépensables. Par exemple un wallet multisig 3 sur 5, nécessitera au moins 3 signatures sur les 5 possibles.

L'enjeu est alors de se coordonner entre signataires pour signer une "PSBT" pour "Partially Signed Bitcoin Transaction" tour à tour. Dans ce cadre, "**Key Teleport**" peut être utilisé pour se transmettre la PSBT entre cosignataires de manière simple et confidentielle. Un simple appel visio entre cosignataires fera l'affaire.

Voilà comment procéder ici dans le cadre d'un multisig 3 sur 4.

**Signataire 1:**

Le signataire 1 importe puis signe la PSBT. Enfin il clique sur **"T"** afin d'utiliser **"Key Teleport"** pour transmettre la PSBT au signataire 2.

![CCQ-key-teleport](assets/fr/09.webp)


Après avoir sélectionné le signataire 2 en cliquant sur **"ENTER"**, un "TELEPORT PASSWORD" (ici JJ YC AB 6A) est fourni, qu'il faudra transmettre au signataire 2 par un autre canal de communication. Par exemple un SMS ou un appel vocal mais **pas** en visio.

Pressez à nouveau **"ENTER"** et un QR code représentant la PSBT signée par 1 puis chiffrée par le "TELEPORT PASSWORD" apparait.

![CCQ-key-teleport](assets/fr/10.webp)

**Signataire 2:**

Le signataire 2 scanne le QR code présenté par le signataire 1 en visio. Puis entre le "TELEPORT PASSWORD" transmis par le canal de communication secondaire pour déchiffrer les données transmises.

Le signataire 2 signe la transaction puis clique sur **"T"** pour transmettre la PSBT au signataire 3 via "Key Teleport".
On voit bien que 2 signatures ont déjà été appliquées. Il ne manque plus que celle du signataire 3 pour que la transaction soit valide. On sélectionne donc le signataire 3 en cliquant sur **"ENTER"**.

![CCQ-key-teleport](assets/fr/11.webp)

Et un nouveau "TELEPORT PASSWORD" est créé, suivi là encore d'un QR code encodant la PSBT signée par 1 et 2  puis chiffrée par ce nouveau "TELEPORT PASSWORD" (GW YQ K3 LL).

![CCQ-key-teleport](assets/fr/12.webp)

**Signataire 3:**

On répète la même étape que précédemment.
Le signataire 3 scanne le QR code présenté par le signataire 2 en visio. Puis entre le "TELEPORT PASSWORD" transmis par le canal de communication secondaire.

Le signataire 3 signe la transaction et cette fois puisque 3 signatures sur 4 ont été appliquées , la transaction nous est indiquée comme finalisée, et est prête à être diffusée par différents médiums (SD Card, NFC, QR etc...).

![CCQ-key-teleport](assets/fr/13.webp)

Si la fonctionnalité "Push Tx" de votre ColdCardQ est activée, il vous suffit d'apposer votre ColdCardQ au dos de n'importe quel appareil connecté à Internet et supportant le NFC (smartphone / tablette), pour diffuser la transaction sur le réseau Bitcoin.

![CCQ-key-teleport](assets/fr/14.webp)

*Dans le cadre des transferts de PSBT d'un signataire à l'autre, "Key Teleport" est simplement utilisé via un "Teleport Password" à chaque étape qui chiffre la PSBT lors du transfert d'un signataire à l'autre. Comme les données transmises ne permettent pas de voler les fonds, pas besoin d'avoir recours à un Diffie-Hellman comme dans le cas d'envoi de secrets ultra confidentiels (seed, mot de passe etc...)*.

![CCQ-key-teleport](assets/fr/15.webp)

*Source : [Site officiel de ColdCard](https://coldcard.com/)*
