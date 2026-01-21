---
name: Ashigaru - Stowaway
description: Comment faire une transaction Payjoin sur Ashigaru ?
---
![cover](assets/cover.webp)

> *Force blockchain spies to rethink everything they think they know.*

Le Payjoin est une structure de transaction Bitcoin conçue pour renforcer la confidentialité des utilisateurs en impliquant une collaboration directe avec le destinataire du paiement. Plusieurs implémentations existent afin de faciliter sa mise en œuvre et d’automatiser le processus. Parmi elles, la plus connue reste sans doute Stowaway, initialement développée par l’équipe de Samourai Wallet et aujourd’hui intégrée dans son fork Ashigaru.

## Comment fonctionne Stowaway ?

Comme mentionné précédemment, Ashigaru intègre un outil de PayJoin appelé `Stowaway`. Celui-ci est disponible dans l’application Ashigaru sur Android. Pour qu’un Payjoin puisse être réalisé, le destinataire (qui endosse également le rôle de collaborateur) doit utiliser un logiciel compatible avec Stowaway, c’est-à-dire seulement Ashigaru pour le moment.

Stowaway repose sur une catégorie de transactions que Samourai désignait sous le nom de "*Cahoots*". Un Cahoot est une transaction collaborative entre plusieurs utilisateurs, impliquant un échange d’informations en dehors de la blockchain Bitcoin. À l’heure actuelle, Ashigaru propose deux outils de Cahoots : Stowaway (les Payjoins) et StonewallX2.

https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Les transactions Cahoots nécessitent un échange de transactions partiellement signées entre les utilisateurs. Ce processus peut être long et fastidieux, surtout lorsqu’il est réalisé à distance. Il reste toutefois possible de le faire manuellement si les collaborateurs se trouvent au même endroit. Concrètement, cela implique de scanner successivement cinq codes QR échangés entre les deux participants.

À distance, cette méthode devient trop complexe. Pour y remédier, Samourai a développé un protocole de communication chiffré reposant sur Tor, nommé "*Soroban*". Grâce à Soroban, les échanges indispensables à un Payjoin sont automatisés et s’effectuent en arrière-plan.

Ces communications chiffrées nécessitent d’établir une connexion et une authentification entre les participants au Cahoot. C’est pourquoi Soroban s’appuie sur les Paynyms des utilisateurs. Si vous ne maîtrisez pas encore le fonctionnement des Paynyms, je vous invite à consulter ce tutoriel dédié pour en apprendre davantage :

https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Pour résumer, un Paynym est un identifiant unique associé à votre portefeuille, permettant d’activer différentes fonctionnalités, notamment des échanges chiffrés. Il se matérialise sous la forme d’un identifiant accompagné d’une illustration. Voici, par exemple, celui que j’utilise sur le Testnet :

![Image](assets/fr/01.webp)

**Pour résumer :**

- `Payjoin` = Structure spécifique de transaction collaborative ;

- `Stowaway` = Implémentation de Payjoin disponible sur Ashigaru ;

- `Cahoots` = Nom donné par Samourai à tous leurs types de transactions collaboratives, notamment les Payjoin `Stowaway`, repris aujourd'hui sur Ashigaru ;

- `Soroban` = Protocole de communication chiffré établi sur Tor permettant de collaborer avec d'autres utilisateurs dans le cadre d'une transaction `Cahoots` ;

- `Paynym` = Identifiant unique d'un portefeuille permettant d'établir une communication avec un autre utilisateur sur `Soroban`, en vue d'effectuer une transaction `Cahoots`.

Pour approfondir le fonctionnement des Payjoins et leur utilité en matière de confidentialité onchain, je vous recommande de consulter cet autre tutoriel :

https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Comment établir une connexion entre Paynyms ?

Pour commencer, vous devrez bien entendu installer Ashigaru et y créer un portefeuille :

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Pour effectuer une transaction Cahoots à distance, notamment un PayJoin (*Stowaway*) via Ashigaru, vous devez d’abord “follow” l’utilisateur avec lequel vous souhaitez collaborer, en utilisant son Paynym. Dans le cadre d’un Stowaway, cela signifie suivre la personne à qui vous souhaitez envoyer des bitcoins. Si vous ne savez pas encore comment suivre un autre Paynym, vous trouverez la procédure détaillée dans ce tutoriel :

https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Comment faire un Payjoin sur Ashigaru ?

Pour effectuer une transaction Stowaway, cliquez sur l’image de votre Paynym en haut à gauche de l’écran, puis ouvrez le menu `Collaborate`. La personne qui participe avec vous à cette transaction doit faire la même manipulation, sauf si vous réalisez l’échange de QR codes en personne.

![Image](assets/fr/02.webp)

Deux options s’offrent à vous: sélectionnez `Initiate` si vous êtes l’émetteur du paiement, ou `Participate` si vous êtes le destinataire du paiement de ce payjoin.

![Image](assets/fr/03.webp)

Si vous avez le rôle du destinataire, la procédure est très simple. Pour une collaboration à distance via le réseau Soroban, cliquez sur `Participate`, choisissez le compte que vous souhaitez utiliser, puis appuyez sur `LISTEN FOR CAHOOTS REQUESTS` afin d’attendre la requête envoyée par le payeur.

![Image](assets/fr/04.webp)

En revanche, pour une collaboration en personne via le scan de QR codes, rendez-vous sur la page d’accueil de votre wallet, appuyez sur l’icône du QR code en haut de l’écran, puis scannez le QR code fourni par le payeur qui initie la transaction.

![Image](assets/fr/05.webp)

Si vous êtes dans le rôle du payeur, c’est-à-dire celui qui initie la transaction, rendez-vous dans le menu `Collaborate`, puis sélectionnez `Initiate`.

![Image](assets/fr/06.webp)

Pour le type de transaction, puisque l'on souhaite ici effectuer un Payjoin Stowaway, choisissez cette option.

![Image](assets/fr/07.webp)

Vous pouvez ensuite choisir entre une collaboration en ligne (*Cahoots* via *Soroban*) ou une collaboration en personne, avec les échanges de QR codes.

![Image](assets/fr/08.webp)

### Cahoots en ligne

Si vous avez opté pour l’option `Online`, sélectionnez ensuite le destinataire parmi les Paynyms que vous suivez.

![Image](assets/fr/09.webp)

Cliquez sur `Set up transaction`, puis choisissez le compte à partir duquel vous souhaitez effectuer la dépense.

![Image](assets/fr/10.webp)

Sur la page suivante, renseignez les détails de la transaction: le montant à envoyer au destinataire et le taux de frais. Pas besoin de renseigner d'adresse de réception, puisque c'est le destinataire lui-même qui la transmettra lors des échanges de PSBT.

Cliquez ensuite sur `Review transaction setup`.

![Image](assets/fr/11.webp)

Vérifiez attentivement les informations, assurez-vous que votre collaborateur est bien en train d’écouter les requêtes de *Cahoots*, puis cliquez sur le bouton vert `BEGIN TRANSACTION` pour initier l’échange des PSBTs via Soroban.

![Image](assets/fr/12.webp)

Patientez jusqu’à la signature complète de la transaction par les deux participants, puis diffusez-la sur le réseau Bitcoin.

![Image](assets/fr/13.webp)

### Échanges en personne

Si vous souhaitez effectuer l’échange en personne, sélectionnez le type de transaction `STONEWALL X2`, puis choisissez l’option `In Person / Manual`.

![Image](assets/fr/14.webp)

Cliquez sur `Set up transaction`, puis choisissez le compte à partir duquel vous souhaitez effectuer la dépense.

![Image](assets/fr/15.webp)

Sur la page suivante, renseignez les détails de la transaction: le montant à envoyer au destinataire et le taux de frais. Pas besoin de renseigner d'adresse de réception, puisque c'est le destinataire lui-même qui la transmettra lors des échanges de PSBT.

Cliquez ensuite sur `Review transaction setup`.

![Image](assets/fr/16.webp)

Vérifiez les détails, puis appuyez sur le bouton vert `BEGIN TRANSACTION` pour lancer l’échange des PSBTs via le scan de QR codes.

![Image](assets/fr/17.webp)

L’échange se fait en alternant le scan avec le collaborateur: cliquez sur `SHOW QR CODE` pour afficher votre QR code à votre collaborateur, qui le scannera. Ensuite, il affichera à son tour le sien en cliquant sur `SHOW QR CODE`, et vous devrez le scanner avec `LAUNCH QR Scanner`. Puis répétez ce processus jusqu’à ce que les cinq étapes de l’échange soient complètes.

![Image](assets/fr/18.webp)

Une fois tous les échanges effectués, vérifiez les détails de la transaction, puis diffusez-la en faisant glisser la flèche verte située en bas de l’écran.

![Image](assets/fr/19.webp)

[La transaction a bien été diffusée](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Sa structure se présente ainsi :

![Image](assets/fr/20.webp)

*Crédit: [mempool.space](https://mempool.space/)*

Si l'on analyse cette transaction, on observe en entrée mon UTXO de `164 211 sats` ainsi que l’UTXO de `190 002 sats` appartenant au destinataire effectif du paiement. En sortie, je récupère un UTXO de change de `63 995 sats`, tandis que le destinataire reçoit un UTXO de `290 002 sats`. En comparant inputs et outputs, on constate que le destinataire a bien gagné `100 000 sats`, ce qui correspond au montant de mon paiement effectif, et que de mon côté, j’ai perdu `100 000 sats`, auxquels s’ajoutent les frais de minage.

Évidemment, je peux décrire cette structure car j’ai moi-même construit la transaction. Mais pour un observateur extérieur, il est généralement impossible de déterminer quels UTXOs appartiennent à quel participant, que ce soit en inputs ou en outputs.

Pour approfondir vos connaissances sur la gestion de la confidentialité onchain sur Bitcoin, je vous recommande de suivre ma formation BTC 204 sur Plan ₿ Academy:

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
