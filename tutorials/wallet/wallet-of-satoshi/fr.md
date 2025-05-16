---
name: Wallet de Satoshi
description: La Wallet la plus simple pour démarrer
---
![cover](assets/cover.webp)

ce tutoriel a été rédigé par_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


## Téléchargement, configuration et utilisation de Wallet de Satoshi


Wallet de Satoshi est un Lightning Network Wallet, de garde, et très simple d'utilisation.

Dans le cadre du cours [BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), il est utilisé pour les bons Redeem Lightning Network.


**N'oubliez jamais** : _pas vos clés, pas vos pièces_


Les portefeuilles de dépôt ne permettent pas aux utilisateurs d'exercer un contrôle total sur leurs fonds. Ils ne sont normalement pas recommandés, sauf pour les débutants. Le WoS doit être utilisé comme un Wallet transitoire ou pour conserver de l'argent de poche, et non pour accumuler des fonds à long terme.


---

Le Wallet of Satoshi (WoS) est un produit de conservation, mais il jouit d'une certaine réputation. Nous pouvons raisonnablement nous tourner vers un outil comme le WoS, par exemple, pour augmenter notre capacité à recevoir des liquidités. Nous déléguons temporairement au WoS le "sale boulot" qui consiste à gérer la liquidité des canaux pour nous. Lorsqu'un certain montant est atteint, nous vidons le WoS On-Chain au profit de notre Wallet, qui n'est pas un canal de garde.


**WARNING⚠️ : Il est recommandé de lire le tutoriel dans son intégralité avant de poursuivre**


### Téléchargement de Wallet de Satoshi


Allez sur le Play Store et téléchargez WoS


![image](assets/it/01.webp)


**Note:** Le WoS n'est téléchargé qu'à partir des magasins officiels. Si le système d'exploitation de l'appareil est programmé, l'ouverture du WoS est précédée d'une vérification par le système d'exploitation lui-même. Après la phase de vérification, choisissez _Ouvrir_.


![image](assets/it/02.webp)


Wallet de Satoshi s'ouvre avec l'écran suivant, et il faut cliquer sur _Start_


![image](assets/it/03.webp)


### Création d'un compte pour le WoS


A ce stade, le Wallet est déjà opérationnel, mais pour plus de sécurité, nous procédons à la configuration d'un login : il sera nécessaire pour récupérer les fonds en cas de dysfonctionnement ou de perte de l'appareil. Sélectionnez donc le menu en haut à gauche.


![image](assets/it/04.webp)


Toute la fenêtre de menu s'ouvre, dans laquelle vous devez exclusivement définir la devise (Wallet de Satoshi présente par défaut le dollar US comme devise de référence) et la couleur du thème (clair/foncé), selon votre goût. N'utilisez pas les autres commandes.


Le WoS étant un outil de conservation, nous ne pouvons pas sauvegarder le Wallet avec la phrase Mnemonic, mais nous pouvons permettre au WoS de récupérer nos fonds, en cas de perte ou de non-utilisation de l'appareil mobile, en cliquant sur _Login/Register_

Une fenêtre apparaît nous demandant d'entrer un email Address. Il peut s'agir d'un **mail Proton** (recommandé), mais il doit être fonctionnel, car il nous permettra de récupérer les fonds dans la Wallet en cas de perte/vol ou d'endommagement du téléphone portable.


![image](assets/it/08.webp)


Wallet de Satoshi a envoyé un message à la boîte aux lettres électronique indiquée.


![image](assets/it/09.webp)


Dans la boîte aux lettres, nous trouverons deux mots, que nous devrons saisir, en les réécrivant, dans l'espace fourni par l'application.


- ne pas activer le traducteur : les mots sont et doivent rester en anglais**
- réécrire les deux mots en respectant les majuscules et les minuscules**


![image](assets/it/10.webp)


Après avoir transcrit les deux mots, cliquez sur _OK_.


![image](assets/it/11.webp)


Le résultat devrait être une image apparaissant en haut, avec le symbole de la coche pour la vérification.


![image](assets/it/12.webp)


alors que dans la section des paramètres, la barre rouge _Login/Register_ affiche désormais l'email Address de l'utilisateur.


![image](assets/it/13.webp)


### Réception des paiements


Pour recevoir sur WoS, cliquez sur _Receive_ et une série de commandes apparaîtra.


![image](assets/it/14.webp)


Vous pouvez recevoir


- via LN-Address **a**
- via LN, en réglant le paramètre Invoice **b**
- on chain (WoS soutient le réseau Bitcoin mais avec des échanges sous-marins payants) **c**
- en scannant le code QR d'un LNurl-p **d**


![image](assets/it/15.webp)


### Création d'une Invoice


Cliquez sur _Receive_ et choisissez la commande avec le symbole Lightning Network.


![image](assets/it/16.webp)


Le menu de création de la Invoice apparaît, où l'on clique sur _Add Amount_ pour écrire le montant exact et ajouter une description, dans cet exemple, "My first Invoice".


![image](assets/it/17.webp)


Avec le clavier, nous fixons le montant.


![image](assets/it/18.webp)


pour ensuite recevoir le paiement de la Invoice. Le paiement reçu se présente comme suit :


![image](assets/it/19.webp)


### Collecte auprès du TPV


La Wallet de la Satoshi possède une caractéristique par défaut qui la rend particulièrement adaptée aux commerçants : le point de vente. Voyons comment l'activer.


Dans l'écran principal, sélectionnez le menu en haut à droite.


![image](assets/it/20.webp)


Sélectionnez ensuite _Point de vente_.


![image](assets/it/21.webp)


Avec la dernière version du WoS, veillez à sélectionner le _Keypad_.


![image](assets/it/22.webp)

puis tapez le montant sur le clavier, dans l'exemple qui suit égal à 10 cents / 118 Sats. Ajoutez une description pour la collection, dans ce cas "ma deuxième avec POS". Un grand bouton Green s'allume et doit être cliqué

![image](assets/it/23.webp)


pour generate le Invoice et le montrer, par exemple, à un client.


![image](assets/it/24.webp)


Ce paiement est également perçu !


![image](assets/it/25.webp)


### Envoi des paiements


La simplicité est une force de l'écran principal du WoS. Pour payer une Invoice, cliquez sur _Envoyer_


![image](assets/it/26.webp)


Lors de la première utilisation, le WoS demande l'autorisation d'accéder à la caméra


![image](assets/it/27.webp)


À partir de ce moment, l'appareil photo s'active


![image](assets/it/28.webp)


En encadrant la Invoice, nous voyons qu'un paiement de 210 Sats a été demandé. Une description est également lue, si le demandeur en a défini une. Cet écran est à la fois un résumé et une demande de confirmation : Le WoS "demande l'autorisation" d'envoyer le paiement, ce qui lui est accordé en cliquant sur le bouton Green _Send_


![image](assets/it/29.webp)


Lorsque le paiement arrive à destination, le WoS le notifie à l'aide de l'écran suivant


![image](assets/it/30.webp)


A partir de l'écran principal, en cliquant sur _History_ (juste en dessous du solde), la liste des transactions apparaît


![image](assets/it/31.webp)


#### Récupération du compte WoS


Nous allons maintenant voir comment installer le WoS sur un nouvel appareil ; cela sera également utile en cas de vol, de perte ou d'impossibilité d'utiliser le téléphone portable sur lequel le Wallet était précédemment installé. Une fois réinstallé, il faut refaire la procédure d'enregistrement du compte que nous venons d'expliquer, avec une seule variante : à la fin de la demande de connexion avec l'e-mail précédemment défini, WoS apparaîtra comme suit :


![image](assets/it/33.webp)


Un message nous avertit qu'un courriel a été envoyé avec la procédure de réactivation du compte. Vous devez ouvrir votre boîte de réception.


**IMPORTANT** : ouvrez l'e-mail à partir d'un PC ou, en tout cas, d'un appareil différent de celui sur lequel vous vous apprêtez à récupérer le compte WoS. Dans la boîte de réception, nous trouvons un message qui nous montre un code QR à encadrer


![image](assets/it/34.webp)


Une fois le code QR cadré, le compte récupéré apparaît sur la page principale du WoS, avec le solde et l'historique.