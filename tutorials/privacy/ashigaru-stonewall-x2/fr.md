---
name: Ashigaru - Stonewall x2
description: Comprendre et utiliser les transactions Stonewall x2 sur Ashigaru
---
![cover stonewall x2](assets/cover.webp)

> *Make every spend a coinjoin.*

## C'est quoi une transaction Stonewall x2 ?

Stonewall x2 est une forme spécifique de transaction Bitcoin visant à accroître la confidentialité des utilisateurs lors d'une dépense, par la collaboration avec une tierce personne non impliquée dans cette dépense. Cette méthode simule un mini-coinjoin entre deux participants, tout en effectuant un paiement à une troisième partie. Les transactions Stonewall x2 sont disponibles sur l’application Ashigaru, un fork de Samourai Wallet (l’équipe à l’origine de la création de ce type de transaction).

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Son fonctionnement est relativement simple : on utilise un UTXO en notre possession pour effectuer le paiement et on sollicite l'aide d'une tierce personne qui contribue également avec un UTXO lui appartenant. La transaction se solde avec quatre outputs : deux d'entre eux de montants égaux, l'un destiné à l'adresse du bénéficiaire du paiement, l'autre à une adresse appartenant au collaborateur. Un troisième UTXO est renvoyé à une autre adresse du collaborateur, lui permettant de récupérer le montant initial (une action neutre pour lui, modulo les frais de minage), et un dernier UTXO revient à une adresse nous appartenant, qui constitue le change du paiement.

On définit ainsi trois rôles différents dans les transactions Stonewall x2 :
- L'émetteur, qui réalise le paiement effectif ;
- Le collaborateur, qui met des bitcoins à disposition afin d'améliorer l'ensemble d'anonymat de la transaction, tout en récupérant intégralement ses fonds à la fin (une action neutre pour lui, modulo les frais de minage) ;
- Le destinataire, qui peut ignorer la nature spécifique de la transaction et attend simplement un paiement de la part de l'émetteur.

Prenons un exemple pour bien comprendre. Alice est chez le boulanger pour acheter sa baguette de pain qui coûte `4 000 sats`. Elle souhaite payer en bitcoins tout en conservant une certaine forme de confidentialité sur son paiement. Elle fait donc appel à son ami Bob, qui va l'aider dans cette démarche.

![image](assets/fr/01.webp)

En analysant cette transaction, on peut voir que le boulanger a effectivement reçu `4 000 sats` en paiement pour la baguette. Alice a utilisé `10 000 sats` en input et a récupéré `6 000 sats` en output, soit un solde net de `-4 000 sats`, ce qui correspond au prix de la baguette. Quant à Bob, il a fourni `15 000 sats` en input et a reçu deux outputs : l'un de `4 000 sats` et l'autre de `11 000 sats`, ce qui fait bien un solde de `0`. 

Dans cet exemple, j'ai intentionnellement négligé les frais de minage afin de faciliter la compréhension. En réalité, les frais de transaction sont partagés à parts égales entre l'émetteur du paiement et le collaborateur.

## Quelle est la différence entre Stonewall et Stonewall x2 ?

Une transaction StonewallX2 fonctionne exactement comme une transaction Stonewall, à la différence près que la première est collaborative, alors que la seconde non. Comme nous l'avons vu, une transaction Stonewall x2 implique la participation d'une tierce personne, qui est extérieure au paiement, et qui va mettre à disposition ses bitcoins pour améliorer la confidentialité de la transaction. Dans une transaction Stonewall classique, le rôle du collaborateur est pris par l'émetteur. 

Reprenons notre exemple d'Alice à la boulangerie. Si elle n'avait pas pu trouver une personne comme Bob pour l'accompagner dans sa dépense, elle aurait pu faire un Stonewall toute seule. Ainsi, les deux UTXO en entrée auraient été les siens, et elle en aurait récupéré 3 à la sortie.

![image](assets/fr/02.webp)


D'un point de vue extérieur, le paterne de la transaction serait resté le même.

![image](assets/fr/05.webp)

La logique devrait donc être la suivante lorsque l'on souhaite utiliser un outil de dépense Ashigaru :
- Si le commerçant ne prend pas en charge les Payjoin Stowaway, on peut faire une transaction collaborative avec une autre personne extérieure au paiement grâce aux Stonewall x2 ;
- Si l'on ne trouve personne pour faire une transaction Stonewall x2, on peut faire une transaction Stonewall seul, qui va mimer le comportement d'une transaction Stonewall x2.

https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Quelle est l'utilité d'une transaction Stonewall x2 ?

La structure Stonewall x2 ajoute énormément d'entropie à la transaction et vient brouiller les pistes de l'analyse de chaîne. Vue de l'extérieur, une telle transaction peut être interprétée comme un petit Coinjoin entre deux personnes. Mais en réalité, il s'agit d'un paiement. Cette méthode génère donc des incertitudes dans l'analyse de chaîne, voire oriente vers de fausses pistes.

Reprenons l'exemple d'Alice, Bob et le Boulanger. La transaction sur la blockchain se présenterait ainsi :

![image](assets/fr/03.webp)

Un observateur extérieur qui s'appuie sur les heuristiques courantes d'analyse de chaîne pourrait conclure à tort que "*Alice et Bob ont réalisé un petit coinjoin, avec un UTXO chacun en entrée et deux UTXO chacun en sortie*".

![image](assets/fr/04.webp)

Cette interprétation est inexacte, car, comme vous le savez, un UTXO a été envoyé au Boulanger, Alice n'a qu'un output de change, et Bob en a deux.

![image](assets/fr/01.webp)

Même si l'observateur extérieur parvient à identifier le paterne de la transaction Stonewall x2, il ne disposera pas de toutes les informations. Il ne pourra pas déterminer lequel des deux UTXO de mêmes montants correspond au paiement. De plus, il ne sera pas en mesure de savoir si c'est Alice ou Bob qui a effectué le paiement. Enfin, il ne pourra pas déterminer si les deux UTXO en entrée proviennent de deux personnes différentes ou s'ils appartiennent à une seule personne qui les a fusionnés. Ce dernier point est dû au fait que les transactions Stonewall classiques, dont nous avons parlé au-dessus, suivent exactement le même paterne que les transactions Stonewall x2. Vu de l'extérieur et sans informations supplémentaires sur le contexte, il est impossible de différencier une transaction Stonewall d'une transaction Stonewall x2. Or, les premières ne sont pas des transactions collaboratives, alors que les secondes le sont. Cela permet d'ajouter encore plus de doutes sur cette dépense.

![image](assets/fr/05.webp)


## Comment établir une connexion entre Paynyms ?

Comme pour les autres transactions collaboratives sur Ashigaru (*Cahoots*), la réalisation d'un Stonewall x2 implique l'échange de transactions partiellement signées entre l'émetteur et le collaborateur. Cet échange peut s'effectuer manuellement, dans le cas où vous vous trouvez physiquement avec votre collaborateur, ou automatiquement grâce au protocole de communication Soroban.

Si vous choisissez la seconde option, vous allez devoir établir une connexion entre Paynyms avant de pouvoir effectuer un Stonewall x2. Pour ce faire, votre Paynym doit "*follow*" le Paynym de votre collaborateur, et vice-versa. Pour savoir comment faire, vous pouvez suivre le début de cet autre tutoriel :

https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Comment faire une transaction Stonewall x2 sur Ashigaru ?

Pour effectuer une transaction Stonewall x2, cliquez sur l’image de votre Paynym en haut à gauche de l’écran, puis ouvrez le menu `Collaborate`. La personne qui participe avec vous à cette transaction doit faire la même manipulation, sauf si vous réalisez l’échange de QR codes en personne.

![Image](assets/fr/06.webp)

Deux options s’offrent à vous : sélectionnez `Initiate` si vous êtes l’émetteur du paiement, ou `Participate` si vous êtes la personne qui collabore à la transaction sans en être ni le payeur, ni le destinataire effectif.

![Image](assets/fr/07.webp)

Si vous avez le rôle du collaborateur, la procédure est très simple. Pour une collaboration à distance via le réseau Soroban, cliquez sur `Participate`, choisissez le compte que vous souhaitez utiliser, puis appuyez sur `LISTEN FOR CAHOOTS REQUESTS` afin d’attendre la requête envoyée par le payeur.

![Image](assets/fr/08.webp)

En revanche, pour une collaboration en personne via le scan de QR codes, rendez-vous sur la page d’accueil de votre wallet, appuyez sur l’icône du QR code en haut de l’écran, puis scannez le QR code fourni par le payeur qui initie la transaction.

![Image](assets/fr/09.webp)

Si vous êtes dans le rôle du payeur, c’est-à-dire celui qui initie la transaction, rendez-vous dans le menu `Collaborate`, puis sélectionnez `Initiate`.

![Image](assets/fr/10.webp)

Pour le type de transaction, puisque l'on souhaite ici effectuer un Stonewall x2, choisissez cette option.

![Image](assets/fr/11.webp)

Vous pouvez ensuite choisir entre une collaboration en ligne (*Cahoots* via *Soroban*) ou une collaboration en personne, avec les échanges de QR codes.

![Image](assets/fr/12.webp)

### Cahoots en ligne

Si vous avez opté pour l’option `Online`, sélectionnez ensuite votre collaborateur parmi les Paynyms que vous suivez.

![Image](assets/fr/13.webp)

Cliquez sur `Set up transaction`, puis choisissez le compte à partir duquel vous souhaitez effectuer la dépense.

![Image](assets/fr/14.webp)

Sur la page suivante, renseignez les détails de la transaction : l’adresse du destinataire réel du paiement, le montant à lui envoyer et le taux de frais. Cliquez ensuite sur `Review transaction setup`.

![Image](assets/fr/15.webp)

Vérifiez attentivement les informations, assurez-vous que votre collaborateur est bien en train d’écouter les requêtes de *Cahoots*, puis cliquez sur le bouton vert `BEGIN TRANSACTION` pour initier l’échange des PSBTs via Soroban.

![Image](assets/fr/16.webp)

Patientez jusqu’à la signature complète de la transaction par les deux participants, puis diffusez-la sur le réseau Bitcoin.

![Image](assets/fr/17.webp)

### Échanges en personne

Si vous souhaitez effectuer l’échange en personne, sélectionnez le type de transaction `STONEWALL X2`, puis choisissez l’option `In Person / Manual`.

![Image](assets/fr/18.webp)

Cliquez sur `Set up transaction`, puis choisissez le compte à partir duquel vous souhaitez effectuer la dépense.

![Image](assets/fr/19.webp)

Sur la page suivante, renseignez les détails de la transaction : l’adresse du destinataire réel du paiement, le montant à lui envoyer et le taux de frais. Cliquez ensuite sur `Review transaction setup`.

![Image](assets/fr/20.webp)

Vérifiez les détails, puis appuyez sur le bouton vert `BEGIN TRANSACTION` pour lancer l’échange des PSBTs via le scan de QR codes.

![Image](assets/fr/21.webp)

L’échange se fait en alternant le scan avec le collaborateur : cliquez sur `SHOW QR CODE` pour afficher votre QR code à votre collaborateur, qui le scannera. Ensuite, il affichera à son tour le sien en cliquant sur `SHOW QR CODE`, et vous devrez le scanner avec `LAUNCH QR Scanner`. Puis répétez ce processus jusqu’à ce que les cinq étapes de l’échange soient complètes.

![Image](assets/fr/22.webp)

Une fois tous les échanges effectués, vérifiez les détails de la transaction, puis diffusez-la en faisant glisser la flèche verte située en bas de l’écran.

![Image](assets/fr/23.webp)

[La transaction a bien été diffusée](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Sa structure se présente ainsi :

![Image](assets/fr/24.webp)

*Crédit: [mempool.space](https://mempool.space/)*

On peut observer deux inputs provenant de mon portefeuille, respectivement `91 869 sats` et `64 823 sats`, tandis que les deux autres inputs proviennent du wallet de mon collaborateur. Du côté des outputs, un UTXO de `100 000 sats` est envoyé au destinataire effectif du paiement et deux UTXOs de `100 000 sats` et `159 578 sats` retournent vers le portefeuille de mon collaborateur. Pour lui, l’opération est neutre, puisqu’il récupère l’intégralité des fonds qu’il avait placés en input (hors frais de minage auxquels il a contribué). Enfin, de mon côté je reçois un UTXO de change de `56 270 sats`, correspondant à la différence entre le total de mes inputs et le paiement de `100 000 sats` envoyé au destinataire.

Évidemment, je peux décrire cette structure car j’ai moi-même construit la transaction. Mais pour un observateur extérieur, il est généralement impossible de déterminer quels UTXOs appartiennent à quel participant, que ce soit en inputs ou en outputs.

Pour approfondir vos connaissances sur la gestion de la confidentialité onchain sur Bitcoin, je vous recommande de suivre ma formation BTC 204 sur Plan ₿ Academy :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
