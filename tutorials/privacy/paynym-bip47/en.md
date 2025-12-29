---
name: BIP47 - PayNym
description: Use a reusable payment code on Ashigaru
---
![cover](assets/cover.webp)


The worst privacy mistake you can make on Bitcoin is reusing addresses. Every time the same address receives several payments, these transactions are linked together, providing the world with a map of your transactions. It is therefore strongly recommended that you always generate a unique address for each receipt. But for some Bitcoin applications, this is not a simple matter.


BIP47, proposed by Justus Ranvier in 2015, provides an elegant answer to this problem. It introduces the concept of a **reusable payment code**: a unique identifier enabling a virtually unlimited number of onchain bitcoin payments to be received, without ever reusing an address. Thanks to a cryptographic mechanism based on an ECDH (*Diffie-Hellman on elliptic curves*) exchange, each payment to the same code results in a blank address, specific to the relationship between sender and recipient.


![Image](assets/fr/01.webp)


This BIP47 principle is implemented in particular by **PayNym**, the system originally developed by Samourai Wallet and now taken over by Ashigaru. In this tutorial, we'll look at how to activate your PayNym, exchange payment codes with a correspondent and carry out transactions without reusing an address.


I won't go into the detailed operation of the BIP47 here. If you'd like to delve deeper into the subject, please refer to chapter 6.6 of my BTC 204 training course.


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prerequisites


To follow this tutorial, all you need is a wallet on the Ashigaru app. If you don't know how to download, verify, install the application or create a wallet, I recommend you consult this tutorial first:


https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Request PayNym


The first step is to claim your PayNym. This operation only needs to be carried out once per wallet. It associates your BIP47 payment code derived from your seed (`PM...`) with a unique identifier specific to the PayNym implementation. This shorter, more legible identifier can then be transmitted to your correspondents to facilitate exchanges, without having to share the long, complete BIP47 code.


To do so, click on your PayNym image at the top left of the interface, then on your payment code `PM...`.


![Image](assets/fr/02.webp)


Then click on the three small dots in the top right-hand corner, and select `Claim PayNym`.


![Image](assets/fr/03.webp)


Confirm by clicking on the `CLAIM YOUR PAYNYM` button.


![Image](assets/fr/04.webp)


Refresh the page: your PayNym ID is now displayed below your image, just above your BIP47 payment code.


![Image](assets/fr/05.webp)


Your PayNym is now active and ready to be used for your first BIP47 transactions.


## Connect with a contact


There are two types of connection between PayNym: **follow** and **connect**. The `follow` operation is completely free of charge. It establishes a link between two PayNym through Soroban, a Tor-based encrypted communication protocol developed by the Samourai team and adopted by Ashigaru. This link enables two users following each other to exchange information privately, in particular to coordinate collaborative transactions such as Stowaway or StonewallX2, which we'll look at in another tutorial. This step is specific to PayNym and is not part of the BIP47 protocol.


![Image](assets/fr/06.webp)


The connection operation (`connect`), on the other hand, requires a on-chain transaction. It consists in performing a notification transaction as defined in BIP47. This Bitcoin transaction contains metadata in a `OP_RETURN` output, which establishes an encrypted communication channel between the payer and the recipient. From this channel, the payer will be able to generate unique receiving addresses for each payment, and the recipient will be notified of these payments, and will be able to generate the private keys associated with the addresses to spend these funds later.


This notification transaction has a cost: the mining fee and 546 sats sent to the recipient's notification address to signal the connection. Once the connection has been established, an almost infinite number of payments can be made via BIP47.


In a nutshell:


- follow": free, establishes encrypted communication via Soroban, useful for Ashigaru's collaborative tools;
- `Connect`: chargeable, performs the BIP47 notification transaction to activate the channel between payer and recipient.


To interact with a PayNym, you must first *follow* it. This is the first step before establishing a BIP47 connection. Let's say you want to send recurring payments to PayNym `+instinctiveoffer10`.


Go to your PayNym page on Ashigaru, then click on the `+` button at the bottom right of the interface.


![Image](assets/fr/07.webp)


You can then either paste in the recipient's full payment code, or scan their QR code.


![Image](assets/fr/08.webp)


If you only have his PayNym ID, go to [Paynym.rs](https://paynym.rs/) to find the QR code associated with his payment code.


![Image](assets/fr/09.webp)


Once you've scanned the QR code, click on the `FOLLOW` button to follow the PayNym.


![Image](assets/fr/10.webp)


The `FOLLOW` action is sufficient for collaborative transactions (*cahoots*). However, to send BIP47 payments, you need to establish a connection: click on `CONNECT` to perform the notification transaction.


![Image](assets/fr/11.webp)


The notification transaction is then broadcast on the network. Wait until it has at least one confirmation before making your first payment.


![Image](assets/fr/12.webp)


## Make a BIP47 payment


You are now connected to the recipient and can send a payment to a unique address, automatically generated using the BIP47 protocol, without any prior exchange with the recipient.


From your PayNym main page, click on the contact to whom you wish to send a payment.


![Image](assets/fr/13.webp)


At the top right of the interface, click on the arrow icon.


![Image](assets/fr/14.webp)


Enter the amount to be sent. You don't need to enter a receiving address: it will be automatically derived using the BIP47 protocol.


![Image](assets/fr/15.webp)


Carefully check the transaction details, including fees, then drag the green arrow at the bottom of the screen to sign and broadcast the transaction.


![Image](assets/fr/16.webp)


The transaction has been sent.


![Image](assets/fr/17.webp)


In this example, the payment was made to another of my PayNym wallets. I can therefore see that it has arrived on my other Ashigaru wallet, without any address having been exchanged manually: only the PayNym identifier was used.


![Image](assets/fr/18.webp)


You now know how to use BIP47 reusable payment codes thanks to the PayNym implementation on the Ashigaru application. You can now share this payment code with anyone who wants to send you payments (especially recurring payments). You can also publish your PayNym ID on your website or social networks to receive donations.


To deepen your knowledge of this protocol, understand in detail how it works and its implications for confidentiality, I strongly recommend that you take my BTC 204 course:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c