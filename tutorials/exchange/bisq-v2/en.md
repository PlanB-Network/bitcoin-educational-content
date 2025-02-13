---
name: Bisq 2
description: Complete guide to using Bisq 2 and exchanging bitcoins P2P
---
![cover](assets/cover.webp)

## Introduction

KYC-free peer-to-peer (P2P) exchanges are essential for preserving users' confidentiality and financial autonomy. They enable direct transactions between individuals without the need for identity verification, which is crucial for those who value privacy. For a more in-depth understanding of the theoretical concepts, take a look at the BTC204 course:

https://planb.network/courses/btc204
### What is Bisq 2?

Bisq 2 is the new version of the popular decentralized Bisq exchange, launched in 2024. Unlike its predecessor, Bisq 2 has been developed to support multiple exchange protocols, offering users greater flexibility.

**Key new features:**


- Support for multiple privacy networks (Tor, I2P)
- Multiple identities for greater confidentiality
- REST API for trading bots
- Support for multiple portfolio types
- Role system with compulsory deposit in BSQ

This guide focuses exclusively on "Bisq Easy", the only protocol currently available. Bisq Easy has been designed specifically for new Bitcoin users. This protocol enables users to buy and sell Bitcoins against fiat currencies on a decentralized peer-to-peer platform. Transactions are limited to the equivalent of 600 USD (with a minimum of 6 USD), and exchange security relies on the reputation of BTC sellers. Bisq Easy has no trading fees or security deposit requirements. Bisq Easy is expected to replace Bisq 1 for cash exchanges below 600 USD (or equivalent).

**Main features:**


- Cross-platform desktop application
- Several exchange protocols available
- Decentralized P2P network
- Focus on confidentiality (no KYC, use of Tor)
- Non-custodial (you retain control of your funds)
- Open source (AGPL)

### Differences with Bisq 1

**For buyers:**


- No security deposit required
- No trading fees
- No mining fees
- Security based on vendor reputation
- Lower trading limits (equivalent to USD 600)

**For sellers:**


- No security deposit required
- Building a reputation
- Possibility of burning BSQ or creating BSQ bonds
- Potentially higher sales premium (10-15% above market)

**Important note:** Once the Bisq Multisig protocol has been implemented in Bisq 2, the old version of Bisq can be phased out. However, Bisq 1 will continue to be used as a management tool for the Bisq CAD and for BSQ-BTC exchanges.

### Exchange process


- The creator of the offer defines the terms of the exchange
- Once the traders have agreed on the terms (payment method and price), the exchange begins
- The seller sends his bank details to the buyer, and the buyer sends his Bitcoin address to the seller
- Buyer makes payment in cash and notifies seller
- Once payment has been received, the seller sends the bitcoins to the buyer's address
- The exchange is complete when the buyer receives the bitcoins

### Important rules


- Before exchanging payment details, the exchange can be cancelled without justification
- After details have been exchanged, failure to meet obligations may result in banishment
- For bank transfers, **never use the terms "Bisq" or "Bitcoin "** in the reason for payment (this could lead to the funds being frozen or even cause the recipient's or payer's bank account to be blocked)
- Traders must log on at least once a day to follow the process
- In the event of a problem, traders can call on the services of a mediator

## Installation and configuration

### 1. Download and Verify Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Go to [bisq.network](https://bisq.network/downloads/)
- Download the Bisq 2 version corresponding to your operating system (scroll down the page)
- Verify the authenticity of the downloaded file (strongly recommended). For a detailed guide to signature verification, see the following tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Installation according to your system

Please follow the installation steps appropriate for your operating system. If you encounter any difficulties during installation, you can consult the detailed guide on the [official Bisq wiki](https://bisq.wiki/Downloading_and_installing).

### 3. First start-up


- Launch Bisq 2 and accept the terms of use

![Conditions d'utilisation](assets/fr/01.webp)


- Create a new profile by choosing a name and avatar

![Création du profil](assets/fr/02.webp)


- You are then taken to the application's main dashboard, where you can launch Bisq Easy to buy or sell your first bitcoins

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Setting up payment methods


- Access the payment accounts section from the main menu

![Liste des comptes de paiement](assets/fr/04.webp)


- Add a new payment method by filling in the required information

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Pre-configuring payment methods is optional, but recommended to save time when trading. You can also configure your payment methods directly during a trade by contacting your exchange partner.

### 5. Account security

**Data backup:**

Unlike Bisq 1, Bisq 2 does not currently integrate a Bitcoin wallet: transactions are therefore carried out via your own external wallets. Nevertheless, we recommend that you regularly back up your Bisq 2 data folder. To locate your data folder, consult the [official Bisq wiki](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Identity management:**

Bisq 2 lets you create multiple identities. Each identity can be used for different types of transaction. Your identities are stored in the data folder.

## Buying and Selling Bitcoins

### How to buy Bitcoins

**Option 1: Take advantage of an existing offer**


- On the main screen, select "Bisq Easy", "Getting started" tab, then click on "Start trade wizard"

![Lancer trade wizard](assets/fr/06.webp)


- Choose "Buy Bitcoin" and select your currency

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Set up your preferred payment methods (SEPA, Revolut, etc.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- At this point, either you have a list of offers corresponding to your previous criteria, or you need to go to the "Offerbook"

![Liste des offres](assets/fr/10.webp)


- In the second case, you can display and filter offers using the buttons at the top right of the interface

![Filtres des offres](assets/fr/11.webp)


- Once you've chosen your offer, all you have to do is choose your payment method, then validate the trade summary

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Option 2: Create your own offer**


- Select "Bisq Easy" then "Offerbook"
- Choose your trading pair (e.g. BTC/EUR)
- Click on "Create offer
- Follow the offer creation wizard: Define the amount (fixed or range)

![Configuration du montant](assets/fr/20.webp)


- Select accepted payment methods

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Check the summary and publish the offer

![Récapitulatif et publication](assets/fr/22.webp)

Once the exchange has been initiated :


- Send your Bitcoin address or Lightning invoice to the seller

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Receive the seller's bank details

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Make the payment (without mentioning "Bisq" or "Bitcoin")
- Notify the seller of your payment

![Notification paiement](assets/fr/18.webp)


- Wait for the bitcoins to arrive

![Attente réception](assets/fr/19.webp)

### How to sell Bitcoins?

The selling process on Bisq 2 follows a similar logic to that of buying, with the same main steps but in reverse order. You can either create your own offer to sell, or respond to an existing offer to buy. Here's a breakdown of the various options and stages in the process:

**Option 1: Create an offer to sell**


- Select "Bisq Easy" then "Offerbook"
- Click on "Create offer" and choose "Sell Bitcoin"
- Configure your offer :
 - Select currency (EUR, USD, etc.)
 - Choose the accepted payment methods
 - Set the amount (between 6 and 600 USD equivalent)
 - Set your price (fixed or % of market)
- Check details and publish the offer

**Option 2: Take up an existing offer**


- Browse offers in the "Offerbook" tab
- Filter by currency and payment method
- Select an offer that suits you
- Check details and accept the offer

**Sales process:**

Once the exchange has been initiated :


   - Send your bank details to the buyer
   - Wait for the buyer's Bitcoin address
   - Check that the address is valid

After payment notification :


   - Check that payment has been received on your account
   - Confirm that the amount and details match
   - Send bitcoins to the address provided
   - Mark the transaction as completed

Finalization :


   - Wait for confirmation from the buyer
   - Leave feedback on the transaction
   - Build your reputation for future sales

**Important note:** As a seller, you need to be particularly vigilant about the risk of chargebacks. Give preference to secure payment methods, and always check that payment has been received before sending bitcoins.

## Good Practices and Safety

### Safety Tips

**For buyers:**


- Start with small amounts
- Check sellers' reputations (minimum score of 30,000)
- Use only the suggested payment methods
- Check that the seller is active before sending payment
- Use only the bank details provided in the exchange chat
- Never communicate outside the Bisq 2 platform
- Keep proof of payment
- Never send sensitive information

**For sellers:**


- Be careful with new accounts
- Avoid payment methods sensitive to chargebacks (PayPal, Venmo)
- Check that the account details correspond to the buyer
- Limit communication to chat Bisq 2
- Open a mediation in case of doubt

### Reputation building (for salespeople)

To enhance your reputation on Bisq as a seller, conduct regular transactions and maintain professional communication with buyers. Respond quickly to buyer requests to ensure a positive experience. You can also create a BSQ bond to show your commitment to the platform. These actions will build trust and attract more buyers.

### Dispute Resolution


- Contact your counterpart via chat
- If necessary, open a dispute
- Provide all requested proofs
- Follow the mediator's instructions

### Privacy policy :


- No registration or centralized identity verification required
- All connections go through the Tor network (and soon I2P)
- No central server to store data
- Transaction details are only readable by the parties involved

### Protection against censorship :


- Fully distributed P2P network
- Using the Tor network (and soon I2P) to resist censorship
- Open source project managed by a DAO, with no centralized legal entity

## Advantages and disadvantages

### Benefits of Bisq 2


- Maximum confidentiality**: No KYC, use of Tor
- Decentralization**: No central server
- Security**: Open source, non-custodial code
- Intuitive interface**: simpler than Bisq 1
- Flexibility**: Multiple exchange protocols

### Bisq 2 disadvantages


- Limited liquidity** (for the moment) :
 - New protocol in start-up phase
 - Few sales offers available
 - Potentially long waiting times to find a buyer
- Trading limits**: Maximum of USD 600 per transaction (with Bisq easy)
- Desktop only**: No mobile application

## Future Protocols

Although Bisq Easy is currently the only protocol available, several other protocols are under development for Bisq 2 :


- Bisq Lightning**: Exchange protocol based on an escrow system using multiparty computation cryptography on the Lightning network.
- Bisq MuSig**: Migration of the main protocol from Bisq 1 to Bisq 2, using a 2-on-2 multisig with security deposits.
- BSQ Swaps**: Instant atomic swaps between BSQ and BTC.
- Liquid Swaps**: Exchange of assets on the Liquid network (USDT, BTC-L) via atomic swaps.
- Monero Swaps**: Atomic exchanges between Bitcoin and Monero.
- Liquid MuSig**: Version of the multisig protocol using L-BTC for lower costs and greater confidentiality.
- Submarine Swaps**: Exchanges between Bitcoin on the Lightning network and Bitcoin on-chain.
- Stablecoin Swaps**: Atomic exchanges between Bitcoin and USD stablecoins.
- Multisig Options**: Creation of P2P put and call options with BTC blocking in an on-chain multisig transaction.
- Multisig Open Contracts**: Enables the creation of customized conditional contracts using a 2-on-3 multisig system with arbitrage.

These protocols are currently under development and will be progressively integrated into Bisq 2, offering greater flexibility to users according to their specific needs.

## Useful Resources


- Official website: [bisq.network](https://bisq.network)
- Documentation: [Bisq Wiki](https://bisq.wiki)
- Support: [Forum Bisq](https://bisq.community)
- Source code : [GitHub](https://github.com/bisq-network)