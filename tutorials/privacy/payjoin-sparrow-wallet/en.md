---
name: Payjoin - Sparrow Wallet
description: How to make a Payjoin transaction on Sparrow Wallet?
---
![tutorial cover image sparrow payjoin](assets/cover.jpeg)

> *"Force blockchain spies to rethink everything they think they know."*

Payjoin is a specific Bitcoin transaction structure that enhances user privacy during spending by collaborating with the payment recipient. There are several implementations that facilitate the setup and automation of PayJoin. Among these implementations, the most well-known is Stowaway developed by the [Samourai Wallet](https://samouraiwallet.com/stowaway) team. This tutorial aims to guide you through the process of making a Stowaway Payjoin transaction using the Sparrow Wallet software.

## How does Stowaway work?

As mentioned earlier, Samourai Wallet offers a PayJoin tool called "Stowaway." It is accessible through the Sparrow Wallet software on PC or the Samourai Wallet application on Android. To perform a Payjoin, the recipient, who also acts as a collaborator, must use software compatible with Stowaway, namely Sparrow or Samourai Wallet. These two software are interoperable, allowing for Stowaway transactions between a Sparrow wallet and a Samourai wallet, and vice versa.

Stowaway relies on a category of transactions that Samourai refers to as "Cahoots." A Cahoot is essentially a collaborative transaction between multiple users that requires off-chain information exchange. Currently, Samourai offers two Cahoots tools: Stowaway (Payjoins) and StonewallX2 (which we will explore in a future article).

Cahoots transactions involve exchanging partially signed transactions between users. This process can be lengthy and cumbersome, especially when done remotely. However, it can still be done manually with another user, which can be convenient if the collaborators are physically close. In practice, this involves manually exchanging five QR codes to be scanned successively.

When done remotely, this process becomes too complex. To address this issue, Samourai has developed an encrypted communication protocol based on Tor, called "Soroban." With Soroban, the necessary exchanges for a Payjoin are automated behind a user-friendly interface. This is the second method we will explore in this article.

These encrypted exchanges require establishing a connection and authentication between Cahoots participants. Soroban communications rely on the users' Paynyms. If you are not familiar with Paynyms, I invite you to refer to this article for more details: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/paynym-bip47).
To put it simply, a Paynym is a unique identifier linked to your wallet that allows for various functionalities, including encrypted messaging. The Paynym is presented in the form of an identifier and an illustration representing a robot. Here is an example of mine on the Testnet: ![Paynym Sparrow](assets/en/1.png)

**In summary:**
- *Payjoin* = Specific structure of collaborative transaction;
- *Stowaway* = Payjoin implementation available on Samourai and Sparrow Wallet;
- *Cahoots* = Name given by Samourai to all their types of collaborative transactions, including Payjoin Stowaway;
- *Soroban* = Encrypted communication protocol established on Tor, allowing collaboration with other users in the context of a Cahoots transaction.
- *Paynym* = Unique identifier of a wallet allowing communication with another user on Soroban, in order to carry out a Cahoots transaction.

## How to establish a connection between Paynyms?

To perform a remote Cahoots transaction, specifically a PayJoin (Stowaway) via Samourai or Sparrow, it is necessary to "Follow" the user you intend to collaborate with, using their Paynym. In the case of a Stowaway, this means following the person you want to send bitcoins to.

**Here is the procedure to establish this connection:**

First, you need to obtain the recipient's Paynym identifier. This can be done using their nickname or payment code. To do this, from the recipient's Sparrow wallet, select the `Tools` tab, then click on `Show PayNym`.
![Show Paynym](assets/en/2.png)
![Paynym Sparrow](assets/en/1.png)
On your side, open your Sparrow Wallet and access the same `Show PayNym` menu. If you are using your Paynym for the first time, you will need to obtain an identifier by clicking on `Retrieve PayNym`.
![Retrieve paynym](assets/en/3.png)
Next, enter your collaborator's Paynym identifier (either their nickname `+...` or their payment code `PM...`) in the `Find Contact` box, then click on the `Add Contact` button.
![add contact](assets/en/4.png)
The software will then offer you a `Link Contact` button. It is not necessary to click on this button for our tutorial. This step is only necessary if you plan to make payments to the Paynym indicated in the context of [BIP47](https://planb.network/tutorials/privacy/paynym-bip47), which is unrelated to our tutorial.

Once the recipient's Paynym is followed by your Paynym, repeat this operation in the opposite direction so that your recipient also follows you. You can then perform a Payjoin.

## How to perform a Payjoin on Sparrow Wallet?
If you have completed these few preliminary steps, you are finally ready to perform the Payjoin transaction! To do this, follow our video tutorial:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**External resources:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.
