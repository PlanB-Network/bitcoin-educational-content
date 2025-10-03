---
name: Debifi
description: Obtenir un prêt sans garde de fonds garanti par Bitcoin.
---

![cover](assets/cover.webp)


## Introduction

Depuis des siècles, le prêt traditionnel a permis le financement de nombreux projets. Cependant, il reste lent, coûteux et peu inclusif, surtout pour celles et ceux qui n’ont pas accès à une infrastructure bancaire solide.

Avec l’essor du protocole Bitcoin, une nouvelle ère financière s’est ouverte, amenant avec elle plusieurs défis. Au nombre de ces défis, subsistait celui-ci : comment obtenir des liquidités sans être obligé de vendre son Bitcoin, et donc sans perdre son exposition à son potentiel de croissance ?

De cette réflexion est née **Debifi**, une plateforme qui se positionne comme une alternative moderne aux banques. L’objectif est clair : rendre le crédit aussi simple et transparent que possible, en alliant les avantages du système financier traditionnel à la liberté offerte par Bitcoin. Le nom Debifi traduit bien cette vision : ***Decentralized Bitcoin Finance***, une contraction qui illustre la rencontre entre finance décentralisée et innovation Bitcoin. 

 Debifi est une plateforme de prêts adossés au Bitcoin non custodial, ce qui signifie que vous gardez le contrôle de vos clés privées. Elle permet aux utilisateurs de débloquer de la liquidité en échange de leurs bitcoins verrouillés en garantie. Contrairement aux prêts bancaires traditionnels, Debifi utilise un système d’escrow multisignature (3 sur 4) et n’accepte pas l'hypothèque du collatéral, garantissant ainsi plus de sécurité et de transparence. 
 
 En pratique, cela veut dire que ni Debifi ni un prêteur individuel ne peuvent dépenser votre BTC sans l’accord de trois parties (vous, le prêteur et un tiers de confiance). Cela rend le système plus sûr : si vous empruntez sur Debifi, vous conservez la propriété de votre Bitcoin jusqu’au remboursement complet du prêt.

## Avantages de Debifi 

Avec Debifi, ce sont des prêts collatéralisés, une sécurité blockchain (multisignature, 2FA), un choix de stablecoins/liquidités, une confidentialité et un contrôle total du Bitcoin. Debifi « vous fait garder votre argent » (your keys, your coins), tout en offrant des taux compétitifs et un accès mondial aux prêts garantis par BTC.

Voici un petit tableau comparatif entre un prêt sur Debifi et un prêt bancaire traditionnel : 

| Caractéristiques       | Prêt via Debifi                                                       | Prêt bancaire traditionnel                                                 |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Accessibilité          | ✔️ Ouvert à tout détenteur de Bitcoin (même sans historique bancaire) | ❌ Souvent réservé aux clients avec garanties physiques et dossiers solides |
| Vitesse d’obtention    | ✔️ Liquide en quelques minutes/heures                                 | ❌ Processus long (jours ou semaines)                                       |
| Garanties exigées      | ✔️ Collatéral en Bitcoin uniquement                                   | ❌ Garanties physiques (maisons, terrains, revenus stables)                 |
| Contrôle de l’actif    | ✔️ Vous conservez l’exposition au Bitcoin et son potentiel de hausse  | ❌ Vous n’avez aucun lien entre le prêt et vos actifs financiers            |
| Souplesse géographique | ✔️ Disponible partout (sans contrainte géographique bancaire)         | ❌ Limité à la juridiction de la banque                                     |
| Risque principal       | ❌ Risque de liquidation si le prix du BTC chute trop                  | ❌ Risque de saisie de biens ou impact négatif sur la cote de crédit        |

Avant de vous montrer pas à pas comment faire un emprunt sur Debifi, il me semble indispensable de m'attarder sur certains points.


## Définitions

- **Les frais d’origine ou commissions** (origination fees) sont des frais uniques prélevés au moment où un prêt est accordé, et calculés en pourcentage du montant emprunté. Ces frais couvrent les coûts administratifs, opérationnels et de gestion.

- **Un collatéral** (ou garantie) est un actif que tu déposes pour sécuriser un emprunt. Dans le cas de Debifi, le collatéral est du Bitcoin (BTC) que l’emprunteur dépose dans l’escrow multisig 3/4.

- **Le système multisig escrow (3/4)** est un mécanisme de dépôt sécurisé où les bitcoins d’un emprunteur sont placés dans une adresse multisignature. Concrètement quatre (4) parties détiennent chacune une clé (emprunteur, prêteur, Debifi, tiers indépendant). Pour déplacer les fonds, il faut au moins 3 signatures sur 4.

- **Un stablecoin** est une cryptomonnaie dont la valeur est rattachée à un actif stable (ex. dollar US), ce qui évite la volatilité du Bitcoin. Par exemple, 1 USDC vaut toujours ~1 $, car il est garanti par des réserves en fiat.

- **Le ratio prêt/collatéral ou Loan-to-Value (LTV)** d'un prêt détermine combien de liquidités vous pouvez emprunter en garantie de votre Bitcoin. Ratio LTV = Montant du prêt / Montant de la garantie * 100. Par exemple un LTV de 50 % signifie que la valeur du prêt est égale à 50 % de la valeur du Bitcoin déposé.


Tutoriel vidéo de BTC Sessions :

![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)

## Débuter avec Debifi

Pour débuter sur Debifi, il vous faut des prérequis.
### Prérequis
 
 Avant de pouvoir emprunter sur Debifi, assurez-vous de disposer des éléments suivants :

- Portefeuille Bitcoin : où vous détenez vos BTC (idéalement non custodial, par exemple hardware wallet ou un portefeuille mobile de confiance). C’est depuis ce portefeuille que vous enverrez le collatéral Bitcoin sur Debifi et que vous recevrez les fonds. 

- Stablecoins ou fiat : Debifi prête en stablecoins et quelques devises fiat. Les principaux stablecoins utilisés sont USDT et USDC.  

Vous pouvez utiliser Aqua, un portefeuille Bitcoin et Liquid mais qui supporte aussi la gestion des stablecoins USDT sur divers réseaux. Ou encore le COLDCARD (le Mk4 ou le Q) qui est actuellement le seul hardware pris en charge par Debifi.

https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

- KYC (*Know Your Customer*) : en fonction de l’offre de prêt choisie, un processus de vérification d’identité peut être requis. Sur Debifi, chaque offre indique si la KYC est nécessaire ou non. Donc, préparez-vous en conséquence. Le KYC est assuré par des prestataires tiers fiables tels que Sumsub.

![image](assets/fr/03.webp)

- Application d'authentification à double facteurs : Debifi exige un code Authenticator pour chaque action importante. C'est une couche supplémentaire de sécurité. Dans ce tutoriel, nous utiliserons Google Authenticator. Alternativement, vous pouvez utiliser d'autres selon votre convenance. 

https://planb.network/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

- Site web et application mobile Debifi : Debifi est à la fois un site web et une application mobile, et les deux fonctionnent en binôme. L’application mobile devient un portefeuille, qui stocke votre clé privée, et gère la signature des contrats. En outre, vous devez utiliser le site web pour engager des contrats (une grande interface vous permet de voir de façon générale les contrats de prêts et leurs spécificités).

- L’application mobile Debifi (iOS/Android) est obligatoire pour prendre des prêts. Vous devez télécharger l’application, créer un compte et « lier » votre appareil (enregistrement de l’appareil à votre compte). L’appli Debifi gère l’authentification à deux facteurs (2FA) et sans smartphone, vous ne pouvez pas confirmer les transactions sur Debifi.

### Création d’un compte 

Rendez-vous sur [le site officiel de Debifi](https://debifi.com/app).

![image](assets/fr/04.webp)

Installez votre application selon le type de smartphone dont vous disposez, puis ouvrez-la. 

![image](assets/fr/05.webp)

![image](assets/fr/06.webp)

Une fois dans l'application, cliquez sur le menu **Settings**. 

![image](assets/fr/07.webp) 

Ensuite, cliquez sur **Login or create account** pour créer un compte avec votre adresse e-mail. 

 ![image](assets/fr/08.webp) 

![image](assets/fr/09.webp)

![image](assets/fr/10.webp)   

Vous recevrez un code de vérification par e-mail. Ce code est à copier-coller dans l'application. Ensuite, ouvrez l’application Debifi sur votre smartphone et connectez-vous.

![image](assets/fr/11.webp)   

### Sécurisation de votre compte 

Pour la sécurité, Debifi vous demandera de suivre trois étapes.

![image](assets/fr/12.webp)

- D'abord, vous devrez définir un code PIN fort pour accéder à votre application ultérieurement.

![image](assets/fr/13.webp)

- Ensuite, configurer une authentification à deux facteurs (2FA) afin d'associer votre appareil à votre compte grâce au code 2FA.

![image](assets/fr/14.webp)

- Enfin, sauvegardez les 12 mots de votre clé privée en la notant sur un support fiable et en la conservant en lieu sûr. Cette phase est essentielle pour la récupération de votre compte et la gestion de vos fonds.

![image](assets/fr/15.webp)

- Pour plus de sécurité, vous avez la possibilité d'ajouter même une passphrase.

![image](assets/fr/16.webp)

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Notez que seul votre smartphone enregistré pourra ouvrir votre compte (c’est une mesure supplémentaire de sécurité). 

Une fois ces étapes achevées, cliquez sur le menu **Offers** pour voir les offres de prêt disponibles. Lorsque vous cliquez sur une offre, cela vous redirige vers le site web de Debifi.

![image](assets/fr/17.webp)

### Accédez au site Web et explorez les offres de prêt

Une fois votre appareil connecté, rendez-vous sur le [site de Debifi](https://debifi.com/). Connectez-vous dans le but d'établir une connexion sécurisée entre l'application mobile Debifi et la plateforme web. Cela vous facilite ainsi l'interaction avec les offres de prêt disponibles (une vue claire sur les détails de chaque offre) et la gestion de votre compte.

![image](assets/fr/18.webp)

![image](assets/fr/19.webp)

![image](assets/fr/20.webp)

![image](assets/fr/21.webp)


Vidéo tutoriel sur comment se connecter avec son compte sur la plateforme :

![video](https://youtu.be/cUwCfTKDAOo)

## Demande de prêt

La plateforme vous met en relation avec des liquidités de qualité institutionnelle et vous propose une gamme d'options adaptées à vos besoins. Parcourez-la pour découvrir les offres disponibles. Vous avez également la flexibilité d'ajuster les paramètres du prêt en fonction de votre tolérance au risque individuelle et de votre situation financière.

![image](assets/fr/22.webp)

 Les devises fiat que Debifi propose actuellement sont consultables sur la plateforme. 

![image](assets/fr/23.webp)

### Clauses contractuelles claires et flexibles

Debifi mise sur des conditions de prêt transparentes et flexibles pour répondre aux besoins de chaque partie (prêteur et emprunteur). Les clauses essentielles comprennent :

#### Le ratio prêt/collatéral (LTV)
Les tranches du prêt Bitcoin sont généralement au nombre de trois (3) :

- Conservatrice (20 % – 40 % LTV), qui correspond à un emprunt à faible risque est idéal pour maximiser la sécurité contre la volatilité des prix du Bitcoin ;

- Équilibrée (50 % LTV) ; 

- Agressive (70 % – 85 % LTV), qui permet une liquidité accrue, mais comporte un risque très élevé de liquidation lors des baisses du marché. Une surveillance active des conditions du marché Bitcoin est nécessaire lorsque vous optez pour une offre dans cette tranche. 

#### Taux d'intérêt

La fixation des taux dépend généralement de votre LTV choisi, de la durée du terme du prêt, la volatilité des garanties et les évaluations des risques spécifiques à la plateforme. Ils restent fixes pendant toute la durée du prêt.

#### Durée de Prêt et Flexibilité du Remboursement

Les calendriers de remboursement pour les prêts sont souvent flexibles et adaptés aux besoins de l'utilisateur. Les paiements peuvent être effectués à tout moment tant que les exigences en matière de garantie sont respectées. Les paiements de prêts sont généralement des intérêts pendant toute la durée du prêt, le principal étant dû à l'échéance du prêt.

#### Droits de Liquidation (Appels de Marge)

Comme le prix du bitcoin est volatil, un prêt responsable inclut des politiques spécifiques d'appels de marge dans l'accord. Cette politique permet de notifier à l'emprunteur de soit fournir une garantie supplémentaire, soit rembourser une partie du prêt.

### Lancement du processus de prêt

Pour sélectionner une offre de prêt adaptée à vos besoins, cliquez dessus pour voir ces caractéristiques. 

![image](assets/fr/24.webp)

Vous pouvez voir : 
1. Le nom de l'institution prêteuse ;
2. La tranche de montants dans lequel se situe ce prêt ;
3. Que vous recevrez les fonds en USDC Ethereum ;
4. La tranche de période dans laquelle se situe le prêt, le taux d'intérêt et le ratio LTV ;
5. Le KYC est requis pour cette offre ;
6. Le montant précis dont vous avez besoin doit être inscrit (ce montant doit être dans la tranche, voir 2) ;
7. L'adresse Ethereum USDC qui doit recevoir les fonds doit être renseignée.

Une fois que les caractéristiques de l'offre vous conviennent et que vous aviez renseigné les informations nécessaires, appuyez sur ''**Demande de contrat**''.

![image](assets/fr/25.webp)

Retournez dans l'application mobile pour ''**Provide public key**''.

![image](assets/fr/26.webp)

Appuyez sur '' **Provide public key** '', ensuite choisissez la source de fourniture de la clé publique. Le prêteur aussi sera amené à fournir une clé publique de son côté.

![image](assets/fr/27.webp)

![image](assets/fr/28.webp)

![image](assets/fr/29.webp)

![image](assets/fr/30.webp)

L'étape suivante sera celle de signer le contrat. Toujours dans l'application mobile, appuyez sur '' **Sign contract** ''

![image](assets/fr/31.webp)

![image](assets/fr/32.webp)

Lorsque vous finissez de signer le contrat, Debifi crée automatiquement une adresse Bitcoin multisignature unique (escrow 3-sur-4) pour votre contrat. Tant que vos bitcoins sont dans l’escrow, ils ne peuvent pas être utilisés ailleurs. 

### Dépôt de la garantie et réception de vos fonds

La dernière étape consiste à déposer votre garantie Bitcoin dans le système de séquestre multisignature. Debifi vous indique alors l’adresse (B) d’escrow et la quantité de BTC (A) à envoyer comme (collatéral + commission). 

![image](assets/fr/33.webp)

Vous recevrez également cette notification dans votre application mobile.

![image](assets/fr/34.webp)

Dès confirmation de votre dépôt, le prêteur versera le montant du prêt à l'adresse de réception que vous avez indiquée, finalisant ainsi la transaction et vous donnant accès aux fonds dont vous avez besoin.

Vous recevrez ensuite une notification de Debifi, vous demandant de payer les frais du prêt ou les commissions afin de faire progresser le statut de votre prêt.

En réalité, une fois le contrat créé, les frais du prêt sont prélevés automatiquement sur le collatéral bloqué par l'emprunteur dans l'adresse d'entiercement multisignature. 

Tout ce que vous avez à faire est de signer une transaction qui permettrait à Debifi de déduire ses commissions de la garantie. De son côté, votre prêteur devra également signer la transaction de prélèvement des frais, sinon Debifi ne pourra pas recevoir sa commission.

![image](assets/fr/35.webp)

Les frais de prêt applicables sont de 1,5 à 2 %, selon la durée du contrat. La plateforme facture des commissions en Bitcoin uniquement.

## Suivi du prêt 

Une fois le prêt en cours, Debifi vous permet de surveiller votre contrat en temps réel. Dans l’interface, vous verrez notamment :

- Le montant emprunté et la durée restante.
- Le ratio LTV actuel (Loan-to-Value) : Le LTV augmente si le prix du BTC chute (puisque votre collatéral vaut moins). Un seuil d’alerte (généralement 90 %) est fixé. Si votre LTV dépasse ce seuil, il y a risque de liquidation forcée. Debifi vous donnera alors 24 h pour réagir.

Les emprunteurs seront informés de la baisse de prix. Cette information sera également disponible sur la page récapitulative du contrat. Pour rétablir le ratio prêt/valeur initial d'un prêt, l'emprunteur doit :

- soit, déposer une garantie supplémentaire ;
- soit, procéder à un remboursement total ou partiel de la dette.

En cas d'augmentation du prix de la garantie, l'emprunteur conserve toute plus-value sur la garantie. Il ne doit que le montant du prêt, qui est prédéterminé et indépendant du cours du Bitcoin.


## Remboursement et récupération du collatéral

À la fin de la durée convenue (ou avant, si vous le souhaitez), vous devrez rembourser le prêt. 
Dans Debifi :

- Allez dans votre contrat et cliquez sur **Make a repayment**. Entrez le montant total dû (capital + intérêts).

- Envoyez les stablecoins depuis votre portefeuille à l’adresse du prêteur indiquée, et revenez confirmer le remboursement sur la plateforme en copiant dans l'onglet dédié l'**ID** de la transaction de remboursement. Cela permet à Debifi d'effectuer plus facilement ses vérifications.

Une fois le paiement confirmé par le prêteur (et par vous), Debifi vous demandera alors de **refund**. Votre Bitcoin collatéral est libéré et vous pouvez le renvoyer depuis l’escrow vers votre propre portefeuille.  N’oubliez pas de récupérer tous vos bitcoin.

Dès l'instant où vous recevez vos bitcoins, le contrat de prêt passe en statut **Contract completed**. 

Bravo ! Vous avez finalisé le processus.


## Bonnes pratiques et sécurité

Quels que soient vos objectifs ou vos motivations — financement d’un projet, acquisition de biens, achat de bitcoins, etc. — faites preuve d’une extrême prudence avant de contracter un prêt adossé à Bitcoin. Prenez le temps de mûrement réfléchir à votre décision, car Bitcoin demeure un actif volatil. **Une forte baisse de son prix pourrait entraîner la liquidation forcée de vos bitcoins**.

Surveillez votre ratio prêt/collatéral (LTV). Configurez des alertes (prix BTC, LTV) si possible. Ne laissez pas votre ratio s’approcher de 90 %. Si vous avez des doutes, augmentez le collatéral ou remboursez plus tôt.

Maîtrisez vos clés. Détenir votre BTC dans un portefeuille sûr (idéalement hardware ou un portefeuille réputé). Ne définissez pas un code PIN en rapport avec une date importante de votre vie et ne partagez jamais votre phrase de récupération. Sur Debifi, vous générez votre clé privée dans l’application – Debifi ne la connaît pas.

Commencez petit si possible. Lors d’un premier prêt, testez un montant modeste pour vous familiariser au processus.

N’utilisez que le site officiel Debifi pour être au parfum des actualités relatives à Debifi, et évitez les liens inconnus ou phishing.  Mettez à jour l’application, protégez votre smartphone par un code confidentiel, et privilégiez un hardware wallet compatible.

Par ailleurs, si vous êtes un prêteur, cette vidéo tutoriel vous guidera dans l'utilisation de la plateforme Debifi. En passant par la sélection des emprunteurs qui s'intéressent à votre offre, la fourniture des clés publiques, la signature des accords, le transfert des stablecoins, etc. 

![video](https://youtu.be/g8iLxwI4xT0)

Vous savez désormais comment prendre en main la plateforme Debifi pour obtenir un prêt.

Je vous conseille de suivre ce cours qui vous permet d'examiner de manière approfondie Bitcoin, les Stablecoins et leur apport de souveraineté.

https://planb.network/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46 

