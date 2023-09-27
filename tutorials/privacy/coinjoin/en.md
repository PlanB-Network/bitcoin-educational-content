---
name: Coinjoin
description: Understanding and using CoinJoin on Bitcoin.
---

![Caption](assets/1.jpeg)

# Understanding and using CoinJoin on Bitcoin.

## Introduction

One of the initial problems with any peer-to-peer payment system is double spending. How can we prevent malicious actors from abusing the payment network by spending the same units multiple times without relying on a central authority?

Satoshi Nakamoto came up with a solution to this problem with his Bitcoin protocol, an electronic peer-to-peer payment network that operates without the intervention of any central authority. In his White Paper, he explains that the only way to confirm the absence of a transaction, and thus verify that there is no attempt at double spending, is to be aware of all the transactions made on the distributed payment network.

In order for each user to be informed of the transactions, they must be publicly announced. The peer-to-peer payment system proposed by the Bitcoin protocol has therefore been made possible by a completely transparent and distributed infrastructure. Thus, anyone with a node is able to verify the chain of electronic signatures and the history of each coin, from its creation by a miner.

> This principle of distributing the ledger and publicly announcing new transactions is used in the latest cryptocurrency (bitcoin), but it was already used in previous cryptocurrencies such as b-money, invented by Wei Dai in 1998.
>
> This transparency and distribution imply that every user of the Bitcoin network is able to trace and observe the transactions of all other users. Privacy is therefore impossible at the payment level. Instead, it is achieved at the level of personal identification.

Instead of associating each unit of account with an identity (name, surname...), as in the traditional banking system, bitcoins are associated with a pair of keys. Users are therefore anonymously represented by a cryptographic identifier.

Thus, the loss of privacy on Bitcoin occurs when an observer is able to link certain UTXOs (Unspent Transaction Outputs) to certain users. When this link is made between a user and their units of account, it is then possible to track their payments and analyze the history of their bitcoins.

CoinJoin is a practice that allows breaking the history of UTXOs in order to provide a certain level of privacy to the Bitcoin user.
In this article, we will study together what CoinJoin is, how it works, and how to use it properly. We will mainly talk about Whirlpool, the most efficient implementation of CoinJoin today in my opinion, but we will also discuss other existing implementations. I will also talk to you about indicators that allow you to accurately calculate the level of privacy of your bitcoins. To not only stay in theory, I will show you concretely how to make a CoinJoin transaction in different ways. Finally, we will study the best practices to observe in order to not lose the gained privacy after a series of CoinJoins, and I will present you the different tools of the Samourai Wallet that allow this.

If you like this article, share it on social networks and with people you know who need it.

> Summary:
>
> - CoinJoin and bitcoin mixing.
> - Different implementations of CoinJoin.
> - The theoretical functioning of Whirlpool.
> - Tutorial: Whirlpool on Sparrow Wallet.
> - Tutorial: Whirlpool CLI on Dojo and Whirlpool GUI.
> - Best practices in post-mix.
> - Spending tools.
> - Is it wrong to mix bitcoins?

If you are a beginner Bitcoin user, before being able to approach this article, I strongly advise you to understand the structure of a Bitcoin transaction (UTXO, inputs, and outputs) by reading this short article on the subject: Mechanism of a Bitcoin transaction: UTXO, inputs, and outputs.

_The use of CoinJoin can present indirect risks for its user. Some providers may potentially block your funds and/or your account as a result of your actions, and may ask for justifications regarding the origin of these funds. The information contained in this article does not constitute advice on computer systems and software, nor any encouragement to carry out CoinJoins. Carrying out a CoinJoin involves using a software wallet connected to the internet (known as "hot"). It is possible that your funds may be lost and/or stolen. I advise you to do your own research on the various existing risks. This article cannot in any case be considered a sole source of information on these subjects._

## CoinJoin and bitcoin mixing.

Before we begin, it is important to understand the difference between CoinJoin and mixing.

Mixing (in English: "mixing", "blender" or "tumbler") is a technique that allows mixing UTXOs, that is, mixing bitcoins, in order to break their histories and blur tracing. The objective of this type of operation is to pseudonymize UTXOs so that the user gains in privacy. Pseudonymization occurs when the UTXO is part of a group of several other indistinguishable UTXOs.
Mixing and CoinJoin are initially two techniques with the same objective, but they do not work in the same way. Mixing relies on a trusted third party to whom we will entrust our bitcoins to mix, while CoinJoin relies solely on a coordinator who will synchronize the users' actions but will never have control over the funds.

With the arrival of CoinJoin, mixing quickly became obsolete and users turned away from it. There are still a few mixing services like ChipMixer. However, today this technique only exists on the sidelines while CoinJoin is used by more and more individuals.

As a result, in the common language of bitcoiners, many use the word "mixing" to ultimately refer to a CoinJoin. Even though this semantics is initially incorrect, it is generally accepted among users. We then talk about "mixed bitcoins" to refer to UTXOs that come out of a CoinJoin transaction.

![Caption](assets/1.jpeg)

CoinJoin is therefore a technique that allows breaking the history of UTXOs. It is based on a collaborative transaction with the same name: the CoinJoin transaction. This type of transaction was initially proposed by Gregory Maxwell in 2013 on the Bitcoin Talk forum: [link](https://bitcointalk.org/index.php?topic=279249.0)

The general operation is as follows: different users wishing to mix deposit an amount as input of a transaction. These inputs will come out as different outputs of the same amount (possibly with change, but we will study that later). At the output of the transaction, it is therefore impossible to determine which output belongs to which user. There is technically no link between the inputs and outputs of the CoinJoin transaction. The link between each user and each UTXO is broken, just like the history of each coin.

To allow CoinJoin without any user losing control of their funds at any time, the transaction is first constructed by the coordinator and then transmitted to each user. Each user then signs the transaction on their own side, verifying that it suits them, and then all the signatures are added to the transaction. If a user or the coordinator tries to steal the funds of others by modifying the outputs of the CoinJoin transaction, then the signatures will be invalid and the transaction will be rejected by the nodes.

If I may make an analogy, we can imagine CoinJoin as a chase between a helicopter and a car. Let's imagine a helicopter trying to follow a white car. The helicopter represents the person who wants to analyze your payments and the white car represents your UTXO. The helicopter can easily follow the car by flying above it.
Let's imagine that there are now four other similar white vehicles driving on this road near the followed car. The helicopter can still follow the white car it initially followed.
Now, let's imagine that these five cars enter a tunnel, preventing the helicopter from seeing the cars for a short moment. Upon exiting the tunnel, the helicopter will not be able to determine which of the five white cars corresponds to the car it initially followed. In this example, the tunnel acts as a CoinJoin. Your output UTXO from the CoinJoin transaction will be hidden among a group of other UTXOs. A potential observer will know that your UTXO is in this group, but they will not be able to determine with certainty which one is yours.

The technical goal for the CoinJoin user is to have the largest possible "Anonymity Sets" on their UTXOs. This concept is very important to understand for the future. "Anonymity Sets," sometimes also referred to as "Anon Sets," refers to the parameters used to calculate the level of anonymity of a given UTXO. There are two types: prospective score and retrospective score.

The prospective score indicates the size of the UTXO group in which our UTXO is hidden. For example, if I do a CoinJoin with four other users, my prospective score will be equal to five immediately after the CoinJoin transaction.

If we go back to our helicopter example, each white car exiting the tunnel has a prospective score of five. The helicopter knows that its target is among this group of five cars, but it is unable to distinguish which one is its initial target car.

I will explain in more detail what these two parameters represent in this section: Anon Sets. For now, just remember that the higher the Anon Sets are for a mixed UTXO, the more difficult it will be to trace it by an observer.

# Different CoinJoin implementations.

A CoinJoin transaction could be done manually, directly with other Bitcoin users you meet. However, this solution, besides being very tedious, is not very efficient. For the CoinJoin transaction to be efficient, fast, and scalable across the network, it is necessary to be able to collaborate with any other user in the world. Instead, the services of a coordinator are used, whose role is to develop an implementation with a transaction model, connect different users, and transmit the information necessary for the successful completion of the collaborative transaction.

There are mainly three implementations of CoinJoin on Bitcoin:

> JoinMarket.
>
> Wasabi.
>
> Whirlpool.
> Even though the ultimate goal of these three implementations is the same, namely to break the history of a UTXO by conducting CoinJoin transactions, their operations are very different. It is therefore important to understand the workings of each one in order to choose the implementation that best meets our expectations.

As you may have understood if you follow me on Twitter, personally, I prefer to use the Whirlpool implementation. So I will quickly explain the theoretical functioning of the other two solutions, detailing why I find them less suitable. Then, we will study in more detail the functioning of Whirlpool, the implementation developed by the Samourai Wallet team, which in my opinion is the best CoinJoin solution currently available.

The characteristics mentioned for each implementation are currently valid. It is possible that they have evolved by the time you read this article.

![Caption](assets/2.jpeg)

## JoinMarket.

JoinMarket stands out from the other main implementations thanks to its user matchmaking model. Indeed, it is based on an exchange market between users who provide liquidity for mixing, and users who take liquidity to mix.

When you want to perform a CoinJoin on JoinMarket, you have to choose between leaving your bitcoins so that others can use them for mixing in exchange for a fee, or taking liquidity from other users to mix directly by paying the requested fee. There are therefore "makers" who leave their bitcoins available and "takers" who use the liquidity. The "takers" pay the "makers" for their service.

We are therefore talking about a completely free market, with no conditions of use.

The main disadvantage of this service is that it is quite complex to use. You need to have a minimum knowledge of Linux command lines to be able to use it properly. This implementation is relatively efficient, but it is clearly not suitable for the general public.

In terms of the features related to the CoinJoin transaction, JoinMarket has some weaknesses compared to Whirlpool. For example, the structure of the CoinJoin transaction used means that there cannot be 0% deterministic links between inputs and outputs. It can also be noted that JoinMarket does not include a tool to prevent a new CoinJoin between coins that have already met in the past.

In terms of additional services offered to the user, JoinMarket does not include a tool to easily calculate the Anon Sets of a UTXO. As for the tools for spending mixed UTXOs, the implementation only offers PayJoin.

## Wasabi 2.0.

Finally, JoinMarket is an interesting implementation of CoinJoin, but it is not intended for everyone. If you are comfortable with command lines, if you have a good understanding of how CoinJoin works, and if you like the "takers" / "makers" model, then this implementation may suit you.

The CoinJoin service of Wasabi theoretically works like Whirlpool's. Unlike JoinMarket, where organization is done on a free market, Wasabi acts as a coordinator that automatically mixes the bitcoins of all users of the service.

The structure of the CoinJoin transaction itself is, however, quite different from that of Whirlpool. As we will see in the next section, the increase in prospective score (Anon Set) of the mixed UTXOs on Whirlpool is achieved through the accumulation of several CoinJoins with few users each time. On the contrary, the Anon Sets of the mixed UTXOs on Wasabi are achieved through few transactions with a large number of users.

Example of a CoinJoin possibly performed on Wasabi 1.0:
[https://kycp.org/#/b994a9cbdc20e971207bde4f800b9ce99dba35478a2a997bc48e7f9f80bd2d02](https://kycp.org/#/b994a9cbdc20e971207bde4f800b9ce99dba35478a2a997bc48e7f9f80bd2d02)

Example of a CoinJoin performed on Whirlpool: [https://kycp.org/#/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://kycp.org/#/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

The two implementations also differ in change management. On Whirlpool, the change is separated and isolated from the UTXOs before the CoinJoin through the TX0 (I will talk about it in the next section). On Wasabi, the change is an output of the CoinJoin transaction. The choice of this CoinJoin structure on Wasabi means that deterministic links remain between the inputs and certain outputs.

In version 2.0, Wasabi has completely changed its CoinJoin fee policy. The coordinator fees are now 0.3% for UTXOs greater than 0.01 bitcoin, and they are waived for UTXOs below this amount. Small UTXOs also benefit from free remixes. Note that even if the coordinator fees are waived, the user will still have to pay mining fees for all transactions, including remix transactions.

Thus, unlike Whirlpool, the more significant Anon Sets you want to have on your mixed UTXOs with Wasabi, the more fees you will have to pay. This is true for both version 1.0 and version 2.0 of Wasabi. Even though the latest version offers coordinator fees for small UTXOs, there are still mining fees. Furthermore, when using version 2.0, I had the impression that the maximum prospective score achievable on Wasabi is 300. On Whirlpool, it is easy to reach a prospective score with five digits within a few months, and this score is not limited.

Beyond the structure of CoinJoin itself, in my opinion, Wasabi is sorely lacking complementary tools for CoinJoin, especially for properly spending mixed UTXOs. In version 1.0, there is no spending tool. In version 2.0, Wasabi has included a tool for spending mixed UTXOs that allows for adjusting inputs and outputs automatically to maximize privacy by removing change. Although this feature can be useful, it seems to be much less effective and practical to use compared to the myriad of tools offered on Samourai and Sparrow Wallet for properly spending UTXOs mixed with Whirlpool. I will discuss all these tools further in the article, in this section: Spending Tools.

Unlike Whirlpool, Wasabi does not separate the accounts of mixed UTXOs, non-mixed UTXOs, and change UTXOs. This wallet structure allows for address reuse between mixed UTXOs and other UTXOs. If this happens, it can completely break a CoinJoin.

Finally, after trying version 2.0, I really come out with the impression of not having control over my CoinJoin when using Wasabi. Everything is simplified and automated, the user interface is beautiful, but is this what we expect from a CoinJoin implementation?

## Theoretical Operation of Whirlpool.

Unlike the other implementations mentioned, Whirlpool stands out for the construction of "ZeroLink" CoinJoin transactions, which means there is strictly no technical link between all the inputs and outputs.

This is made possible by a CoinJoin transaction where each user deposits the same amount as input, which then comes out as an equal number of outputs with the same amount.

With this type of restrictive construction on the inputs, the Whirlpool CoinJoin transaction is the only one that allows users to have 0% deterministic links between the inputs and outputs. This means that each output has an equal probability of belonging to a user as all the other outputs of the transaction.

The number of participants in each mix is limited to 5: 2 entrants and 3 remixers (we will later discover what this consists of). Therefore, every CoinJoin transaction on Whirlpool always has 5 inputs and 5 outputs.
![Schematic representation of a Whirlpool CoinJoin transaction.](assets/3.jpeg)

## Whirlpool Design.

The model proposed by Whirlpool is based on very small transactions. Unlike Wasabi and JoinMarket, the strength of Anon Sets is not acquired by the number of users participating in the CoinJoin, but by the succession of several small CoinJoins of 5 participants each time.

The user will be required to pay only once, when entering a pool, and then they can remix as much as they want for free. It is the new entrants who pay the mining fees for the remixers.

The Anon Sets will exponentially increase as the user and their encountered peers remix. The objective is therefore to take full advantage of all these free remixes that each time add depth to the UTXO's Anon Sets.

Whirlpool was designed based on 2 main criteria:

- That the implementation is usable on mobile.

- That the remix cycles are done quickly.

For these two reasons, the Samourai teams chose to limit the number of users to 5 per cycle. A lower number would not have allowed for an efficient CoinJoin and would have greatly reduced the Anon Sets per cycle. A higher number would probably not have been manageable on mobile clients, and it would have reduced the flow of cycles.

Finally, there is no need to have a high number of participants per CoinJoin on Whirlpool since the Anon Sets are created through the accumulation of multiple mixing cycles.

## Pools and fees.

In order for these multiple cycles to effectively increase the UTXO's Anon Sets, a certain framework must be put in place to restrict the amounts of UTXOs used. Whirlpool defines different pools.

A pool is a group of users who want to mix and have agreed on the amount of UTXOs used to optimize the CoinJoin's operation. Each pool defines a fixed amount of UTXO that the user must adapt to in order to enter. In practice, when you want to perform CoinJoins, you must choose a pool to enter and start mixing. The different pools currently available on Whirlpool are:

- 0.5 bitcoin.
- 0.05 bitcoin.
- 0.01 bitcoin.
- 0.001 bitcoin (= 100,000 sats).

Therefore, everyone can find a suitable option.

Each pool has a maximum amount to enter:

| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
| -------------- | ---------------------------------- | --- | ---- | --- |
| 0.5            | 35                                 |     | 0.05 | 3.5 |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

To enter a pool, fees must be paid. They are fixed for each pool and are intended for the teams that develop and manage Whirlpool in order to compensate them for this service. The fees are only charged once when you access the pool. Once you have entered a pool, you can remix as many times as you want for free.

Currently, here are the fees applied for each pool:

| Pool (bitcoin) | Entry fees (bitcoin) |
| -------------- | -------------------- |
| 0.5            | 0.0175               |
| 0.05           | 0.00175              |
| 0.01           | 0.0005 (50,000 sats) |
| 0.001          | 0.00005 (5,000 sats) |

You can easily calculate the fees incurred on your mixes with Whirlpool on this website: [https://www.whirlpoolfees.com/](https://www.whirlpoolfees.com/)

Also note that these fees are an "entry ticket" for the pool. Therefore, whether you enter pool 0.01 with 0.01 btc or with 0.5 btc, the fees will be exactly the same. Before mixing, a user must therefore consider whether they want to pay lower fees with a small pool, in which case they will end up with multiple small UTXOs, or if they prefer to use a larger pool by paying higher fees, but ending up with fewer UTXOs.

After the different mixing cycles, it is generally not recommended to merge multiple mixed UTXOs together. This could compromise the hard-earned privacy. Therefore, it is sometimes better to use a larger pool, even if it means paying higher fees, in order to end up with fewer UTXOs of larger sizes.

The other fees to consider will obviously be the mining fees inherent to any Bitcoin transaction. As a Whirlpool user, you will have to pay the mining fees for Tx0 and the mining fees for the initial mix. All other remixes will be free for you since Whirlpool's fee model is based on new entrants.

Each CoinJoin consists of 5 users. Among them, 2 are entrants and 3 are remixes. Thus, the two entrants of each mix will pay the mining fees for the 5 users, and then these two entrants will in turn benefit from the free remixes.

![caption](assets/4.jpeg)'
Thanks to this fee model, Whirlpool truly differentiates itself from other CoinJoin services, as the UTXO Anon Sets are not proportional to the price paid by the user. This means that very high Anon Sets can be achieved by simply paying the pool fees and the mining fees for two transactions (Tx0 and initial mix).

Of course, the user will also have to pay the mining fees when they want to withdraw their UTXO from the pool after performing multiple remixes.

As explained earlier, a UTXO is said to be in a pool when it is available for mixing. This does not mean that the user loses ownership. Throughout the different CoinJoins with Whirlpool, you remain fully in control of your keys and therefore in control of your bitcoins.

## Accounts on Whirlpool.

In order to implement this type of CoinJoin transaction, a wallet using Whirlpool will need to derive multiple accounts.

An account is a subsection within an HD wallet. This separation occurs at depth 3 of the wallet, i.e., at the xpub/xprv level.

If you are not familiar with the concept of accounts within an HD wallet, I recommend reading my dedicated e-book on this topic, which you can download for free by clicking here. I have also written an entire article on the functioning of derivation paths: Understanding the derivation paths of a Bitcoin wallet.

You obviously don't need to understand all of this to use Whirlpool, but just remember that an account is a subsection of an HD wallet that is completely separate from other accounts and has its own xpub/zpub.

It is thanks to this strict separation of different accounts that it is impossible for address reuse to occur between mixed and non-mixed bitcoins on Whirlpool.

On each HD wallet, it is possible to derive up to 2^(32/2) different accounts. The first account, which you unknowingly use as the default account on your wallet, is account 0'.

When using a wallet adapted for Whirlpool, it will automatically create 5 accounts:

> The Deposit account determined by index 0'.
>
> The Bad Bank (doxxic change) account determined by index 2,147,483,644'.
>
> The Pre Mix account determined by index 2,147,483,645'.
>
> The Post Mix account determined by index 2,147,483,646'.
>
> The Ricochet account determined by index 2,147,483,647': This last account is not directly used within the Whirlpool protocol, but it is linked to it. I will talk more about it later in the section dedicated to spending tools.

Each account has its own purpose and is intended for a specific task.

All accounts depend on the same seed. Therefore, the user can easily recover access to all their funds in case of a problem with their recovery phrase and optional passphrase. However, the recovery software will still need to be informed of the different indexes of the used accounts.

Now let's look at the different steps of a CoinJoin Whirlpool within these accounts.

## Tx0.

At the start of a CoinJoin, everything begins with the Deposit account. This is the account you use by default when creating a new Bitcoin wallet. This account needs to be credited with the bitcoins that the user wants to mix.

Tx0 is the first transaction in the Whirlpool mixing process. Its objective is to clean the UTXO(s) to be mixed before sending them to the first mix. This transaction will divide the input UTXO into several UTXOs that correspond to the chosen pool amount. All these equalized UTXOs will be sent to the Premix account. The remaining difference that cannot enter the chosen pool will be separated into a dedicated account: Bad Bank (or "Doxxic Change").

Tx0 will also be used to pay the coordinator fees.

You will need to pay mining fees for Tx0.

![Diagram of a CoinJoin Bitcoin Tx0!](assets/5.jpeg)

Credit (modified image): KYCP.org: https://kycp.org/#/a126e48d4a6eb8d19682ec0e23ad45e76cd52b45f6c17be5068ae051d4b2cc24

In this example of a Tx0 transaction, we can see an input of 2.2550 bitcoins from the user's deposit account initiating Tx0. This input is divided into several output UTXOs representing:

- Coordinator fees, here: 0.0250 B.

- Four UTXOs ready to be mixed, which will go to the user's Premix account. These UTXOs are also registered with the coordinator.

- The remaining difference that cannot enter the pool because it is too small: this is the toxic change that will go to its dedicated and isolated account.

The fees here are different from the ones I provided in the previous table because Samourai has reduced its prices for Whirlpool in March 2021.

## Doxxic Change account.

The change that cannot be included in the pool is sent to the Doxxic Change account (also known as "Bad Bank") to completely separate it from the rest of the accounts.

This UTXO is dangerous for the user's privacy because not only is it still attached to its past, and therefore potentially to the owner's identity, but it is also marked as belonging to an owner who has done a CoinJoin.
If this UTXO is merged with mixed UTXOs, the latter will lose all the previously gained confidentiality. If it is merged with other Doxxic Changes, the user risks losing confidentiality. It must therefore be treated with caution. I will explain precisely how to handle this toxic UTXO in this section.

## Pre Mix Account.

In the Pre Mix account, we will find the UTXOs equalized during Tx0 ready to be mixed. These UTXOs are slightly higher than the pool amount as they will have to cover the mining fees of their initial mix.

Once these UTXOs have passed through their initial mix, the Pre Mix account will be empty and new UTXOs will be present in the next account.

## Post Mix Account.

The Post Mix account receives freshly mixed UTXOs from their initial mix. It also receives all other UTXOs that remain available for remixes.

If the Whirlpool client is running, the UTXOs present in the Post Mix account are available for remixes. They will be randomly selected to be remixed.

When the user wants to spend mixed UTXOs, they can do so directly from this Post Mix account. It is also advisable to leave mixed UTXOs in this account, not only to be remixed for free, but also to keep them within the Whirlpool circuit, otherwise they may lose confidentiality.

## Anon Sets.

As explained earlier, Anon Sets are two parameters that allow you to calculate how confidential a UTXO is, and therefore how effective your CoinJoin session is.

The first parameter is the prospective score (in English: "Forward-looking Anon Set"). Although this terminology is incorrect, this score is often directly referred to as "Anon Set" for short.

The prospective score of a UTXO represents the size of the group among which it is hidden at a given time.

To give you an image, the prospective score is the number of current UTXOs that can correspond to a given UTXO in the past. For example, imagine an actor observing the Bitcoin chain who tracks a UTXO that belongs to you before it enters the CoinJoin pool. After your coin has gone through several mixes, the observer wonders where it has gone. He then starts tracing the different possible paths and, thanks to the nature of CoinJoin, he will come across several UTXOs that could potentially correspond to yours. This number of potential UTXOs is the prospective score of your UTXO among them.

Thus, at the output of a first Whirlpool CoinJoin, a UTXO will have a prospective score of 5. That is, it will be hidden in a probable group of 5 UTXOs:

![Calculation diagram of the prospective score of a Bitcoin UTXO](assets/6.jpeg)

If someone is monitoring my input UTXO, they will not be able to know which of these 5 output UTXOs belongs to me.

This prospective score increases as the user's remixes, as well as the remixes of the peers they have encountered during their previous mixes, increase. Let's take our example with a UTXO that currently has a prospective score of 5. If this UTXO, which belongs to us, is remixed, then its score will increase to 9.

What is very interesting about Whirlpool is that even if my UTXO is not remixed, since it is part of a group where it cannot be distinguished from others, its score will increase based on the remixes of its peers encountered in the past.

Let's imagine that our UTXO has gone through a first mix and therefore has a score of 5. If a UTXO present in the same mix goes through a new remix, then the score of my UTXO will increase to 9, even though it has not moved since the initial mix:

![Calculation diagram of the prospective score of a Bitcoin UTXO](assets/7.jpeg)

This exponential increase in the prospective score is possible because if a UTXO encountered by the UTXO I encountered during my first mix is remixed, then my Anon Set increases even more:

![Calculation diagram of the prospective score of a Bitcoin UTXO](assets/8.jpeg)

This exponential increase is made possible by Whirlpool's unique model established on numerous successive small CoinJoins.

As a reminder, all these remixes are free, so it is very wise to let your UTXOs mix and remix themselves, while taking advantage of the remixes of the peers encountered, as long as you do not need to spend these UTXOs that belong to you.

![stylish video](assets/7-5.mp3)

The second Anon Set that can be determined for a given UTXO to calculate its level of privacy is the retrospective score (in English "Backward-looking Anon Set").

This retrospective score is, in a way, the legacy left by the peers before your initial mix. It indicates the number of Tx0s that can correspond to your mixed UTXO.

Therefore, it allows us to assess the level of privacy of a UTXO against an attempt to trace it back, as opposed to the first one mentioned.

Remember, for the prospective score, this parameter allows us to judge how confidential we are in case of an attempt to trace from an input UTXO of CoinJoin cycles to our output UTXO. For the retrospective score, the parameter allows us to judge how confidential an input UTXO is by starting the tracing from an output UTXO of a cycle. In other words, we reverse the path.

For example, let's imagine that a Bitcoin chain observer knows a UTXO and wants to trace its origin. They will then see that this UTXO has passed through CoinJoins, and they will come across many UTXOs as inputs to CoinJoins that could potentially be the one they are looking for. This number of potential UTXOs is the retrospective score of the traced UTXO.

To calculate this retrospective score, you first need to count all the UTXOs from a Tx0 starting from the targeted UTXO. Then, you will need to analyze the remixing UTXOs as inputs to the transaction and trace back to the 3 previous CoinJoin transactions from which they originated. The same calculation will be performed on each of these three transactions. This process continues until the CoinJoin Genesis transaction, which is the first CoinJoin transaction in the pool.

![Calculation diagram of the retrospective score of a Bitcoin UTXO](assets/9.jpeg)

In the above diagram, calculating the retrospective score of one of the UTXOs output from the top CoinJoin is equivalent to calculating the number of Tx0 (blue bubbles) present in the ascending CoinJoins up to the targeted CoinJoin, until the CoinJoin Genesis.

Unlike the prospective score of a UTXO, which starts at 5 after its initial mix and increases, the retrospective score of a UTXO will be immediately very high once you have performed your initial mix. The more recently an UTXO has been mixed, the higher its retrospective score. You benefit from the inheritance of previous mixes in the chosen pool.

## Whirlpool Stats Tool (WST).

To easily calculate the Anon Sets of one of your UTXOs mixed on Whirlpool, you can use the Whirlpool Stats Tool (WST). It is a tool specifically designed to calculate your Anon Sets on Whirlpool.

If you are a RoninDojo user, the tool is pre-installed on your node. To access it from RoninCLI, go to:

```
Samourai Toolkit > Whirlpool Stat Tool
```

If you do not have a RoninDojo, here is how to install the WST tool on a Linux machine:

You will need: Tor Browser (or Tor), Python 3.4.4 or higher, git, and pip3.

To check their version, enter the commands:

```
python --version
git --version
pip --version
```

Install the dependencies:

```
pip install PySocks
pip install requests[sock5]
pip install plotly
pip install datasketch
pip install numpy
```

Install Whirlpool Stats Tool:

````
#Clone the repository:
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git

#Access the /whirlpool_stats directory:
```markdown
cd whirlpool_stats
#Install dependencies with pip:
pip3 install -r ./requirements.txt
````

I personally had some issues with this latest version of WST. If it doesn't work for you, you can also clone the previous version on github which works perfectly: https://github.com/Samourai-Wallet/whirlpool_stats. The following steps will be the same. Just note that the 100k sats pool did not exist at that time, so you need to manually add it to the code if you are using the old release.

Then create a working directory to store transaction data, and launch WST:

#Access the desired directory, for example home:

```
cd ~

#Create a dedicated directory, for example named "wst":
mkdir wst

#Access the subdirectory /whirlpool_stats:
cd whirlpool_stats/whirlpool_stats/

#Launch WST:
python3 wst.py
```

Once WST is installed and launched, here's how to calculate Anon Sets. These steps are similar whether you are on a regular machine or on RoninDojo:

Enter the following command to set the proxy to Tor (for RoninDojo this command is mandatory):

```
        socks5 127.0.0.1:9050
```

If you are using Tor Browser, it must be running and the command will be:

```
        socks5 127.0.0.1:9150
```

Then access the working directory created in the previous step with the workdir command. If you are on RoninDojo, skip this step:

```
workdir /home/psyduck/wst
#Replace the path in this example with your own path.
```

![Launching WST command lines](assets/10.jpeg)

Next, download the data from the pool that contains your transaction:

```
download 0001

#Replace 0001 with the pool denomination code you are interested in.
```

The denomination codes are as follows in WST:

- 0.5 bitcoins pool: 05
- 0.05 bitcoins pool: 005
- 0.01 bitcoins pool: 001
- 0.001 bitcoins pool: 0001

Once the data is downloaded, load it with the command:

```
load 0001

#Replace 0001 with the pool denomination code you are interested in.
```

![Downloading WST data from OXT command lines](assets/11.jpeg)

After loading the data, enter the score command followed by your TXID (transaction identifier) to get its Anon Sets:

```
score TXID

#Replace TXID with the identifier of your transaction.
```

![Result of calculating Anon Sets for a UTXO with WST](assets/11.jpeg)
WST then displays the backward-looking score and the forward-looking score. In addition to the scores of the Anon Sets, WST also provides the diffusion rate of your output in the pool based on the anon set.

Please note that the forward-looking score of your UTXO is calculated from the TXID of your initial mix, not from your last mix. On the contrary, the backward-looking score of a UTXO is calculated from the TXID of the last cycle.

## Muuuh xpubs.

There is a lot of misinformation about how Whirlpool works. The most common one is probably the criticism that Samourai has access to users' xpubs on a server.

In reality, the Whirlpool protocol works without needing access to users' xpubs. The need for xpub is at the wallet level, like all other software, and is limited to a specific use:

- If you use Whirlpool on Samourai Wallet without using your own Dojo, then yes, Samourai's Dojo knows your xpub.

- If you use Whirlpool on Samourai Wallet with your own Dojo, no xpub leaks.

- If you use Whirlpool on Sparrow Wallet without using your own node, the third-party node you are connected to sees your transactions.

- If you use Whirlpool on Sparrow Wallet with your own node, nothing leaks on this front.

Like any other Bitcoin wallet, you should use your own node. Otherwise, you lose independence, privacy, and trust. But ultimately, this has nothing to do with the Whirlpool protocol. In this regard, Samourai Wallet acts like any other existing wallet.

Now that we have seen the theory and the general functioning, let's try the practice!

# Practical section

## Tutorial: Whirlpool on Sparrow Wallet.

There are many options for using Whirlpool. The first one I want to present to you is the implementation of Sparrow Wallet, an open-source Bitcoin wallet management software on PC.

This method has the advantage of being fairly easy to use, quick to set up, and requiring no device other than a computer and an internet connection. However, this method has a notable disadvantage that is not found in the second tutorial you will find in the next section:

- The mixes will only occur when Sparrow is launched and connected. This means that if you want to mix and remix your bitcoins 24/7, you will have to keep your computer on constantly.

The unique solution to this problem is to use your own Dojo. I will talk about it in the next section.
If you have never used Whirlpool before, and you want to do it for now more for understanding than for efficiency, I advise you to start slowly with Sparrow to fully understand the mechanisms.

Let's get started, let's see together how to do it:

To begin, you will obviously need the Sparrow software. You can directly download it from the official Sparrow Wallet website or from their GitHub:

- [https://sparrowwallet.com/download/](https://sparrowwallet.com/download/)

- [https://github.com/sparrowwallet/sparrow/releases](https://github.com/sparrowwallet/sparrow/releases)

Before installing the software, it will be important to verify the signature and integrity of the executable you just downloaded. If you don't know how to do this, I explain how to do it on Windows in this article: [How to verify the integrity of a Bitcoin software on Windows?](https://example.com)

Once the software is installed, you will need to create a Bitcoin wallet. Note that to mix, you must have a software wallet (known as "hot"). Therefore, you will not be able to mix with a wallet secured by a hardware wallet.

It is not mandatory, but if you plan to mix significant amounts, I strongly recommend using a strong passphrase on this wallet. If you don't know how to create a wallet on Sparrow, I explain in detail how to do it in the 5th part of the following article: [Everything you need to know about the Bitcoin Passphrase](https://example.com)

Once the wallet is created, send the sats to be mixed to it. Simply click on "Receive" and send them to an address that belongs to you as you would normally do.

Here, you can see that I have just created my wallet and sent a little over 199k sats to it:

![Receiving bitcoins on Sparrow Wallet](assets/12.JPEG)

For now, you are using a regular account. This account indexed 0' will become your Deposit account for mixing.

To mix this UTXO that you just received, go to the list of UTXOs in the account by clicking on "UTXOs" on the left side of the interface:

![Selecting UTXOs to mix on Sparrow Wallet](assets/13.JPEG)

Then select the different UTXOs to mix by clicking on them. If you want to select multiple ones, hold down the control key and click on each of them. Once the UTXO is selected, it will be highlighted in blue.

Then click on the "Mix Selected" button at the bottom of the interface:

![Starting the bitcoin mixing process on Sparrow Wallet](assets/14.JPEG)

A window opens to explain the operation of Whirlpool. This is a simplification of what I explained in the previous section.

Click on "Next" after reading.

![Introduction to the operation of Whirlpool](assets/15.JPEG)

We also explain how accounts work. Click on "Next" after reading.
Introduction to Whirlpool accounts](assets/16.JPEG)

On the next page, you can enter a SCODE if you have one. A SCODE is a discount code to be applied to the pool entry fee. Samourai Wallet sometimes provides them to its users on special occasions (e.g. Christmas). Don't forget to follow them on Twitter so you don't miss out on future SCODES:

[https://twitter.com/SamouraiWallet](https://twitter.com/SamouraiWallet)

Next, choose the mining fees you wish to allocate to Tx0 and the initial mix. This will affect the speed at which your first mix is confirmed. As a reminder, you pay mining fees for your Tx0 and initial mix, but you won't pay mining fees for any other remixes.

Once you've chosen your fees, click "Next".

Whirlpool mining fee settings](assets/17.JPEG)

On this new window, you can choose which pool to enter by clicking on the drop-down list. The window also tells you the pool fee you'll be paying and the number of UTXO that will enter that pool. Then click on "Preview Premix".

In my example, I had an UTXO of 199k sats, so I'll enter the 100k sats pool with just one UTXO:

![Choose mix pool](assets/18.JPEG)

Sparrow will then ask you to enter your wallet password, which you set when you created it in the software.

Confirm Bitcoin wallet password](assets/19.JPEG)

This will take you to your Tx0 preview.

First of all, you can see that Sparrow has derived the various accounts required to use Whirlpool. You can see them on the left of the screen.

You can also see the structure of your transaction with the various outputs:

- Pool fees (coordinator).

- Premix UTXO.

- Doxxic Change.

![Verification of final Tx0 before distribution](assets/20.JPEG)

If you're happy with the transaction, click on the "Broadcast Transaction" button to broadcast your Tx0. If not, you can also modify the parameters of this Tx0 by clicking on the "Clear" button and restarting the construction of this transaction.

![Broadcast Tx0](assets/21.JPEG)

Once the Tx0 has been broadcast, you'll find your UTXO ready for mixing in the Premix account. Your UTXO is now registered by the coordinator and will be sent to its initial mix.

![Tx0 diffusée en attente de confirmation](assets/22.JPEG)

Here, we can see that my UTXO from Tx0 has been confirmed once. We can also see the initial mix that was built and broadcasted, but is awaiting confirmation:

![Confirmed Tx0, broadcasted initial mix](assets/23.JPEG)

If we go to the Postmix account, we can see that the UTXO from the initial mix has been broadcasted but not yet confirmed. Once it is confirmed, it will automatically remain available for future remixes that will not be charged.

In the "Mixes" column, you can observe the number of remixes for your different UTXOs. As a reminder, it is not so much the number of remixes that is important, but rather the Anon Sets, although the two pieces of information are partly related.

![Confirmed initial mix, UTXO awaiting remixes](assets/24.JPEG)

There you go, your UTXO has been mixed. It is currently in the pool awaiting remixes. If you want to stop mixing, simply click on the "Stop Mixing" button. You can restart it by clicking on the "Start Mixing" button.

If you want to keep your UTXO available for remixing, you must keep the Sparrow Wallet software open and your computer turned on (not in sleep mode).

You can optionally disable sleep mode in your operating system's settings. There is also an option to select in the Sparrow software to prevent your machine from going to sleep:

> Tools > Prevent Computer Sleep

![Prevent computer from going to sleep](assets/25.JPEG)

The "Mix to" button on your Postmix account in the UTXO section allows you to set up automatic sending of your mixed UTXO to the wallet of your choice. You can choose the number of remixes to be performed before sending to this wallet.

This option allows you, for example, to automatically send your Postmix to your hardware wallet. However, it is generally not recommended to use this option. I will explain why in the section: Best Practices in Post-Mixing.

I have presented one of the options for mixing with Whirlpool here, but there are others. For example, you can directly mix from your smartphone using the Samourai Wallet app on Android. The process will be similar to the one described in this section.

![Samourai](assets/26.JPEG)

## Tutorial: Whirlpool CLI on Dojo and Whirlpool GUI.

If you want to move on to the next stage, you can mix with Whirlpool on your own Dojo.

Dojo is an implementation of a Bitcoin node developed by the Samourai Wallet team. If you use your own Dojo for CoinJoin on Samourai, the xpubs of your different accounts will not be transmitted to third-party servers. This will increase your privacy by eliminating one of the risks inherent in Whirlpool.

In addition, Dojo integrates Whirlpool CLI, which allows you to run remixes 24/7 without the need to constantly keep your wallet open on another device. This solution requires running a Bitcoin node and is slightly more complex to set up than the previous example. However, it allows you to enjoy the best CoinJoin experience on Whirlpool with minimal associated risks.

To run your own Dojo, you can either directly install your Dojo node or use Dojo on another Bitcoin node implementation. The options available at present are:

- RoninDojo, which is simply a Dojo with additional tools and includes an installation wizard and an administration wizard. I explain in detail how to set up and use RoninDojo in this article: Installing and using your RoninDojo Bitcoin node.

- Umbrel via the "Samourai Server" application.

- MyNode with the "Dojo" application.

- Nodl with the "Dojo" application.

For our example, we will use three different interfaces:

- Samourai Wallet.

- Whirlpool GUI.

- Whirlpool CLI.

Whirlpool CLI will run on the Dojo in order to take advantage of the aforementioned benefits. It will be responsible for communicating with the coordinator and managing the mixes.

Whirlpool GUI is the graphical interface we will use to see what is happening on Whirlpool CLI and to initiate remote mixes. The GUI will be installed on a separate PC from the Dojo for easy management.

Samourai Wallet will host our CoinJoin wallet. It is a free and open-source application that you can download on Android or an emulator. With this application, you will always have control over your mixing wallet and can easily spend your postmix while on the go.

### Step 1: Prepare your Dojo.

The first step is to have a Dojo. You will need to retrieve the Dojo connection URL, which is in the form of a Tor address. You can also use its QR code. This address will allow you to connect your Samourai Wallet to your node via Dojo.

If you are using Umbrel, go to the App Store in the left menu and install "Samourai Server". Once the application is launched, you will find the QR code for connecting to the Dojo.

If you are using RoninDojo, go to RoninUI in your browser, log in, and click on "Manage" in blue at the bottom of the "Dojo" box. You can access the Samourai Dojo QR code by clicking on "Display Values".

![Dojo connection address](assets/27.JPEG)

### Step 2: Prepare your wallet.

For the wallet, we will use Samourai Wallet. You can download it from the Google Play Store or directly with the APK file on their official website.
Launch the application and connect to your Dojo using the QR code from the previous step. Once connected, click on "Create a new wallet".

![Connecting to Dojo from Samourai](assets/28.JPEG)

Samourai will then ask you to create a Passphrase. If you are not familiar with what a Passphrase is and how to properly configure it, I strongly recommend reading my article on this topic: Everything you need to know about the Bitcoin Passphrase.

Choose a strong Passphrase and make a physical backup of it. Click "next" to continue.

![Creating the wallet passphrase](assets/29.JPEG)

Then, you will need to choose a PIN to access the application. This PIN is very important, but it is not linked to your Bitcoin wallet. It is specific to the operation of the Samourai application. You will need it to access your wallet from the Samourai application. However, if you need to recover your wallet, only your Passphrase and recovery phrase (mnemonic) will be necessary. Choose a strong PIN, make a backup of it, and click "Next".

![Choosing the Samourai application PIN](assets/30.JPEG)

You will be asked to confirm this PIN a second time. Then, you will be able to access the recovery phrase of your Samourai wallet. Just like the passphrase, this information must be properly backed up on a physical and secure medium, otherwise you may permanently lose access to your bitcoins in case of a problem. To learn more about the recovery phrase, I recommend reading this article: What is the Bitcoin recovery phrase?

After validating, you will arrive at your new Samourai wallet. Before doing anything, start by testing your backups. Before doing this, retrieve an xpub from your wallet to make sure you are on the right one:

> Settings > Wallet > Show BIP44 XPUB

You will be given a QR code with the value of the XPUB. Simply write down the last 8 characters of this xpub on a piece of paper. For example:

> X2GGWaLt

This will ensure that you are on the correct wallet and that you have not made a typo in the passphrase.

Then, either overwrite the empty wallet or reinstall the Samourai application and try to rebuild it using only your previously made backups. To do this, after connecting to your Dojo, click on "Restore an existing wallet".
Enter the recovery phrase and passphrase noted on your physical backups, choose the same PIN as before, and then restore this wallet. If it doesn't work, then the backup of your recovery phrase is not good. Start again from step 2.
If you are able to access the wallet, go check that the first BIP 44 XPUB is still the same. Go to:

> Settings > Wallet > Show BIP44 XPUB

Check that the last 8 characters match the ones you noted on the piece of paper earlier. If not, then the backup of your passphrase is not good (or you made a typing error). Start again from step 2.
If your backup is functioning properly, you can proceed to the next step with peace of mind.

> Please note that this test of backing up a new wallet should also be performed on any other wallet, not just Samourai.

### Step 3: Prepare Whirlpool GUI.

We will now install Whirlpool GUI, the graphical interface that will allow you to manage your CoinJoins. Go to your personal computer.

First, you will need to install the Java Developer Kit (JDK). You can, for example, install OpenJDK for free from this website: https://adoptopenjdk.net/ This will allow you to compile and run software developed in Java.

![Installation of OpenJDK](assets/31.JPEG)

Once OpenJDK is installed, you can install Whirlpool GUI from the official Samourai Wallet website: https://samouraiwallet.com/download/whirlpool

Launch Whirlpool GUI. In order for Whirlpool GUI to connect, you will need to have either Tor Daemon or Tor Browser running in the background on your PC. You will need to start them before each use of Whirlpool GUI on this computer. If you do not have Tor, install it from the official website before starting: https://www.torproject.org/download/

![Whirlpool GUI connection choice](assets/32.JPEG)

From Whirlpool GUI, click on "Advanced: Remote CLI" to connect your Whirlpool CLI to your Dojo. You will need the Tor address of your Whirlpool CLI.

- To find it on Umbrel: simply launch the Samourai Server application, you will find it on the page.

- To find it on RoninDojo: go to the RoninCLI main menu and then to Credentials > Whirlpool.

In Whirlpool GUI, enter the Tor address found earlier in the "CLI address" box. Leave the "http://" but do not include the ":8899". Simply paste the address that was given to you.
On the next box, enter 9050 if you are using Tor Daemon or 9150 if you are using the Tor browser. If this is the first time you are connecting to your Whirlpool CLI from a Whirlpool GUI, you can leave the API key box empty. Otherwise, fill it in.
![Connecting Whirlpool GUI to Dojo](assets/33.JPEG)

Click on the "Connect" button to pair your Whirlpool GUI with your Whirlpool CLI. Please be patient, as it may take a few moments to establish the connection.

Next, you will be able to pair your Samourai wallet. Click on the QR code symbol on the right side of the screen to scan.

![Connecting Whirlpool GUI to Samourai wallet](assets/34.JPEG)

From your Samourai Wallet, go to:

> ... > Settings > Transactions > Pair with Whirlpool GUI

Scan the QR code of your Samourai wallet on Whirlpool GUI.

![Pairing Samourai wallet with Whirlpool GUI](assets/35.JPEG)

Make sure the connection is established on Whirlpool GUI. On the next page, activate "Use Dojo as wallet backend". Then click on the "Initialize GUI" button.

![Setting up Whirlpool GUI](assets/36.JPEG)

Then, you will be asked to confirm the passphrase of your Samourai wallet. Click on "Sign in" once finished.

![Confirmation of wallet passphrase](assets/37.JPEG)

Please wait a moment. Once the configuration is complete, you will arrive at Whirlpool GUI:

![Access to Whirlpool GUI interface](assets/38.JPEG)

### Step 4: Mix!

Everything is set up, you are ready to mix your bitcoins. To do this, send the sats to mix to the Deposit account of your Samourai wallet. You also have the option to do this directly from Whirlpool GUI.

Click on the "Deposit" button to generate a receiving address.

![Generating a Bitcoin receiving address](assets/39.JPEG)

On this page, you can see the minimum amounts to deposit to enter a specific pool. Always plan to deposit slightly more than this amount, otherwise your UTXO may not be able to enter the desired pool until mining fees decrease.

Therefore, send your bitcoins to mix to the generated address. You can generate a new address by clicking on the "Renew address" button.

For added security on your deposit, it is recommended to deposit your funds with Samourai Wallet. Simply click on the blue "+" at the bottom right of the application, then on "Receive".
Once the deposit is confirmed, you will be able to see it appear in the "Deposit" account on Whirlpool GUI. To start the Coinjoin series, select the UTXOs to send for mixing and click on the "Premix" button. Be careful, if you select multiple different UTXOs simultaneously, they will be merged during TX0. This can lead to a loss of privacy, especially if the sources of the UTXOs are different.
![Launching the Tx0 mix](assets/40.JPEG)

The Whirlpool configuration page opens. Choose the pool you want to enter. Choose the mining fees allocated to TX0 and the initial CoinJoin. At the bottom of the page, you are shown the change amount and the amount and number of equalized UTXOs. If the configuration suits you, click on the "Premix" button to start the CoinJoin process.

![Configuring the Tx0 mix](assets/41.JPEG)

Once TX0 is created, you can see your equalized UTXOs in the "Premix" account awaiting confirmation. If you want your Premix to be automatically mixed, and your future postmixes to automatically remix 24/7, activate the "Automatically mix premix & postmix" option from the "Configuration" tab on the left side of your window.

You can now exit Whirlpool GUI, your UTXOs are available for 24/7 CoinJoin thanks to your Whirlpool CLI on your Dojo.

You can observe your UTXOs from the "Postmix" account on Whirlpool GUI, or from the Whirlpool interface on Samourai Wallet. To do this, click on the small white Samourai logo at the top left of your screen. Whirlpool accounts are easily distinguishable on Samourai Wallet with a light blue color:

![Observing CoinJoin mixes from Samourai](assets/42.JPEG)

To spend your postmixes, simply click on the + at the bottom right of the screen, then choose a suitable spending tool.

To easily track your automatic mixes, I also recommend setting up a Watch-Only wallet with the Android Sentinel application. Enter the ZPUB of your PostMix account there, and follow the evolution of your CoinJoin in real time.

# Best practices in post-mix.

After mixing, it will be important to follow some best practices if you don't want to lose all the privacy you have gained through mixing.

## Post-mix UTXOs.

The best option after mixing is to leave your UTXOs in your PostMix wallet waiting to be spent. You can even let them remix without limits until you need them to buy something.
Some users will prefer to move their mixed bitcoins to a hardware wallet for added security. You can do this, but be very careful and follow the recommendations given by Samourai Wallet. Without doing so, you risk losing all the privacy you gained previously.

The most common mistake is UTXO merging. It is essential not to merge, meaning not to input mixed UTXOs and non-mixed UTXOs in the same transaction. This requires managing your UTXOs within your wallet and labeling them correctly to avoid any mistakes. Beyond CoinJoin, UTXO merging is generally a bad practice that often leads to a loss of privacy when not properly controlled.

You should also be cautious about consolidating mixed UTXOs themselves. It is possible to do small consolidations if your mixed UTXOs have significant Anon Sets, but this will reduce the level of privacy for your bitcoins.

Be very careful that the consolidation is not too large or that it does not occur after too few remixes, otherwise it will be possible to link your UTXOs before and after the CoinJoin through simple deduction. If you are not familiar with these concepts, it is safest not to consolidate UTXOs in post-mix and to send them one by one to your hardware wallet with a new blank address each time. Once again, remember to label each received UTXO properly.

I also advise against moving your post-mix to a wallet that uses minority scripts. For example, if you enter Whirlpool from a multisig wallet using P2WSH scripts, there is little chance that you will be mixed with other users who have the same type of wallet originally. If you withdraw your post-mix to the same multisig wallet, the level of privacy for your mixed bitcoins will be greatly reduced.

As with any other Bitcoin transaction, it is also important not to reuse receiving addresses. Remember, receiving addresses are meant to be used only once. Any new incoming transaction requires generating a new blank address.

> 1 UTXO = 1 Address

The simplest and safest option is to leave your mixed UTXOs undisturbed in their PostMix wallet. You can let them remix themselves and only touch them when you want to separate them, meaning when you want to spend them.

## Doxxic change UTXOs.

Next, you will need to be careful with the management of your "Doxxic Change", the change that could not enter the mixing pool. These toxic UTXOs created as a result of using Whirlpool are dangerous for your privacy as they link you to your use of CoinJoin. Therefore, it is important not to use them for anything and especially not to merge them with any other UTXO. Here's what you can do with them:

- Mix them in smaller pools: if your UTXO is large enough to enter a smaller pool on its own, then mix it. This is probably one of the best solutions. However, you should never merge multiple doxxic changes together to enter a pool. It's a bad idea that will link your different inputs in Whirlpool.

- Label them as "non-spendable" and leave them in the dedicated account: another good solution is simply not to touch them anymore and label them as "non-spendable" to ensure that you don't use them. If the price of bitcoin appreciates, new smaller pools will likely be created, allowing you to mix your small doxxic changes properly.

- Donate them: it is important to make small donations, according to what you can, to different developers working on Bitcoin and related software, as well as content producers who help us understand the use of these same software. You can also choose to donate to different associations that accept bitcoin payments. If your doxxic change is a burden for you, donate it.

- Use them to buy gift cards: some websites allow you to buy gift cards with bitcoin so that you can shop at different well-known merchants. You can get rid of your doxxic change by buying this type of gift card.

There are probably other techniques to get rid of a doxxic change. Some talk about anonymizing them using the Lightning Network, while others use a swap with Monero. These techniques may be good, but I don't discuss them in this article because I'm not familiar with them. I encourage you to do your own research on these topics.

# Spending tools.

So, as you can see, the safest practice in Post-Mix is to leave your mixed UTXOs in their dedicated account and not touch them until you want to spend them.

It will be important to finish the job beautifully and use tools specifically designed to optimize our privacy when spending a mixed UTXO.
The availability of these tools depends on the wallet software chosen by the user. Samourai Wallet stands out from its peers thanks to the diversity and efficiency of the tools it offers. Some of these tools are also available on Sparrow Wallet. Let's see together what these tools are and how to use them.

## PayJoin - Stowaway.

PayJoin is a CoinJoin between two people with a specific structure. It is used in the context of spending bitcoins. It can be used to spend mixed bitcoins as well as non-mixed bitcoins.

This specific transaction structure was first implemented by Samourai Wallet with the Stowaway tool. A BIP followed this implementation, taking the idea of PayJoin and renaming it P2EP (Pay-to-End-Point).

The specificity of PayJoin is that it produces a transaction that appears ordinary but is actually a mini CoinJoin between two users. To do this, the transaction structure involves the transaction recipient alongside the actual sender in the inputs. The recipient includes a payment to themselves in the middle of the transaction to be paid.

For example, if you buy a baguette from your baker for 4000 sats from a UTXO of 10,000 sats, and you want to do a PayJoin, your baker will add to your original transaction a UTXO of 15,000 sats that belongs to them as an input, which they will fully recover as an output, in order to blur heuristic analysis:

![Bitcoin PayJoin Transaction Diagram](assets/43.JPEG)

In this example, we can see that the Baker put in 15,000 as input and came out with 19,000. The difference is indeed 4,000 sats, which is the price of their baguette. You, who want to buy the baguette for 4,000 sats, entered with 10,000 and came out with 6,000. The difference is indeed -4,000 sats, which is the price of the baguette. In this example, I intentionally neglected mining fees to simplify.

Thanks to this structure, PayJoin breaks the common ownership heuristic of Bitcoin transaction inputs. When someone observes this payment, they will think that you simply combined 2 of your UTXOs to purchase an item for 19,000 sats and that you received change for 6,000 sats. In reality, we have seen that the situation is quite different. The chain analysis is therefore blurred, and the payment parameters are difficult to understand for anyone observing them.

This type of transaction can be an excellent solution for spending freshly mixed bitcoins without losing privacy.

JoinMarket also includes a PayJoin tool for spending, you can discover it by clicking here.
As seen previously, Samourai Wallet also has its PayJoin tool: Stowaway. You can use it either from the Sparrow Wallet software or from the Samourai Wallet application.

Stowaway is based on a type of transaction they call "Cahoots," which is a collaborative transaction between multiple users that requires an exchange of information outside the Bitcoin chain. To date, there are two Cahoots tools on Samourai: Stowaway and StonewallX2, which we will discover later.

Cahoots collaborative transactions require exchanging partially signed transactions between users. This process can be quite long and prohibitive to perform, especially if you are remote from the other user. However, it is still possible to do this manually with another Samourai Wallet user, which can be a good option if you are physically with the collaborating person. The manual process involves exchanging 5 QR codes to scan one by one.

At a distance, this process becomes too complex. Samourai has therefore developed an excellent solution: its own encrypted communication protocol established on Tor, Soroban. Thanks to Soroban, users no longer need to perform all these QR code exchanges. The exchanges are done automatically in the background, well hidden behind an optimized user interface.

Encrypted exchanges still require a form of connection and authentication between Cahoots collaborators. Soroban exchanges are therefore established on the users' PayNyms. If you are unfamiliar with PayNyms, I discuss them in detail in this article: What is PayNym and BIP47?

To put it simply, a PayNym is a kind of identifier linked to your wallet that allows you to set up a whole range of functionalities, including encrypted message exchanges. The PayNym is represented by an identifier and a drawing of a robot. Here is mine, for example (on the Testnet):

![PayNym on Sparrow Wallet](assets/44.JPEG)

To be able to perform a remote Cahoots transaction, and therefore a PayJoin via Samourai or Sparrow, you must "Follow" another user via their PayNym. In this case, to perform a Stowaway (PayJoin), you need to follow the person you want to send bitcoins to.

To do this from Sparrow Wallet, simply enter the PayNym or scan the collaborator's QR code in the "Find Contact" box, as you can see in the previous screenshot.

On Samourai, click on the blue "+" at the bottom right of the screen, then on "PayNyms" in purple. If you don't have a PayNym yet, you can generate yours by following the instructions.

![Samourai Wallet Bitcoin Wallet](assets/45.JPEG)

**Tutorial performed on the Testnet: these are not real bitcoins.**

Once in the PayNym interface, click on the blue "+". You can then follow your collaborator's PayNym by pasting their identifier or scanning their QR code.

Then click on "Follow":

![Follow a PayNym](assets/46.JPEG)

You are then asked if you want to "connect" to it. This functionality allows you to use BIP47 later on. It incurs some fees. In our case, we don't need it, so we won't connect.

![Connect to a PayNym](assets/47.JPEG)

In my example, I did a PayJoin between my Samourai Wallet and my Sparrow Wallet. To access PayNym on Sparrow Wallet, simply click on "Tools" and then on "Show PayNym".

![Show PayNym on Sparrow Wallet](assets/48.JPEG)

Here, you can see that my orange PayNym has received the Follow request from my white PayNym (on Samourai). I'm nice, I followed back:

![Follow PayNym on Sparrow Wallet](assets/49.JPEG)

Now that the Nyms are connected, they can communicate with each other via Soroban in an encrypted manner. We can now initiate a Cahoots transaction.

To perform a PayJoin Stowaway from Samourai, you will need to construct a transaction. If you want to spend mixed UTXOs, go to the Post-mix account before initiating the transaction.

Click on the blue "+", then on "send". You can also specifically choose which UTXO you want to send:

![Create a PayJoin Bitcoin from Samourai Wallet](assets/50.JPEG)

Then enter the amount you want to send. In my example, I'm sending 45,000 Testnet sats:

![Setting up the PayJoin Stowaway](assets/51.JPEG)

Click on "Cahoots". This window opens, where you can choose to do either a StonewallX2 or a Stowaway. Here, we want to do a Stowaway:

![Choose the type of collaborative Bitcoin Cahoots transaction](assets/52.JPEG)

As explained earlier, you can either manually perform the PayJoin or do it remotely. It's faster and easier to do it remotely, but it requires being connected via PayNym. In our case, we will choose this "Online" option:

![Choose the type of manual or Soroban collaboration](assets/53.JPEG)

You are then asked to choose your collaborator from your PayNym contacts. Here, I choose "luckyfrost", which is my orange PayNym on Sparrow:

![Choose the collaborator](assets/54.JPEG)

Confirm by clicking on "Verify Transaction".

![Verify the PayJoin Stowaway Bitcoin transaction](assets/55.JPEG)
You can then choose the mining fees allocated to this transaction. It should be noted that these fees will be paid by the initial issuer of the transaction. Click on "Start Stowaway".
![Choice of mining fees](assets/56.JPEG)

You are then invited to wait for your peer to confirm that they agree to carry out this collaborative transaction.

To confirm a cahoot request on Samourai, click on the blue "+", then on "Receive" in green. An address is displayed. In the top right corner, click on the three dots, then on "Receive Online Cahoots".

To confirm on Sparrow Wallet, click on the "Tools" tab, then on "Find Mix Partner". A window opens, click on "Next" and then on "Next" again to confirm the collaborative transaction.

The Cahoot is in progress. Your two wallets exchange partially signed encrypted transactions over Tor thanks to Soroban.

![Cahoots process via Soroban for Stowaway](assets/57.JPEG)

Once the Stowaway transaction is constructed, you can broadcast the transaction to send it to the Bitcoin network nodes.

![Cahoots completed, broadcasting the PayJoin Stowaway transaction](assets/58.JPEG)

There you go, the Stowaway transaction is broadcasted. Congratulations.

By observing the transaction, you can see the inputs and outputs of the two users. The difference between the output and the input of the white PayNym is indeed -45,000 sats, and the difference for the orange PayNym is +45,000 sats, which is the amount I finally sent.

![Structure of the PayJoin Stowaway transaction](assets/59.JPEG)

### Stonewall.

Stonewall is a specific transaction structure that mimics a CoinJoin between two people, without actually being one.

This transaction is not collaborative, it only involves the UTXOs belonging to the transaction issuer. Therefore, you can create a Stonewall transaction for any occasion without needing to agree with anyone.

Its operation is quite simple: we will input multiple UTXOs belonging to the issuer, and we will have 4 outputs. 2 of these outputs will be exactly the same amount, the others will be change. Among these 2 similar outputs, only one will actually go to the payment recipient.

This structure adds a lot of entropy to the transaction and confuses the tracks. By observing it from the outside, one would think that this transaction is a CoinJoin between two people. In reality, it is a payment. Therefore, it creates doubts in chain analysis.

This Stonewall tool is used by default on Samourai Wallet if your wallet meets the necessary conditions for its implementation. Let's see together how to make a Stonewall. For that, I am sending 50,125 sats using this tool:
![video](assets/60.mp4)

As you can see in this video, the Stonewall option is preselected by default.

This is what the Stonewall transaction looks like that I just performed in the video:

![Structure of the Stonewall transaction](assets/61.JPEG)

It can be seen that Samourai has aggregated 2 UTXOs belonging to me as inputs:

- 130,450 S

- 454,504 S

And, the 4 outputs of the Stonewall transaction can be recognized:

- 50,125 S, which is the actual payment I just made.

- 50,125 S, which returns to another address that belongs to me.

- The two changes: 80,168 S and 404,222 S, which also come back to me.

Therefore, my recipient has only received 50,125 sats, which is the value of the payment I wanted to initiate.

Obviously, if you want to spend post-mix, you will need to first go to your Whirlpool wallet before triggering the transaction.

Samourai will not charge you any fees for constructing a Stonewall transaction. You will obviously have to pay the mining fees for your transaction. These will be higher than a "regular" transaction since it has more inputs and outputs.

If you want to use this tool on Sparrow, I refer you to this tutorial that explains in detail how to perform the operation: [https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym](https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym)

## StonewallX2.

StonewallX2 works exactly like Stonewall, except that the inputs of the transaction are not only those of the sender, but also those of a third person. StonewallX2 is therefore a collaborative transaction between two Samourai users. As with Stowaway (PayJoin), communication between collaborators can be done manually (if you are in the same location) or remotely using Soroban via Tor.

The difference between Stowaway and StonewallX2 lies in the role of the collaborator. In the case of Stowaway, the collaborator is necessarily the payment recipient. In the case of StonewallX2, the collaborator simply provides their bitcoins for mixing, but they are not the payment recipient.

For example, if you want to make a confidential expense, but the merchant you want to send bitcoins to does not support Stowaway, then you can simply do a StonewallX2 with another person who has nothing to do with the transaction. The recipient will still be the merchant, but they do not need to perform all the operations related to Stowaway.
Thus, StonewallX2 is a mini CoinJoin between 2 people that includes a spending output. This adds a lot of entropy to the transaction. This specific structure adds statistical doubt to the links between the sender and the recipient.

If we look at a StonewallX2 transaction from the outside, its structure will be exactly the same as a Stonewall transaction. This adds even more doubt.

To perform a remote StonewallX2 transaction, you will need to be connected with your collaborator's PayNym, just like with stowaway. Once connected with the collaborator, let's see together how to make a remote StonewallX2 transaction. In this example, I am collaborating with my second PayNym on Sparrow Wallet. I don't show it in the video, but the Cahoot collaborator must confirm on their wallet that they want to participate in the joint transaction.

![video](assets/62.mp4)

Here is what the StonewallX2 transaction I just made in the video looks like:

![Structure of the collaborative Bitcoin StonewallX2 transaction](assets/63.JPEG)

The first input of 102,588 S comes from my Samourai wallet. The second input of 104,255 S comes from my collaborator's wallet. We can observe 4 outputs, including 2 of the same amount to confuse the tracks:

- 50,125 sats that go to the recipient of my payment.

- 52,306 sats that represent my change and therefore return to an address in my wallet.

- 50,125 sats that return to my collaborator.

- 53,973 sats that return to my collaborator.

For StonewallX2 transactions, mining fees are shared between the two collaborators. If we calculate the balance of each after the transaction, we have:

- The collaborator who entered with 104,255 sats and exited with 104,098 sats. The difference represents their share of mining fees. If we neglect these fees, the collaborator has indeed performed a blank action.

- For the sender, I entered with 102,588 sats and exited with 52,306 sats. The difference of 50,282 sats represents the amount I owe to the recipient (50,125 sats) plus my share of mining fees.

- The recipient did not enter the transaction and exits with 50,125 sats, which is the amount I want to pay them.

Samourai will not charge you any fees for constructing a StonewallX2 transaction. You will obviously have to pay the mining fees for your transaction. These will be higher than a "classic" transaction since it has more inputs and outputs.

## Ricochet.

The last tool I want to present to you is Ricochet. This tool is slightly different from the previous ones, which all aimed to increase prospective privacy. This tool allows you to reduce the trace left by a CoinJoin on a UTXO, and therefore increase retrospective privacy.

If you perform transactions like CoinJoin and send your mixed bitcoins directly to an exchange, it is possible that the provider will block your account or ask for justifications regarding the origin of your funds. To avoid these hypocritical and unfair blocks, you can use Ricochet to send your mixed funds to an exchange.

Thus, the only use case for Ricochet is when you want to hide the fact that you have performed a CoinJoin in the past on a UTXO that belongs to you.

To reduce this trace, Ricochet will perform 4 transactions where you will send the funds to yourself on different addresses, and then the tool will send the funds to your final target (the exchange). The goal is to add distance between the CoinJoin transaction and the deposit transaction. Thanks to this, chain analysis tools will think that there has been a change of ownership since the CoinJoin, and therefore the provider will probably not take the risk of blocking your account or asking for justifications.

This tool can be essential if you need to exchange mixed bitcoins, or simply if you want to reduce the "trace" of their past mixing.

As we have seen previously, the Ricochet account used for bounce addresses is completely separate from the deposit account.

There are two options for Ricochet:

- Enhanced Ricochet: also known as "staggered delivery", this option will distribute the fees paid to Samourai over the five bounce transactions. It will also ensure that each bounce is present in a different block. This option is therefore designed to be slow, but it optimizes the privacy and resistance to chain analysis of your operation.

- Normal Ricochet: this option allows you to perform the operation quickly, but it will be less confidential and resistant to analysis than the previous option. It is preferred for urgent transfers.

Ricochet is a paid service. You will need to pay 100,000 sats in fees to Samourai.

Here's how to perform a Ricochet on Samourai Wallet:

![video](assets/64.mp4)
You are now ready to use Whirlpool in the best possible way and spend your postmix properly. The spending tools of Samourai Wallet, also included in Sparrow Wallet for the most part, have no more secrets for you. I advise you to practice and try all these tools. To avoid risking your personal funds, feel free to first use them on the Testnet! This network is not reserved only for developers.

# Is it wrong to mix bitcoins?

In the speeches of altcoiners or beginners, CoinJoin is often described as a dark, dubious, or even dangerous practice. This type of nebulous narrative is often due to a technical misunderstanding of Bitcoin and a fantasy of CoinJoin.

All of this is obviously false. CoinJoin is a noble use of Bitcoin that allows individuals to regain control over the privacy of their payments, while improving the external fungibility of the payment network, without falling into absolute anonymity.

As explained earlier, CoinJoin simply allows a user to break the history of their bitcoins, and thus gain privacy on their payments, especially if their identity had been associated with a UTXO in the past.

It is thanks to these tools that allow each user to protect their privacy that we can achieve a free and unconstrained payment network. Without respect for privacy, no freedom exists.

Working to respect the privacy of Bitcoin users is a noble cause. When you perform a CoinJoin, not only do you ensure a certain level of personal privacy, but you also help many other individuals improve theirs.

Yes, CoinJoin is sometimes used by dishonest people. But it is also widely used by obligated individuals, for whom the need for privacy is not a comfort, but an obligation. If everyone only used CoinJoin when it becomes individually mandatory, those who are truly compelled to use this tool would only be mixed with dishonest individuals, and thus become more easily detectable by a tyrannical authority.

I also echo Gregory Maxwell's argument, presented on Bitcoin Talk in 2013 during his introduction of CoinJoin: "In reality, real criminals don't need CoinJoin, [...] they can afford to buy privacy in a way that regular users cannot, it's just an additional cost for their (often very lucrative) business."

In any case, let's remember that CoinJoin is a tool. Like any tool, it can be used constructively or destructively.
Finally, in my opinion, CoinJoin fits perfectly into the ideology and initial development line of Bitcoin. Cypherpunks write code. They develop tools that allow each individual to have control over their privacy and sovereignty on the Internet, two essential characteristics to ensure individual freedom.

Satoshi Nakamoto himself devotes a whole section of his White Paper to respecting the privacy of Bitcoin users. In this document, he highlights the risk of losing privacy if the owner of a key pair is revealed. He explains that if this happens, all of the owner's transactions could be traced. CoinJoin is currently the best solution to break this link between bitcoins and owners, as described by Satoshi Nakamoto in the White Paper.

To conclude, I advise you to study the different contents that I present in the "External Resources" section below, on which I relied to produce this article, and which will surely give you even more knowledge.

## To go further:

- [Everything you need to know about Bitcoin Passphrase.](https://www.pandul.fr/post/tout-savoir-sur-la-passphrase-bitcoin)

- [How to generate your own Bitcoin mnemonic phrase?](https://www.pandul.fr/post/comment-g%C3%A9n%C3%A9rer-soi-m%C3%AAme-sa-phrase-mn%C3%A9monique-bitcoin)

- [What is PayNym and BIP47?](https://www.pandul.fr/post/qu-est-ce-que-paynym-et-bip47)

## External Resources:

Twitter thread "Why we CoinJoin" by @SamouraiWallet:

https://twitter.com/SamouraiWallet/status/1489220847336308739

Article "HOW TO WHIRLPOOL ON DESKTOP WITH RONINDOJO" by ECONOALCHEMIST on https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/guides/how-to-whirlpool-with-ronindojo

Article "THE EASIEST WAY TO WHIRLPOOL YOUR BITCOIN AND PRESERVE PRIVACY" by ECONOALCHEMIST on https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/guides/how-to-whirlpool-bitcoin-on-mobile

Article "HOW TO WHIRLPOOL YOUR BITCOIN ON DESKTOP WITH SPARROW WALLET" by ECONOALCHEMIST on https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/technical/how-to-whirlpool-bitcoin-sparrow-wallet

Article "Diving head first into Whirlpool Anonymity Sets" by Samourai Wallet.

https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7

Twitter thread by @BrotherRabbit/\_ on the prospective score on Whirlpool:

https://twitter.com/BrotherRabbit_/status/1528399310227906561

Samouraï tutorial by JohnOnChain (Privacy), from the YouTube channel Découvre Bitcoin:

https://www.youtube.com/watch?v=kS6iC_ovarQ
Resources on Ricochet:
[Ricochet](https://docs.samourai.io/en/wallet/features/ricochet)

Resources on spending tools on Sparrow Wallet:
[Sparrow Wallet](https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym)

Resources on spending tools on Samourai Wallet:
[Samourai Wallet](https://docs.samourai.io/en/spend-tools#ricochet)

Article on the installation and use of WST (in Spanish):
[WST](https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/)

Article "Dealing with Coinjoin Change Outputs" by BitcoinQ+A on [bitcoiner.guide](https://bitcoiner.guide/):

[Dealing with Coinjoin Change Outputs](https://bitcoiner.guide/doxxic/)

Series of 4 articles "Understanding Bitcoin Privacy with OXT" by Samourai Wallet on [Medium](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-4-4-16cc0a8759d5)

Resources on Whirlpool by Samourai Wallet:
[Whirlpool](https://code.samourai.io/whirlpool/Whirlpool/-/blob/whirlpool/README.md)

[Basic Concepts](https://docs.samourai.io/whirlpool/basic-concepts)

[Whirlpool Features](https://docs.samourai.io/en/wallet/features/whirlpool)
