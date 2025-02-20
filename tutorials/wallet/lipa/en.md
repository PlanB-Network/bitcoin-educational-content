---
name: Lipa
description: Setting up and using the Lipa lightning mobile wallet
---
![cover](assets/cover.webp)

A Bitcoin Lightning wallet is a mobile application that enables instant, low-cost transactions on Bitcoin's Lightning network. Unlike transactions on the main blockchain (on-chain), Lightning payments are near-instantaneous and require minimal fees, making them particularly suitable for small, everyday payments.

Lightning wallets, like all mobile wallets, are considered "hot" wallets because they are connected to the Internet. They are therefore primarily intended for managing small amounts of money for your day-to-day spending. For larger amounts, it is preferable to use more secure storage solutions such as hardware wallets.

If you would like to learn more about the Lightning network and understand how it works technically, I recommend you take this course:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
In this tutorial, we'll be taking a look at **Lipa**, a simple and effective Lightning wallet developed in Switzerland.

## Introducing Lipa

Lipa is a non-custodial Lightning wallet distinguished by its simplicity of use and uncluttered interface. Developed by a Swiss team, it emphasizes confidentiality and ease of use for beginners.

Key features include:


- Intuitive user interface
- Autonomous Lightning channel management
- LNURL protocol support
- Possibility of buying bitcoins directly in the application

## Installing and configuring Lipa

The first step is to download the Lipa app. For the moment, it is only available on iOS :


- [For Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

The Android version is currently under development and will be available soon.

![Installation de Lipa](assets/fr/01.webp)

Once you've launched the application, you'll arrive on the home screen, which offers you two options:


- Create a new wallet
- Restore an existing wallet from a backup

Once you've chosen your option, the application prompts you to enable notifications. This step is important, as notifications are necessary for :


- Receive alerts when payments are received, even when the application is closed
- Be informed of the steps involved in buying bitcoin via their integrated solution

The application then presents its main functions through a series of introductory screens:


- Seamless payment receipt**: Users can receive Bitcoin payments even when the application is closed, guaranteeing reliability and convenience.
- Non-custodial Lightning addresses**: Lipa now supports non-custodial Lightning addresses, enhancing privacy and security by giving users full control over their bitcoins.
- Control over analytical data** : With transparency and confidentiality paramount, users can view the types of data collected and choose their sharing preferences.
- Send via phone number**: No need for complex addresses - simply select a contact, enter the amount, and send bitcoins directly to their phone number.

The application also benefits from continuous improvements in terms of stability, security and reliability, to guarantee an optimal user experience.

## Application navigation

Lipa's interface is organized around 4 main tabs accessible via the navigation bar at the bottom of the screen:

![Navigation principale](assets/fr/02.webp)


- Home**: Displays your current balance and transaction history
- Scanner**: Allows you to scan QR codes to make payments
- Map**: Displays an interactive map of Bitcoin-accepting businesses in your area
- Settings**: Access to application settings, backup and preferences

An additional menu can be accessed by pulling down the home screen:

![Menu supplémentaire](assets/fr/03.webp)

This gesture reveals additional functions such as :


- Buying bitcoins
- On-chain bitcoin deposit
- Creating Lightning invoices to receive bitcoins
- Lightning invoice payment

## Save your wallet

To back up your wallet, go to the "Settings" tab and select "Recovery phrase". Lipa uses a recovery phrase which it is essential to write down carefully on a physical medium (paper, metal). This phrase is the only way to recover your funds if your phone is lost or stolen. To validate your backup, the application will ask you to confirm 3 random words from your phrase.

![Backup](assets/fr/04.webp)

For more information on how to properly back up and manage your recovery phrase, I highly recommend following this other tutorial, especially if you're a beginner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Receive bitcoins

To receive bitcoins, you have two options. To access these options, return to the home screen and pull down the screen. Then you can either :


- Select "Transfer BTC" to receive bitcoins on-chain. Then simply scan the QR code with your other wallet and complete the transaction.
- Select "Request" to receive via the Lightning network and enter the amount you wish to receive.

In both cases, you'll have to pay a fee equivalent to 0.4% of the amount, or around 2,500 sats if the application has to open a new payment channel (which will inevitably be the case for the first payment).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Send bitcoins

To send bitcoins, go to the home screen, pull down the screen and select "Pay". Then simply either :


- enter a lightning LNURL address
- scan a lightning QR code to make the payment.

You can also go to the second tab at the bottom of the screen to scan a QR code directly.

![Envoi de bitcoins](assets/fr/07.webp)

## Buy bitcoins

Lipa offers the possibility of purchasing bitcoins directly in the application for a fee of 1.5%. To make a purchase, go to the home screen and pull down to display the menu. Then select "Buy BTC". Three introductory screens will guide you through the purchase process.

![Menu d'achat](assets/fr/08.webp)

Then simply enter the bank details of the account you will be using to make the purchase. Choose your currency and enter your e-mail address.

After the loading screen, you'll find the reference number to be included in the transfer you're about to make, as well as the bank details for the exchange.

![Sélection du montant](assets/fr/09.webp)

All you have to do is use your bank to transfer the desired amount, set up the transfer by indicating the RIB previously retrieved and indicate the reference at the time of the transaction so that Lipa can associate this bank movement with your Lipa wallet.

![Confirmation d'achat](assets/fr/10.webp)

## Advantages and disadvantages

### Benefits


- Intuitive interface
- Correct service charges
- Non custodial
- Integrated bitcoin purchasing solution
- BTCmap integration
- NFC support

### Disadvantages


- It's not possible to send bitcoins on chain
- Slightly longer than average payment

Lipa is an excellent choice for getting started with the Lightning Network, particularly suited to users looking for a simple solution for everyday payments. Its ease of use and uncluttered interface make it an ideal wallet for beginners, while offering the essential features for everyday Lightning use.

## Resources


- [Lipa's official website](https://lipa.swiss/)
- [Lipa support](https://getlipa.atlassian.net/servicedesk/customer/portal/1)