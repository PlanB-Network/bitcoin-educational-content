---
name: SAFU Ninja
description: Sauvegarder sa seed avec la méthode SAFU Ninja
---

![cover](assets/cover.webp)
## 1. Introduction

La méthode **Ninja SAFU** est une solution **DIY (Do It Yourself)** qui vous permet de créer une sauvegarde **durable, sécurisée et discrète** de votre **seed phrase** (phrase mnémonique de 12 ou 24 mots définie par la norme **BIP-39**). Cette phrase est indispensable pour restaurer un portefeuille Bitcoin ou tout autre portefeuille compatible.

Au lieu de noter vos mots sur du papier, une méthode simple mais vulnérable, vous allez les graver sur des **rondelles en acier inoxydable**, assemblées sur un **boulon**. Le résultat est une sauvegarde compacte, résistante au feu, à la corrosion, à l’eau et aux chocs. Contrairement au papier, qui peut être détruit par les flammes, l’humidité ou le temps, l’acier inoxydable garantit une conservation à long terme, même dans des conditions extrêmes (jusqu’à 1300°C ou 20 tonnes de pression).

L’approche Ninja SAFU présente plusieurs avantages :

- **Confidentialité** : Vous n’achetez pas un produit identifié comme étant destiné à la sauvegarde de cryptomonnaies. Les composants sont standards (rondelles, boulon, boîte métallique), disponibles en quincaillerie, ce qui réduit le risque de ciblage en cas de fuite de données chez un vendeur spécialisé.

- **Abordabilité** : Le coût de cette solution se situe entre **15 et 140 EUR**, selon les outils déjà en votre possession.

- **Fiabilité** : Testée depuis 2020, la méthode a été éprouvée par des experts en sécurité comme [Jameson Lopp](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/), qui lui ont fait subir des stress tests rigoureux (chaleur extrême, corrosion, pression mécanique).

Ce guide vous accompagnera pas à pas pour réaliser votre propre sauvegarde Ninja SAFU, afin de mieux protéger vos bitcoins contre la perte ou la destruction. Pour approfondir vos connaissances en sauvegarde et protection d'une seed phrase, vous pouvez consulter les annexes.


## 2. Matériel

Pour réaliser une sauvegarde Ninja SAFU, vous aurez besoin des composants suivants, tous disponibles dans des quincailleries ou en ligne. 

### 2.1 Matériel nécessaire

- **Rondelles en acier inoxydable (M8 recommandé)** :
	- **Matériau** : Acier inoxydable (ex. : 304 ou V4A pour une résistance accrue à la corrosion)
    - **Taille** : M8 (diamètre intérieur 8 mm, diamètre extérieur ~24 mm). Les rondelles M6 sont trop petites et difficiles à graver.
    - **Quantité** : 12 ou 24 rondelles pour une seed phrase standard, plus les optionnelles (voir section 3.4) et une dizaine pour les tests ou erreurs.

- **Boulon et écrou en acier inoxydable (M8)** :
	- **Spécifications** : Boulon 2,5 à 5 cm de long selon le nombre et l'épaisseur des rondelles, de diamètre 8mm. Un écrou à oreilles facilite l’ouverture sans outils, mais il est possible de prendre un écrou simple.

![image](assets/fr/03.webp)

- **Jeu de poinçons lettres et chiffres (3 mm ou 6 mm)** :
    - **Spécifications** : Des caractères hauts de 6 mm facilitent la lisibilité et peuvent être préférables si une partie de la lettre est dégradée. Choisissez un jeu robuste pour un usage répété.

![image](assets/fr/04.webp)

- **Marteau ou massette** :
    - Une massette est préférable pour une force d’estampage suffisante et précise

- **Enclume ou surface robuste** :
	- Une surface dure et épaisse (ex. : enclume de 1 kg ou pavé de 10 cm) pour absorber les chocs.

Si vous ne souhaitez pas investir dans un jeu de poinçons, il est également possible de graver vos rondelles avec un stylo graveur. Cette solution, souvent plus économique, requiert toutefois davantage de soin pour obtenir un résultat satisfaisant.

### 2.2 Outils optionnels

- **Dispositif de frappe** : Maintient la rondelle et guide le poinçon, permettant pour un estampage précis et net, une meilleure orientation et un espacement régulier des lettres

![image](assets/fr/05.webp)

- **Dispositifs de scellement** : Pochette scellée ou bande de scellement

![image](assets/fr/06.webp)

- **Conteneur hermétique** : Pour stocker le bloc de rondelles

![image](assets/fr/07.webp)
### 2.3 Sécurité

- **Gants** et **Lunettes de sécurité** recommandés.
- **Clef à pipe** dans laquelle glisser le poinçon, de sorte à tenir le poinçon avec la clef à pipe et non avec les doigts.

### 2.4 Quantités et coût estimé

- **Quantité pour une sauvegarde de 24 mots** : 24 rondelles (minimum), 1 boulon, 1 écrou à oreilles, 1 jeu de poinçons, 1 marteau/massette, 1 enclume/support.

- **Coût total** : 
	- Rondelles, et boulon/écrou : ~ 15 EUR
	- Set de poinçons : ~ 45 EUR
	- Étui protecteur : ~ 55 EUR
	- Avec tous les accessoires : ~ 140 EUR

- Exemple de matériel en annexe.


## 3. Instructions étape par étape

1. **Se préparer :**
	- Lieu privé, sans caméra (y compris smartphones)
	- Surface robuste pour absorber les chocs
	- Gants et lunettes de sécurité
	- Nettoyez les rondelles de toute graisse ou impureté
	- Entrainez-vous sur des rondelles de test
2. **Graver les mots mnémoniques** :
    - Gravez le mot complet sur une face. Ne vous limitez pas aux 4 premières lettres, au cas où la 4ème serait endommagée.
    - Frappez fermement avec le marteau, en tenant le poinçon avec une clé à pipe
3. **Numéroter les rondelles** :
    - Sur la même face, gravez le numéro de position du mot, indispensable si les rondelles se détachent.
4. **Graver des informations** (optionnel et conseillé) :
    - Gravez le mot en redondance sur l'autre face de la rondelle
    - Gravez un identifiant pour le portefeuille sur une rondelle supplémentaire
    - Gravez le chemin de dérivation du compte que vous utilisez sur une rondelle supplémentaire. Vous pouvez retrouver cette information dans les paramètres de votre logiciel de portefeuille. Par exemple, pour un portefeuille Taproot standard, le chemin de dérivation par défaut sera : `m / 86' / 0' / 0' /`
    - Gravez le code PIN permettant de déverrouiller votre hardware wallet ou les mots anti-phishing si vous utilisez une COLDCARD.
5. **Ne PAS graver la passphrase :**
	-  Si vous utilisez une passphrase, évitez absolument de la noter sur le même support que votre phrase mnémonique. La passphrase a précisément pour rôle de protéger votre portefeuille en cas de vol de la phrase mnémonique. Plus d'informations en annexe.
6. **Vérifier la lisibilité** :
    - Assurez-vous que chaque mot et numéro est clair et lisible. 
7. **Assembler les rondelles** :
    - Enfilez les rondelles sur le boulon dans l’ordre des numéros.
    - Optionnel : ajoutez des rondelles vierges aux extrémités.
    - Vissez l’écrou à oreilles pour sécuriser la pile.
    - Serrez fermement : la protection contre l'eau, le feu et les contraintes mécaniques sera augmentée.
8. **Tester la sauvegarde** :
    - A partir de votre nouvelle sauvegarde, essayez de récupérer votre portefeuille
- **Sceller la sauvegarde** (optionnel et conseillé) :
	- Par bandes de scellage, ou sous pochette scellée.
	- En cas d'utilisation d'une pochette, notez son numéro d'identification unique, de sorte à pouvoir contrôler qu'il s'agit de la bonne pochette et non d'un leurre remplaçant l'original.


## 4. Stockage

### 4.1 Choisissez un lieu adapté

Stockez votre sauvegarde dans un **endroit discret**, à l’abri des regards et accessible pour des vérifications périodiques. Privilégiez un **stockage ignifuge et étanche**, chez vous ou dans un lieu sous votre **contrôle exclusif**.

Évitez les lieux où vous dépendez d’un tiers (coffre bancaire, notaire) : vous perdriez l’accès autonome à vos fonds, ce qui va à l’encontre des principes de souveraineté de Bitcoin.

Ne révélez jamais que vous utilisez une méthode comme Ninja SAFU. La discrétion est une couche de sécurité à part entière.

### 4.2 Redondance

Créez éventuellement **plusieurs exemplaires** et stockez-les en **différents lieux géographiques**.
Même si les matériaux choisis pour votre dispositifs sont résistants à l'eau et au feu, vous ne pourrez pas accéder à votre dispositif s'il est enfoui sous des m3 de gravats de votre logement, et sera très difficilement voire impossible à récupérer.


## 5. Suivi et maintenance

Même bien stockée, votre sauvegarde nécessite un **contrôle régulier** :

- A l'abri des regards, inspectez la sauvegarde **une à deux fois par an**.
- En cas de **dégradation des gravures**, recréez une nouvelle sauvegarde, **testez-la**, puis **détruisez soigneusement l’ancienne copie**.
- Si la sauvegarde est sous pochette scellée :
	- Vérifiez son identifiant
	- Vérifiez son intégrité
	- Régulièrement, ouvrez l'enveloppe pour inspecter l’état des gravures, et si tout va bien placez la sauvegarde dans une nouvelle pochette


*STAY SAFU !*
![image](assets/fr/08.webp)


## ANNEXES

### A.1 Sauvegarder sa phrase de récupération

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 Comprendre la Passphrase BIP39

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Les rouages des portefeuilles Bitcoin

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Classement de la méthode Ninja SAFU

Selon les travaux de Jameson Lopp : 

- [Compte rendu](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/) sur la méthode Ninja SAFU

- Tableau comparatif [complet](https://jlopp.github.io/metal-bitcoin-storage-reviews/?ref=blog.lopp.net)

- Tableau partiel : 
  ![image](assets/fr/09.webp)

### A.5 Exemple de matériel

- **Rondelles**
	- [Titan](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-wallet)
- **Rondelles + écrou + étui protecteur**
	- [Titan](https://pleb.style/fr-fr/products/titan-wallet-premium-acier-steel-wallet-backup?variant=50022696419664)
	- [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-wallet-plebstyle-acier-backup)
- **Set de poinçons**
	- [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Base de frappe**
	- [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Dispositif de frappe** (guide)
	- [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- **Dispositif de scellement**
	- [Pochette scellée](https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
	- [Bandes de scellement](https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Kit complet**
	- [Titan](https://pleb.style/fr-fr/products/titan-wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
	- [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-wallet-starter-kit)

Nota : Les liens fournis vers des boutiques en ligne sont à titre informatif.
Aucun partenariat commercial n’existe entre Plan B et les vendeurs et fabricants mentionnés.
La responsabilité de Plan B ne saurait être engagée en cas de défaut, de variation de prix ou de problème lié à la qualité ou à la livraison des produits. **DYOR**


### A.6 Crédits photos

https://pleb.style/fr/
https://x.com/lopp/status/1463155802345193475
https://bitcointalk.org/index.php?topic=5389446.0
https://x.com/econoalchemist/status/1329271981712289797
https://www.waivio.com/@themarkymark/create-your-own-metal-seed-key-backup
https://github.com/minibolt-guide/minibolt/blob/main/bonus/bitcoin/safu-ninja.md
