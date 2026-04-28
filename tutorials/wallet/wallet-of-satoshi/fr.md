---
name: Wallet of Satoshi
description: Le Wallet le plus simple pour démarrer
---
![cover](assets/cover.webp)

---

*Attention : depuis le début de l’année 2026, Wallet of Satoshi en mode custodial (tel que présenté dans ce tutoriel) n’est plus accessible au sein de l’Union européenne. Si vous résidez dans cette zone et souhaitez continuer à utiliser cet outil, vous devrez passer par un VPN situé hors de l’UE. Une autre option consiste à utiliser Wallet of Satoshi en mode self-custodial. Un tutoriel dédié sera prochainement publié sur Plan ₿ Academy.*

---

Ce tutoriel a été rédigé par [Bitcoin Campus](https://linktr.ee/bitcoincampus_).

## Téléchargement, configuration et utilisation de Wallet of Satoshi


Wallet of Satoshi est un portefeuille Lightning, de garde, et très simple d'utilisation.

Dans le cadre du cours [BTC105 - Finding Now](https://planb.academy/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), il est utilisé pour les bons Redeem Lightning Network.


**N'oubliez jamais :** ***not your keys, not your coins*** (_pas vos clés, pas vos pièces_).


Les portefeuilles de dépôt ne permettent pas aux utilisateurs d'exercer un contrôle total sur leurs fonds. Ils ne sont normalement pas recommandés, sauf pour les débutants. WoS doit être utilisé comme un portefeuille transitoire ou pour conserver de l'argent de poche, et non pour accumuler des fonds à long terme.


---

Wallet of Satoshi (WoS) est un produit de garde, mais il jouit d'une certaine réputation. Nous pouvons raisonnablement nous tourner vers un outil comme WoS, par exemple, pour augmenter notre capacité à recevoir des liquidités. Nous déléguons temporairement à WoS le "sale boulot" qui consiste à gérer la liquidité des canaux pour nous. Lorsqu'un certain montant est atteint, nous envoyons les sats de WoS vers une adresse on-chain de notre portefeuille non dépositaire (*non-custodial*).


**WARNING⚠️ : Il est recommandé de lire le tutoriel dans son intégralité avant de poursuivre.**


### Téléchargement de Wallet of Satoshi


Allez sur le Play Store et téléchargez WoS.


![image](assets/it/01.webp)


**Note :** WoS n'est à télécharger qu'à partir des magasins officiels. Si le système d'exploitation de l'appareil est programmé, l'ouverture de WoS est précédée d'une vérification par le système d'exploitation lui-même. Après la phase de vérification, choisissez _Ouvrir_.


![image](assets/it/02.webp)


Wallet of Satoshi s'ouvre avec l'écran suivant, cliquez sur _Début_.


![image](assets/it/03.webp)


### Création d'un compte sur Wallet of Satoshi


À ce stade, le portefeuille est déjà opérationnel, mais pour plus de sécurité, nous procédons à la configuration d'un compte : il sera nécessaire pour récupérer les fonds en cas de dysfonctionnement ou de perte de l'appareil. Sélectionnez le menu en haut à gauche.


![image](assets/it/04.webp)


Toute la fenêtre de menu s'ouvre, dans laquelle vous devez exclusivement définir la devise (Wallet of Satoshi présente par défaut le dollar US comme devise de référence) et la couleur du thème (clair/foncé), selon votre goût. N'utilisez pas les autres commandes.


WoS étant un outil de conservation, nous ne pouvons pas sauvegarder le portefeuille avec la phrase Mnemonic, mais nous pouvons permettre à WoS de récupérer nos fonds, en cas de perte ou de non-utilisation de l'appareil mobile, en cliquant sur _Connexion / Enregistrement_.

Une fenêtre apparaît nous demandant d'entrer une adresse email. Il peut s'agir d'un **mail Proton** (recommandé), mais il doit être fonctionnel, car il nous permettra de récupérer les fonds du portefeuille en cas de perte/vol ou d'endommagement du téléphone portable.


![image](assets/it/08.webp)


Wallet of Satoshi a envoyé un message à la boîte mail indiquée.


![image](assets/it/09.webp)


Dans la boîte mail, nous trouverons deux mots, que nous devrons saisir, en les réécrivant, dans l'espace fourni par l'application.


- Ne pas activer le traducteur : les mots sont et doivent rester en anglais.
- Réécrire les deux mots en respectant les majuscules et les minuscules.


![image](assets/it/10.webp)


Après avoir transcrit les deux mots, cliquez sur _OK_.


![image](assets/it/11.webp)


Le symbole de la coche devrait apparaître en haut à droite pour indiquer que la vérification est réussie.


![image](assets/it/12.webp)


Dans la section des paramètres, la barre rouge _Connexion / Enregistrement_ affiche désormais l'adresse email de l'utilisateur.


![image](assets/it/13.webp)


### Réception des paiements


Pour obtenir des fonds sur WoS cliquez sur _Recevoir_, une série de commandes apparaîtra.


![image](assets/it/14.webp)


Vous pouvez recevoir :


- Via LN-Address (**a**) ;
- Via LN, en réglant les paramètres de l'invoice (**b**) ;
- On-chain, WoS supporte le réseau Bitcoin mais avec des échanges sous-marins payants (*submarine swap*) (**c**) ;
- En scannant le QR code d'un LNurl-p (**d**).


![image](assets/it/15.webp)


### Création d'une invoice


Cliquez sur _Recevoir_ et choisissez la commande avec le symbole "Lightning Network".


![image](assets/it/16.webp)


Le menu de création de l'invoice s'affiche. Cliquez sur _Montant / Remarque_ pour saisir le montant exact et ajouter une description, dans cet exemple, "my first invoice".


![image](assets/it/17.webp)


Avec le clavier nous indiquons le montant, pour ensuite recevoir le paiement de l'invoice.


![image](assets/it/18.webp)


Le paiement reçu se présente comme suit :


![image](assets/it/19.webp)


### Collecte depuis le Point De Vente


Wallet of Satoshi possède une caractéristique par défaut qui le rend particulièrement adapté aux commerçants : le point de vente. Voyons comment l'activer.


Dans l'écran principal, sélectionnez le menu en haut à droite.


![image](assets/it/20.webp)


Sélectionnez ensuite _Point de vente_.


![image](assets/it/21.webp)


Avec la dernière version de WoS, veillez à sélectionner le _Clavier_.


![image](assets/it/22.webp)

Puis saisissez le montant sur le clavier, dans l'exemple suivant, il est égal à 10 cents / 118 Sats. Ajoutez une description pour l'encaissement, dans ce cas "my second with POS". Un grand bouton vert s'allume, sur lequel il faut cliquer pour générer l'invoice.

![image](assets/it/23.webp)

Vous pouvez ensuite la montrer, par exemple, à un client.


![image](assets/it/24.webp)


Ce paiement est également reçu !


![image](assets/it/25.webp)


### Envoi des paiements


La simplicité est une force de l'écran principal de WoS. Pour payer une invoice, cliquez sur _Envoyer_.


![image](assets/it/26.webp)


Lors de la première utilisation, WoS demande l'autorisation d'accéder à la caméra.


![image](assets/it/27.webp)


À partir de ce moment, l'appareil photo s'active.


![image](assets/it/28.webp)


En scannant l'invoice, nous voyons qu'un paiement de 210 Sats a été demandé. Une description est également affichée, si le demandeur en a défini une. Cet écran est à la fois un résumé et une demande de confirmation : WoS "demande l'autorisation" d'envoyer le paiement, ce qui lui est accordé en cliquant sur le bouton vert _Envoyer_.


![image](assets/it/29.webp)


Lorsque le paiement arrive à destination, WoS le notifie comme indiqué sur l'écran suivant.


![image](assets/it/30.webp)


À partir de l'écran principal, en cliquant sur _Historique de paiement_ (juste en dessous du solde), la liste des transactions apparaît.


![image](assets/it/31.webp)


#### Récupération du compte WoS


Nous allons maintenant voir comment installer WoS sur un nouvel appareil ; cela sera également utile en cas de vol, de perte ou d'impossibilité d'utiliser le téléphone portable sur lequel le portefeuille était précédemment installé. Une fois réinstallé, il faut refaire la procédure d'enregistrement du compte que nous venons d'expliquer, avec une seule variante : à la fin de la demande de connexion avec l'e-mail précédemment défini, WoS apparaîtra comme suit :


![image](assets/it/33.webp)


Un message nous avertit qu'un courriel a été envoyé avec la procédure de réactivation du compte. Vous devez ouvrir votre boîte de réception.


**IMPORTANT** : ouvrez l'email à partir d'un PC ou, en tout cas, d'un appareil différent de celui sur lequel vous vous apprêtez à récupérer le compte WoS. Dans la boîte de réception, nous trouvons un message qui nous montre un QR code à encadrer.


![image](assets/it/34.webp)


Une fois le QR code scanné, le compte récupéré apparaît sur la page principale de WoS, avec le solde et l'historique.
