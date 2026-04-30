---
name: Peach
description: Complete guide to using Peach and trading bitcoins in P2P
---

![cover](assets/cover.webp)




## Introduction


KYC-free peer-to-peer (P2P) exchanges are essential for preserving users' confidentiality and financial autonomy. They enable direct transactions between individuals without the need for identity verification, which is crucial for those who value privacy. For a more in-depth understanding of theoretical concepts, see the BTC204 course:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. What is Peach?


Peach is a P2P exchange platform that allows users to buy and sell bitcoins without KYC. It offers an intuitive interface and advanced security features. Compared to other solutions such as Bisq, HodlHodl, and Robosat, Peach stands out for its ease of use.

A multisignature escrow system (2-2) guarantees the security of funds during transactions. Peach supports various payment methods, and features a reputation system to guide traders in their actions. As usual with P2P platforms, it is therefore important to maintain a good reputation in order to maintain credibility with other traders.


### 2. Privacy and collected data


**What information does Peach collect?


Peach strives to store the absolute minimum of data about its users. Here is an overview of the data stored on our servers:



- A hash of your unique application identifier (AdID)
- A hash of your payment data
- Your encrypted conversations
- Transaction data to ensure that anonymous users do not exceed the trading limit (types of payment methods used, purchase and sale amounts)
- Addresses used to send and receive from the escrow account
- Usage data (Firebase & Google Analytics), only with your consent


As a reminder, a hash is data rendered unrecognizable, similar to encryption. The same data will always produce the same hash, making it possible to detect duplicates without knowing the original data.


*For a more detailed explanation of hashing, take this course:*


https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Who can see my payment details?



- Only your counterparty can see your payment details
- Data are transmitted via Peach servers, but are fully encrypted from end to end
- In the event of a dispute, your payment details and conversation history will be visible to the assigned Peach mediator


## Installation and configuration


### 1. Install Peach application


![Installation de Peach](assets/fr/01.webp)



- Download the application from [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). On iOS, you will first need to install the [testflight](https://apps.apple.com/us/app/testflight/id899247664) app.
- Follow the installation instructions on your device.
- During installation, you'll be asked to choose whether you'd like to share certain data to enhance the Peach application. (image 1)
- On the next screen (image 2), you have two options:
 - If you are a new user, click on "New user" to create a new profile
 - If you already have an account, use "Restore" to restore your existing profile
- If you have a referral code, you can enter it here.
- To restore an existing account (image 3), you'll need :
 - Your backup file
 - The password to decrypt this file


### 2. Overview of Main Screens


The Peach application is organized around four main screens accessible from the bottom navigation bar:


![Navigation dans l'application](assets/fr/02.webp)



- Home (4)** : The main screen from which you can choose to buy or sell, create new transactions and access available offers:
 - create offers with the two buttons below (create buy / create sell)
 - take advantage of existing offers created by other users, using the two buttons below ("Buy"/"Sell").



- Wallet (5)** : Your integrated bitcoin wallet that allows you to :
 - Check your balance
 - Receive bitcoins
 - Envoyer bitcoins (with coin control)
 - View your transaction history
 - Financing your sales



- Trades (6)**: your current and past contracts, under three tabs:
 - Purchases in progress
 - Sales in progress
 - The history of your exchanges



- Settings (7)** : The configuration hub for
 - View your profile (reputation, badges, limits, etc.)
 - Managing security (backup, pin)
 - Manage your payment methods
 - Contact support
 - Change language
 - etc.


### 3. Configure your payment methods


![Accès aux paramètres de paiement](assets/fr/03.webp)


You can manage your payment methods in the settings (image 8)


Peach offers online payments, and face-to-face payments (at registered meetups only).


**Online payments


**Important:**

to protect users, Peach requires that the source of funds matches that advertised. It is up to traders to ensure that this is the case, for their own protection.


![Configuration des paiements en ligne](assets/fr/04.webp)


To add a method :


- In the "online" tab, click on "add a currency/method"
- Choose your currency
- Select your preferred payment method


*Types of payment methods available:*


***For bank transfers: ***


- SEPA (standard or instant)
- Fill in your SEPA bank details.


***Online wallets accepted :***


- Several options available depending on your country (Revolut, Paypal, Wise, Strike, etc.)
- Follow the instructions to add your login details


*gift card usable:*** Gift card usable:*** Gift card usable:*** Gift card usable:*** Gift card usable:*** Gift card usable:***


- Amazon, Steam, etc.
- Enter the card's country of issue and other necessary information


***National payment options:***

Country-specific payment systems :


- Satispay (Italy)
- MB Way (Portugal)
- Bizum (Spain)
- Faster Payments (United Kingdom)
- etc.


***For face-to-face payments: ***


![Configuration des paiements en personne](assets/fr/05.webp)



- Select "Meetup" (image 12)
- Then select your meetup from the list (image 13)


### Directions for use



- You can add several payment methods
- The more methods you add, the wider the range of offers you'll have access to
- Check the accuracy of your information before registering
- You can change or delete your payment methods at any time


**Security note**: Your payment information is encrypted and is only shared with your exchange partner during a transaction, except in the event of a dispute where a Peach mediator will also have access.


### 4. How to secure your portfolio


**Understanding your Peach account


A Peach account has no username and password. It's a file stored locally on your phone, which means Peach doesn't need to store your data or know your identity: you're in control. This file contains all your data: including the 12 bitcoin recovery words, PGP keys, payment details and so on. So it's crucial to save this file and protect it with a __robust__ password.


This approach guarantees a degree of confidentiality, and leaves the responsibility for data and backup management in the hands of the user. Losing your phone without a backup means losing access to your Peach account and funds.


**Create your backups**




- Access settings from the tab at the bottom right of the home screen
- Select the "backups" option in the settings menu


![Processus de sauvegarde](assets/fr/06.webp)


Two types of backup are available:


**Save account file (image 14)**


- Click on "Create new backup"
- Create a **strong** password to encrypt your backup file
- Send this file to a location that will ensure its redundancy in the event of the phone being lost.


The file backup restores your complete Peach account, including :


- Your portfolio
- Your payment methods
- Payment data
- Transaction history with details of counterparties and conversations with them


**Saving the recovery phrase (image 15)**


- Follow the instructions to display your recovery phrase
- Carefully write down the words in the correct order
- Store this backup in a secure location, ideally different from the account file


The recovery phrase allows you to recover :


- Your reputation, your trades
- Your bitcoin funds


But **NOT** the following:


- Your current and past conversations
- Payment data
- Counterparty information in transaction history



## Buying and selling bitcoins


### 1.a How to buy bitcoins: Take an offer to sell


A buyer's first reflex should be to check out the offers for sale that are already financed with bitcoin.


![Vue des offres de vente et filtres](assets/fr/07.webp)



- On the home screen, click on the "Buy" button (image 16)
- You can then browse a list of bitcoins that have been placed in the escrow system and are ready for sale (image 17). You can see the amount, the price (in % relative to the KYC market), the payment methods and the currencies accepted.
- Use filters to sort and order offers (image 18).
- Note: the button at the bottom of the filters page allows you to receive notification when an offer matching your filters has been published; and the "reset" button, which simply clears all filters (image 18).


![Sélection et confirmation d'achat](assets/fr/08.webp)



- View the offer that suits you and send an exchange request (image 19)
- You can make several exchange requests, and the first positive offer will cancel your other requests.
- Make payment by the agreed method.

**Reminder:** the source of funds must match the one you specified when adding the payment method.


- Confirm your payment in the application as soon as it's done**.
- Wait for the seller to receive the payment and declare it as such (image 20)
- And finally, evaluate your experience with the salesperson (image 21)


![Réception des bitcoins](assets/fr/09.webp)



- Track the status of your transaction
- Check confirmation of receipt of bitcoins
- Funds will be available in your Peach portfolio (image 22 and 23)


### 1.b How to buy bitcoins: Create a bid


If you can't find a suitable offer to sell, you can create an offer to buy. Since this doesn't commit any bitcoin at this stage, you'll have less chance of finding an exchange partner, especially if your track record and reputation are poor or non-existent. To remedy this, it's important, when creating the offer, to *make a high-premium offer* to motivate sellers to select your offer. Let's proceed:


![Creation d'ordre d'achat](assets/fr/10.webp)



- On the home screen, click on the "Create a purchase offer" button (image 24)
- Add a payment method, if you haven't already done so, and enter your preferences (quantity, premium etc.) (image 25).

The "instant" option lets you accept a trade request automatically.


 - Click again on "create a bid" to continue
- Once created, it's the sellers' turn to come to you with an exchange request. You can close and exit the app with no worries.
- You can change the premium if you don't receive any requests. Remember: a higher premium will motivate sellers to come looking for your offer (image 26).
- You'll find your offer in the "Buy" tab, which itself is in the "Exchange" window (fig. 27)


![Reception d'une demande de vente, messagerie](assets/fr/11.webp)



- When you receive a buy request (fig. 28) (and if you haven't deactivated instant trade in fig. 25), accept the trade after checking the seller's reputation. If instant trade is enabled, jump directly to image 29.
- The seller must then place the bitcoin in the escrow system, ("fund the safe"). (image 29)
- Then pay the seller at the destination shown in Fig. 30, via your personal banking system. Don't drag the "I've made the payment" cursor until you've done so!
- You can communicate with the seller via the messaging system (P2P encrypted). In the event of a problem, you can open a dispute by clicking on the icon in the top right-hand corner (image 31). A Peach mediator will then enter the discussion.


![Offre de vente completée](assets/fr/12.webp)



- Once the seller has received the money, he will report it and the escrow system will release the bitcoin, which will be on its way to your wallet (by default via GroupHug, Peach's transaction grouping system, which runs once a day),
- Rate your experience with the seller


That's it!


**Note for new buyers:** sellers base their trades on buyers' reputations, and tend to avoid bids from buyers with no completed trades. It's easier, in the first instance, to build a reputation by taking existing offers to sell.



### 2.a How to sell bitcoins: Create a sale


The quickest and easiest way to sell on Peach is to **create an offer to sell**.


![Création d'un ordre de vente](assets/fr/13.webp)



- From the home page, click on "Create a sales offer" (image 32)
- Set up your offer, make sure you insert a payment method and the right parameters

you can also :


  - create several identical offers
  - activate "instant exchange" so that the first buyer to come along can take the contract (without your confirmation) and proceed with payment.
  - choose a refund address
  - finance the trunk from your wallet Peach
- Finance the transaction by sending the bitcoins to the address provided (image 34)
- Wait for confirmation of the transaction. Once done, your offer will be visible on the market.


![Attente du paiement](assets/fr/14.webp)



- Wait for a buyer to take up your offer. Consider increasing the premium (%) if you want to speed things up (image 36)
- Once you've received an exchange request, check the buyer's reputation. Judge for yourself whether the profile is suitable for you, and click "accept" if it is. (37)
- Now it's the buyer's turn to make the payment from his bank to yours. He will then forward the payment to you. Don't hesitate to contact the buyer in chat.
- after checking that the funds have been received by your bank*, release the funds by clicking on the "i have received payment" button (image 38). Never confirm receipt of a payment before checking that it has been received in your account.
- Evaluate the transaction
- Bitcoins are automatically released to the buyer,


There you go!


**Safety note and tips for a successful transaction:**


 - Observe the buyer's details, and check that the origin of the funds matches the one described on Peach If the origin of the funds does not match the one announced, go to Chat and open an argument (image 39), and send the funds back to their origin.
 - Follow the instructions in the yellow cat.
 - Respond quickly to messages from your counterparty
 - be wary of the buyer's attitude, especially when dealing with a profile with little experience
 - Don't hesitate to use the mediation service if you have a problem


### 2.b How to sell bitcoins: take a bid


It's also possible to view and select purchase offers. You'll need to be particularly careful, as this is where the most scammers are to be found.


![Prendre une offre d'achat](assets/fr/15.webp)



- From the home page, click on "Sales" (image 40)
- Use the filters to view and select the most attractive offers (image 41)


![vérification de la réputation](assets/fr/16.webp)



- before requesting a trade, we recommend that you assess the suitability of the buyer's profile. You can click on an offer, then on the user's ID to see his profile. For example, the offer in image 42 could be considered "risky" (new user, relatively high amount). The "risk" you run in taking up this offer is simply that of wasting time, as long as you don't make the mistake of releasing the bitcoins without having received the money. You can still deposit the bitcoins in the safe.

The one in image 43, on the other hand, comes from an experienced trader (image 44), with no disputes in its history. It's therefore a less risky offer.


![Match avec vendeur](assets/fr/17.webp)



- Once the offer has been requested, if the buyer accepts your request, the application will take you to image 34, where you can continue the trade as described below.



## Advantages and disadvantages


### Peach benefits



- No KYC required**: Preserves user confidentiality.
- No access to bank details**: Peach has no access to your bank details or your identity.
- Interface intuitive**: Easy to use for intermediate users.
- Open Source** : Source code is public and verifiable by the community.


### Peach disadvantages



- Limited Liquidity**: Less trading volume than more established platforms.
- Regulatory risk** : The application is managed by a Swiss company. It is therefore subject to Swiss regulations, which could evolve and potentially censor the application.


## Useful resources



- French explanatory video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Quick start guide: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (beware of scammers, administrators will never write to you first by private message)