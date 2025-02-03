---
name: LNP2PBot
description: Complete guide to LNP2PBot and P2P bitcoin trading
---
![cover](assets/cover.webp)

## Introduction

KYC-free peer-to-peer (P2P) exchanges are essential for preserving users' confidentiality and financial autonomy. They enable direct transactions between individuals without the need for identity verification, which is crucial for those who value privacy. For a more in-depth understanding of the theoretical concepts, take a look at the BTC204 course:

https://planb.network/courses/btc204
Buying and selling bitcoin peer-to-peer (P2P) is one of the most private methods of acquiring or disposing of bitcoins. LNP2PBot is an open source Telegram bot that facilitates P2P exchanges on the Lightning network, enabling fast, low-cost, KYC-free transactions.

### Why use Lnp2pbot?


- No KYC required
- Fast transactions on the Lightning Network
- Low costs
- Simple interface via Telegram, a popular messaging application accessible from anywhere in the world
- Integrated reputation system
- Automatic escrow for secure trading
- Multi-currency support
- Active and growing community

### Prerequisites

To use Lnp2pbot, you will need :

1. Lightning Network wallet (Breez, Phoenix or Blixt recommended)

2. Telegram application installed (https://telegram.org/)

3. A Telegram account with a defined username

## Installation and configuration

### 1. Configuring your Lightning wallet

Start by installing a compatible Lightning wallet. Here are our detailed recommendations:

**Recommended portfolios**


- [Breez](https://breez.technology)**:
  - Excellent for beginners
  - Intuitive, modern interface
  - Non-custodial (you retain control of your funds)
  - Perfectly compatible with Lnp2pbot
  - Available on iOS and Android

Below is the link to the tutorial for this wallet:

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co)** :
  - Simple and reliable
  - Automatic channel configuration
  - Native support for BOLT11 invoices
  - Excellent for everyday transactions
  - Available on iOS and Android

Below is the link to the tutorial for this wallet:

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io)** :
  - More technical but very complete
  - Advanced configuration options
  - Perfect for experienced users
  - Open source
  - Available on Android

Below is the link to the tutorial for this wallet:

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f
**Important notes on other portfolios**

⚠️ **Important**: Before selling sats, make sure your portfolio supports "hold" invoices, which are used by the bot as an escrow system.


- Wallet of Satoshi**: Works well for receiving sats, but can have delays in updating the balance if a sale is cancelled.
- Muun**: Not recommended as payments may fail due to bot routing fee limits (maximum 0.2%).
- Aqua**: Works to receive sats, but can have long delays (up to 48 hours) for balance updates in the event of a sale cancellation.

💡 **Tip**: For optimum experience, opt for recommended portfolios (Breez, Phoenix or Blixt).

⚠️ **Important**: Don't forget to save your recovery phrases in a safe place.

### 2. Getting started with Lnp2pbot

1. Click on this link to access the bot: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram will open automatically

3. Click on "Start" or send the command "/start"

4. The bot will ask you to create a username if you don't already have one

5. The bot will guide you through the initial configuration

### 3. Join the community


- Join the main channel: [@p2plightning](https://t.me/p2plightning)
- Support: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Buying and Selling Bitcoins

There are two main ways to exchange bitcoins on Lnp2pbot:

1. Browse and respond to existing offers in the marketplace

2. Create your own offer to buy or sell

In this guide, we'll take a detailed look at how :


- Buy bitcoins from an existing offer
- Sell bitcoins by creating your own offer

### How to buy Bitcoins

**1. Find and select an offer**

![Sélection d'une offre de vente](assets/fr/01.webp)

Browse the offers in [@p2plightning](https://t.me/p2plightning) and click on the "Buy satoshis" button under the ad you're interested in.

**2. Validate offer and amount**

![Validation de l'offre](assets/fr/02.webp)

1. Return to bot chat

2. Confirm your choice of offer

3. Enter the amount in fiat currency you wish to purchase

4. The bot will ask you to provide a Lightning invoice for the amount in satoshis

**3. Contact the seller**

![Mise en relation](assets/fr/03.webp)

Once the invoice has been sent, the bot puts you in touch with the seller.

**4. Communication with the seller**

![Chat privé](assets/fr/04.webp)

Click on the seller's nickname to open a private chat channel where you can exchange fiat payment details.

**5. Confirmation of payment

![Confirmation du paiement](assets/fr/05.webp)

After making the fiat payment, use the `/fiatsent` command in the bot chat. Once the transaction is complete, you'll be able to rate the seller and the transaction will be closed.

### How to sell Bitcoins

**1. Create a sales offer**

![Création d'une offre de vente](assets/fr/06.webp)

To create a sales offer, simply use the command :

`/sell`

The bot will then guide you step by step:

1. Choose your currency

2. Indicate the amount of satoshis to sell

3. For the price, you have two options:


   - Set a fixed price for the quantity of satoshis
   - Use the market price with the option of applying a premium (positive or negative)

💡 **Tip**: The premium allows you to adjust your price in relation to the market price. For example, a premium of -1% means you're selling for 1% less than the market price.

**2. Confirmation of order creation**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Once the order has been created, you'll see a confirmation with the option to cancel the order using the `/cancel` command.

**3. Manage sales**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- When a buyer responds to your offer, you'll receive a notification with a QR code and an invoice to pay.
- Check the buyer's profile and reputation.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Click on the buyer's nickname to open a private discussion channel.
- Communicate fiat payment details to the buyer.
- Wait for confirmation of fiat payment from the buyer.
- Check that payment has been received on your account.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Confirm the transaction with `/release` and complete the order. You will have the opportunity to rate the buyer.

## Good Practices and Safety

### Safety tips


- Start with small amounts
- Always check users' reputations
- Use only the suggested payment methods
- Keep all communications in bot chat
- Never share sensitive information

### Reputation system


- Each user has a reputation score
- Successful transactions increase your score
- Choose users with a good reputation
- Report any suspicious behavior to the moderators

### Dispute resolution

1. When problems arise, stay calm and professional

2. Use the `/dispute` command to open a ticket

3. Provide all necessary proof

4. Wait for a moderator

## Comparison with other solutions

Lnp2pbot has several advantages and disadvantages over other P2P exchange solutions such as Peach, Bisq, HodlHodl, and Robosat:

### Advantages of Lnp2pbot


- No KYC required** : Unlike some platforms, Lnp2pbot does not require identity verification, thus preserving user confidentiality.
- Fast transactions**: Thanks to the Lightning network, transactions are almost instantaneous.
- Low fees** : Transaction costs are lower than for traditional exchanges.
- Mobile availability**: LNP2PBot is accessible via Telegram, making it easy to use on mobile devices.
- Easy to use** : Lnp2pbot's intuitive interface makes it easy to use, even for less experienced users.

### Disadvantages of Lnp2pbot


- Telegram dependency**: Using Lnp2pbot requires a Telegram account, which may not be suitable for all users.
- Less liquidity**: Compared to more established platforms like Bisq, liquidity can be more limited.

In comparison, solutions such as Bisq offer greater liquidity and a desktop interface, but may involve higher fees and longer transaction times. HodlHodl and Robosat, meanwhile, also offer KYC-free trading, but with different fee structures and interfaces.

## Useful resources


- Official website: https://lnp2pbot.com/
- Documentation: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Support: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)