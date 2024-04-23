---
name: Payjoin - Samourai Wallet
description: How to perform a Payjoin transaction on Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)

> *"Force blockchain spies to rethink everything they think they know."*

Payjoin is a specific Bitcoin transaction structure that enhances user privacy during a spend by collaborating with the payment recipient. There are several implementations that facilitate the setup and automation of PayJoin. Among these implementations, the most well-known is Stowaway, developed by the teams at [Samourai Wallet](https://samouraiwallet.com/stowaway). This tutorial explains how to perform a Stowaway Payjoin transaction using the Samourai Wallet application.

## How does Stowaway work?

As mentioned earlier, Samourai Wallet offers a PayJoin tool called "Stowaway." It is accessible through the Sparrow Wallet software on PC or the Samourai Wallet application on Android. To perform a Payjoin, the recipient, who also acts as a collaborator, must use software compatible with Stowaway, namely Sparrow or Samourai. These two software are interoperable, allowing for a Stowaway transaction between a Sparrow wallet and a Samourai wallet, and vice versa.

Stowaway relies on a category of transactions that Samourai refers to as "Cahoots." A Cahoot is essentially a collaborative transaction between multiple users, requiring off-chain information exchange. To date, Samourai offers two Cahoots tools: Stowaway (Payjoins) and StonewallX2 (which we will explore in a future article).

Cahoots transactions involve exchanges of partially signed transactions between users. This process can be lengthy and cumbersome, especially when done remotely. However, it can still be manually performed with another user, which can be convenient if the collaborators are physically close. In practice, this involves manually exchanging five QR codes to be scanned successively.

When done remotely, this process becomes too complex. To address this issue, Samourai has developed an encrypted communication protocol based on Tor, called "Soroban." With Soroban, the exchanges necessary for a Payjoin are automated behind a user-friendly interface. This is the second method we will study in this article.

These encrypted exchanges require establishing a connection and authentication between the Cahoots participants. Soroban communications are therefore based on the users' Paynyms. If you are not familiar with Paynyms, I invite you to consult this article for more details: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/paynym-bip47).
To put it simply, a Paynym is a unique identifier linked to your wallet that allows for various functionalities, including encrypted messaging. The Paynym is presented in the form of an identifier and an illustration representing a robot. Here is an example of mine on the Testnet: ![paynym samourai wallet](assets/en/1.webp)

**In summary:**
- _Payjoin_ = Specific structure of collaborative transactions;
- _Stowaway_ = Payjoin implementation available on Samourai and Sparrow Wallet;
- _Cahoots_ = Name given by Samourai to all their types of collaborative transactions, including Payjoin Stowaway;
- _Soroban_ = Encrypted communication protocol established on Tor, allowing collaboration with other users in the context of a Cahoots transaction;
- _Paynym_ = Unique identifier of a wallet allowing communication with another user on Soroban, in order to carry out a Cahoots transaction.

[**-> Learn more about Payjoin transactions and their utility**](https://planb.network/tutorials/privacy/payjoin)

## How to establish a connection between Paynyms?

To carry out a remote Cahoots transaction, specifically a PayJoin (Stowaway) via Samourai, it is necessary to "Follow" the user with whom you intend to collaborate, using their Paynym. In the case of a Stowaway, this means following the person to whom you want to send bitcoins.

**Here is the procedure to establish this connection:**

To begin, you need to obtain the payment code of the recipient's Paynym for the Payjoin. In the Samourai Wallet application, the recipient must tap on the icon of their Paynym (the little robot) located at the top left of the screen, and then click on their Paynym nickname, starting with `+...`. For example, mine is `+namelessmode0aF`. If your collaborator uses Sparrow Wallet, I invite you to consult our dedicated tutorial by clicking here.

![connexion paynym samourai](assets/en/2.webp)

Your collaborator will then be redirected to their Paynym page. From there, they can either share their Paynym credentials with you or share their QR code for you to scan. To do this, they must click on the small "share" icon located at the top right of their screen.
![partager paynym samourai](assets/en/1.webp)

On your side, launch your Samourai Wallet application and access the "PayNyms" menu in the same way. If this is your first time using your Paynym, you will need to obtain the identifier.

![demander un paynym](assets/en/3.webp)

Then click on the blue "+" at the bottom right of the screen.
![ajouter paynym collaborateur](assets/en/4.webp)
You can then paste your collaborator's payment code by selecting `COLLER LE CODE PAIEMENT`, or open the camera to scan their QR code by pressing `SCANNEZ LE CODE QR`.![paste paynym identifier](assets/en/5.webp)

Click on the `SUIVRE` button.
![follow paynym](assets/en/6.webp)
Confirm by clicking `YES`.
![confirm follow paynym](assets/en/7.webp)
The software will then offer you a `SE CONNECTER` button. It is not necessary to click on this button for our tutorial. This step is only required if you plan to make payments to the other Paynym as part of the [BIP47](https://planb.network/tutorials/privacy/paynym-bip47), which is unrelated to our tutorial.
![connect paynym](assets/en/8.webp)
Once the recipient's Paynym is followed by your Paynym, repeat this operation in the opposite direction so that the recipient also follows you. You can then perform a Payjoin.

## How to do a Payjoin on Samourai Wallet?

If you have completed these preliminary steps, you are finally ready to perform the Payjoin transaction! To do this, follow our video tutorial:

![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**External resources:**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://samouraiwallet.com/stowaway.
