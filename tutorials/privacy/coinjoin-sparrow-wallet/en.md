---
name: Coinjoin - Sparrow Wallet
description: How to perform a coinjoin on Sparrow Wallet?
---
![cover](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, the Whirlpool tool no longer functions, even for individuals who have their own Dojo or are using Sparrow Wallet. However, it remains possible that this tool could be reinstated in the coming weeks or relaunched in a different manner. Moreover, the theoretical part of this article remains relevant for understanding the principles and objectives of coinjoins in general (not just Whirlpool), as well as understanding the effectiveness of the Whirlpool model.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

In this tutorial, you will learn what a coinjoin is and how to perform one using the Sparrow Wallet software and the Whirlpool implementation.

## What is a coinjoin on Bitcoin?
**A coinjoin is a technique that breaks the traceability of bitcoins on the blockchain**. It relies on a collaborative transaction with a specific structure of the same name: the coinjoin transaction.

Coinjoins enhance the privacy of Bitcoin users by complicating chain analysis for external observers. Their structure allows merging multiple coins from different users into a single transaction, thus blurring the trails and making it difficult to determine the links between input and output addresses.

The principle of the coinjoin is based on a collaborative approach: several users who wish to mix their bitcoins deposit identical amounts as inputs of the same transaction. These amounts are then redistributed as outputs of equal value to each user. At the end of the transaction, it becomes impossible to associate a specific output with a known user at the input. No direct link exists between the inputs and outputs, which breaks the association between the users and their UTXO, as well as the history of each coin.
![coinjoin](assets/notext/1.webp)

Example of a coinjoin transaction (not from me): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

To perform a coinjoin while ensuring that each user retains control over their funds at all times, the process begins with the construction of the transaction by a coordinator, who then transmits it to each participant. Each user then signs the transaction after verifying that it suits them. All collected signatures are finally integrated into the transaction. If an attempt to divert funds is made by a user or the coordinator, through a modification of the coinjoin transaction's outputs, the signatures will prove invalid, leading to the rejection of the transaction by the nodes.

There are several implementations of coinjoin, such as Whirlpool, JoinMarket, or Wabisabi, each aiming to manage coordination among participants and increase the efficiency of coinjoin transactions.

In this tutorial, we focus on the **Whirlpool** implementation, which I consider to be the most effective solution for performing coinjoins on Bitcoin. Although available on several wallets, this tutorial exclusively explores its use with the Sparrow Wallet Desktop software.
## Why Perform CoinJoins on Bitcoin?

One of the initial problems with any peer-to-peer payment system is double-spending: how to prevent malicious individuals from spending the same monetary units multiple times without resorting to a central authority for arbitration?

Satoshi Nakamoto provided a solution to this dilemma through the Bitcoin protocol, a peer-to-peer electronic payment system that operates independently of any central authority. In his white paper, he emphasizes that the only way to certify the absence of double-spending is to ensure the visibility of all transactions within the payment system.

To ensure that each participant is aware of the transactions, they must be publicly disclosed. Thus, the operation of Bitcoin relies on a transparent and distributed infrastructure, allowing any node operator to verify the entirety of the electronic signature chains and the history of each coin, from its creation by a miner.

The transparent and distributed nature of Bitcoin's blockchain means that any network user can follow and analyze the transactions of all other participants. Consequently, anonymity at the transaction level is impossible. However, anonymity is preserved at the level of individual identification. Unlike the traditional banking system where each account is linked to a personal identity, on Bitcoin, funds are associated with pairs of cryptographic keys, thus offering users a form of pseudonymity behind cryptographic identifiers.

Therefore, confidentiality on Bitcoin is compromised when external observers manage to associate specific UTXOs with identified users. Once this association is established, it becomes possible to trace their transactions and analyze the history of their bitcoins. Coinjoin is precisely a technique developed to break the traceability of UTXOs, thus offering a certain layer of confidentiality to Bitcoin users at the transaction level.

## How Does Whirlpool Work?

Whirlpool stands out from other coinjoin methods by using "_ZeroLink_" transactions, which ensure that there is strictly no technical link possible between all the inputs and all the outputs. This perfect mixing is achieved through a structure where each participant contributes an identical amount in input (except for mining fees), thus generating outputs of perfectly equal amounts.

This restrictive approach on inputs gives Whirlpool coinjoin transactions a unique characteristic: the total absence of deterministic links between the inputs and the outputs. In other words, each output has an equal probability of being attributed to any participant, compared to all the other outputs of the transaction.
Initially, the number of participants in each Whirlpool coinjoin was limited to 5, with 2 new entrants and 3 remixers (we will explain these concepts further on). However, the increase in on-chain transaction fees observed in 2023 prompted the Samourai teams to rethink their model to improve privacy while reducing costs. Thus, taking into account the market situation of fees and the number of participants, the coordinator can now organize coinjoins including 6, 7, or 8 participants. These enhanced sessions are referred to as "_Surge Cycles_". It is important to note that, regardless of the setup, there are always only 2 new entrants in the Whirlpool coinjoins.

Therefore, Whirlpool transactions are characterized by an identical number of inputs and outputs, which can be:
- 5 inputs and 5 outputs;
![coinjoin](assets/notext/2.webp)
- 6 inputs and 6 outputs;
![coinjoin](assets/notext/3.webp)
- 7 inputs and 7 outputs;
![coinjoin](assets/notext/4.webp)
- 8 inputs and 8 outputs.
![coinjoin](assets/notext/5.webp)
The model proposed by Whirlpool is thus based on small coinjoin transactions. Unlike Wasabi and JoinMarket, where the robustness of the anonsets relies on the volume of participants in a single cycle, Whirlpool bets on the chaining of several small-sized cycles.

In this model, the user incurs fees only upon their initial entry into a pool, allowing them to participate in a multitude of remixes without additional fees. It is the new entrants who bear the mining fees for the remixers.

With each additional coinjoin in which a coin participates, along with its past encountered peers, the anonsets will grow exponentially. The goal is thus to take advantage of these free remixes which, with each occurrence, contribute to strengthening the density of the anonsets associated with each mixed coin.

Whirlpool was designed taking into account two important requirements:
- The accessibility of implementation on mobile devices, given that Samourai Wallet is primarily a smartphone application;
- The speed of the remixing cycles to promote a significant increase in anonsets.

These imperatives guided the choices of the developers of Samourai Wallet in the design of Whirlpool, leading them to limit the number of participants per cycle. Too few participants would have compromised the effectiveness of the coinjoin, drastically reducing the anonsets generated with each cycle, while too many participants would have posed management problems on mobile applications and would have impeded the flow of cycles.

**Ultimately, there is no need to have a high number of participants per coinjoin on Whirlpool since the anonsets are made over the accumulation of several coinjoin cycles.**
[-> Learn more about Whirlpool anonsets.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Coinjoin pools and fees
To ensure that multiple cycles effectively increase the anonsets of mixed coins, a certain framework must be established to restrict the amounts of UTXOs used. Whirlpool defines different pools for this purpose.

A pool represents a group of users wishing to mix together, who agree on the amount of UTXOs to use to optimize the coinjoin process. Each pool specifies a fixed amount for the UTXO, which the user must adhere to in order to participate. Thus, to perform coinjoins with Whirlpool, you need to select a pool. The currently available pools are as follows:
- 0.5 bitcoins;
- 0.05 bitcoin;
- 0.01 bitcoin;
- 0.001 bitcoin (= 100,000 sats).

By joining a pool with your bitcoins, they will be divided to generate UTXOs that are perfectly homogeneous with those of the other participants in the pool. Each pool has a maximum limit; thus, for amounts exceeding this limit, you will be forced either to make two separate entries within the same pool or to move to another pool with a higher amount:

| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

As mentioned previously, a UTXO is considered to belong to a pool when it is ready to be integrated into a coinjoin. However, this does not mean that the user loses possession of it. **Through the various mixing cycles, you retain full control of your keys and, consequently, your bitcoins.** This is what differentiates the coinjoin technique from other centralized mixing techniques.

To enter a coinjoin pool, service fees as well as mining fees must be paid. The service fees are fixed for each pool and are intended to compensate the teams responsible for the development and maintenance of Whirlpool. For Sparrow Wallet users, these fees are passed on by the Samourai teams to the developers of Sparrow.

The service fees for using Whirlpool are to be paid once upon entering the pool. Once this step is completed, you have the opportunity to participate in an unlimited number of remixes without additional fees. Here are the current fixed fees for each pool:

| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


These fees essentially act as an entry ticket to the chosen pool, regardless of the amount you put in coinjoin. So, whether you join the 0.01 pool with exactly 0.01 BTC or you enter with 0.5 BTC, the fees will remain the same in absolute value.

Before proceeding with coinjoins, the user therefore has a choice between 2 strategies:
- Opt for a smaller pool to minimize service fees, knowing that they will receive several small UTXOs in return;
- Or prefer a larger pool, agreeing to pay higher fees to end up with a reduced number of larger-value UTXOs.

It is generally advised against merging several mixed UTXOs after the coinjoin cycles, as this could compromise the acquired confidentiality, especially due to the Common-Input-Ownership Heuristic (CIOH). Therefore, it might be wise to choose a larger pool, even if it means paying more, to avoid having too many small-value UTXOs as output. The user must weigh these trade-offs to choose the pool they prefer.

In addition to service fees, the mining fees inherent to any Bitcoin transaction must also be considered. As a Whirlpool user, you will be required to pay the mining fees for the preparation transaction (`Tx0`) as well as those for the first coinjoin. All subsequent remixes will be free, thanks to Whirlpool's model which relies on the payment of new entrants.

Indeed, in each Whirlpool coinjoin, two users among the inputs are new entrants. The other inputs come from remixers. As a result, the mining fees for all participants in the transaction are covered by these two new participants, who will then also benefit from free remixes:
![coinjoin](assets/en/6.webp)
Thanks to this fee system, Whirlpool truly differentiates itself from other coinjoin services since the anonsets of the UTXOs are not proportional to the price paid by the user. Thus, it is possible to achieve considerably high levels of anonymity by only paying the pool's entry fees and the mining fees for two transactions (the `Tx0` and the initial mix).

It is important to note that the user will also have to cover the mining fees to withdraw their UTXOs from the pool after completing their multiple coinjoins, unless they have selected the `mix to` option, which we will discuss in the tutorial below.

### The HD wallet accounts used by Whirlpool
To perform a coinjoin via Whirlpool, the wallet must generate several distinct accounts. An account, in the context of an HD (Hierarchical Deterministic) wallet, constitutes a section that is completely isolated from the others, this separation occurring at the third depth level of the wallet's hierarchy, that is, at the level of the `xpub`.
An HD wallet can theoretically derive up to `2^(32/2)` different accounts. The initial account, used by default on all Bitcoin wallets, corresponds to the index `0'`.

For wallets adapted to Whirlpool, such as Samourai or Sparrow, 4 accounts are used to meet the needs of the coinjoin process:
- The **deposit** account, identified by the index `0'`;
- The **bad bank** (or doxxic change) account, identified by the index `2 147 483 644'`;
- The **premix** account, identified by the index `2 147 483 645'`;
- The **postmix** account, identified by the index `2 147 483 646'`.

Each of these accounts fulfills a specific function within the coinjoin.

All these accounts are linked to a single seed, which allows the user to recover access to all of their bitcoins by using their recovery phrase and, if applicable, their passphrase. However, it is necessary to specify to the software, during this recovery operation, the different account indexes that were used.

Let's now look at the different stages of a Whirlpool coinjoin within these accounts.

### The different stages of coinjoins on Whirlpool
**Stage 1: The Tx0**
The starting point of any Whirlpool coinjoin is the **deposit** account. This account is the one you automatically use when you create a new Bitcoin wallet. This account must be credited with the bitcoins you wish to mix.

The `Tx0` represents the first stage of the Whirlpool mixing process. It aims to prepare and equalize the UTXOs for the coinjoin, by dividing them into units corresponding to the amount of the selected pool, in order to ensure the homogeneity of the mixing. The equalized UTXOs are then sent to the **premix** account. As for the difference that cannot enter the pool, it is separated into a specific account: the **bad bank** (or "doxxic change").

This initial transaction `Tx0` also serves to settle the service fees due to the mix coordinator. Unlike the following stages, this transaction is not collaborative; the user must therefore assume the full mining fees:
![coinjoin](assets/en/7.webp)
In this example of a transaction `Tx0`, an input of `372,000 sats` from our **deposit** account is divided into several outgoing UTXOs, which are distributed as follows:
- An amount of `5,000 sats` intended for the coordinator for service fees, corresponding to the entry into the pool of `100,000 sats`;
- Three UTXOs prepared for mixing, redirected to our **premix** account and registered with the coordinator. These UTXOs are equalized at `108,000 sats` each, in order to cover the mining fees for their future initial mix;
- The surplus, which cannot enter the pool because it is too small, is considered toxic change. It is sent to its specific account. Here, this change amounts to `40,000 sats`;
- Finally, there are `3,000 sats` that do not constitute an output, but are the mining fees necessary to confirm the `Tx0`.

For example, here is a real Tx0 Whirlpool (which does not come from me): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Step 2: The Toxic Change**
The surplus, not having been able to integrate into the pool, here equivalent to `40,000 sats`, is redirected to the **bad bank** account, also referred to as "toxic change", to ensure a strict separation from the other UTXOs in the wallet.

This UTXO is dangerous for the user's privacy because not only is it always attached to its past, and therefore possibly to the identity of its owner, but in addition, it is noted as belonging to a user who has performed a coinjoin.

If this UTXO is merged with mixed outputs, the latter will lose all the privacy gained during the coinjoin cycles, notably because of the CIOH (*Common-Input-Ownership-Heuristic*). If it is merged with other toxic changes, the user risks losing privacy since this will link the different entries of the coinjoin cycles. It must therefore be treated with caution. The way to manage this toxic UTXO will be detailed in the last part of this article, and future tutorials will delve deeper into these methods on the PlanB Network.

**Step 3: The Initial Mix**
After the completion of the `Tx0`, the equalized UTXOs are sent to the **premix** account of our wallet, ready to be introduced into their first cycle of coinjoin, also called "initial mix". If, as in our example, the `Tx0` generates multiple UTXOs intended for mixing, each of them will be integrated into a separate initial coinjoin.
At the end of these initial mixes, the **premix** account will be empty, while our coins, having paid the mining fees for this first coinjoin, will be adjusted exactly to the amount defined by the chosen pool. In our example, our initial UTXOs of `108 000 sats` will have been reduced to exactly `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Step 4: The Remixes**
After the initial mix, the UTXOs are transferred to the **postmix** account. This account gathers the already mixed UTXOs and those waiting for remixing. When the Whirlpool client is active, the UTXOs located in the **postmix** account are automatically available for remixing and will be randomly chosen to participate in these new cycles.

As a reminder, remixes are then 100% free: no additional service fees or mining fees are required. Keeping the UTXOs in the **postmix** account thus maintains their value intact, and at the same time improves their anonsets. That's why it's important to allow these coins to participate in multiple coinjoin cycles. It costs you strictly nothing, and it increases their levels of anonymity.

When you decide to spend mixed UTXOs, you can do so directly from this **postmix** account. It is advisable to keep the mixed UTXOs in this account to benefit from free remixes and to prevent them from leaving the Whirlpool circuit, which could decrease their privacy.

As we will see in the following tutorial, there is also the `mix to` option which offers the possibility to automatically send your mixed coins to another wallet, such as a cold wallet, after a defined number of coinjoins.

After discussing the theory, let's dive into practice with a tutorial on using Whirlpool via the Sparrow Wallet desktop software!

## Tutorial: Coinjoin Whirlpool on Sparrow Wallet
There are numerous options for using Whirlpool. The first one I want to introduce to you is the Sparrow Wallet option, an open-source Bitcoin wallet management software for PC.
Using Sparrow has the advantage of being quite easy to get started with, quick to set up, and requiring no equipment other than a computer and an internet connection. However, there is a notable disadvantage: coinjoins will only occur when Sparrow is launched and connected. This means that if you want to mix and remix your bitcoins 24/7, you will need to constantly keep your computer turned on.

### Install Sparrow Wallet
To begin, you will obviously need the Sparrow Wallet software. You can directly download it from [the official website](https://sparrowwallet.com/download/) or on [their GitHub](https://github.com/sparrowwallet/sparrow/releases).

Before installing the software, it will be important to verify the signature and integrity of the executable you just downloaded. If you want more details on the installation process and verification of Sparrow software, I advise you to read this other tutorial: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*

### Create a Software Wallet
After installing the software, you will need to proceed with creating a Bitcoin wallet. It is important to note that to participate in coinjoins, the use of a software wallet (also called a "hot wallet") is essential. Therefore, **it will not be possible to perform coinjoins with a wallet secured by a hardware wallet**.

Although it is not imperative, in case you plan to mix significant amounts, it is highly recommended to opt for the use of a strong BIP39 passphrase for this wallet.

To create a new wallet, open Sparrow, then click on the `File` tab and `New Wallet`.

![sparrow](assets/notext/9.webp)

Choose a name for this wallet, for example: "Coinjoin Wallet". Click on the `Create Wallet` button.

![sparrow](assets/notext/10.webp)

Leave the default settings, then click on the `New or Imported Software Wallet` button.

![sparrow](assets/notext/11.webp)

When you access the wallet creation window, I recommend choosing a 12-word sequence, as it is amply sufficient. Select `Generate New` to generate a new recovery phrase, and click on `Use Passphrase` if you wish to add a BIP39 passphrase. It is important to make a physical backup of your recovery information, whether on paper or on a metal support, to ensure the security of your bitcoins.

![sparrow](assets/notext/12.webp)
Ensure the validity of your recovery phrase backup before clicking on `Confirm Backup...`. Sparrow will then ask you to enter your phrase again to verify that you have taken note of it. Once this step is completed, continue by clicking on `Create Keystore`.
![sparrow](assets/notext/13.webp)

Leave the suggested derivation path as default and press `Import Keystore`. In my example, the derivation path differs slightly since I am using the Testnet for this tutorial. The derivation path that should appear for you is as follows:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

After that, Sparrow will display the derivation details of your new wallet. In case you have set a passphrase, it is highly recommended to note your `Master fingerprint`. Although this master key fingerprint is not sensitive data, it will be useful for you to later verify that you are indeed accessing the correct wallet and to confirm the absence of errors when entering your passphrase.

Click on the `Apply` button.

![sparrow](assets/notext/15.webp)

Sparrow invites you to create a password for your wallet. This password will be required to access it via the Sparrow Wallet software. Choose a strong password, make a backup of it, and then click on `Set Password`.

![sparrow](assets/notext/16.webp)

### Receiving bitcoins
After creating your wallet, you will initially have a single account, with the index `0'`. This is the **deposit** account we talked about in the previous parts. This is the account to which you will need to send the bitcoins to mix.

To do this, select the `Receive` tab on the left side of the window. Sparrow will automatically generate a new blank address to receive bitcoins.

![sparrow](assets/notext/17.webp)

You can enter a label for this address, and then send the bitcoins to be mixed to it.

![sparrow](assets/notext/18.webp)

### Making the Tx0
Once your transaction is confirmed, you can then go to the `UTXOs` tab.

![sparrow](assets/notext/19.webp)

Next, choose the UTXO(s) you wish to submit to the coinjoin cycles. To select multiple UTXOs simultaneously, hold down the `Ctrl` key while clicking on the UTXOs of your choice.

![sparrow](assets/notext/20.webp)

Then click on the `Mix Selected` button at the bottom of the window. If this button does not appear on your interface, it's because you are on a wallet secured with a hardware wallet. You need to use a software wallet to perform coinjoins with Sparrow.
![sparrow](assets/notext/21.webp)
A window opens to explain how Whirlpool works. This is a simplification of what I explained in the previous parts. Click on `Next` to proceed.

![sparrow](assets/notext/22.webp)

On the next page, you can enter a "SCODE" if you have one. An SCODE is a promotional code that offers a discount on the service fees of the pool. Samourai Wallet occasionally provides such codes to its users during special events. I advise you to [follow Samourai Wallet](https://twitter.com/SamouraiWallet) on social media so you don't miss out on future SCODES.

On the same page, you will also need to set the fee rate for the `Tx0` and your initial mix. This choice will influence the speed of confirmation for your preparatory transaction and your first coinjoin. Remember that you are responsible for the mining fees for the `Tx0` and the initial mix, but you will not owe mining fees for subsequent remixes. Adjust the `Premix Priority` slider according to your preferences, then click on `Next`.

![sparrow](assets/notext/23.webp)

In this new window, you will have the option to select the pool you wish to enter using the dropdown list. In my case, having initially selected a UTXO of `456 214 sats`, my only possible choice is the pool of `100 000 sats`. This interface also informs you about the service fees to be paid as well as the number of UTXOs that will be integrated into the pool. If the conditions seem satisfactory to you, continue by clicking on `Preview Premix`.

![sparrow](assets/notext/24.webp)

After this step, Sparrow will ask you to enter the password for your wallet, the one you established when creating it on the software. Once the password is entered, you will access the preview of your `Tx0`. On the left side of your window, you will see that Sparrow has generated the different accounts necessary for using Whirlpool (`Deposit`, `Premix`, `Postmix`, and `Badbank`). You will also have the opportunity to view the structure of your `Tx0`, with the different outputs:
- The service fees;
- The equalized UTXOs intended to enter the pool;
- The toxic change (Doxxic Change).

![sparrow](assets/notext/25.webp)

If the transaction is to your liking, click on `Broadcast Transaction` to broadcast your `Tx0`. Otherwise, you have the option to adjust the parameters of this `Tx0` by selecting `Clear` to erase the entered data and start the creation process from the beginning.

### Performing Coinjoins
Once the Tx0 is broadcast, you will find your UTXOs ready to be mixed in the `Premix` account.
![sparrow](assets/notext/26.webp)

Once the `Tx0` is confirmed, your UTXOs will be registered with the coordinator, and the initial mixes will start automatically in succession.

![sparrow](assets/notext/27.webp)

By checking the `Postmix` account, you will observe the UTXOs resulting from the initial mixes. These coins will remain ready for subsequent remixing, which will not incur any additional fees.

![sparrow](assets/notext/28.webp)

In the `Mixes` column, it is possible to see the number of coinjoins performed by each of your coins. As we will see in the following sections, what truly matters is not so much the number of remixes per se, but rather the associated anonsets, although these two indicators are partially related.

![sparrow](assets/notext/29.webp)

To temporarily stop the coinjoins, simply click on `Stop Mixing`. You will have the option to resume operations at any time by selecting `Start Mixing`.

![sparrow](assets/notext/30.webp)

To ensure continuous availability of your UTXOs for remixing, it is necessary to keep the Sparrow software active. Closing the software or turning off your computer will pause the coinjoins. A solution to circumvent this problem is to disable sleep functions through your operating system's settings. Additionally, Sparrow offers an option to prevent your computer from automatically going to sleep, which you can find under the `Tools` tab titled `Prevent Computer Sleep`.

![sparrow](assets/notext/31.webp)

### Completing the coinjoins
To spend your mixed bitcoins, you have several options. The most direct method is to access the `Postmix` account and select the `Send` tab.

![sparrow](assets/notext/32.webp)

In this section, you will have the option to enter the destination address, the amount to send, and the transaction fees, in the same way as for any other transaction made with Sparrow Wallet. If you wish, you can also take advantage of advanced privacy features such as Stonewall, by clicking on the `Privacy` button.

![sparrow](assets/notext/33.webp)

[-> Learn more about Stonewall transactions.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

If you wish to make a more precise selection of your coins to spend, go to the `UTXOs` tab. Select the UTXOs you specifically want to consume, then press the `Send Selected` button to initiate the transaction.

![sparrow](assets/notext/34.webp)
Finally, the `Mix to...` option available on Sparrow allows for the automatic removal of a selected UTXO from coinjoin cycles, without incurring additional fees. This feature enables the determination of a number of remixes after which the UTXO will not be reintegrated into your `Postmix` account, but will instead be transferred directly to another wallet. This option is often used to automatically send mixed bitcoins to a cold wallet.
To use this option, start by opening the recipient wallet alongside your coinjoin wallet within the Sparrow software.

![sparrow](assets/notext/35.webp)

Then, go to the `UTXOs` tab, then click on the `Mix to...` button at the bottom of the window.

![sparrow](assets/notext/36.webp)

A window opens, start by selecting the destination wallet from the dropdown list.

![sparrow](assets/notext/37.webp)

Choose the coinjoin threshold beyond which the withdrawal will be made automatically. I cannot give you an exact number of remixes to perform, as this varies according to your personal situation and your privacy goals, but avoid choosing a threshold too low. I recommend consulting this other article to learn more about the remixing process: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

You can leave the `Index range` option on its default value, `Full`. This function allows for mixing simultaneously from different clients, but that's not what we want to do in this tutorial. To finalize and activate the `Mix to...` option, press `Restart Whirlpool`.

![sparrow](assets/notext/38.webp)

However, be cautious when using the `Mix to` option, as removing mixed coins from your `Postmix` account can significantly increase the risk of compromising your privacy. The reasons for this potential are detailed in the following sections.

## How to know the quality of our coinjoin cycles?
For a coinjoin to be truly effective, it is essential that it presents good homogeneity between the amounts of inputs and outputs. This uniformity amplifies the number of possible interpretations in the eyes of an external observer, thereby increasing the uncertainty around the transaction. To quantify this uncertainty generated by a coinjoin, one can resort to calculating the transaction's entropy. For an in-depth exploration of these indicators, I refer you to the tutorial: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). The Whirlpool model is recognized as the one that brings the most homogeneity in coinjoins.
Next, the performance of several coinjoin cycles is evaluated based on the size of the groups in which a coin is concealed. The size of these groups defines what is called the anonsets. There are two types of anonsets: the first assesses the privacy gained against retrospective analysis (from the present to the past) and the second, against prospective analysis (from the past to the present). For a detailed explanation of these two indicators, I invite you to consult the tutorial: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## How to manage postmix?
After performing coinjoin cycles, the best strategy is to keep your UTXOs in the **postmix** account, waiting for their future use. It is even advisable to let them remix indefinitely until you need to spend them.

Some users might consider transferring their mixed bitcoins to a wallet secured by a hardware wallet. This is possible, but it is important to follow the recommendations of Samourai Wallet meticulously so as not to compromise the acquired confidentiality.

Merging UTXOs is the most frequently made mistake. It is necessary to avoid combining mixed UTXOs with unmixed UTXOs in the same transaction, in order to avoid the CIOH (*Common-Input-Ownership-Heuristic*). This requires careful management of your UTXOs within your wallet, especially in terms of labeling. Beyond coinjoin, merging UTXOs is generally a bad practice that often leads to a loss of privacy when not managed properly.

It is also important to be cautious about consolidating mixed UTXOs with each other. Moderate consolidations are conceivable if your mixed UTXOs have significant anonsets, but this will inevitably decrease the confidentiality of your coins. Ensure that consolidations are neither too large nor carried out after an insufficient number of remixes, as this risks establishing deducible links between your UTXOs before and after the coinjoin cycles. In case of doubt about these manipulations, the best practice is not to consolidate the postmix UTXOs, and to transfer them one by one to your hardware wallet, generating a new blank address each time. Again, remember to properly label each received UTXO.
It is also advised against transferring your postmix UTXOs to a wallet using uncommon scripts. For example, if you enter Whirlpool from a multisig wallet using `P2WSH` scripts, there's little chance you'll be mixed with other users who have the same type of wallet originally. If you withdraw your postmix to this same multisig wallet, the privacy level of your mixed bitcoins will be greatly diminished. Beyond scripts, there are many other wallet fingerprints that can trick you.
As with any Bitcoin transaction, it's also important not to reuse receiving addresses. Each new transaction should be received on a new, blank address.

The simplest and safest solution is to let your mixed UTXOs rest in their **postmix** account, letting them remix and only touching them to spend. Samourai and Sparrow wallets have additional protections against all these chain analysis-related risks. These protections help you avoid making mistakes.

## How to manage doxxic change?
Next, you need to be careful in managing doxxic change, the change that couldn't enter the coinjoin pool. These toxic UTXOs, resulting from the use of Whirlpool, pose a risk to your privacy since they establish a link between you and the use of coinjoin. Therefore, it's imperative to handle them with care and not to combine them with other UTXOs, especially mixed UTXOs. Here are different strategies to consider for using them:
- **Mix them in smaller pools:** If your toxic UTXO is significant enough to enter a smaller pool alone, consider mixing it. This is often the best option. However, it's crucial not to merge several toxic UTXOs to access a pool, as this could link your different entries;
- **Mark them as "non-spendable":** Another approach is to no longer use them, to mark them as "non-spendable" in their dedicated account, and to just Hodl. This ensures you don't accidentally spend them. If the value of bitcoin increases, new pools more suited to your toxic UTXOs might emerge;
- **Make donations:** Consider making donations, even modest ones, to developers working on Bitcoin and its associated software. You can also donate to organizations accepting BTC. If managing your toxic UTXOs seems too complicated, you can simply get rid of them by making a donation;
- **Buy Gift Cards:** Platforms such as [Bitrefill](https://www.bitrefill.com/) allow you to exchange bitcoins for gift cards that can be used at various merchants. This can be a way to dispose of your toxic UTXOs without losing the associated value.
- **Consolidate them on Monero:** Samourai Wallet now offers an atomic swap service between BTC and XMR. This is ideal for managing toxic UTXOs by consolidating them on Monero, without compromising your privacy via the CIOH, before sending them back to Bitcoin. However, this option can be costly in terms of mining fees and the premium due to liquidity constraints.
- **Send them to the Lightning Network:** Transferring these UTXOs to the Lightning Network to benefit from reduced transaction fees is an option that might be interesting. However, this method may reveal certain information depending on your use of Lightning and should therefore be practiced with caution.

Detailed tutorials on implementing these different techniques will be offered soon on PlanB Network.

**Additional Resources:**
[Sparrow Wallet Video Tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)
[Samourai Wallet Video Tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Samourai Wallet Documentation - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter Thread on CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog Post on CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).
