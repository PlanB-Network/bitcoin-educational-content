---
name: BitcoinVoucherBot
description: Un robot Telegram pour acheter Bitcoin en toute confidentialité
---
![image](assets/cover.webp)

_Ce tutoriel a été rédigé par_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

## Introduction

Le BitcoinVoucherBot est un outil qui permet d'acheter des bitcoins en Exchange contre des euros.

### KYC Light

L'action de changer les euros pour la Bitcoin est la première et la plus fondamentale étape pour commencer à étudier ce sujet, mais c'est apparemment aussi la plus difficile et la plus complexe. Il existe de nombreuses options : offrir du Bitcoin par le biais d'échanges centralisés, de rencontres sur le thème du Bitcoin, d'amis, de connaissances, et plus encore. Nous nous joignons à la communauté Bitcoiner et **nous recommandons absolument l'utilisation d'échanges centralisés** afin d'accorder plus d'attention à la vie privée.

Bien que ce choix puisse être moins pratique, il est important de comprendre que les bourses appliquent la réglementation "Know Your Cutomer" (KYC), attribuant ainsi une identité, ainsi qu'un emplacement physique, à chaque Satoshi acheté auprès d'elles. la "commodité" a des effets secondaires frappants.

### Comment faire ?

Voici le service [BitcoinVoucherBot :](https://t.me/BitcoinVoucherBot), un bot Telegram qui agit comme un conduit entre nos transferts SEPA et les achats Sats.

### Pré-requis

Pour commencer à utiliser BitcoinVoucherBot, il n'est pas nécessaire de communiquer des informations personnelles sensibles à l'équipe du Bot. **Aucune autorisation n'est nécessaire**.

Il suffit d'avoir un compte Telegram déjà actif et un compte bancaire. **Remarque** : Un compte ouvert auprès de Poste Italiane (pour les clients italiens) ou, plus généralement, faisant référence à une carte rechargeable ne convient pas.

Dans le chat de Telegram, nous préparons une commande, nous la payons par virement bancaire et enfin, par l'intermédiaire du robot, nous recevons un bon d'achat émis par une société tierce qui ne connaît pas l'objet de l'achat.

### Activation du robot et menu

L'activation est une opération simple à effectuer une seule fois. Depuis Telegram, recherchez _@BitcoinVoucherBot_ et dès que vous arrivez sur le chat du Bot, un gros bouton _Start/Start_ apparaît en bas. L'opération fait réagir le Bot, qui présente un menu des principales commandes à sa disposition. Les premiers messages de bienvenue apparaissent également, pour lesquels nous recommandons une lecture attentive.

**Attention** : il y a plusieurs arnaqueurs qui se font passer pour le VoucherBot original. Si vous n’êtes pas sûr de la recherche via Telegram, accédez au lien de BitcoinVoucherBot depuis le [site officiel](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

Les options apparaissent en cliquant sur le bouton _Menu_ dans le coin inférieur gauche : vous pouvez cliquer sur le mot correspondant à la commande, ou taper dans la boîte de message la barre oblique `/` suivie de la commande tapée.

![image](assets/it/02.webp)

Les principales opérations sont les suivantes


- _/purchase_ : il s'agit de la procédure d'achat proprement dite. Lorsque la transaction est terminée, le code QR est automatiquement généré par le robot, prêt à être échangé.
- _/refill_ : disponible au moment de la rédaction de ce tutoriel, mais nous ne l'aborderons pas car, pour des raisons techniques, cette option pourrait être supprimée ultérieurement.
- _/swap_ : ouvre la procédure d'échange, disponible soit avec un bot Telegram pratique, soit via le web.
- _/ap_ : plan d'accumulation, qui vous permet de mettre en place un **Plan d'Accumulation Constante (PAC)**.
- _/lnaddress_ : avec laquelle on nous demande de relier une LN Address propre, pour une procédure particulière que nous verrons plus tard.
- _/credits_ : pour vérifier combien il reste de crédits pour les bons generate.
- _/myorders_ : montre les commandes passées avec le robot (**Avertissement** le système ne suit que les 10 dernières commandes passées et non l'historique complet).
- _/fees_ : une commande pour vérifier les frais de réseau. Pour les évaluer, il est toujours préférable de s'appuyer sur Mempool.space.
- _/support_ : en cas de besoin, affiche les contacts permettant de signaler les problèmes à l'équipe d'assistance.

## Procédure d’achat de Bitcoin

### Préparation de la commande

Cliquez sur _/achat_ dans le menu de commande

![image](assets/it/03.webp)

Plusieurs opportunités se présentent, mais nous choisissons _BTC Vouchers_

![image](assets/it/04.webp)

BitcoinVoucherBot vous permet d'acheter Bitcoin onchain, Lightning et Liquid.

A ce stade, choisissez _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

L'écran change rapidement et VoucherBot propose des dénominations d'achat. Elles vont d'un minimum de 100,00 € à 900,00 €.

En cas de premier achat, seules les dénominations 100,00 €, Onchain et Lightning sont proposées. Pour plus de confidentialité, nous vous conseillons de choisir _Lightning ⚡️_

![image](assets/it/06.webp)

Le VoucherBot nous signale qu'un premier choix a été fait et que, pour le confirmer, nous devons choisir _Proceed_

![image](assets/it/07.webp)

Il s'agit maintenant de choisir le mode de paiement. Le transfert se fait par virement bancaire **(accepté uniquement SEPA)**. VoucherBot propose comme destinataire une société qui fournit deux comptes bancaires, l'un au Royaume-Uni et l'autre en Suisse. C'est la banque suisse qui a été choisie pour réaliser ce tutoriel

![image](assets/it/08.webp)

À ce stade, il nous est demandé de saisir notre numéro IBAN, celui à partir duquel le transfert vers la banque choisie commencera. Ces informations constituent un puzzle qui permettra au robot, c'est-à-dire à une machine, de rassembler certaines informations pour que le processus d'achat se déroule sans intervention humaine.

L'IBAN doit être inscrit dans la barre de message, vérifié et envoyé au bot.

![image](assets/it/09.webp)

Un message de contrôle apparaît maintenant dans le chat avec VoucherBot.

Si tout est correct, continuez en cliquant sur _Proceed_.

![image](assets/it/10.webp)

### Paiement

Après quelques instants, nécessaires au traitement des données, VoucherBot répond par un message contenant tous les détails nécessaires à la réalisation de la commande. En fonction des exigences de votre banque, les informations pertinentes sont les suivantes :


- `IBAN`, qui est essentiel pour le dépôt, ainsi que pour le Address du destinataire ;
- `le montant choisi` précédemment à travers la limite, qui doit être respectée pour permettre à VoucherBot de reconnaître la commande lorsque le paiement est reçu ;
- `Raison du paiement`, qui est la raison du paiement. **Il doit être copié et collé sans rien enlever ni ajouter dans le champ approprié de votre transfert. Tout "." ou "-" présent dans le motif du paiement peut être remplacé par un "espace blanc "**.
- un `OrderID` unique auquel se référer pour toute demande d'assistance.

Vous pouvez ensuite procéder au paiement, via votre application ou votre banque. Lorsque le paiement a été accepté par la banque, il est important de ne pas oublier d'appuyer sur _Notify payment_ dans le chat avec VoucherBot. Cette simple opération vous avertit qu'un paiement est en cours d'acheminement.

![image](assets/it/11.webp)

VoucherBot répond par un message contenant un avertissement très important : **ne supprimez pas le chat**, au moins jusqu'à ce que le bon soit reçu, car c'est le seul moyen de reconstituer la commande et de la maintenir.

![image](assets/it/12.webp)

---
A noter :


- seuls les virements SEPA sont acceptés ;
- les délais d'attente dépendent uniquement de la manière dont les banques (qui ne travaillent pas 24 heures sur 24, 7 jours sur 7 et 365 jours par an comme Bitcoin) traitent le bon. La réception du bon peut prendre de quelques heures à trois jours ouvrables ;
- pour tout besoin, Bitcoin VoucherBot dispose d'un excellent service [support](https://t.me/BitcoinVoucherGroup) sur Telegram.

---
### Rachat

Dès que le paiement est effectué avec succès, Bitcoin VoucherBot envoie le bon directement dans le chat. Le bon éclair se présente sous la forme d'un code QR, imprimé sur un fond orange.

![image](assets/it/31.webp)

Il y a toutes les données nécessaires pour l'encaisser :


- le montant en Sats, équivalent à celui envoyé par virement bancaire, hors frais de service et de réseau ;
- un identifiant de référence du bon ;
- la date à laquelle le bon doit être remboursé sous peine de perdre les fonds, c'est-à-dire 25 jours après son émission.

Vous pouvez encaisser le bon en cadrant le code QR à l'aide de la fonction de balayage d'un Wallet Lightning Network compatible, ou via LNURL, également indiqué sous le code QR.

Pour ce tutoriel, nous avons utilisé Wallet Of Satoshi, en utilisant la fonction de scan activée par le bouton _Send_.

![image](assets/it/32.webp)

Avec l'appareil photo du téléphone portable activé, encadrez le code QR dans le chat, en ouvrant Telegram depuis l'ordinateur

![image](assets/it/34.webp)

Avant de continuer, Wallet Of Satoshi affiche un écran de vérification comprenant le montant, qui correspond exactement à celui indiqué sur le bon, et comme description, BitcoinVoucherBot. Pour encaisser le bon, il suffit de cliquer sur _Receive_.

![image](assets/it/35.webp)

Wallet Of Satoshi traite pendant quelques instants.

![image](assets/it/36.webp)

et enfin la collecte est déclarée et immédiatement disponible dans le solde de la Wallet.

**Wallet of Satoshi est une application custodial : immédiatement après l’encaissement du bon, il est conseillé de transférer les sats vers un portefeuille non-custodial.**

![image](assets/it/37.webp)

### Comment encaisser un bon d'achat onchain

Comme nous l'avons vu dans la préparation de la commande, VoucherBot permet d'acheter des Sats directement sur la chaîne, en choisissant le bon éponyme.

**Note** : La préparation de la commande et le paiement ne changent pas, ils sont toujours les mêmes. Ce qui change, c'est la manière d'encaisser un bon d'achat onchain.

Après avoir terminé la commande, effectué le paiement, appuyé sur _Notify payment_ et attendu le temps technique de la banque pour effectuer le transfert, VoucherBot répondra en envoyant le bon d'achat directement dans le chat.

Ce bon se présente également sous la forme d'un code QR, mais la couleur principale est le jaune canari et, surtout, dans la description, il est bien expliqué qu'il s'agit d'un bon onchain, que vous encaissez directement sur votre Wallet onchain et, pour lancer la procédure d'encaissement, vous devez cliquer sur _Redeem on Telegram_. Le bon onchain contient également les informations déjà vues pour le lightning one :


- le montant en Sats, équivalent à celui envoyé par virement bancaire, hors frais de service et de réseau ;
- un code de bon d'achat ;
- un identifiant de référence du bon ;
- la date à laquelle le bon doit être remboursé sous peine de perdre les fonds, c'est-à-dire 25 jours après son émission.

![image](assets/it/22.webp)

**WARNING ⚠️:** cliqué comme expliqué, le pop-up d'un autre bot s'ouvre : **Voucher RedeemBot.**

Voucher RedeemBot est l'outil mis à disposition à cet effet. Qu'il s'agisse de la première utilisation ou de commandes antérieures, il est toujours nécessaire de cliquer sur _START_ à chaque fois qu'un nouveau rachat est effectué.

![image](assets/it/23.webp)

À ce stade, RedeemBot charge le bon onchain, facilement reconnaissable grâce au code du bon et à l'ID de référence. Il déverrouille également la barre pour écrire des messages et commencer à chatter avec le bot, qui nous invite en fait à lui dire un Address onchain de notre Wallet.

**Remarque** : Cette Address doit être de type SegWit.

![image](assets/it/24.webp)

Nous ouvrons notre Wallet à ce stade et generate a SegWit Address

![image](assets/it/25.webp)

nous le copions

![image](assets/it/26.webp)

et le coller dans le chat avec RedeemBot

![image](assets/it/27.webp)

Nous avons maintenant un écran de contrôle, pour vérifier que le code du bon est correct, ainsi que la Address que nous avons communiquée à RedeemBot. Vérifions-le bien car, en cliquant sur _Proceed_, la transaction commence et il n'y aura aucun moyen de la retrouver si nous avons, par exemple, communiqué la mauvaise Address.

![image](assets/it/28.webp)

La transaction a commencé et la procédure Redeem du bon onchain se termine.

![image](assets/it/29.webp)

tandis que le montant peut être vu venir dans l'histoire de notre Wallet.

![image](assets/it/30.webp)