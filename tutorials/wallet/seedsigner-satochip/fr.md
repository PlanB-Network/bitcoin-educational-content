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

## 1. Installer le firmware





## 2. Assembler le lecteur de smartcard




## 3. Flasher une smartcard avec l’applet Satochip (optionnel)





## 4. Création et sauvegarde de la seed




## 5. Importer le wallet dans Sparrow



## 6. Recevoir et envoyer des bitcoins



## 7. Explorer les adresses de réception




## 8. Récupérer son portefeuille


### 8.1. Récupérer son portefeuille avec le Satochip




### 8.2. Récupérer son portefeuille avec le SeedSigner






