---
name: Coinos
description: Une application web simple qui permet d’envoyer, de recevoir et d'accepter des paiements Bitcoin.
---
![cover](assets/cover.webp)

## Introduction

Dans un monde où les paiements deviennent de plus en plus numériques, Bitcoin s’impose progressivement comme une alternative. Pourtant, pour beaucoup de novices, gérer un portefeuille ou accepter des paiements Bitcoin peut sembler compliqué.

C’est là qu’entre en jeu Coinos, une plateforme conçue par Adam Soltys, un développeur web qui avait créé la première version pour aider les commerçants de sa région à accepter les paiements en Bitcoin.

Coinos est une plateforme simple et intuitive, pensée pour une utilisation fluide. Elle permet d’envoyer, de recevoir et d’accepter des paiements en Bitcoin, Liquid ou Lightning, directement depuis ton navigateur, sans aucune installation technique. Accessible à tous, Coinos combine les avantages de Bitcoin avec la simplicité d’une application web (**Application Web Progressive**), idéale pour les particuliers, les commerçants et les curieux.

Vidéo tutoriel

![vidéo](https://youtu.be/GADLcQ4g8DU)

## Premiers pas avec Coinos

Vous n'avez pas besoin de connaissances techniques ou approfondies avant de prendre en main **Coinos**. Néanmoins, une compréhension basique des transactions Bitcoin on chain, Lightning et Liquid est un plus. 

### Création de compte 

Rendez-vous sur le site web de [Coinos](https://coinos.io/) dans votre navigateur et cliquez sur **Commencer en quelques secondes**.

![screen|220](assets/fr/03.webp)

Entrez votre **Nom d'utilisateur** et un **Mot de passe**, puis cliquez sur **Enregistrer**. 

!![screen|220](assets/fr/04.webp)

Vous serez ensuite redirigé vers l'interface principale du portefeuille. Que ce soit sur votre ordinateur ou sur votre smartphone, l'interface demeure la même. 

![screen|220](assets/fr/05.webp)

![screen](assets/fr/06.webp)

En haut, au-dessus de votre avatar, vous avez l'icône de l'interface :
 1. **principale**

![screen|220](assets/fr/07.webp)

 2. **de réception**

![screen|220](assets/fr/08.webp)

 2.  **de l'historique des transactions**

![screen|220](assets/fr/09.webp)

 4.  **d'envoi**

![screen|220](assets/fr/10.webp)

 5.  **du menu déroulant**

  ![screen|220](assets/fr/11.webp)
  
Ensuite, vous avez
- votre **avatar** ;
- votre **nom d'utilisateur ;
- un **petit menu déroulant** qui renferme votre adresse Lightning Coinos, une URL publique et un code de paiement (adresse LNURL) ;
- et une icône **crayon** qui vous redirige vers le sous-menu **Compte**.

![screen|220](assets/fr/12.webp)

Au milieu, vous avez les icônes **Recevoir** et **Envoyer**. 
Juste au-dessus de l’icône **Recevoir**, le solde de votre portefeuille est affiché en Satoshi ainsi que dans la monnaie locale que vous avez sélectionnée.

Dans les deux coins inférieurs gauche et droit, on retrouve respectivement le prix actuel d'un bitcoin dans la monnaie locale choisie et le nombre de Satoshi équivalant à une unité de compte libellée dans la monnaie locale choisie. 

![screen|220](assets/fr/13.webp)

Coinos, en tant que portefeuille web, n'est pas disponible sur le Play store ni sur l'App store. Toutefois, il existe une manière de l'installer. 
Depuis votre navigateur, une fois sur Coinos, cliquez d'abord sur les **trois points** situés dans le coin supérieur de votre écran.

![screen|220](assets/fr/14.webp)

Ensuite sur **Ajouter à l'écran d'accueil**.

![screen|220](assets/fr/15.webp)

Enfin, cliquez sur **Installer**.

![screen|220](assets/fr/16.webp)

Bingo ! Vous pourrez maintenant le voir s'afficher dans le menu des applications de votre téléphone.

![screen|220](assets/fr/17.webp)

### Configuration du portefeuille

Cliquez sur le **bouton de l'interface du menu déroulant** puis sur **Préférences**.

![screen|220](assets/fr/18.webp)

Dans **Préférences**, on retrouve (4) quatre sous-menus qui vous permettent de configurer votre portefeuille :

1. **Compte**

Dans ce sous-menu, vous avez la possibilité de modifier votre nom d'utilisateur, de définir un nouveau mot de passe, de changer votre avatar (image de profil), d'ajouter une photo de bannière et même une description.

![screen|220](assets/fr/19.webp)

![screen|220](assets/fr/20.webp)

2. **Point de vente** 
Ici, vous choisissez la langue, la monnaie locale, vous ajoutez un e-mail, activez les notifications selon votre convenance, voire connectez votre portefeuille à Square si vous êtes commerçant…

![screen|220](assets/fr/21.webp)

![screen|220](assets/fr/22.webp)

3. **Nostr**
Si vous disposez d'un compte sur Nostr, vous pouvez le connecter à votre compte Coinos, etc.

![screen|220](assets/fr/23.webp)

4. **Sécurité**
Vous avez la possibilité d'activer un code de sécurité, d'activer l'authentification à deux facteurs, et même d'ajouter un autre compte dans ce sous-menu.

![screen|220](assets/fr/24.webp)

N'oubliez pas de cliquer sur **Sauvegarder les paramètres** à chaque fois que vous opérez une modification afin d'enregistrer vos changements.

![screen|220](assets/fr/25.webp)

Une fois votre configuration achevée, revenez sur l'interface principale en cliquant sur son **icône**.

## Les Types de paiements Bitcoin Supportés

Coinos supporte les transactions :

- **Bitcoin sur la chaîne principale (on chain)** avec des formats d'adresse tels que SegWit, Taproot et Legacy ;
- **Lightning** LNURL, Bolt 11 et Bolt 12 ;
-  et d'autres, notamment via le réseau **Liquid** et **Ecash**. 

![screen|220](assets/fr/26.webp)

Pour rappel, **Ecash** (XEC) est un jeton issu du projet Bitcoin Cash ABC, lui-même issu d’un fork de Bitcoin Cash et rebaptisé Ecash quelques années plus tard.

## Recevoir des bitcoins

Pour recevoir des bitcoins sur Coinos, cliquez soit sur **Recevoir**, soit sur l'icône de l'**interface de réception**. Une fois sur l’interface de réception, demandez à votre expéditeur **par quel réseau il souhaite envoyer les bitcoins**, afin de déterminer **quelle adresse lui communiquer**.

### Réception sur la chaîne principale 

Cliquez sur **Bitcoin**. 

![screen|220](assets/fr/27.webp)

Un code QR ainsi qu’une adresse de réception sont alors générés automatiquement. 

![screen|220](assets/fr/28.webp)

Vous pouvez les personnaliser en définissant un montant spécifique et un mémo (étiquette).

![screen|220](assets/fr/29.webp)

![screen|220](assets/fr/30.webp)

Votre **code QR** et votre **adresse Bitcoin personnalisés** sont désormais prêts ; il ne vous reste plus qu’à les transmettre à votre expéditeur pour recevoir vos bitcoins.

![screen|220](assets/fr/31.webp)

### Réception via Liquid

Cliquez sur **Plus d'options**, puis sur **Liquid**.

![screen|220](assets/fr/32.webp)

![screen|220](assets/fr/33.webp)

Un code QR et une adresse de réception Liquid sont également générés. 

![screen|220](assets/fr/34.webp)

Coinos vous rappelle que vous ne devez envoyer sur cette adresse ou via ce code QR que des **bitcoins Liquid** (**L-BTC**).

Vous avez la possibilité de les personnaliser avec un montant bien défini et une étiquette. 

![screen|220](assets/fr/35.webp)

Transmettez-le à votre expéditeur et recevez vos **L-BTC**.

![screen|220](assets/fr/36.webp)

### Réception par Lightning Network 

Par défaut, l'interface de réception s'ouvre sur l'option Lightning. Vous avez donc votre QR code et votre adresse Lightning que vous pouvez personnaliser avec un montant spécifique et un mémo.

![screen|220](assets/fr/37.webp)

![screen|220](assets/fr/38.webp)

Votre **code QR** et votre **adresse Lightning personnalisés** sont à présent prêts. Envoyez-les à votre expéditeur et recevez vos satoshis instantanément. 

![screen|220](assets/fr/39.webp)

De plus, pour la réception par **Lightning**, vous avez la possibilité d’utiliser le petit menu déroulant de l'interface principale du portefeuille. Ce dernier vous fournit votre adresse Lightning… Vous le copiez ou switchez vers le code QR.

![screen|220](assets/fr/40.webp) 

Notez qu'à chaque fois que vous définissez un montant, quel que soit le réseau utilisé, Coinos vous met l'équivalent en satoshis.


## Envoyer des bitcoins 

Si vous désirez envoyer des bitcoins depuis votre portefeuille Coinos, cliquez sur l'**icône de l'interface d'envoi**. Une fois sur l'interface, plusieurs options s'offrent à vous, notamment :
1. Scannez un code QR généré par le récepteur.

2. Collez une adresse copiée dans le presse-papiers. 

3. Sélectionnez immédiatement dans la section **Contacts** le nom d'utilisateur de quelqu'un avec qui vous aviez l'habitude de réaliser des transactions.

4. Tapez dans le champ dédié une adresse Bitcoin (on chain, Liquid, LN), une facture Lightning ou tapez le nom d'utilisateur Coinos de votre récepteur. 

![screen|220](assets/fr/41.webp)

Après avoir tapé ou collé l’adresse, appuyez sur **Suivant**, saisissez le montant de la transaction, puis appuyez à nouveau sur **Suivant**.

![screen|220](assets/fr/42.webp)

![screen|220](assets/fr/43.webp)

La dernière étape avant l'envoi consiste à vérifier les informations et à ajuster les frais de réseau selon votre convenance. 

![screen|220](assets/fr/44.webp)

Pour ajuster, appuyez sur le petit triangle puis choisissez vos frais de réseau en fonction de la vitesse de transaction voulue. Plus l'exécution de votre transaction est rapide, plus vous payez de frais de réseau. 
Aussi, des frais de plateforme sont prélevés par Coinos. Lorsque tout est en ordre et selon votre convenance, appuyez sur **Envoyer**.

![screen|220](assets/fr/45.webp)

Bravo ! Votre envoi est effectué.

![screen|220](assets/fr/46.webp)

Essayons maintenant un envoi entre utilisateurs Coinos. Envoyons 21 satoshis à Adam Soltys. Personnellement, il dispose d'une adresse Coinos unique (adam).

![screen|220](assets/fr/47.webp)

![screen|220](assets/fr/48.webp)

![screen|220](assets/fr/49.webp)

Vous pouvez aussi essayer de m'envoyer quelques satoshis via mon adresse Lightning Raimi@coinos.io.

Notons que les transactions entre utilisateurs Coinos sont exemptes de tout frais de plateforme.

## Historique des transactions 

Pour voir l'historique de vos transactions, cliquez sur l'**icône de l'interface de l'historique des transactions**.
Pour chaque transaction, les informations suivantes seront affichées : le montant, le réseau utilisé, ainsi que la date et l'heure. Tandis que le solde affiché sur l'interface principale du portefeuille est un solde unifié.

![screen|220](assets/fr/50.webp)

![screen|220](assets/fr/51.webp)


## Fonctionnalités supplémentaires 

Sur Coinos, vous disposez de fonctionnalités supplémentaires au nombre desquelles nous pouvons citer :

- La **Carte des commerçants**
Coinos intègre dans son portefeuille une carte des commerçants qu'il a activés. Tous ces commerçants répertoriés par Coinos acceptent Bitcoin comme moyen de paiement, notamment via leur portefeuille Coinos.
Pour visionner les commerces enregistrés, cliquez sur l'icône du **menu déroulant**, puis sur **Carte**. Vous accédez alors à la liste des commerces et de leur emplacement dans le monde. 

![screen|220](assets/fr/52.webp)

![screen|220](assets/fr/53.webp)

Lorsque vous cliquez sur un commerce, vous verrez son étiquette et en cliquant sur l'étiquette, vous accéderez à son profil Coinos. Ce qui vous permet de payer vos achats dans ce commerce grâce à Coinos. 

![screen|220](assets/fr/54.webp)

![screen|220](assets/fr/55.webp)

- **Assistance** 

Pour toutes difficultés rencontrées dans l'utilisation de Coinos, vous pouvez :
1. soit remplir un formulaire directement dans l'application pour soumettre vos préoccupations 
2. soit écrire directement un courriel à 
support@coinos.io.

Pour accéder à ce menu, cliquez sur l'icône du menu déroulant puis sur **Assistance**.

![screen|220](assets/fr/56.webp)

![screen|220](assets/fr/57.webp)

## Sécurité et Bonnes pratiques

La sécurité est un point essentiel quand on dépense des bitcoins. Même si Coinos rend l’expérience simple et fluide, il est important de protéger ses bitcoins.

1. Utilisez un mot de passe solide 
Choisissez toujours un mot de passe unique, long et difficile à deviner.

2. Activez la double authentification (2FA).

3. Gardez vos identifiants privés 
Ne partagez jamais votre mot de passe avec quelqu’un d’autre. Coinos ne les demandera jamais par message ou email.

4. Ne stockez pas de grosses sommes sur l’instance hébergée
Coinos est pratique pour les paiements quotidiens, mais reste une solution custodial.
Gardez seulement ce dont vous avez besoin pour vos transactions courantes. Pour des montants importants, optez pour un portefeuille non custodial.

Je vous remercie d'avoir lu cet article jusqu'à la fin. Si ce tutoriel vous a été utile, merci de me laisser un pouce vert ci-dessous. N'hésitez pas à les partager, si vous avez des apports.
Merci infiniment!
Je vous suggère de découvrir ce tutoriel sur Aqua. Il s'agit également d'un portefeuille, à l'instar de Coinos qui supporte Bitcoin, Liquid et Lightning.

https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125
