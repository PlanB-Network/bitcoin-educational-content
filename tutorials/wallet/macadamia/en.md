---
name: Macadamia Wallet
description: Cashu mobile wallet for anonymous and instant BTC payments
---

![cover](assets/cover.webp)


Macadamia Wallet is an iOS mobile wallet that implements the Cashu protocol, a Chaumian ecash system enabling totally anonymous Bitcoin payments. Thanks to blind signatures, no observer can link your deposits to your spending, offering confidentiality similar to physical cash.


In this tutorial, we'll look at how to install and configure Macadamia, perform your first Cashu transactions (Mint, Send, Receive, Melt), and manage multiple mints to secure your funds.


## What is Macadamia Wallet?


### The Cashu protocol


Cashu uses blind signatures invented by David Chaum: you deposit bitcoins with a "mint" server, which issues equivalent tokens in satoshis. The mint signs these tokens without seeing their content, making it impossible to link a token to a user. Exchanges are off-chain, peer-to-peer, and totally opaque - even the mint can't track who's paying whom.


Macadamia is an open source wallet iOS developed in Swift/SwiftUI. It works without account or KYC, your tokens are stored locally and protected by a seed phrase. Code is auditable on GitHub and tokens are interoperable with other Cashu wallets (Minibits, Cashu.me).


### Custodial model and compromise


**Important**: Cashu operates on a custodial model. Tokens are promises to pay (IOUs) backed by the mint's Bitcoin reserves. If the mint disappears, your tokens lose their value. This is the compromise for maximum confidentiality.


Use Macadamia as a physical wallet: small amounts only. Spread your funds over several mints to dilute risk.


## Main features


Macadamia implements the four fundamental operations of the Cashu protocol. **Mint** converts your satoshis into tokens via a Lightning invoice. **Send** lets you send tokens free of charge via QR code or link, completely off-chain. **Receive** lets you receive tokens or generate a Lightning invoice. **Melt** pays a Lightning invoice by destroying your tokens.


wallet supports the management of multiple mints simultaneously. You can swap tokens between different mints via Lightning.


## Supported platforms


Macadamia is available only on iOS 17 or higher for iPhone and iPad. The native Swift/SwiftUI application offers optimum integration with the Apple ecosystem.


The Cashu protocol guarantees interoperability between wallets. You can restore your seed phrase in other applications such as Minibits on Android or Nutstash on desktop.


The current version is distributed via TestFlight. Use only small amounts with this beta version.


## Installation


Macadamia is currently available via TestFlight, Apple's beta testing program. Here's how to install it:


### Installation via TestFlight


**Step 1: Download TestFlight**


If you don't already have the TestFlight app on your device, search for "TestFlight" in the App Store and install it. TestFlight is Apple's official application for testing beta versions of iOS applications.


**Step 2: Join the Macadamia beta program** (in French)


Once TestFlight is installed, follow this invitation link from your iPhone or iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)


The link will automatically open TestFlight and offer you to install Macadamia Wallet. Touch "Accept" then "Install" to start the download. The application weighs around ten megabytes and takes just a few seconds to install.


![Installation TestFlight](assets/fr/01.webp)


### Important information about beta versions


Macadamia is still in the active development phase. TestFlight versions are updated frequently and may introduce new features or correct bugs. However, as with any beta version, malfunctions may occur. **We strongly recommend that you use only small amounts**, which you accept could be lost in the event of a technical problem.


Macadamia does not collect any user data according to the displayed privacy policy. Be sure to check that the developer is cypherbase UG when installing.


## Initial configuration


On first launch, Macadamia generates a BIP-39 sentence of 12 words. Write them down in a safe place - never as a screenshot. These words allow you to recreate your wallet and spend your tokens.


![Configuration initiale](assets/fr/02.webp)


Follow the four steps: welcome, accept terms, save seed sentence, and final confirmation.


![Interface principale](assets/fr/03.webp)


Once configuration is complete, Macadamia presents three main tabs. **Wallet** displays your balance and transaction history. **Mints** lets you manage your Cashu servers. **Settings** gives access to settings and your seed phrase.


![Ajout d'un mint](assets/fr/04.webp)


You now need to configure a mint, i.e. a Cashu server that will issue your tokens. Go to the "Mints" tab, tap "Add new Mint URL", and enter the address of your chosen mint (e.g. mint.cubabitcoin.org). Check out bitcoinmints.com or cashu.space for reputable public mints. Validate only mints whose reputation you have checked, as they will have custody of your satoshis.


## Daily use


### Creation of new tokens (Mint)


To feed your wallet Macadamia with ecash, you need to perform a "Mint" operation (to create tokens). Touch "Receive", then choose the "Lightning" option. Enter the desired amount (e.g. 1000 sats), select the mint to be used, then generate the Lightning invoice.


![Opération Mint](assets/fr/05.webp)


Pay the Lightning invoice generated with your usual wallet (Phoenix, Zeus, BlueWallet).


![Confirmation Mint](assets/fr/06.webp)


Cashu tokens appear instantly in your balance after payment.


### Send tokens


To send Cashu tokens to another user, touch the "Send" button on the main screen, then select "Ecash". Enter the amount to be sent (e.g. 50 sats) and add a descriptive memo if required.


![Envoi Ecash](assets/fr/07.webp)


Share the QR code or generated text via iMessage, Signal or Telegram. The recipient claims the funds instantly and free of charge.


### Receive tokens


To receive Cashu tokens sent by another user, touch "Receive" then select "Ecash". Scan the token QR code or paste the token link you received.


![Réception Ecash](assets/fr/08.webp)


Touch "Redeem" to claim token.


### Lightning (Melt) payments


To pay a Lightning invoice with your Cashu tokens, touch "Send" then select "Lightning". Paste a BOLT11 invoice you wish to pay.


![Paiement Lightning](assets/fr/11.webp)


The mint destroys your tokens and executes the Lightning payment. So you can pay for any Lightning service while preserving your anonymity.


### Swap between mints


When you receive tokens from a mint you haven't configured, Macadamia offers you several options for managing these tokens.


![Swap inter-mints](assets/fr/09.webp)


Add the new mint or swap the tokens to an existing mint. The swap uses Lightning as a bridge to transfer your funds anonymously.


### Advanced multi-mint management


Macadamia offers sophisticated tools for managing multiple mints simultaneously and strategically allocating your funds.


![Gestion multi-mints](assets/fr/10.webp)


"Distribute Funds" automatically distributes your balance according to percentages (e.g. 50/50). "Transfer" allows manual transfers between mints to diversify your risks.


## Advantages and limitations


**Highlights** :



- Maximum confidentiality**: Untraceable transactions, even by the mint. No blockchain metadata, trackless peer-to-peer exchanges.
- Fast and free**: Free instant transfers within a mint, ideal for micropayments.
- Interoperability**: standardized Cashu tokens for use with other compatible wallets (Minibits, Nutstash).
- Simplicity**: Interface iOS native is accessible to beginners while remaining auditable (open source).


**Constraints** :



- Custodial model**: mint trust required. If a mint disappears, your tokens lose their value.
- iOS only**: No Android/desktop version. Cashu interoperability allows access via other wallets, but the optimal experience remains iOS.
- Mint dependency**: Mint offline = unable to carry out transactions requiring its intervention (Mint, Melt).
- Emerging technology** : Active development, possible bugs, evolving standards.


## Best practices



- Diversify your mints**: Spread your chips across several reputable mints to dilute risk.
- Limit amounts**: Use Macadamia as a physical wallet for daily payments, not as a safe.
- Secure your seed**: Keep your 12-word phrase on paper in a safe place. Test restoration occasionally.
- Check mints**: Consult cashu.space and community forums before adding a mint. Choose those with good uptime and a solid reputation.
- VPN or Tor**: Hide your IP with VPN/Tor to maximize network privacy.
- Join the community**: Telegram/Discord Cashu groups for updates, mint recommendations and best practices.


## Conclusion


Macadamia Wallet brings the properties of physical cash to digital Bitcoin. By combining Chaum and Lightning blind signatures, it offers an elegant solution for transactional confidentiality. Its native iOS interface makes sophisticated cryptographic technology accessible while remaining open source and interoperable with the Cashu ecosystem.


The custodial model demands vigilance and good security practices. Used correctly, Macadamia becomes an invaluable tool for everyday payments requiring anonymity, complementing non-custodial wallets for savings.


## Resources


### Official documentation


- Official website: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub source code: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)


### Cashu documentation


- Technical documentation: [docs.cashu.space](https://docs.cashu.space)
- List of public mints: [bitcoinmints.com](https://bitcoinmints.com)
- Official protocol website: [cashu.space](https://cashu.space)


### Community


- Telegram Cashu group: [t.me/cashu_ecash](https://t.me/cashu_ecash)