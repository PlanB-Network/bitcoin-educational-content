---
name: Boltz
description: Swap between different Bitcoin layers while maintaining control.
---


![cover](assets/cover.webp)


Since its deployment in 2009, Bitcoin's peer-to-peer electronic cash system has grown exponentially, giving life to solutions that today enable it to be a system we can use instantly in our everyday actions, notably through Lightning Network.


However, a major problem remained between the Bitcoin protocol layers: fluid interoperability. In order to exploit the full potential of Bitcoin, it was imperative to find a solution that would enable transactions between the different layers of the protocol. This need gave rise in 2019 to Boltz, a bridge that links several Bitcoin layers.


## What is Boltz?


[Boltz](https://boltz.Exchange) is a non-custodial platform ideal for anyone wishing to transact between the different layers of the Bitcoin protocol:


- on chain**: Bitcoin's main chain where transactions are confirmed every 10 minutes on average, transaction fees are often high, which does not necessarily meet users' needs ;
- Lightning Network**: The Bitcoin overlay for instant payments at low fees, allowing the Bitcoin to be used for daily payments;
- Liquid Network**: an overlay for Bitcoin created by Blockstream, enabling fast, confidential transactions and the use of other Bitcoin-based financial instruments;
- RootStock**: A solution for developing smart contracts based on the Bitcoin protocol.


![layers](assets/fr/01.webp)


Interoperability between these different layers is of major importance, as it gives users the flexibility they need to take full advantage of everything the Bitcoin ecosystem has to offer.


Boltz uses atomic swaps. This technology enables bitcoins to be exchanged between 2 layers (e.g. BTC onchain in exchange for BTC on Lightning) directly between two parties, without the need for trust and without the need for an intermediary. These exchanges are called "atomic" because they can only produce two results:


- Either the exchange is successful and the two participants have effectively exchanged their BTC ;
- Either the exchange fails, and both participants leave with their original BTC.


In this way, you retain permanent self-custody of your bitcoins, and the exchange is not based on any trust in the counterparty: either the exchange succeeds or fails, but neither party can steal the other's funds.


An atomic exchange works with smart contracts [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). In this type of contract, the amount is "locked" in a two-way channel and a time restriction is introduced, so that if the transaction is not completed within a certain time, the balance reverts to the depositor. This is the mechanism used by the Boltz platform.


## Your first exchanges with Boltz


Boltz is a non-depository web platform that requires no personal information from you. Boltz has a minimalist, fluid Interface that allows you to start trading in less than a minute.


![boltz](assets/fr/02.webp)


Once on the platform, you can create atomic exchanges between the different layers of the Bitcoin ecosystem.


![home](assets/fr/03.webp)


You'll see the minimum and maximum number of satoshis (the smallest unit of Bitcoin) you can trade via Boltz, including network charges and a percentage levied by Boltz of between 0.1% and 0.5%.


![fees](assets/fr/04.webp)


Then select the layer from which you wish to make an atomic exchange, and select the layer on which you wish to receive the bitcoins.


![couches](assets/fr/05.webp)


In this tutorial, we'll be focusing on atomic exchange from the main layer to Lightning Network.


You can configure the base unit for your exchanges by choosing between the options :


- BTC ;
- Sats.


![unités](assets/fr/06.webp)


Once you've completed your basic configurations, insert the amount of your atomic exchange, then create a Lightning invoice for the equivalent amount, or simply insert your LNURL.


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)


To be on the safe side, please check the parameters of your atomic exchange to export the backup keys linked to your exchange.


On the **Settings** icon, download the backup key and save the file appropriately.


![settings](assets/fr/08.webp)


![rescue-key](assets/fr/09.webp)


This file contains the 12 keywords of the portfolio associated with your atomic exchanges.


Then click on the **Create atomic exchange** button and proceed with payment of the indicated amount.


![payment](assets/fr/10.webp)


https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Once your payment has been made and confirmed, you will automatically receive the equivalent amount on your Lightning wallet.


In the **Refund** menu, find your atomic exchange history to identify the exchange on which you wish to be refunded. You can also import a history of exchanges you've made on another device, for example, using the backup key file associated with these exchanges.


![refund](assets/fr/11.webp)


In the **History** menu, you can download a more detailed history of the exchanges associated with your rescue key by clicking on the **Backup** button.


![backup](assets/fr/12.webp)


⚠️ Please do not divulge this file either, as it contains all the information associated with your transactions and the backup key linked to these transactions.


Boltz offers you a high level of confidentiality thanks to its access via a `.onion` link on the Tor network. Make atomic exchanges totally anonymous by selecting the **Onion** menu, after activating Tor browsing in your browser.


![onion](assets/fr/13.webp)


https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

By now you're familiar with Boltz, a unique exchange platform that enables interoperability between the different layers of the Bitcoin ecosystem.