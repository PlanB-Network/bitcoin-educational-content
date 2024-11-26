---
name: Payjoin - Sparrow Wallet
description: How to make a Payjoin transaction on Sparrow Wallet?
---

![tutorial cover image sparrow payjoin](assets/cover.webp)

_**WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24, Payjoins Stowaway on Samourai Wallet now only work by manually exchanging PSBT between the involved parties, provided both users are connected to their own Dojo. As for Sparrow, Payjoins via BIP78 still work. However, these tools may be restarted in the coming weeks. In the meantime, you can always read this article to understand the theoretical functioning of payjoins._

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

> _"Force blockchain spies to rethink everything they think they know."_

Payjoin is a specific Bitcoin transaction structure that enhances user privacy during spending by collaborating with the payment recipient. There are several implementations that facilitate the setup and automation of PayJoin. Among these implementations, the most well-known is Stowaway developed by the Samourai Wallet team. This tutorial aims to guide you through the process of making a Stowaway Payjoin transaction using the Sparrow Wallet software.

## How does Stowaway work?

As mentioned earlier, Samourai Wallet offers a PayJoin tool called "Stowaway." It is accessible through the Sparrow Wallet software on PC or the Samourai Wallet application on Android. To perform a Payjoin, the recipient, who also acts as a collaborator, must use software compatible with Stowaway, namely Sparrow or Samourai Wallet. These two software are interoperable, allowing for Stowaway transactions between a Sparrow wallet and a Samourai wallet, and vice versa.

Stowaway relies on a category of transactions that Samourai refers to as "Cahoots." A Cahoot is essentially a collaborative transaction between multiple users that requires off-chain information exchange. Currently, Samourai offers two Cahoots tools: Stowaway (Payjoins) and StonewallX2 (which we will explore in a future article).

Cahoots transactions involve exchanging partially signed transactions between users. This process can be lengthy and cumbersome, especially when done remotely. However, it can still be done manually with another user, which can be convenient if the collaborators are physically close. In practice, this involves manually exchanging five QR codes to be scanned successively.

When done remotely, this process becomes too complex. To address this issue, Samourai has developed an encrypted communication protocol based on Tor, called "Soroban." With Soroban, the necessary exchanges for a Payjoin are automated behind a user-friendly interface. This is the second method we will explore in this article.

These encrypted exchanges require establishing a connection and authentication between Cahoots participants. Soroban communications rely on the users' Paynyms. If you are not familiar with Paynyms, I invite you to refer to this article for more details: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/paynym-bip47)
To put it simply, a Paynym is a unique identifier linked to your wallet that allows for various functionalities, including encrypted messaging. The Paynym is presented in the form of an identifier and an illustration representing a robot. Here is an example of mine on the Testnet: ![Paynym Sparrow](assets/en/1.webp)

**In summary:**

- _Payjoin_ = Specific structure of collaborative transaction;
- _Stowaway_ = Payjoin implementation available on Samourai and Sparrow Wallet;
- _Cahoots_ = Name given by Samourai to all their types of collaborative transactions, including Payjoin Stowaway;
- _Soroban_ = Encrypted communication protocol established on Tor, allowing collaboration with other users in the context of a Cahoots transaction.
- _Paynym_ = Unique identifier of a wallet allowing communication with another user on Soroban, in order to
  carry out a Cahoots transaction.

[**-> Learn more about Payjoin transactions and their utility**](https://planb.network/tutorials/privacy/payjoin)

## How to establish a connection between Paynyms?

To perform a remote Cahoots transaction, specifically a PayJoin (Stowaway) via Samourai or Sparrow, it is necessary to "Follow" the user you intend to collaborate with, using their Paynym. In the case of a Stowaway, this means following the person you want to send bitcoins to.

**Here is the procedure to establish this connection:**

First, you need to obtain the recipient's Paynym identifier. This can be done using their nickname or payment code. To do this, from the recipient's Sparrow wallet, select the `Tools` tab, then click on `Show PayNym`.
![Show Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
On your side, open your Sparrow Wallet and access the same `Show PayNym` menu. If you are using your Paynym for the first time, you will need to obtain an identifier by clicking on `Retrieve PayNym`.
![Retrieve paynym](assets/notext/3.webp)
Next, enter your collaborator's Paynym identifier (either their nickname `+...` or their payment code `PM...`) in the `Find Contact` box, then click on the `Add Contact` button.
![add contact](assets/notext/4.webp)
The software will then offer you a `Link Contact` button. It is not necessary to click on this button for our tutorial. This step is only necessary if you plan to make payments to the Paynym indicated in the context of BIP47, which is unrelated to our tutorial.

Once the recipient's Paynym is followed by your Paynym, repeat this operation in the opposite direction so that your recipient also follows you. You can then perform a Payjoin.

## How to perform a Payjoin on Sparrow Wallet?

If you have completed these few preliminary steps, you are finally ready to perform the Payjoin transaction! To do this, follow our video tutorial:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**External resources:**

- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.
