---
name: Sats.mobi

description: Un gardien accessible par télégramme Wallet
---

![cover](assets/cover.webp)


ce tutoriel a été rédigé par_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi est un Wallet qui fonctionne sur Telegram, avec toutes les fonctionnalités d'un Lightning Network (custodial) Wallet, plus une série de fonctionnalités très divertissantes. Il est issu d'un Fork du LightningTipBot, aujourd'hui abandonné, dont il a hérité de toutes les fonctionnalités tout en y ajoutant d'autres plus récentes, ce qui le rend plus moderne. Comme LNTipBot, Sats.Mobi adhère également à la philosophie de l'open-source. Le Wallet peut être configuré et géré indépendamment en le clonant à partir de ce [dépôt] (https://github.com/massmux/SatsMobiBot).


Si vous préférez l'utiliser simplement, démarrer une discussion sur Telegram révélera qu'il s'agit d'un robot.


## Paramètres

Dans la barre de recherche de Telegram, cherchez "satsmobi" et le lien vers le [bot] (@SatsMobiBot) apparaîtra.


**Attention** : Si vous n'êtes pas sûr de pouvoir effectuer une recherche via Telegram, accédez au bot en toute sécurité en utilisant le [lien] suivant (https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Pour commencer, il vous suffit d'appuyer sur _START_


![image](assets/it/02.webp)


Pour explorer le Wallet, vous pouvez sélectionner _Menu_ en bas à gauche.


![image](assets/it/03.webp)


Choisissez maintenant _/help_ parmi les commandes principales.


![image](assets/it/04.webp)


Sats.Mobi nous accueille en affichant un message, énumérant toutes les principales fonctionnalités. Au démarrage, le bot a également créé un LN Address, lié à l'identifiant choisi sur Telegram (qui est unique par défaut). Les commandes d'envoi et de réception de Sats avec ce Wallet sont visibles, ainsi que d'autres fonctions que nous verrons plus tard. Il est intéressant de jeter un coup d'œil au menu _/avancé_


![image](assets/it/05.webp)


Il est à noter que Sats.Mobi a également créé un LN Address anonyme, à utiliser pour gagner en confidentialité. Le bot fonctionne avec des commandes : il suffit de cliquer sur le mot correspondant ou de taper la barre oblique "/" dans la barre de message, suivie de la commande à exécuter. Même si le Wallet vient d'être créé, choisissez par exemple _/transactions_


![image](assets/it/06.webp)


Cette commande affiche la liste des dernières transactions, dans ce cas précis égale à zéro.


![image](assets/it/07.webp)


## Réception Sats

La commande pour créer une Invoice et recevoir une Sats est _/invoice_. Sats.Mobi fonctionne exclusivement en Satoshi, la plus petite unité de Bitcoin ; par conséquent, pour créer la Invoice, il faut écrire le montant en Sats dans la barre de message et l'envoyer ensuite dans le chat avec le bot.

![image](assets/it/08.webp)


Dans l'exemple suivant, on a choisi de recevoir un montant de 210 Sats.


![cover](assets/it/09.webp)


Après quelques instants d'attente, la Invoice est disponible sous forme de texte et de code QR. En payant la Invoice, la Wallet affiche le solde. Si, pour une raison quelconque, le total n'est pas mis à jour, écrivez _/balance_ et appuyez sur la touche `enter`.


![image](assets/it/10.webp)


## Envoi de Sats


Bien que les Sats soient un bien extrêmement précieux, dont on ne devrait pas se séparer à la légère, Sats.Mobi rend cette partie attrayante, effectuer quelques brefs tests (c.-à-d. quelques transactions d'essai) ne posera pas de problème.


### Paiement d'une Invoice


La manière la plus simple de payer une Invoice est de copier la chaîne de messages `lnbc1xxxxx` et de la coller dans la barre de messages après avoir tapé la commande _/pay_. **La syntaxe correcte** exige de laisser un espace après la commande.


![image](assets/it/11.webp)


La Wallet envoie un message de demande de confirmation. En cliquant sur _Pay_, la Invoice est payée.


![image](assets/it/12.webp)


Sats.Mobi peut compter sur un nœud Lightning efficace et bien connecté, les paiements échouent rarement car il parvient toujours à trouver le bon itinéraire.


### Payer confortablement à partir d'un téléphone portable


Naviguant sur Telegram, Sats.Mobi est également disponible sur mobile. La fonction la plus pratique pour payer avec un téléphone portable est de scanner un code QR, mais ce Wallet en est dépourvu de par sa conception, puisqu'il ne s'agit pas d'une application autonome, mais d'un réseau social. Sats.Mobi est donc programmé pour faciliter au maximum l'expérience mobile : il peut en effet décoder une image, comme une photo prise du code QR de la Invoice que vous voulez payer.


Supposons, par exemple, que vous souhaitiez payer une Invoice de 50 Sats.


![image](assets/it/20.webp)


Lorsque cela nous est montré, nous pouvons prendre une photo du code QR correspondant.


![image](assets/it/21.webp)


Nous ouvrons ensuite Telegram sur le mobile et, dans le chat avec Sats.Mobi, nous joignons la photo du code QR qui vient d'être prise


![cover](assets/it/22.webp)


Une fois sélectionné, nous l'envoyons au robot :


![image](assets/it/23.webp)

Sats.Mobi décode la photo et **présentera immédiatement la demande de paiement**, avec la description correcte. Le chat demande une confirmation, pour continuer il faut appuyer sur _/pay_

![image](assets/it/24.webp)


Veuillez patienter quelques instants pour permettre le traitement du paiement.


![image](assets/it/25.webp)


Le Invoice pour 50 Sats a été payé, un résultat obtenu sans l'utilisation d'une caméra et de sa fonction de balayage intégrée.


### Sats.Mobi dans Telegram Groups


![image](assets/it/27.webp)


Parmi les fonctionnalités qui ont rendu LNTipBot célèbre et que Sats.Mobi apporte à Telegram, il y a celle qui rend l'expérience amusante et interactive pour les membres d'un groupe.

Les propriétaires peuvent inviter le robot à rejoindre le groupe de discussion, puis désigner Sats.Mobi comme administrateur. À partir de ce moment, le plaisir commence, car les membres peuvent commencer à récompenser d'autres utilisateurs pour leur contribution au groupe.


- _/tip_ ajoute un conseil en répondant à un message ;
- _/send_ envoie des fonds en spécifiant une LN Address ou une poignée Telegram comme destinataire ;
- _/faucet_ (dans le menu _/avancé_) permet de créer une série de conseils que les membres les plus rapides du groupe peuvent collecter en cliquant sur _/collect_ ;
- l'option _/tipjar_ (dans le menu _/avancé_) permet de créer un autre type de distribution qui peut être envoyé aux utilisateurs du groupe.


Chacune de ces commandes a sa syntaxe, qui est expliquée dans le menu principal des commandes.


Et si nous ne sommes pas le propriétaire d'un groupe ? Pas de problème : il suffit de demander au fondateur d'inviter Sats.Mobi, de l'ajouter en tant qu'administrateur du groupe, et le tour est joué !


## Point de vente (POS)


Lorsque Sats.Mobi est lancé pour la première fois, le robot crée également une autre fonction pour l'utilisateur : **le POS**. Le "dispositif" est activé par l'utilisateur avec la commande _/pos_ ou en cliquant sur le bouton correspondant dans la console en bas à droite. En fait, le POS est une application web qui s'ouvre comme une fenêtre contextuelle sur le chat Telegram


![image](assets/it/14.webp)


Le Interface affiche la poignée Telegram personnelle de l'utilisateur en haut à gauche et s'utilise simplement comme tous les TPV : en tapant le montant sur le clavier. Supposons maintenant que nous voulions collecter 21 centimes d'euro pour un service. Sachant que Sats.Mobi ne gère nativement que le Sats, il n'est pas facile de faire la conversion dans sa tête. Par contre, le TPV affiche l'euro comme unité de compte, en affichant en même temps l'équivalent en Satoshi.


![image](assets/it/15.webp)

En cliquant sur _/OK_, la Invoice s'affiche et peut être montrée au client via un code QR ou envoyée sous forme de chaîne de caractères par messagerie instantanée, afin qu'elle puisse être payée.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Bien entendu, le TPV est également disponible sur les téléphones mobiles, accessibles de la même manière que précédemment.


![image](assets/it/18.webp)


Il est également bien affiché sur l'écran du téléphone portable :


![image](assets/it/19.webp)


## Caractéristiques supplémentaires


D'autres caractéristiques complètent l'offre du Sats.Mobi Wallet qui, comme nous l'avons vu, élargit le concept du Wallet au-delà des opérations de réception et d'envoi de paiements :


- _/nostr_ : pour connecter le Wallet à votre propre utilisateur Nostr afin de recevoir des zaps ;
- _/cashback_ : montre un code qui peut être présenté à un commerçant pour obtenir une remise en argent sur un achat ;
- buy_ : lance une procédure guidée au sein du bot, qui permet d'acheter des Sats pour des euros ;
- activatecard_ : pour demander l'activation d'une carte de débit NFC, rechargeable via le Sats.Mobi Wallet et pour laquelle des notifications peuvent être activées ;
- _/link_ : crée un lien vers votre propre Zeus ou Blue Wallet, qui peuvent être utilisés comme télécommandes pour ce Wallet.


## Conclusion

Sats.Mobi est un Wallet agréable et amusant à utiliser, qui rappelle les expériences vécues avec LNTipBot en utilisant les fonctions plus avancées de LNBits. Cependant, il est important de se rappeler qu'il s'agit d'un **service de garde**. Par conséquent, il doit être utilisé pour détenir très peu de Sats, ce n'est pas un Wallet principal pour vos fonds Lightning Network. Il existe également une limite de capacité intrinsèque, égale à 500 000 Sats, limite qu'il est conseillé de ne pas dépasser.


Si vous êtes à la recherche de portefeuilles Lightning Network non gardiens, nous vous conseillons de vous tourner vers d'autres produits.


---
### Documentation


- [Github] (https://github.com/massmux/SatsMobiBot)
- Playlist de [vidéos](https://www.youtube.com/results?search_query=Sats.mobi) demo