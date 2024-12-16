---
name: Theoretical introduction to the Lightning Network
goal: Discover the Lightning Network from a technical perspective
objectives: 
  - Understand how network channels work.
  - Familiarize yourself with the terms HTLC, LNURL and UTXO.
  - Understand liquidity management and LNN fees.
  - Recognize the Lightning Network as a network.
  - Understand the theoretical uses of the Lightning Network.
---
# A journey to Bitcoin's second layer

Dive into the heart of the Lightning Network, an essential system for the future of Bitcoin transactions. LNP201 is a theoretical course on the technical operation of Lightning. It reveals the fundamentals and inner workings of this second-layer network, designed to make Bitcoin payments fast, economical and scalable.

Thanks to its network of payment channels, Lightning enables fast, secure transactions without registering each exchange on the Bitcoin blockchain. Over the course of the chapters, you'll learn how channels are opened, managed and closed, how payments are securely routed via intermediate nodes while minimizing the need for trust, and how to manage liquidity. You'll discover what commitment transactions are, HTLC, revocation keys, punishment mechanisms, onion routing and invoices.

Whether you're a beginner or a more experienced Bitcoin user, this course will provide you with invaluable information for understanding and using the Lightning Network. Although we'll cover some of the fundamentals of how Bitcoin works in the first few parts, it's essential to master the basics of Satoshi's invention before diving into LNP201.

Enjoy your discovery!

+++
# The fundamentals

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Understanding the Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Comprendre le lightning Network](https://youtu.be/PszWk046x-I)

Welcome to LNP201, a training course designed to explain the technical operation of the Lightning Network.

The Lightning Network is a payment channel network built on top of the Bitcoin protocol, aimed at enabling fast, low-cost transactions. It enables the creation of payment channels between participants, within which transactions can be carried out almost instantaneously and at minimal cost, without having to register each transaction individually on the blockchain. The Lightning Network thus aims to improve Bitcoin's scalability and make it possible to use it for low-value payments.

Before exploring the "network" aspect, it's important to understand the concept of a **payment channel** on Lightning, how it works and its specific features. This is the subject of this first chapter.

### The payment channel concept

A payment channel allows two parties, in this case **Alice** and **Bob**, to exchange funds on the Lightning network. Each protagonist has a node, symbolized by a circle, and the channel between them is represented by a segment.

![LNP201](assets/fr/01.webp)

In our example, Alice has 100,000 satoshis on her side of the channel, and Bob has 30,000, for a total of 130,000 satoshis, which is the **channel capacity**.

**But what is a satoshi?**

The **satoshi** (or "sat") is a unit of account in Bitcoin. Like a cent for the euro, a satoshi is simply a fraction of a Bitcoin. One satoshi is equivalent to **0.00000001 Bitcoin**, or one hundred millionth of a Bitcoin. Using satoshi becomes increasingly practical as Bitcoin's value rises.

### Allocation of funds in the channel

Back to the payment channel. The key notion here is "channel side". Each participant has funds on his side of the channel: Alice 100,000 satoshis and Bob 30,000. As we've seen, the sum of these funds represents the total capacity of the channel, an element fixed when it was opened.

![LNP201](assets/fr/02.webp)

Let's take an example of a Lightning transaction. If Alice wishes to send 40,000 satoshis to Bob, this is possible, as she has sufficient funds (100,000 satoshis). After this transaction, Alice will have 60,000 satoshis on her side and Bob will have 70,000.

![LNP201](assets/fr/03.webp)

The **channel capacity** of 130,000 satoshis remains constant. What changes is the allocation of funds. This system doesn't allow you to send more funds than you have. For example, if Bob wanted to send 80,000 satoshis back to Alice, he couldn't, because he only has 70,000.

Another way to imagine the allocation of funds is to imagine a **cursor** that indicates where the funds are in the channel. Initially, with 100,000 satoshis for Alice and 30,000 for Bob, the cursor is logically on Alice's side. After the transaction of 40,000 satoshis, the cursor will move slightly to Bob's side, who now has 70,000 satoshis.

![LNP201](assets/fr/04.webp)

This representation can be useful for imagining the balance of funds in a channel.

### The fundamental rules of a payment channel

The first point to remember is that the **channel capacity** is fixed. It's a bit like the diameter of a pipe: it determines the maximum quantity of funds that can be sent through the channel at one time.

For example, if Alice has 130,000 satoshis of her own, she can only send Bob a maximum of 130,000 satoshis in a single transaction. However, Bob can then send these funds back to Alice, either partially or in full.

What's important to understand is that the channel's fixed capacity limits the maximum amount of a transaction, but not the total number of possible transactions, nor the overall volume of funds exchanged within the channel.

**What should you learn from this chapter?

- The capacity of a channel is fixed and determines the maximum amount that can be sent in a single transaction.
- The funds in a channel are divided between the two participants, and each can only send the other the funds it has on its side.
- The Lightning Network enables funds to be exchanged quickly and efficiently, while respecting the limitations imposed by channel capacity.
That's the end of this first chapter, in which we've laid the foundations of the Lightning Network. In the next few chapters, we'll look at how to open a channel and expand on the concepts we've covered here.

## Bitcoin, addresses, UTXO and transactions

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, adresses, utxo et transactions](https://youtu.be/cadCJ2V7zTg)

This chapter is a little special in that it's not directly dedicated to Lightning, but to Bitcoin. Indeed, the Lightning Network is a Bitcoin overlay. It is therefore essential to have a good understanding of certain fundamental Bitcoin concepts if we are to correctly grasp how Lightning works in subsequent chapters. In this chapter, we'll review the basics of Bitcoin receiving addresses, UTXOs and how Bitcoin transactions work.

### Bitcoin addresses, private and public keys

A Bitcoin address is a sequence of characters derived from a **public key**, itself calculated from a **private key**. As you probably know, we use it to lock bitcoins, which is equivalent to receiving them in our wallet.

The private key is a secret element that **must never be shared**, whereas the public key and address can be shared without any security risk (their disclosure only represents a risk to your confidentiality). Here's a common representation we'll be adopting throughout this training course:

- Private keys** will be represented **vertically**.
- The **public keys** will be represented **horizontally**.
- Their color indicates who owns them (Alice in orange and Bob in black...).
### Bitcoin transactions: sending funds and scripts

In Bitcoin, a transaction consists of sending funds from one address to another. For example, Alice sends 0.002 Bitcoin to Bob. Alice uses the private key associated with her address to **sign** the transaction, proving that she is indeed able to spend these funds. But what exactly is going on behind this transaction? The funds on a Bitcoin address are locked by a **script**, a kind of mini-program which imposes certain conditions on the spending of the funds.

The most common script requires a signature with the private key associated with the address. When Alice signs a transaction with her private key, she **unlocks the script** blocking the funds, and they can then be transferred. Transferring the funds involves adding a new script to the funds, stipulating that to spend them, this time a signature with **Bob's** private key is required.

![LNP201](assets/fr/05.webp)

### UTXO: Unspent Transaction Outputs

On Bitcoin, what we actually exchange are not bitcoins directly, but **UTXO** (_Unspent Transaction Outputs_).

A UTXO is a piece of bitcoin that can be of any value, for example **2,000 bitcoins**, **8 bitcoins** or **8,000 sats**. Each UTXO is blocked by a script, and to spend it, you need to satisfy the conditions of the script, often a signature with the private key corresponding to a given receiving address.

UTXO cannot be divided. Whenever they are used to spend the amount of bitcoins they represent, it must be done in full. It's a bit like a banknote: if you have a €10 bill and you owe the baker €5, you can't just cut the bill in half. You have to give him the €10 bill, and he'll give you €5 change. It's exactly the same principle for UTXO on Bitcoin! For example, when Alice unlocks a script with her private key, she unlocks the entire UTXO. If she wishes to send only part of the funds represented by this UTXO to Bob, she can "fragment" it into several smaller ones. She will then send 0.0015 BTC to Bob and send the remainder, 0.0005 BTC, back to herself via a **exchange address**.

Here is an example of a transaction with 2 outputs:

- A UTXO of 0.0015 BTC for Bob, blocked by a script requiring a signature with Bob's private key.
- A UTXO of 0.0005 BTC for Alice, blocked by a script requiring its own signature.
![LNP201](assets/fr/06.webp)

### Multisignature addresses

In addition to simple addresses generated from a single public key, it is possible to create **multisignature addresses** from several public keys. A special case of interest for the Lightning Network is the **2/2 multisignature address**, generated from two public keys:

![LNP201](assets/fr/07.webp)

To spend the funds locked with this 2/2 multisignature address, you need to sign with the two private keys associated with the public keys.

![LNP201](assets/fr/08.webp)

This type of address is precisely the representation on the Bitcoin blockchain of the payment channels on the Lightning Network.

**What should you learn from this chapter?**

- A **Bitcoin address** is derived from a public key, itself derived from a private key.
- Funds on Bitcoin are locked by **scripts**, and to spend those funds, you have to satisfy the script, which usually amounts to providing a signature with the corresponding private key.
- The **UTXO** are pieces of bitcoin blocked by scripts, and each transaction on Bitcoin consists of unlocking a UTXO and then creating one or more new ones in return.
- **2/2** multi-signature addresses require the signature of two private keys to spend funds. It is these specific addresses that Lightning uses to create payment channels.
This chapter on Bitcoin has given us the opportunity to review a few essential concepts for the future. In the next chapter, we're going to find out just how channel opening works on the Lightning Network.

# Opening and closing channels

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Channel opening

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![ouvrir un canal](https://youtu.be/B2caBC0Rxko)

In this chapter, we'll take a closer look at how to open a payment channel on the Lightning Network and understand the link between this operation and the underlying Bitcoin system.

### Lightning channels

As we saw in the first chapter, a **payment channel** on Lightning can be compared to a "pipe" for exchanging funds between two participants (**Alice** and **Bob** in our examples). The capacity of this channel corresponds to the sum of the funds available on each side. In our example, Alice has **100,000 satoshis** and Bob has **30,000 satoshis**, giving a **total capacity** of **130,000 satoshis**.

![LNP201](assets/fr/09.webp)

### Levels of information exchange

It's important to distinguish between the different Lightning exchange levels:

- Peer-to-peer communications (Lightning protocol)**: these are the messages Lightning nodes send to each other to communicate. We'll represent these messages as dotted black lines on our diagrams.
- Payment channels (Lightning protocol)**: these are the paths for exchanging funds on Lightning, which we'll represent as black lines.
- Bitcoin transactions (Bitcoin protocol)** : these are transactions carried out onchain, which we'll represent in orange lines.
![LNP201](assets/fr/10.webp)

Note that it's possible for a Lightning node to communicate via the P2P protocol without opening a channel, but to exchange funds, a channel is required.

### Steps to open a Lightning channel

1. **Message exchange**: Alice wants to open a channel with Bob. She sends him a message containing the amount she wants to deposit in the channel (130,000 sats) and her public key. Bob replies by sharing his own public key.

![LNP201](assets/fr/11.webp)

2. **Multisignature address creation**: With these two public keys, Alice creates a **2/2 multisignature address**, which means that funds later deposited at this address will require both signatures (Alice and Bob) to be spent.

![LNP201](assets/fr/12.webp)

3. **Deposit transaction**: Alice prepares a Bitcoin transaction to deposit funds on this multisignature address. For example, she may decide to send **130,000 satoshis** to this multisignature address. This transaction is **built but not yet published** on the blockchain.

![LNP201](assets/fr/13.webp)

4. **Withdrawal transaction**: Before publishing the deposit transaction, Alice constructs a withdrawal transaction so that she can recover her funds in the event of a problem with Bob. Indeed, when Alice publishes the deposit transaction, her sats will be locked on a 2/2 multisignature address which requires both her signature and Bob's signature to be released. Alice insures herself against this risk of loss by constructing the withdrawal transaction that allows her to recover her funds.

![LNP201](assets/fr/14.webp)

5. **Bob's signature**: Alice sends Bob the deposit transaction for proof and asks him to sign the withdrawal transaction. Once Bob's signature has been obtained on the withdrawal transaction, Alice is assured of being able to retrieve her funds at any time, as all that's missing is her own signature to unlock the multisignature.

![LNP201](assets/fr/15.webp)

6. **Publication of the deposit transaction**: Once Bob's signature has been obtained, Alice can publish the deposit transaction on the Bitcoin blockchain, thus officially opening the Lightning channel between the 2 users.

![LNP201](assets/fr/16.webp)

### When is the channel open?

The channel is considered open once the deposit transaction is included in a Bitcoin block and has reached a certain confirmation depth (number of subsequent blocks).

**What should you learn from this chapter?

- The opening of a channel begins with the exchange of **messages** between the two parties (exchange of amounts and public keys).
- A channel is formed by creating a **2/2 multisignature address** and depositing funds into it via a Bitcoin transaction.
- The person opening the channel ensures that he/she can **reclaim his/her funds** through a withdrawal transaction signed by the other party before publishing the deposit transaction.
In the next chapter, we'll look at the technical operation of a Lightning transaction in a channel.

## Commitment transaction

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![trasanction lightning & transaction d'engagement](https://youtu.be/aPqI34tpypM)

In this chapter, we'll take a look at the technical operation of a transaction within a channel on the Lightning Network, i.e. when funds are moved from one side of the channel to the other.

### Reminder of a channel's life cycle

As seen above, a Lightning channel begins by being **opened** via a Bitcoin transaction. The channel can be **closed** at any time, also via a Bitcoin transaction. Between these two moments, an almost infinite number of transactions can be carried out within the channel, without going through the Bitcoin blockchain. Let's take a look at what happens during an in-channel transaction.

![LNP201](assets/fr/17.webp)

### Initial state of the canal

When the channel is opened, Alice has deposited **130,000 satoshis** on the channel's multisignature address. Thus, in the initial state, all funds are on Alice's side. Before opening the channel, Alice also had Bob sign a **withdrawal transaction**, which would allow her to recover her funds if she wished to close the channel.

![LNP201](assets/fr/18.webp)

### Unpublished transactions: commitment transactions

When Alice makes a transaction in the channel to send funds to Bob, a new Bitcoin transaction is created to reflect this change in the distribution of funds. This transaction, called a **commitment transaction**, is not published on the blockchain, but represents the new state of the channel following the Lightning transaction.

For example, Alice sends 30,000 satoshis to Bob:

- Initially**: Alice owns 130,000 satoshis.
- After the transaction**: Alice owns 100,000 satoshis, and Bob 30,000 satoshis.
To validate this transfer, Alice and Bob create a new **unpublished Bitcoin transaction** that would send **100,000 satoshis to Alice** and **30,000 satoshis to Bob** from the multisignature address. Both parties construct this transaction independently, but with the same data (amounts and addresses). Once constructed, each party signs the transaction and exchanges signatures with the other. This allows each party to publish the transaction at any time, if necessary, to recover their share of the channel on the main Bitcoin blockchain.

![LNP201](assets/fr/19.webp)

### Transfer process: the invoice

When Bob wishes to receive funds, he sends Alice an **_invoice_** for 30,000 satoshis. Alice then proceeds to pay this invoice by starting the transfer within the channel. As we have seen, this process relies on the creation and signature of a new **commitment transaction**.

Each commitment transaction represents the new distribution of funds in the channel after the transfer. In this example, after the transaction, Bob has 30,000 satoshis and Alice has 100,000 satoshis. Should either of the two participants decide to publish this commitment transaction on the blockchain, it would lead to the channel being closed, and the funds would be distributed in accordance with this latest allocation.

![LNP201](assets/fr/20.webp)

### New status after a second transaction

Let's take another example: after the first transaction where Alice sent 30,000 satoshis to Bob, Bob decides to send **10,000 satoshis back to Alice**. This creates a new channel state. The new **commitment transaction** will represent this updated distribution:

- Alice** now owns **110,000 satoshis**.
- Bob** owns **20,000 satoshis**.
![LNP201](assets/fr/21.webp)

Once again, this transaction is not published on the blockchain, but can be at any time if the channel is closed.

In short, when funds are transferred within a Lightning :

- Alice and Bob create a new **commitment transaction**, reflecting the new distribution of funds.
- This Bitcoin transaction is **signed** by both parties, but **not published** on the Bitcoin blockchain as long as the channel remains open.
- Commitment transactions guarantee that each participant can recover his or her funds at any time on the Bitcoin blockchain by publishing the last signed transaction.
However, there is a potential flaw in this system, which we'll address in the next chapter. There, we'll look at how each participant can protect himself against an attempt at cheating by the other party.

## Revocation key

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

![transactions partie 2](https://youtu.be/RRvoVTLRJ84)

In this chapter, we'll take a closer look at how transactions work on the Lightning Network, covering the mechanisms for protecting against cheating, to ensure that each party complies with the rules within a channel.

### Reminder: commitment transactions

As previously mentioned, Lightning transactions are based on unpublished **commitment transactions**. These transactions reflect the current distribution of funds in the channel. When a new Lightning transaction is carried out, a new commitment transaction is created and signed by both parties to reflect the new state of the channel.

Let's take a simple example:

- Initial state**: Alice owns **100,000 satoshis**, Bob **30,000 satoshis**.
- After a transaction in which Alice sends **40,000 satoshis** to Bob, the new commitment transaction distributes the funds as follows:
  - Alice : **60,000 satoshis**
  - Bob: **70,000 satoshis**
![LNP201](assets/fr/22.webp)

Both parties can, at any time, publish the **last signed commitment transaction** to close the channel and recover their funds.

### The flaw: cheating by publishing an old transaction

A potential problem arises if one of the parties decides to **cheat** by publishing an older commitment transaction. For example, Alice could publish an older commitment transaction where she owned **100,000 satoshis**, even though she only has **60,000** in reality. This would enable her to steal **40,000 satoshis** from Bob.

![LNP201](assets/fr/23.webp)

Worse still, Alice could publish the very first withdrawal transaction, the one before the channel opened, where she owned **130,000 satoshis**, and thus steal the channel's entire funds.

![LNP201](assets/fr/24.webp)

### Solution: the revocation key and timelock

To avoid this cheating by Alice, on the Lightning Network, we add **security mechanisms** to commitment transactions:

1. **Timelock**: Each commitment transaction includes a timelock for Alice's funds. The timelock is a smart contract primitive that defines a time condition to be met before a transaction can be added to a block. This means that Alice won't be able to get her funds back until a certain number of blocks later, if she publishes one of the commitment transactions. This timelock starts to apply as soon as the commitment transaction is confirmed. Its duration is generally proportional to the size of the channel, but it can also be configured manually.

2. **Revocation key**: Alice's funds can also be spent immediately by Bob if he has the **revocation key**. This key consists of a secret held by Alice and a secret held by Bob. Note that this secret is different for each commitment transaction.

Thanks to these 2 mechanisms combined, Bob has time to detect Alice's cheating attempt, and to punish her by recovering her output thanks to the revocation key, which for Bob means recovering all the funds in the channel. Our new commitment transaction will now look like this:

![LNP201](assets/fr/25.webp)

Let's take a closer look at how this mechanism works.

### Transaction update process

When Alice and Bob update the channel state with a new Lightning transaction, they exchange upstream their respective **secrets** for the previous commitment transaction (the one that's about to become obsolete and could allow one of them to cheat). This means that, in the new channel state :

- Alice and Bob have a new commitment transaction representing the current distribution of funds after the Lightning transaction.
- Each has the other's secret for the previous transaction, enabling them to use the revocation key only if one of them tries to cheat by publishing a transaction with an old state in the mempools of the Bitcoin nodes. Indeed, to punish the other party, it is necessary to hold both secrets and the other's commitment transaction, which includes the signed input. Without this transaction, the revocation key alone is useless. The only way to obtain this transaction is to retrieve it from mempools (in transactions awaiting confirmation) or from confirmed transactions on the blockchain during the timelock, which proves that the other party is trying to cheat, whether voluntarily or not.
Let's take an example to understand this process:

1. **Initial state**: Alice owns **100,000 satoshis**, Bob **30,000 satoshis**.

![LNP201](assets/fr/26.webp)

2. Bob wants to receive 40,000 satoshis from Alice via their Lightning channel. To do this :

   - It sends him an invoice and his secret for the revocation key of his previous commitment transaction.
   - In response, Alice provides her signature for Bob's new commitment transaction, as well as her secret for the revocation key of his previous transaction.
   - Finally, Bob sends his signature for Alice's new commitment transaction.
   - These exchanges enable Alice to send **40,000 satoshis** to Bob on Lightning via their channel, and the new commitment transactions now reflect this new distribution of funds.
![LNP201](assets/fr/27.webp)

3. If Alice tries to publish the old commitment transaction where she still owned **100,000 satoshis**, Bob, having obtained the revocation key, can immediately recover the funds thanks to this key, while Alice is blocked by the timelock.

![LNP201](assets/fr/28.webp)

Although in this case Bob has no economic interest in trying to cheat, if he does cheat, Alice also benefits from symmetrical protection offering the same guarantees.

**What should you learn from this chapter?

Commitment transactions** on the Lightning Network include security mechanisms that reduce both the risk of cheating and the incentive to do so. Before signing a new commitment transaction, Alice and Bob exchange their respective **secrets** for previous commitment transactions. If Alice tries to publish an old commitment transaction, Bob can use the **revocation key** to recover the full amount before Alice can (as she is blocked by the timelock), thus punishing her for trying to cheat.

This security system ensures that participants comply with Lightning Network rules, and that they cannot profit from the publication of old commitment transactions.

At this stage of the course, you'll know how Lightning channels are opened and how transactions in these channels work. In the next chapter, we'll look at how to close a channel and get your bitcoins back onto the main blockchain.

## Channel closure

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![fermer un canal](https://youtu.be/FVmQvNpVW8Y)

In this chapter, we'll look at **closing a channel** on the Lightning Network, which is achieved through a Bitcoin transaction, just like opening a channel. Having seen how transactions within a channel work, it's now time to see how to close a channel and recover the funds on the Bitcoin blockchain.

### Reminder of a channel's life cycle

The **life cycle of a channel** begins with its **opening**, via a Bitcoin transaction, then Lightning transactions are carried out within it, and finally, when the parties wish to recover their funds, the channel is **closed** via a second Bitcoin transaction. Intermediary transactions carried out on Lightning are represented by unpublished **commitment transactions**.

![LNP201](assets/fr/29.webp)

### The three types of channel closure

There are three main ways to close this channel, which can be called **the good, the bad and the ugly** (inspired by Andreas Antonopoulos in _Mastering the Lightning Network_):

1. **The good one**: the **cooperative closing**, where Alice and Bob agree to close the canal.

2. **The brute**: the **forced closure**, where one of the parties decides to close the channel in an honest way, but without the agreement of the other.

3. **The trickster**: the **closing with cheating**, where one of the parties tries to steal funds by publishing an old commitment transaction (any one, but not the last one, which reflects the real and fair distribution of funds).

Let's take an example:

- Alice owns **100,000 satoshis** and Bob **30,000 satoshis**.
- This distribution is reflected in **2 commitment transactions** (one per user) which are not published, but could be in the event of channel closure.
![LNP201](assets/fr/30.webp)

### The right one: cooperative closure

In a **cooperative closing**, Alice and Bob agree to close the canal. Here's how it goes:

1. Alice sends a message to Bob via the Lightning communication protocol to propose closing the channel.

2. Bob accepts, and the two parties make no further transactions in the channel.

![LNP201](assets/fr/31.webp)

3. Alice and Bob negotiate the **closing transaction fee** together. These fees are generally calculated according to the Bitcoin fee market at the time of closure. It's important to note that **it's always the person who opened the channel** (Alice in our example) who pays the closing fee.

4. They build a new **closing transaction**. This transaction resembles a commitment transaction, but with no timelock or revocation mechanisms, since both parties are cooperating and there is no risk of cheating. This cooperative closing transaction is therefore different from a commitment transaction.

For example, if Alice owns **100,000 satoshis** and Bob owns **30,000 satoshis**, the closing transaction will send **100,000 satoshis** to Alice's address and **30,000 satoshis** to Bob's address, without timelock constraints. Once this transaction has been signed by both parties, it is published by Alice. Once the transaction has been confirmed on the Bitcoin blockchain, the Lightning channel is officially closed.

![LNP201](assets/fr/32.webp)

Cooperative closing** is the preferred closing method, because it's fast (no timelock) and transaction fees are adjusted according to current Bitcoin market conditions. This avoids paying too little, which would risk blocking the transaction in mempools, or overpaying unnecessarily, resulting in unnecessary financial loss for participants.

### The brute: forced closure

When Alice's node sends a message to Bob's node requesting a cooperative closure, if Bob doesn't respond (for example, due to an Internet outage or a technical problem), Alice can perform a **forced closure** by publishing the **last signed commitment transaction**.

In this case, Alice will simply publish the last commitment transaction, which reflects the state of the channel at the time the last Lightning transaction took place with the correct allocation of funds.

![LNP201](assets/fr/33.webp)

This transaction includes a **timelock** for Alice's funds, which makes closing slower.

![LNP201](assets/fr/34.webp)

Also, commitment transaction fees may be inappropriate at the time of closing, as they were set at the time the transaction was created, sometimes several months earlier. In general, Lightning customers overestimate fees to avoid future problems, but this can result in fees that are excessive, or conversely too low.

In short, **forced closure** is an option of last resort when the peer no longer responds. It is slower and less economical than cooperative closure. It should therefore be avoided whenever possible.

### The trickster: cheating

Finally, a closure with **cheating** occurs when one of the parties attempts to publish an old commitment transaction, often where she held more funds than she should. For example, Alice might publish an old transaction where she owned **120,000 satoshis**, when in reality she only owns **100,000**.

![LNP201](assets/fr/35.webp)

To prevent this cheating, Bob monitors the Bitcoin blockchain and its mempool to make sure Alice doesn't publish an old transaction. If Bob detects an attempt to cheat, he can use the **revocation key** to recover Alice's funds and punish her by taking the entire channel's funds. Since Alice is blocked by the timelock on her output, Bob has time to spend it without a timelock of his own to recover the entire sum on an address belonging to him.

![LNP201](assets/fr/36.webp)

Of course, the cheating can potentially succeed if Bob doesn't show up within the time limit imposed by the timelock on Alice's output. In this case, Alice's output is unblocked, allowing her to use it to create a new output to an address she controls.

**What should you learn from this chapter?

There are three ways to close a channel:

1. **Cooperative closing**: fast and less costly, where both parties agree to close the channel and publish a suitable closing transaction.

2. **Forced closure**: less desirable, as it relies on the publication of a commitment transaction, with potentially inappropriate fees and a timelock, which slows down closure.

3. **Cheating**: if one party tries to steal funds by publishing an old transaction, the other can use the revocation key to punish this cheating.

In the next few chapters, we'll be taking a broader look at the Lightning Network, and how it works.

# A liquidity network

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning le Réseau

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning le réseau](https://youtu.be/RAZAa3v41DM)

In this chapter, we'll explore how payments on the Lightning Network can reach a recipient even if the latter is not directly connected via a payment channel. Lightning is, in effect, a **network of payment channels**, which means that funds can be sent to a remote node via the channels of other participants. We're going to find out how payments are routed on the network, how liquidity moves between channels, and how transaction fees are calculated.

### The network of payment channels

On the Lightning Network, a transaction corresponds to a transfer of funds between two nodes. As seen in the previous chapters, you need to open a channel with a person to carry out Lightning transactions. This channel makes it possible to carry out an almost infinite number of off-chain transactions before closing it again to recover the on-chain balance. However, this method has the disadvantage of requiring a direct channel with the other person to receive or send funds, which implies an opening transaction and a closing transaction for each channel. If I plan to make a large number of payments with this person, opening and closing a channel becomes profitable. On the other hand, if I only need to make a few Lightning transactions, opening a direct channel is not advantageous, as it would cost me 2 on-chain transactions for a limited number of off-chain transactions. This could be the case, for example, when you want to pay with Lightning at a merchant's without planning to return.

To solve this problem, the Lightning Network allows a payment to be routed via several channels and intermediate nodes, enabling a transaction to be carried out without a direct channel to the other person.

For example, suppose :

- Alice** (in orange) has a channel with **Suzie** (in grey) with **100,000 satoshis** on her side and **30,000 satoshis** on Suzie's side.
- Suzie** has a channel with **Bob** in which she has **250,000 satoshis** and Bob has no satoshi.
![LNP201](assets/fr/37.webp)

If Alice wishes to send funds to Bob without opening a direct channel with him, she will have to go through Suzie, and each channel will have to adjust the liquidity on each side. **The satoshis sent remain in their respective channels**; they don't actually "cross" the channels, but the transfer takes place via an adjustment of the liquidity internal to each channel.

Suppose Alice wants to send **50,000 satoshis** to Bob :

1. **Alice** sends 50,000 satoshis to **Suzie** in their common channel.

2. **Suzie** counters this transfer by sending 50,000 satoshis to Bob** in their channel.

![LNP201](assets/fr/38.webp)

The payment is routed to Bob via a liquidity shift in each channel. At the end of the operation, Alice ends up with 50,000 sats. She has transferred 50,000 sats, since she originally had 100,000. Bob, for his part, ends up with a further 50,000 sats. For Suzie (the intermediate node), this operation is neutral: initially, she had 30,000 sats in her channel with Alice and 250,000 sats in her channel with Bob, for a total of 280,000 sats. After the operation, she has 80,000 sats in her channel with Alice and 200,000 sats in her channel with Bob, i.e. the same amount as at the start.

This transfer is thus limited by the **liquidity available** in the direction of the transfer.

### Calculating route and liquidity limits

Let's take a theoretical example of another network with :

- 130,000 satoshis** on Alice's side (orange) in her channel with **Suzie** (grey).
- 90,000 satoshis** on the **Suzie** side and **200,000 satoshis** on the **Carol** side (in pink).
- 150,000 satoshis** for **Carol** and **100,000 satoshis** for **Bob**.
![LNP201](assets/fr/39.webp)

The maximum Alice can send to Bob in this configuration is **90,000 satoshi**, as she is limited by the smallest available liquidity in the channel from **Suzie to Carol**. In the opposite direction (from Bob to Alice), no payment is possible because **Suzie**'s side of the channel with **Alice** contains no satoshi. There is therefore **no route** that can be used for a transfer in this direction.

Alice sends **40,000 satoshis** to Bob via the channels :

1. Alice transfers 40,000 satoshis into her canal with Suzie.

2. Suzie transfers 40,000 satoshis to Carol in their shared channel.

3. Carol finally transfers 40,000 satoshis to Bob.

![LNP201](assets/fr/40.webp)

The **satoshis sent** in each channel **remain in the channel**, so the satoshis sent by Carol to Bob are not the same as those sent by Alice to Suzie. The transfer takes place solely by adjusting the liquidity within each channel. The total capacity of the channels remains unchanged.

![LNP201](assets/fr/41.webp)

As in the previous example, after the transaction, the source node (Alice) has 40,000 satoshis less. The intermediate nodes (Suzie and Carol) retain the same total amount, making the transaction neutral for them. Finally, the destination node (Bob) receives a further 40,000 satoshis.

Intermediary nodes therefore play an important role in the operation of the Lightning network. They make transfers more fluid by offering several payment paths. To encourage these nodes to provide their liquidity and participate in the routing of payments, they are paid a **routing fee**.

### Routing costs

Intermediary nodes apply fees to allow payments to pass through their channels. These fees are defined by **each node for each channel**. Fees have 2 components:

1. "**Base fee**": a fixed amount per channel, often **1 sat** by default, but customizable.

2. "**Fee variable**": a percentage of the amount transferred, calculated in **parts per million (ppm)**. By default, it is **1 ppm** (1 sat per million satoshis transferred), but it can also be adjusted.

Fees also differ depending on the direction of the transfer. For example, for a transfer from Alice to Suzie, Alice's charges apply. Conversely, from Suzie to Alice, Suzie's charges apply.

For example, for a channel between Alice and Suzie, we could have :

- Alice**: basic fee of 1 sat and 1 ppm for variable costs.
- Suzie**: 0.5 sat basic fee and 10 ppm variable fee.
![LNP201](assets/fr/42.webp)

To understand how fees work, let's study the same Lightning network as before, but now with the following routing fees:

- Channel **Alice - Suzie**: base fee of 1 satoshi and 1 ppm for Alice.
- Channel **Suzie - Carol**: base fee of 0 satoshi and 200 ppm for Suzie 1.
- Channel **Carol - Bob**: base fee of 1 satoshi and 1 ppm for Suzie 2.
![LNP201](assets/fr/43.webp)

For the same payment of **40,000 satoshis** to Bob, Alice will have to send a little more, as each intermediary node will charge its own fees:

- Carol** takes 1.04 satoshis from the channel with Bob :
$$ f*{\text{Carol-Bob}} = \text{base fee} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- Suzie** charges 8 satoshis on the channel with Carol :
$$ f*{\text{Suzie-Carol}} = \text{base fee} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

The total charge for this payment on this path is therefore **9.04 satoshis**. Thus, Alice must send **40,009.04 satoshis** for Bob to receive exactly **40,000 satoshis**.

![LNP201](assets/fr/44.webp)

Liquid assets are therefore updated:

![LNP201](assets/fr/45.webp)

### Onion routing

To route a payment from sender to recipient, the Lightning Network uses a method called "onion routing". Unlike conventional data routing, where each router decides where the data should go based on its destination, onion routing works differently:

- The sender node calculates the entire route**: Alice, for example, determines that her payment must pass through Suzie and Carol before reaching Bob.
- Each intermediate node knows only its immediate neighbor** : Suzie knows only that she has received funds from Alice and that she must transfer them to Carol. However, Suzie doesn't know whether Alice is the source node or an intermediate node, nor does she know whether Carol is the recipient node or just another intermediate node. This principle also applies to Carol and all the other nodes in the path. Onion routing thus preserves the confidentiality of transactions by concealing the identity of the sender and final recipient.
For the sender node to calculate a complete route to the recipient in onion routing, it must maintain a **network graph** to know its topology and determine possible routes.

**What should you learn from this chapter?

1. On Lightning, payments can be routed between nodes connected indirectly via intermediate channels. Each of these intermediary nodes acts as a liquidity relay.

2. Intermediary nodes receive a commission for their service, made up of fixed and variable costs.

3. Onion routing allows the sender node to calculate the complete route without the intermediate nodes knowing the source or final destination.

In this chapter, we learned about payment routing on the Lightning Network. But the question arises: what prevents intermediate nodes from accepting an incoming payment without forwarding it to the next destination, with the aim of intercepting the transaction? This is precisely the role of HTLC, which we'll examine in the next chapter.

## HTLC - Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

In this chapter, we'll find out how Lightning enables payments to pass through intermediary nodes without the need to trust them, thanks to **HTLC** (_Hashed Time-Locked Contracts_). These smart contracts guarantee that each intermediary node will only receive funds from its channel if it sends the payment to the final recipient, otherwise the payment will not be validated.

The problem that arises when routing a payment is therefore the trust needed in the intermediary nodes, and between the intermediary nodes themselves. To illustrate this, let's take our example of a simplified Lightning network with 3 nodes and 2 channels:

- Alice has a channel with Suzie.
- Suzie has a channel with Bob.
Alice wants to send 40,000 sats to Bob, but she doesn't have a direct channel to him and doesn't want to open one. She looks for a route and chooses to go through Suzie's node.

![LNP201](assets/fr/46.webp)

If Alice naively sends Suzie 40,000 satoshis in the hope that Suzie will transfer this sum to Bob, Suzie could keep the funds for herself and pass nothing on to Bob.

![LNP201](assets/fr/47.webp)

To avoid this situation, Lightning uses HTLC, which makes payment to the intermediary node conditional, i.e. Suzie must complete certain conditions to access Alice's funds and pass them on to Bob.

### How HTLC (_Hashed Time-Locked Contracts_) work

A HTLC is a special contract based on two principles:

- Access condition** : The recipient must reveal a secret to unlock the payment due.
- Expiry**: If the payment is not fully completed within a defined period, it is cancelled and the funds are returned to the sender.
Here's how the process works in our example with Alice, Suzie and Bob:

![LNP201](assets/fr/48.webp)

**Secret creation**: Bob generates a random secret noted _s_ (the pre-image), and calculates its hash noted _r_ with the hash function noted _h_. The result is :

$$
r = h(s)
$$

Using a hash function makes it impossible to find _s_ with _h(s)_ alone, but if _s_ is provided, it's easy to check that it matches _h(s)_.

![LNP201](assets/fr/49.webp)

**Send payment request**: Bob sends an **invoice** to Alice requesting payment. This invoice includes the _r_ hash.

![LNP201](assets/fr/50.webp)

**Conditional payment**: Alice sends an HTLC of 40,000 satoshis to Suzie. The condition for Suzie to receive these funds is that she provides Alice with a secret _s'_ that verifies the following equation:

$$
h(s') = r
$$

![LNP201](assets/fr/51.webp)

**Transmission of HTLC to final recipient**: Suzie, in order to obtain the 40,000 satoshis from Alice, must transfer a similar HTLC of 40,000 satoshis to Bob, who has the same condition, i.e. he must provide Suzie with a secret _s'_ that verifies the equation :

$$
h(s') = r
$$

![LNP201](assets/fr/52.webp)

**Validation by secret _s_**: Bob provides Suzie with _s_ to receive the 40,000 satoshis promised in the HTLC. With this secret, Suzie can then unlock Alice's HTLC and obtain the 40,000 satoshis from Alice. The payment is then correctly routed to Bob.

![LNP201](assets/fr/53.webp)

This process makes it impossible for Suzie to keep Alice's funds without completing the transfer to Bob, as she must send the payment to Bob to obtain the _s_ secret and thus unlock Alice's HTLC. The operation remains the same even if the route includes several intermediate nodes: simply repeat Suzie's steps for each intermediate node. Each node is protected by the HTLC conditions, as the release of the last HTLC by the recipient automatically triggers the release of all the other HTLCs in the cascade.

### Expiration and management of HTLC in the event of a problem

If, during the payment process, one of the intermediary nodes, or the destination node, becomes unresponsive, for example in the event of an Internet or power cut, then the payment cannot succeed, as the secret enabling HTLC to be unblocked is not transmitted. If we go back to our example with Alice, Suzie and Bob, this problem arises, for example, if Bob doesn't transmit the _s_ secret to Suzie. In this case, all HTLCs upstream of the path are blocked, and so are the funds they secure.

![LNP201](assets/fr/54.webp)

To avoid this, HTLCs on Lightning feature an expiry that allows the HTLC to be deleted if it is not completed within a certain time. Expiration follows a specific order, starting first with the HTLC closest to the recipient, then progressively working backwards to the sender of the transaction. In our example, if Bob never gives the secret _s_ to Suzie, this would cause the HTLC from Suzie to Bob to expire first.

![LNP201](assets/fr/55.webp)

Then Alice's HTLC to Suzie.

![LNP201](assets/fr/56.webp)

If the expiry order were reversed, Alice could recover her payment before Suzie could protect herself from potential cheating. Indeed, if Bob returned to claim his HTLC when Alice had already deleted hers, Suzie would find herself aggrieved. This cascading order of HTLC expiry ensures that no intermediate node suffers unfair losses.

### HTLC representation in commitment transactions

Commitment transactions represent HTLCs so that the conditions they impose on Lightning are transferable to Bitcoin in the event of a forced channel closure during the lifetime of an HTLC. As a reminder, commitment transactions represent the current state of the channel between the 2 users, and enable unilateral forced closure in the event of a problem. For each new channel state, 2 commitment transactions are created: one for each party. Let's go back to our example with Alice, Suzie and Bob, but let's take a closer look at what's happening in the channel between Alice and Suzie when the HTLC is created.

![LNP201](assets/fr/57.webp)

Before the payment of 40,000 sats between Alice and Bob begins, Alice has 100,000 sats in her channel with Suzie, while Suzie has 30,000. Their commitment transactions are therefore as follows:

![LNP201](assets/fr/58.webp)

Alice has just received Bob's invoice, which contains _r_, the hash of the secret. She can therefore build a HTLC of 40,000 satoshis with Suzie. This HTLC is represented in the last commitment transactions as an output called "**_HTLC Out_**" on Alice's side, since the funds are outgoing, and "**_HTLC In_**" on Suzie's side, since the funds are incoming.

![LNP201](assets/fr/59.webp)

These outputs associated with HTLC share exactly the same conditions, namely :

- If Suzie is able to provide the secret _s_, she can unlock this output immediately and transfer it to an address she controls.
- If Suzie doesn't have the secret _s_, she can't unlock this output, and Alice can unlock it after a timelock to send it to an address she controls. The timelock thus gives Suzie time to react if she obtains _s_.
These conditions only apply if the channel is closed (a commitment transaction is published on-chain) while the HTLC is still active on Lightning, i.e. the payment between Alice and Bob has not yet been finalized, and the HTLCs have not yet expired. Thanks to these conditions, Suzie can recover the 40,000 satoshis of HTLC owed to her by providing _s_. Otherwise, Alice recovers the funds after the timelock has expired, because if Suzie doesn't know _s_, this means she hasn't transmitted the 40,000 satoshis to Bob, and Alice's funds are therefore not due to him.

On the other hand, if the channel is closed while several HTLCs are waiting, there will be as many more outputs as there are HTLCs in progress.

If the channel is not closed, then after the Lightning payment has expired or succeeded, new commitment transactions are created to reflect the new, stable state of the channel, i.e. with no pending HTLC. HTLC-related outputs can therefore be removed from commitment transactions.

![LNP201](assets/fr/60.webp)

Finally, in the event of a cooperative channel closure while an HTLC is active, Alice and Suzie stop accepting new payments and wait for the resolution or expiry of the current HTLC. This allows them to publish a lighter closing transaction, without the outputs linked to HTLCs, thus reducing costs and avoiding the need to wait for a possible timelock.

**What should you learn from this chapter?

HTLC allows Lightning payments to be routed through multiple nodes without having to trust them. Here are the key points to remember:

1. HTLC guarantees payment security by means of a secret (pre-image) and an expiry date.

2. HTLC resolution or expiration follows a specific order: from destination to source, to protect each node.

3. As long as an HTLC is neither resolved nor expired, it is maintained as output in the most recent commitment transactions.

In the next chapter, we'll discover how a Lightning transaction's sender node finds and selects routes for its payment to reach the recipient node.

## Finding your way

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![trouver sa voie](https://youtu.be/wnUGJjOxd9Q)

In previous chapters, we have seen how to use other nodes' channels to route payments and reach a node without being directly connected to it via a channel. We also discussed how to guarantee the security of the transfer without relying on intermediary nodes. In this chapter, we'll be looking at how to find the best possible route to reach a target node.

### Routing in Lightning

As we've seen, on Lightning, it's the payment sender node that has to calculate the complete route to the recipient, since we use an onion routing system. Intermediate nodes know neither the point of origin nor the final destination. They only know where the payment originated and to which node they must transfer it next. This means that the sending node must maintain a dynamic local network topology, with existing Lightning nodes and channels between each, taking into account openings, closures and status updates.

![LNP201](assets/fr/61.webp)

Even with this Lightning network topology, there is one essential piece of routing information that remains inaccessible to the transmitting node: the exact distribution of liquidity in the channels at any given moment. Indeed, each channel only displays its **total capacity**, but the internal distribution of funds is known only to the two participating nodes. This poses challenges for efficient routing, as the success of the payment depends in particular on its amount being less than the lowest liquidity on the chosen route. However, not all liquidity is visible to the sending node.

![LNP201](assets/fr/62.webp)

### Network map update

To keep their network map up to date, nodes regularly exchange messages using an algorithm known as "**_gossip_**". This is a distributed algorithm used to spread information epidemically to all nodes in the network, enabling the global state of the channels to be exchanged and synchronized in just a few communication cycles. Each node propagates information to one or more randomly selected or non-randomly selected neighbors, who in turn propagate the information to other neighbors, and so on, until a globally synchronized state is reached.

The 2 main messages exchanged between Lightning nodes are as follows:

- "**Channel Announcements**: messages announcing the opening of a new channel.
- "**Channel Updates**": update messages on the status of a channel, notably on the evolution of charges (but not on the distribution of liquid assets).
Lightning nodes also monitor the Bitcoin blockchain for channel closure transactions. The closed channel is then removed from the card, since we can no longer use it to route our payments.

### Routing a payment

Let's take an example of a small Lightning network with 7 nodes: Alice, Bob, 1, 2, 3, 4, and 5. Let's imagine that Alice wants to send a payment to Bob, but must pass through intermediate nodes.

![LNP201](assets/fr/63.webp)

Here is the actual distribution of funds in these channels:

- Channel between Alice and 1**: 250,000 sats on the Alice side, 80,000 on the 1 side (total capacity of 330,000 sats).
- Channel between 1 and 2**: 300,000 sats on side 1, 200,000 on side 2 (total capacity of 500,000 sats).
- Channel between 2 and 3**: 50,000 sats on side 2, 60,000 on side 3 (total capacity of 110,000 sats).
- Channel between 2 and 5**: 90,000 sats on side 2, 160,000 on side 5 (total capacity of 250,000 sats).
- Channel between 2 and 4**: 180,000 sats on side 2, 110,000 on side 4 (total capacity 290,000 sats).
- Channel between 4 and 5**: 200,000 sats on side 4, 10,000 on side 5 (total capacity of 210,000 sats).
- Channel between 3 and Bob**: 50,000 sats on the 3 side, 250,000 on the Bob side (total capacity of 300,000 sats).
- Channel between 5 and Bob**: 260,000 sats on the 5 side, 100,000 on the Bob side (total capacity of 360,000 sats).
![LNP201](assets/fr/64.webp)

To make a payment of 100,000 sats from Alice to Bob, the routing options are limited by the liquidity available in each channel. The optimal route for Alice, based on known liquidity distributions, could be the sequence `Alice → 1 → 2 → 4 → 5 → Bob` :

![LNP201](assets/fr/65.webp)

But since Alice does not know the exact distribution of funds in each channel, she must estimate the optimal route probabilistically, taking into account the following criteria:

- Probability of success**: a channel with higher total capacity is more likely to contain sufficient liquidity. For example, the channel between node 2 and node 3 has a total capacity of 110,000 sats, so it's unlikely that there will be 100,000 sats or more on the node 2 side, although it's possible.
- Transaction costs**: when choosing the best route, the sender node also takes into account the costs applied by each intermediary node, and seeks to minimize the total cost of routing.
- HTLC expiration**: to avoid blocked payments, the HTLC expiration time is also a parameter to be taken into account.
- Number of intermediate nodes**: finally, in a more global sense, the sender node will try to find a route with as few nodes as possible, in order to reduce the risk of failure and limit Lightning transaction costs.
By analyzing these criteria, the transmitting node can test the most likely routes and try to optimize them. In our example, Alice could rank the best routes as follows:

1. `Alice → 1 → 2 → 5 → Bob`, because it's the shortest route with the highest capacity.

2. `Alice → 1 → 2 → 4 → 5 → Bob`, as this route offers good capabilities, although it's longer than the first.

3. `Alice → 1 → 2 → 3 → Bob`, because this route includes the channel `2 → 3`, which is very limited in capacity, but is still potentially usable.

### Payment execution

Alice decides to test her first route (`Alice → 1 → 2 → 5 → Bob`). She sends an HTLC of 100,000 sats to node 1, which checks that it has sufficient liquidity with node 2, and continues transmission. Node 2 then receives the HTLC from node 1, but realizes that it doesn't have enough liquidity in its channel with node 5 to route a payment of 100,000 sats. It then sends an error message back to node 1, which forwards it to Alice. This route has failed.

![LNP201](assets/fr/66.webp)

Alice then tries to route her payment using her second route (`Alice → 1 → 2 → 4 → 5 → Bob`). She sends an HTLC of 100,000 sats to node 1, which forwards it to node 2, then to node 4, to node 5, and finally to Bob. This time, there's enough cash and the route is up and running. Each node releases its HTLC in cascade, using the pre-image provided by Bob (the _s_ secret), thus successfully finalizing the payment from Alice to Bob.

![LNP201](assets/fr/67.webp)

The route search is carried out as follows: the sender node first identifies the best possible routes, then attempts successive payments until a functional route is found.

Note that Bob can provide Alice with information in the **invoice** to facilitate routing. For example, he can indicate nearby channels with sufficient liquidity, or reveal the existence of private channels. These indications enable Alice to avoid routes with little chance of success, and to try the paths recommended by Bob first.

**What should you learn from this chapter?

1. Nodes maintain a map of the network topology through announcements and by monitoring channel closures on the Bitcoin blockchain.

2. The search for an optimal route for a payment remains probabilistic and depends on many criteria.

3. Bob can provide hints in the **invoice** to guide Alice's routing and save her from testing unlikely routes.

In the next chapter, we'll take a closer look at how invoices work, as well as some of the other tools used on the Lightning Network.

# Lightning Network tools

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Invoice, LNURL and Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![invoice, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

In this chapter, we'll take a closer look at how Lightning **invoices** work, i.e. payment requests sent by the recipient node to the sender node. The aim is to understand how to pay and receive payments over Lightning. We'll also look at 2 alternatives to conventional invoices: LNURL and Keysend.

![LNP201](assets/fr/68.webp)

### The Lightning invoice structure

As explained in the chapter on HTLC, each payment begins with the generation of an **invoice** by the recipient. This invoice is then transmitted to the payer (via QR code or copy-paste) to initiate payment. An invoice consists of two main parts:

1. **Human Readable Part: this section contains clearly visible metadata to enhance the user experience.

2. **Payload**: this section includes information intended for payment processing machines.

The typical invoice structure begins with an identifier `ln` for "Lightning", followed by `bc` for Bitcoin, then the invoice amount. A `1` separator distinguishes the human-readable part from the data part (payload).

Let's take the following invoice as an example:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

We can already divide it into 2 parts. First, there's the part that can be read by humans:

```invoice
lnbc100u
```

Then the payload section:

```invoice
p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

The two parts are separated by a `1`. This separator was chosen rather than a special character to make it easy to copy and paste the entire invoice with a double-click.

In the first part, we can see that :

- `ln` indicates that this is a Lightning transaction.
- `bc` indicates that the Lighnting network is on the Bitcoin blockchain (and not on testnet or Litecoin).
- `100u` indicates the invoice amount, expressed in **microsatoshis** (`u` means "micro"), which here equals 10,000 sats.
The payment amount is expressed in bitcoin sub-units. Here are the units used:

- Millibitcoin (denoted `m`):** Represents one thousandth of a bitcoin.
$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$

- Microbitcoin (denoted `u`):** Also sometimes called "bit", represents one millionth of a bitcoin.
$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$

- Nanobitcoin (denoted `n`):** Represents one billionth of a bitcoin.
$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$

- Picobitcoin (denoted `p`):** Represents one trillionth of a bitcoin.
$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$

### Invoice payload

An invoice's payload includes several pieces of information for processing the payment:

- **Timestamp** : The time of invoice creation, expressed in Unix Timestamp (the number of seconds elapsed since January 1, 1970).
- The secret hash**: As we saw in the section on HTLC, the receiving node must give the sending node the hash of the pre-image. This will be used in HTLC to secure the transaction. We named it "_r_".
- Payment secret**: Another secret is generated by the recipient, but this time transmitted to the sending node. It is used in onion routing to prevent intermediate nodes from guessing whether the next node is the final recipient or not. This maintains a form of confidentiality for the recipient vis-à-vis the last intermediate node on the route.
- Recipient's public key**: Tells the payer the identifier of the person to be paid.
- **Expiry time**: Maximum time for the invoice to be paid (default: 1 hour).
- Routing information**: Additional information provided by the recipient to help the sender optimize the payment route.
- Signature**: Guarantees invoice integrity by authenticating all information.
The invoices are then encoded in **bech32**, the same format as for Bitcoin SegWit addresses (format starting with `bc1`).

### Withdrawal LNURL

In a conventional transaction, such as an in-store purchase, the invoice is generated for the total amount to be paid. Once the invoice has been presented (as a QR code or string of characters), the customer can scan it and finalize the transaction. Payment then follows the classic process we studied in the previous section. However, this process can sometimes be very annoying for the user experience, as it requires the receiver to send information to the sender via the invoice.

For certain situations, such as withdrawing bitcoins from an online service, the traditional process is too restrictive. The **LNURL** withdrawal solution simplifies this process by displaying a QR code which the recipient's wallet scans to automatically create the invoice. The service then pays the invoice, and the user simply sees an instant withdrawal.

![LNP201](assets/fr/69.webp)

LNURL is a communication protocol that specifies a set of features designed to simplify interactions between Lightning nodes and clients, as well as third-party applications. LNURL withdrawal, as we've just seen, is just one example of this functionality.

This protocol is based on HTTP and enables links to be created for various operations, such as a payment request, a withdrawal request, or other functionalities that enhance the user experience. Each LNURL is a URL encoded in bech32 with the prefix lnurl, which, when scanned, triggers a series of automatic actions on the Lightning wallet.

For example, LNURL-withdraw (LUD-03) lets you withdraw funds from a service by scanning a QR code, without having to manually generate an invoice. Or LNURL-auth (LUD-04) lets you connect to online services using a private key on your Lightning wallet instead of a password.

### Sending a Lightning payment without Invoice: Keysend

Another interesting case is the transfer of funds without first receiving an invoice, known as "**Keysend**". This protocol enables funds to be sent by adding a preimage to the encrypted payment data, accessible only by the recipient. This pre-tag allows the recipient to unlock the HTLC, and thus recover the funds without having generated an invoice beforehand.

Simply put, in this protocol, it's the sender who generates the secret used in HTLC, rather than the recipient. In practical terms, this enables the sender to send a payment without having to interact with the recipient beforehand.

![LNP201](assets/fr/70.webp)

**What should you learn from this chapter?**

1. An **Invoice** Lightning is a payment request made up of a human-readable part and a machine-readable data part.

2. The invoice is encoded in **bech32**, with a `1` separator for easy copying, and a data section containing all the information needed to process the payment.

3. Other payment processes exist on Lightning, including **LNURL-Withdraw** for easy withdrawals, and **Keysend** for invoice-free direct transfers.

In the next chapter, we'll look at how a node operator can manage liquidity in his channels, so that he is never blocked and can always send and receive payments on the Lightning Network.

## Managing liquidity

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![gerer sa liquidité](https://youtu.be/YuPrbhEJXbg)

In this chapter, we'll look at strategies for effectively managing liquidity on the Lightning Network. Liquidity management varies according to user type and context. We'll take a look at the main principles and existing techniques to help you understand how to optimize liquidity management.

### Liquidity requirements

There are three main user profiles on Lightning, each with specific cash requirements:

1. **The Payer**: This is the person who makes payments. He needs outgoing liquidity to be able to transfer funds to other users. For example, this could be a consumer.

2. **The Seller (or Payee)**: This is the person who receives the payments. He needs incoming liquidity to be able to accept payments to his node. For example, this could be a business or an online store.

3. **The Router**: An intermediary node, often specialized in payment routing, which must optimize its liquidity in each channel to route a maximum number of payments and earn fees.

Of course, these profiles are not fixed; a user can alternate between payer and payee depending on the transaction. For example, Bob might receive his salary on Lightning from his employer, which places him in the position of "seller" requiring incoming liquidity. Later, if he wishes to use his salary to buy food, he becomes a "payer", requiring outgoing liquidity.

To better understand this, let's take the example of a simple network with three nodes: the buyer (Alice), the router (Suzie) and the seller (Bob).

![LNP201](assets/fr/71.webp)

Let's imagine that the buyer wants to send 30,000 sats to the seller, and that the payment goes through the router node. Each party must then have a minimum amount of liquidity in the direction of payment:

- The payer must have at least 30,000 satoshis on his side of the channel with the router.
- The seller must have a channel where 30,000 satoshis are on the opposite side in order to receive them.
- The router must have 30,000 satoshis on the payer's side in their channel, and also 30,000 satoshis on its side in the channel with the seller, in order to be able to route the payment.
![LNP201](assets/fr/72.webp)

### Liquidity management strategies

Payers need to maintain sufficient liquidity on their side of the channels to guarantee outgoing liquidity. This is relatively straightforward, as new Lightning channels simply need to be opened to provide this liquidity. Indeed, the initial funds blocked in the on-chain multisig are entirely on the payer's side of the Lightning channel at the outset. Payment capacity is therefore guaranteed as long as channels are open with sufficient funds. When outgoing liquidity is exhausted, new channels simply need to be opened.

For the seller, on the other hand, the task is more complex. To be able to receive payments, he needs to have liquidity on the opposite side of his channels. Opening a channel is not enough: he must also make a payment in that channel to move the liquidity to the other side before he can receive payments himself. For some Lightning user profiles, such as merchants, there is a clear disproportion between what their node sends and what it receives, since the aim of a business is above all to take in more than it spends, in order to make a profit. Fortunately, for those users with specific needs in terms of incoming liquidity, several solutions exist:

- Attract channels**: The merchant enjoys an advantage due to the volume of incoming payments expected on his node. Taking this into account, he can try to attract router nodes that are looking for transaction fee income and could open channels to him, in the hope of routing his payments and collecting the associated fees.
- Shifting liquidity** : The seller can also open a channel and transfer part of the funds to the opposite side by making fictitious payments to another node, which will return the money in another way. We'll see how to do this in the next section.
- Triangle opening**: Connection platforms exist for nodes wishing to open channels collaboratively, enabling everyone to benefit from inbound and outbound liquidity immediately. For example, [LightningNetwork+](https://lightningnetwork.plus/) offers this service. If Alice, Bob and Suzie wish to open a channel of 100,000 sats, they can agree on this platform for Alice to open a channel to Bob, Bob to Suzie, and Suzie to Alice. In this way, each has 100,000 sats of outgoing liquidity and 100,000 sats of incoming liquidity, while having tied up only 100,000 sats.
![LNP201](assets/fr/73.webp)

- Channel purchase**: Lightning channel rental services also exist to obtain incoming liquidity, such as [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) or [Pool de Lightning Labs](https://lightning.engineering/pool/). For example, Alice can purchase a channel of one million satoshis to her node in order to receive payments.
![LNP201](assets/fr/74.webp)

Finally, for routers, whose objective is to maximize the number of payments processed and fees collected, they must :

- Open well-supplied channels with strategic nodes.
- Regularly adjust the allocation of funds to channels according to network needs.
### The Loop Out service

The [Loop Out](https://lightning.engineering/loop/) service, offered by Lightning Labs, enables liquidity to be moved to the opposite side of the channel while the funds are recovered from the Bitcoin blockchain. For example, Alice sends 1 million satoshis via Lightning to a loop node, which returns these funds in on-chain Bitcoins. This balances her channel with 1 million satoshis on each side, optimizing her ability to receive payments.

![LNP201](assets/fr/75.webp)

This service allows you to have incoming liquidity, while recovering your bitcoins on-chain, thus limiting the amount of cash tied up in accepting payments with Lightning.

**What should you learn from this chapter?

- To send payments on Lightning, you need to have sufficient liquidity on your side in your channels. To increase this sending capacity, simply open new channels.
- To receive payments, you need to have liquidity on the opposite side in your channels. Increasing this receiving capacity is more complex, as it requires others to open channels to you, or to make payments (fictitious or otherwise) to move liquidity to the other side.
- Keeping liquidity where you want it can be even more difficult, depending on channel usage. That's why tools and services exist to help balance channels as desired.
In the next chapter, I'll review the most important concepts of this training.

# Go further

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Conclusion of the training

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![conclusion](https://youtu.be/MaWpD0rbkVo)

In this final chapter, which marks the end of the LNP201 training course, I'd like to take you back over the important concepts we've seen together.

The aim of this course was to provide you with a comprehensive and technical understanding of the Lightning Network. We discovered how the Lightning Network relies on the Bitcoin blockchain to carry out off-chain transactions, while retaining the fundamental characteristics of Bitcoin, notably the absence of any need to trust other nodes.

### Payment channels

In the first chapters, we saw how two parties, by opening a payment channel, can carry out transactions outside the Bitcoin blockchain. Here are the steps covered:

1. **Channel opening**: The channel is created via a Bitcoin transaction that locks the funds onto a 2/2 multisignature address. This deposit is the Lightning channel's representation on the blockchain.

![LNP201](assets/fr/76.webp)

2. **Transactions in the channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new channel state reflected in a commitment transaction.

![LNP201](assets/fr/77.webp)

3. **Securing and closing**: Participants commit to the new state of the channel by exchanging revocation keys to secure funds and prevent cheating. Both parties can close the channel cooperatively by making a new transaction on the Bitcoin blockchain, or as a last resort by forced closure. Although the latter option is less effective, as it takes longer and is sometimes poorly priced in terms of costs, it still enables funds to be recovered. In the event of cheating, the victim can punish the cheater by recovering all the channel's funds from the blockchain.

![LNP201](assets/fr/78.webp)

### The canal network

After studying isolated channels, we extended our analysis to the channel network:

- Routing** : When two parties are not directly connected by a channel, the network allows them to pass through intermediate nodes. Payments are then routed from one node to another.
![LNP201](assets/fr/79.webp)

- HTLC** : Payments passing through intermediary nodes are secured by "_Hash Time-Locked Contracts_" (HTLC), which allow funds to be blocked until the payment has been completed from end to end.
![LNP201](assets/fr/80.webp)

- Onion routing**: To guarantee payment confidentiality, onion routing hides the final destination from intermediate nodes. The sender node must therefore calculate the entire route, but in the absence of complete information on channel liquidity, it proceeds by successive attempts to route the payment.
![LNP201](assets/fr/81.webp)

### Liquidity management

We have seen that managing liquidity is a challenge on Lightning to ensure the smooth flow of payments. Sending payments is relatively simple: all you have to do is open a channel. However, receiving payments requires liquidity on the opposite side of your channels. Here are some of the strategies we've discussed:

- Attracting channels**: By encouraging other nodes to open channels to you, a user obtains inbound liquidity.
- Liquidity shift**: By sending payments to other channels, liquidity shifts to the opposite side.
![LNP201](assets/fr/82.webp)

- Use of services such as Loop and Pool**: These services enable you to rebalance or buy channels with liquidity on the opposite side.
![LNP201](assets/fr/83.webp)

- Collaborative openings**: There are also platforms for putting people in touch with each other to carry out triangle openings and access incoming liquidity.
![LNP201](assets/fr/84.webp)

### Thanks

I'd like to thank each and every one of you for your interest, support and questions throughout this series. Originally, my idea was to create French-language content around the technical aspects of Lightning, given the lack of resources available. It was a personal challenge that I wanted to take up by combining technical rigor and accessibility. If you like this free training course, please rate it in the "Rate this course" section and share it with your friends and on your social networks.

Thanks, see you soon!

### Bonus: Interview with Fanis

![interview de Fanis](https://youtu.be/VeJ4oJIXo9k)

### Bonus: Interview with Fanis

![interview de Fanis](https://youtu.be/VeJ4oJIXo9k)

# Conclusion

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Rate this course

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Final examination

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

Congratulations! 🎉

You've completed LNP 201 - Introduction to the Lightning Network! You can be proud of yourself, because this is not an easy subject. Few people go this deep down the Bitcoin rabbit hole.

Many thanks to **Fanis Michalakis** for offering us this great free course on the technical workings of the Lightning Network. Feel free to follow him on [Twitter](https://x.com/FanisMichalakis), on [his blog](https://fanismichalakis.fr/) or via his work at [LN Markets](https://lnmarkets.com/).

Now that you've mastered the Lightning Network, I invite you to explore our other free courses on Plan ₿ Network to delve deeper into other aspects of Satoshi Nakamoto's invention :

#### Understand how a Bitcoin wallet works with

https://planb.network/courses/cyp201
#### Discover the story of Bitcoin's origins with

https://planb.network/courses/his201
#### Set up a BTC payment server with

https://planb.network/courses/btc305
#### Mastering privacy principles in Bitcoin

https://planb.network/courses/btc204
#### Learn the basics of mining with

https://planb.network/courses/min201
#### Learn how to create your own Bitcoin community with

https://planb.network/courses/btc302
