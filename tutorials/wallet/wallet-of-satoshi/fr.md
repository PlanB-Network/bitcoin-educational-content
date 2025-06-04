---
name: Wallet de Satoshi (WoS)
description: La Wallet la plus simple à utiliser pour commencer
---
![cover](assets/cover.webp)

ce tutoriel a été rédigé par_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)

# Télécharger, configurer et utiliser Wallet de Satoshi

Wallet de Satoshi est un Wallet Lightning Network, de garde, très simple à utiliser.

Dans le cadre du cours [BTC105 - Finding Yourself Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), il est utilisé pour les bons Redeem Lightning Network.

**souvenez-vous toujours** : _pas vos clés, pas vos pièces_

Wallet custodial, ne permettent pas aux utilisateurs de disposer pleinement de leurs fonds. Ils ne sont normalement pas recommandés, sauf pour ceux qui partent de zéro. Les WoS doivent être utilisés comme passerelle Wallet ou pour stocker de l'argent de poche, et non pour accumuler des fonds à long terme.

---
Le Wallet of Satoshi (WoS) est un produit de conservation, mais il jouit d'une certaine réputation. Nous pouvons raisonnablement nous tourner vers un outil comme le WoS, par exemple, pour accroître notre capacité à recevoir des liquidités. Nous déléguons temporairement au WoS le "sale boulot" qui consiste à gérer la liquidité des canaux pour nous. Une fois que nous aurons atteint un certain montant, nous viderons le WoS On-Chain sur notre Wallet non custodial.

**ATTENZIONE⚠️ : Il est recommandé de lire le tutoriel dans son intégralité avant de poursuivre**

## Téléchargement de Wallet de Satoshi

Allons sur le playstore et téléchargeons WoS

![image](assets/it/01.webp)

**Note:** Le WoS est téléchargé uniquement à partir des magasins officiels. Si le système d'exploitation de l'appareil est programmé, une vérification par le système d'exploitation lui-même a lieu avant l'ouverture du WoS. Une fois la phase de vérification passée, choisissez _Ouvrir_.

![image](assets/it/02.webp)

Wallet de Satoshi s'ouvre avec l'écran suivant et vous devez cliquer sur _Start_

![image](assets/it/03.webp)

## Création d'un compte pour le WoS

A ce stade, Wallet est opérationnel, mais pour plus de sécurité, configurons un login : il sera utilisé pour récupérer les fonds en cas de panne ou de perte de l'appareil. Sélectionnez ensuite le menu en haut à gauche.

![image](assets/it/04.webp)

Toute la fenêtre de menu s'ouvre, dans laquelle il suffit de régler la monnaie (Wallet de Satoshi présente par défaut le dollar américain comme monnaie de référence) et la couleur du thème (clair/foncé), selon votre goût. N'utilisez pas les autres contrôles.

Le WoS étant un outil de conservation, nous ne pouvons pas sauvegarder Wallet avec la phrase Mnemonic. Cependant, nous pouvons permettre au WoS de récupérer nos fonds, en cas de perte ou d'inutilisation de l'appareil mobile, en cliquant sur _Login/Register_

![image](assets/it/07.webp)

Une fenêtre apparaît dans laquelle on nous demande d'entrer un email Address. Il peut s'agir d'un **email Proton** (recommandé), mais cela fonctionne, car c'est celui qui nous permettra de récupérer les fonds Wallet, en cas de perte, de vol ou de panne du téléphone portable

![image](assets/it/08.webp)

Wallet de Satoshi a envoyé un message à la boîte aux lettres électronique signalée

![image](assets/it/09.webp)

Dans la boîte de réception, nous trouverons deux mots, que nous devrons saisir, en les réécrivant, dans l'espace que l'application nous présente


- ne pas activer le traducteur : les mots sont et doivent rester en anglais**
- réécrire les deux mots en respectant les majuscules et les minuscules**

![image](assets/it/10.webp)

Après avoir transcrit les deux mots, cliquez sur _OK_

![image](assets/it/11.webp)

Le résultat est qu'un chiffre doit apparaître en haut, avec un symbole de coche pour la vérification

![image](assets/it/12.webp)

tandis que dans la section des paramètres, la bande rouge de _Login/Register_ affiche désormais l'email Address de l'utilisateur.

![image](assets/it/13.webp)

## Recevoir des paiements

Pour recevoir sur WoS, cliquez sur _Receive_ et une série de commandes apparaît.

![image](assets/it/14.webp)

Vous pouvez recevoir


- via LN-Address **a**
- via LN, réglage Invoice **b**
- on chain (WoS soutient le réseau Bitcoin mais avec des échanges sous-marins payants) **c**
- encadrer le code QR d'une LNurl-p **d**

![image](assets/it/15.webp)

## Invoice Création

Cliquez sur _Receive_ et choisissez la commande avec le symbole Lightning Network

![image](assets/it/16.webp)

Le menu de création de la Invoice apparaît, où l'on clique sur _Add Amount_ pour écrire le montant exact et ajouter une description, dans cet exemple "My first Invoice"

![image](assets/it/17.webp)

A l'aide du clavier, nous fixons le montant

![image](assets/it/18.webp)

et se faire payer par Invoice. Le paiement reçu se présente comme suit :

![image](assets/it/19.webp)

## Collecte auprès du TPV

Le Wallet du Satoshi est doté par défaut d'une caractéristique intéressante, qui le rend particulièrement adapté aux commerçants : POS. Voyons comment l'activer.

Dans l'écran principal, sélectionnez le menu dans le coin supérieur droit

![image](assets/it/20.webp)

Sélectionnez ensuite _Point de vente_

![image](assets/it/21.webp)

Avec la dernière version du WoS, veillez à sélectionner le _Keypad_

![image](assets/it/22.webp)

puis tapez le montant sur le clavier, dans l'exemple suivant égal à 18 cents / 118 Sats. Ajoutez une description pour la collection, dans ce cas "ma deuxième avec POS" Un grand bouton Green s'allume, et il s'agit de cliquer

![image](assets/it/23.webp)

pour generate le Invoice et le montrer, par exemple, à un client.

![image](assets/it/24.webp)

Ce paiement est également perçu !

![image](assets/it/25.webp)

## Envoi des paiements

La simplicité est une force de l'écran principal du WoS. Pour payer une Invoice, cliquez sur _Envoyer_

![image](assets/it/26.webp)

Lors de la première utilisation, le WoS demande des autorisations pour accéder à la caméra

![image](assets/it/27.webp)

À partir de ce moment, la caméra est activée

![image](assets/it/28.webp)

En encadrant la Invoice, nous voyons qu'un paiement de 210 Sats a été demandé. On y lit également une description, si le demandeur en a défini une. Cet écran est à la fois un résumé et une demande de confirmation : Le WoS "demande la permission" d'envoyer le paiement, ce qui lui est accordé en cliquant sur le bouton Green _Send_

![image](assets/it/29.webp)

Lorsque le paiement arrive à destination, le WoS affiche l'écran suivant

![image](assets/it/30.webp)

A partir de l'écran principal, un clic sur _History_ (juste en dessous du solde) permet d'afficher la liste des transactions

![image](assets/it/31.webp)

### Récupération du compte WoS

Nous allons maintenant voir comment installer WoS sur un nouvel appareil ; cela sera également utile en cas de vol, de perte ou d'impossibilité d'utiliser le téléphone portable sur lequel Wallet était précédemment installé. Une fois réinstallé, il faut refaire la procédure d'enregistrement du compte que nous venons d'expliquer, avec une variante : à la fin de la demande de connexion avec l'email précédemment défini, WoS apparaîtra comme ceci :

![image](assets/it/33.webp)

Un message nous avertit que la procédure de réactivation du compte a été envoyée par courriel. Il faut ouvrir sa boîte aux lettres.

**IMPORTANT** : ouvrez le courriel à partir d'un PC ou, en tout cas, d'un appareil autre que ceux sur lesquels vous allez récupérer le compte WoS. Dans la boîte de réception, nous trouvons un message qui nous montre un code QR à encadrer

![image](assets/it/34.webp)

Une fois le code QR cadré, le compte retrouvé apparaîtra sur la page principale du WoS, avec le solde et l'historique.