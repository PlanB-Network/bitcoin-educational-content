---
name: Coinjoin - Dojo
description: How to perform a coinjoin with your own Dojo?
---
![cover](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, the Whirlpool tool no longer functions, even for individuals who have their own Dojo or are using Sparrow Wallet. However, it remains possible that this tool could be reinstated in the coming weeks or relaunched in a different manner. Moreover, the theoretical part of this article remains relevant for understanding the principles and objectives of coinjoins in general (not just Whirlpool), as well as understanding the effectiveness of the Whirlpool model.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

In this tutorial, you will learn what a coinjoin is and how to perform one using the Samourai Wallet software and the Whirlpool implementation, utilizing your own Dojo. In my opinion, this method is currently the best for mixing your bitcoins.

## What is a coinjoin on Bitcoin?
**A coinjoin is a technique that breaks the traceability of bitcoins on the blockchain**. It relies on a collaborative transaction with a specific structure of the same name: the coinjoin transaction.

Coinjoins enhance the privacy of Bitcoin users by complicating chain analysis for external observers. Their structure allows merging multiple coins from different users into a single transaction, thus blurring the trails and making it difficult to determine the links between input and output addresses.

The principle of the coinjoin is based on a collaborative approach: several users who wish to mix their bitcoins deposit identical amounts as inputs of the same transaction. These amounts are then redistributed as outputs of equal value to each user. At the end of the transaction, it becomes impossible to associate a specific output with a known user at the input. No direct link exists between the inputs and outputs, which breaks the association between the users and their UTXO, as well as the history of each coin.
![coinjoin](assets/notext/1.webp)

Example of a coinjoin transaction (not from me): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

To perform a coinjoin while ensuring that each user maintains control over their funds at all times, the process begins with the transaction being constructed by a coordinator, who then transmits it to the participants. Each user then signs the transaction after verifying that it suits them. All collected signatures are finally integrated into the transaction. If an attempt to divert funds is made by a user or the coordinator, through a modification of the coinjoin transaction's outputs, the signatures will prove invalid, leading to the rejection of the transaction by the nodes.

There are several implementations of coinjoin, such as Whirlpool, JoinMarket, or Wabisabi, each aiming to manage coordination among participants and increase the efficiency of coinjoin transactions.
In this tutorial, we will delve into the implementation of **Whirlpool**, which I consider to be the most efficient solution for performing coinjoins on Bitcoin. Although available on several wallets, in this tutorial, we will exclusively explore its use with the Samourai Wallet mobile application, without Dojo.

## Why perform coinjoins on Bitcoin?
One of the initial problems with any peer-to-peer payment system is double spending: how to prevent malicious individuals from spending the same monetary units multiple times without resorting to a central authority to arbitrate?

Satoshi Nakamoto provided a solution to this dilemma through the Bitcoin protocol, a peer-to-peer electronic payment system that operates independently of any central authority. In his white paper, he emphasizes that the only way to certify the absence of double spending is to ensure the visibility of all transactions within the payment system.

To ensure that each participant is aware of the transactions, they must be publicly disclosed. Therefore, the operation of Bitcoin relies on a transparent and distributed infrastructure, allowing any node operator to verify the entirety of the electronic signature chains and the history of each coin, from its creation by a miner.

The transparent and distributed nature of Bitcoin's blockchain means that any user of the network can follow and analyze the transactions of all other participants. As a result, anonymity at the transaction level is impossible. However, anonymity is preserved at the level of individual identification. Unlike the traditional banking system where each account is linked to a personal identity, on Bitcoin, funds are associated with pairs of cryptographic keys, thus offering users a form of pseudonymity behind cryptographic identifiers.

Thus, confidentiality on Bitcoin is compromised when external observers manage to associate specific UTXOs with identified users. Once this association is established, it becomes possible to trace their transactions and analyze the history of their bitcoins. Coinjoin is precisely a technique developed to break the traceability of UTXOs, thereby offering a certain layer of confidentiality to Bitcoin users at the transaction level.

## How does Whirlpool work?
Whirlpool stands out from other coinjoin methods by using "_ZeroLink_" transactions, which ensure that there is strictly no technical link possible between all the inputs and all the outputs. This perfect mixing is achieved through a structure where each participant contributes an identical amount in input (except for mining fees), thus generating outputs of perfectly equal amounts.
This restrictive approach to inputs gives Whirlpool coinjoin transactions a unique feature: the complete absence of deterministic links between the inputs and outputs. In other words, each output has an equal probability of being attributed to any participant, compared to all the other outputs in the transaction.
Initially, the number of participants in each Whirlpool coinjoin was limited to 5, with 2 new entrants and 3 remixers (we will explain these concepts further on). However, the increase in on-chain transaction fees observed in 2023 prompted the Samourai teams to rethink their model to improve privacy while reducing costs. Thus, taking into account the market situation of fees and the number of participants, the coordinator can now organize coinjoins including 6, 7, or 8 participants. These enhanced sessions are referred to as "_Surge Cycles_". It is important to note that, regardless of the setup, there are always only 2 new entrants in the Whirlpool coinjoins.

Thus, Whirlpool transactions are characterized by an identical number of inputs and outputs, which can be:
- 5 inputs and 5 outputs;
![coinjoin](assets/notext/2.webp)
- 6 inputs and 6 outputs;
![coinjoin](assets/notext/3.webp)
- 7 inputs and 7 outputs;
![coinjoin](assets/notext/4.webp)
- 8 inputs and 8 outputs.
![coinjoin](assets/notext/5.webp)
The model proposed by Whirlpool is thus based on small coinjoin transactions. Unlike Wasabi and JoinMarket, where the robustness of anonsets relies on the volume of participants in a single cycle, Whirlpool bets on the chaining of multiple small-sized cycles.

In this model, the user pays fees only upon their initial entry into a pool, allowing them to participate in a multitude of remixes without additional fees. It is the new entrants who cover the mining fees for the remixers.

With each additional coinjoin that a coin participates in, along with its past encountered peers, the anonsets will grow exponentially. The goal is thus to take advantage of these free remixes which, with each occurrence, contribute to enhancing the density of the anonsets associated with each mixed coin.

Whirlpool was designed taking into account two important requirements:
- The accessibility of implementation on mobile devices, given that Samourai Wallet is primarily a smartphone application;
- The speed of remixing cycles to promote a significant increase in anonsets.
These imperatives guided the choices of the developers of Samourai Wallet in the design of Whirlpool, leading them to limit the number of participants per cycle. Too few participants would have compromised the efficiency of the coinjoin, drastically reducing the anonsets generated each cycle, while too many participants would have posed management problems on mobile applications and would have hindered the flow of cycles.
**Ultimately, there is no need to have a high number of participants per coinjoin on Whirlpool since the anonsets are achieved through the accumulation of several coinjoin cycles.**

[-> Learn more about Whirlpool anonsets.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### The pools and coinjoin fees
For these multiple cycles to effectively increase the anonsets of the mixed coins, a certain framework must be established to restrict the amounts of UTXO used. Whirlpool thus defines different pools.

A pool represents a group of users wishing to mix together, who agree on the amount of UTXO to use to optimize the coinjoin process. Each pool specifies a fixed amount for the UTXO, which the user must adhere to in order to participate. Thus, to perform coinjoins with Whirlpool, you need to select a pool. The pools currently available are as follows:
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

As mentioned previously, a UTXO is considered to belong to a pool when it is ready to be integrated into a coinjoin. However, this does not mean that the user loses possession of it. **Through the different mixing cycles, you retain full control of your keys and, consequently, your bitcoins.** This is what differentiates the coinjoin technique from other centralized mixing techniques.

To enter a coinjoin pool, service fees as well as mining fees must be paid. The service fees are fixed for each pool and are intended to compensate the teams responsible for the development and maintenance of Whirlpool.
Service fees for using Whirlpool are to be paid only once upon entering the pool. After this step, you have the opportunity to participate in an unlimited number of remixes without any additional fees. Here are the current fixed fees for each pool:

| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


These fees essentially function as an entry ticket for the chosen pool, regardless of the amount you put in coinjoin. Thus, whether you join the 0.01 pool with exactly 0.01 BTC or enter it with 0.5 BTC, the fees will remain the same in absolute value.

Before proceeding to coinjoins, the user therefore has a choice between 2 strategies:
- Opt for a smaller pool to minimize service fees, knowing that they will receive several small UTXOs in return;
- Or prefer a larger pool, agreeing to pay higher fees to end up with a reduced number of larger-value UTXOs.

It is generally advised against merging several mixed UTXOs after the coinjoin cycles, as this could compromise the acquired confidentiality, especially due to the Common-Input-Ownership Heuristic (CIOH). Therefore, it may be wise to choose a larger pool, even if it means paying more, to avoid having too many small-value UTXOs at the output. The user must weigh these trade-offs to choose the pool they prefer.

In addition to service fees, the mining fees inherent to any Bitcoin transaction must also be considered. As a Whirlpool user, you will be required to pay the mining fees for the preparation transaction (`Tx0`) as well as those for the first coinjoin. All subsequent remixes will be free, thanks to Whirlpool's model which relies on the payment of new entrants.

Indeed, in each Whirlpool coinjoin, two users among the inputs are new entrants. The other inputs come from remixers. As a result, the mining fees for all participants in the transaction are covered by these two new participants, who will then also benefit from free remixes:
![coinjoin](assets/en/6.webp)
Thanks to this fee system, Whirlpool truly differentiates itself from other coinjoin services since the anonsets of the UTXOs are not proportional to the price paid by the user. Thus, it is possible to achieve considerably high levels of anonymity by only paying the entry fee of the pool and the mining fees for two transactions (the `Tx0` and the initial mix).
It is important to note that the user will also have to cover the mining fees to withdraw their UTXOs from the pool after completing their multiple coinjoins, unless they have selected the `mix to` option, which we will discuss in the tutorial below.

### The HD wallet accounts used by Whirlpool
To perform a coinjoin via Whirlpool, the wallet must generate several distinct accounts. An account, in the context of an HD (*Hierarchical Deterministic*) wallet, constitutes a section completely isolated from the others, this separation occurring at the third depth level of the wallet's hierarchy, that is, at the level of the `xpub`.

An HD wallet can theoretically derive up to `2^(32/2)` different accounts. The initial account, used by default on all Bitcoin wallets, corresponds to the index `0'`.

For wallets adapted to Whirlpool, such as Samourai or Sparrow, 4 accounts are used to meet the needs of the coinjoin process:
- The **deposit** account, identified by the index `0'`;
- The **bad bank** (or doxxic change) account, identified by the index `2 147 483 644'`;
- The **premix** account, identified by the index `2 147 483 645'`;
- The **postmix** account, identified by the index `2 147 483 646'`.

Each of these accounts fulfills a specific function within the coinjoin.

All these accounts are linked to a single seed, which allows the user to recover access to all their bitcoins using their recovery phrase and, if necessary, their passphrase. However, it is necessary to specify to the software, during this recovery operation, the different account indexes that were used.

Let's now look at the different stages of a Whirlpool coinjoin within these accounts.

### The different stages of coinjoins on Whirlpool
**Stage 1: The Tx0**
The starting point of any Whirlpool coinjoin is the **deposit** account. This account is the one you automatically use when you create a new Bitcoin wallet. This account must be credited with the bitcoins that one wishes to mix.
The `Tx0` represents the first step in the Whirlpool mixing process. It aims to prepare and equalize the UTXO for the coinjoin, by dividing them into units corresponding to the amount of the selected pool, to ensure the homogeneity of the mixing. The equalized UTXO are then sent to the **premix** account. As for the difference that cannot enter the pool, it is separated into a specific account: the **bad bank** (or "doxxic change").
This initial transaction `Tx0` also serves to settle the service fees due to the mix coordinator. Unlike the following steps, this transaction is not collaborative; the user must therefore bear all the mining fees:
![coinjoin](assets/en/7.webp)

In this example of a `Tx0` transaction, an input of `372,000 sats` from our **deposit** account is divided into several output UTXO, which are distributed as follows:
- An amount of `5,000 sats` intended for the coordinator for service fees, corresponding to the entry into the pool of `100,000 sats`;
- Three UTXO prepared for mixing, redirected to our **premix** account and registered with the coordinator. These UTXO are equalized at `108,000 sats` each, to cover the mining fees for their future initial mix;
- The surplus that cannot enter the pool, being too small, is considered toxic change. It is sent to its specific account. Here, this change amounts to `40,000 sats`;
- Finally, there are `3,000 sats` that do not constitute an output, but are the mining fees necessary to confirm the `Tx0`.

For example, here is a real Whirlpool Tx0 (not from me): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Step 2: The doxxic change**
The surplus that could not be integrated into the pool, here equivalent to `40,000 sats`, is redirected to the **bad bank** account, also referred to as "doxxic change", to ensure a strict separation from the other UTXO in the wallet.

This UTXO is dangerous for the user's privacy because not only is it still attached to its past, and therefore possibly to the identity of its owner, but additionally, it is noted as belonging to a user who has performed a coinjoin.
If this UTXO is merged with mixed outputs, they will lose all the confidentiality gained during the coinjoin cycles, notably because of the Common-Input-Ownership-Heuristic (CIOH). If it is merged with other doxxic changes, the user risks losing confidentiality since this will link the different inputs of the coinjoin cycles. Therefore, it must be handled with caution. The way to manage this toxic UTXO will be detailed in the last part of this article, and future tutorials will cover these methods more thoroughly on PlanB Network.

**Step 3: The Initial Mix**
After the `Tx0` is completed, the equalized UTXOs are sent to the **premix** account of our wallet, ready to be introduced into their first coinjoin cycle, also called the "initial mix". If, as in our example, the `Tx0` generates several UTXOs intended for mixing, each of them will be integrated into a separate initial coinjoin.

At the end of these first mixes, the **premix** account will be empty, while our coins, having paid the mining fees for this first coinjoin, will be adjusted exactly to the amount defined by the chosen pool. In our example, our initial UTXOs of `108 000 sats` will have been reduced to exactly `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Step 4: The Remixes**
After the initial mix, the UTXOs are transferred to the **postmix** account. This account gathers the already mixed UTXOs and those waiting for remixing. When the Whirlpool client is active, the UTXOs located in the **postmix** account are automatically available for remixing and will be randomly chosen to participate in these new cycles.

As a reminder, the remixes are then 100% free: no additional service fees or mining fees are required. Keeping the UTXOs in the **postmix** account thus maintains their value intact and simultaneously improves their anonsets. That's why it's important to allow these coins to participate in multiple coinjoin cycles. It costs you strictly nothing, and it increases their levels of anonymity.

When you decide to spend mixed UTXOs, you can do so directly from this **postmix** account. It is advisable to keep the mixed UTXOs in this account to benefit from free remixes and to avoid them leaving the Whirlpool circuit, which could decrease their confidentiality.

As we will see in the following tutorial, there is also the `mix to` option which offers the possibility to automatically send your mixed coins to another wallet, such as a cold wallet, after a defined number of coinjoins.
After covering the theory, let's dive into practice with a tutorial on using Whirlpool through the Samourai Wallet Android application, synchronized with Whirlpool CLI and GUI on your own Dojo!
## Tutorial: Coinjoin Whirlpool with Your Own Dojo
There are many options for using Whirlpool. The one I want to introduce here is the Samourai Wallet option, an open-source Bitcoin wallet management application on Android, but this time **with your own Dojo**.

Performing coinjoins via Samourai Wallet using your own Dojo is, in my opinion, the most effective strategy for conducting coinjoins on Bitcoin to date. This approach requires some initial investment in terms of setup, but once in place, it offers the possibility to mix and remix your bitcoins continuously, 24 hours a day, 7 days a week, without the need to keep your Samourai application active at all times. Indeed, thanks to Whirlpool CLI operating on a Bitcoin node, you are always ready to participate in coinjoins. The Samourai application then gives you the opportunity to spend your mixed funds at any time, wherever you are, directly from your smartphone. Moreover, this method has the advantage of never connecting you to servers managed by the Samourai teams, thus preserving your `xpub` from any external exposure.

This technique is therefore ideal for those seeking maximum privacy and the highest quality coinjoin cycles. However, it requires having a Bitcoin node at your disposal and, as we will see later, requires some setup. It is thus more suited to intermediate to advanced users. For beginners, I recommend getting acquainted with coinjoin through these two other tutorials, which show how to do it from Sparrow Wallet or Samourai Wallet (without Dojo):
- **[Sparrow Wallet coinjoin tutorial](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Samourai Wallet coinjoin tutorial (without Dojo)](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**.

### Understanding the Setup
To start, you're going to need a Dojo! Dojo is a Bitcoin node implementation based on Bitcoin Core, developed by the Samourai teams.

To run your own Dojo, you have the option of either installing a Dojo node autonomously, or taking advantage of Dojo on top of another "node-in-box" Bitcoin node solution. Currently, the available options are:
- [RoninDojo](https://ronindojo.io/), which is a Dojo enhanced with additional tools, including an installation assistant and an administration assistant. I detail the procedure for setting up and using RoninDojo in this other tutorial: [RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2);
- [Umbrel](https://umbrel.com/) with the "Samourai Server" application;
- [MyNode](https://mynodebtc.com/) with the "Dojo" application;
- [Nodl](https://www.nodl.eu/) with the "Dojo" application;
- [Citadel](https://runcitadel.space/) with the "Samourai" application.
![coinjoin](assets/notext/9.webp)
In our setup, we will interact with three distinct interfaces:
- **Samourai Wallet**, which will host our Bitcoin wallet dedicated to coinjoins. Available for free on Android, this FOSS application allows you to control your mixing wallet, especially for spending your postmix from your smartphone;
- **Whirlpool CLI** (_Command Line Interface_), which will operate on the node hosting the Dojo. This software will have access to the keys of your Samourai wallet. It is responsible for communicating with the coordinator and managing the coinjoins continuously. It acts as a copy of your Samourai wallet on your node, ready to participate in coinjoins at any time;
- **Whirlpool GUI** (_Graphical User Interface_), the graphical user interface we will use to monitor the activity of Whirlpool CLI and initiate mixing remotely. Whirlpool GUI provides a visual representation of the operations conducted by Whirlpool CLI. This software must be installed on a computer separate from the Dojo. For users of Umbrel, MyNode, Nodl, and Citadel, Whirlpool GUI is mandatory. However, with RoninDojo, the Whirlpool GUI interface is already integrated into your node's web interface via the `Whirlpool` application. Therefore, you will not need to install it on a separate PC.

In my opinion, using RoninDojo represents the best solution for performing coinjoins with a Dojo. Since this node-in-box software is in direct partnership with the Samourai teams, RoninDojo is much more optimized for doing this. Moreover, the integration of Whirlpool GUI into the web interface significantly simplifies the setup process. In this tutorial, I will still explain how to do it with the other solutions that integrate Dojo (Umbrel, Nodl, MyNode, and Citadel).

### Preparing Your Dojo
To begin, you will need to install Dojo and obtain the QR code or the link that will allow you to connect to it remotely. This link is a Tor address ending in `.onion`. If you are using RoninDojo, simply navigate to the `Pairing` menu to access this information.
![coinjoin](assets/notext/10.webp)

Below `Samourai Dojo`, click on the `Pair now` button.

![coinjoin](assets/notext/11.webp)

Your connection QR code and the corresponding link will be displayed.

![coinjoin](assets/notext/12.webp)

If you are on Umbrel, go to the App Store and search for the `Samourai Server` application. It is located in the `Bitcoin` tab.

![coinjoin](assets/notext/13.webp)

Install the application.

![coinjoin](assets/notext/14.webp)

Upon opening the application, you will then have access to the QR code for connecting to your Dojo.

![coinjoin](assets/notext/15.webp)

If you are using another node-in-box software such as MyNode, Citadel, or Nodl, the process is similar to that of Umbrel. You need to install the Samourai or Dojo application to obtain the necessary information to connect to your Dojo.

![coinjoin](assets/notext/16.webp)

### Preparing your Samourai Wallet
After retrieving the connection information to your Dojo, it is now time to set up your wallet for coinjoins. There are two scenarios: if you do not yet have a Samourai Wallet on your smartphone, the process is simple, just create a new one.

On the other hand, if you already have a Samourai Wallet, you will need to reinstall the application to associate it with a new Dojo. This step is necessary because the connection to a Dojo can only be established at the first launch of the application. However, thanks to the automatically generated encrypted backup file by Samourai on your phone, this procedure is simple and quick.

*If you have never used Samourai, you can skip these preliminary steps and proceed directly to the installation of the application.*

First and foremost, make sure your Samourai Wallet application is up to date. To do this, check the Google Play Store or compare the version of your application in `Settings > Other` with the one available on the Samourai website.

![coinjoin](assets/notext/17.webp)

Ensure you have your Samourai wallet recovery phrase and that it is legible. Then, conduct a test of your BIP39 passphrase by navigating to `Settings > Troubleshoot > Passphrase/Backup test` to confirm its accuracy.

![coinjoin](assets/notext/18.webp)
Enter your passphrase, then verify that Samourai confirms its validity.
![coinjoin](assets/notext/19.webp)

If your passphrase is invalid, or if you do not have your recovery phrase, it is imperative to immediately stop the procedure! **You risk losing your bitcoins during this operation.** In this case, it is advised to transfer your funds to another wallet and start with a new blank Samourai wallet. The following steps should only be followed if you are certain you have all the necessary backup information and that your passphrase is valid.

Then proceed with creating an encrypted backup of your wallet and copy it to your clipboard. To perform this operation, click on the three small dots located at the top right of the screen, then select `Export wallet backup`.

![coinjoin](assets/notext/20.webp)

**From this step on, do not copy anything else to your clipboard!** It is absolutely essential that you keep your copied backup.

If you have correctly executed the previous steps, you are now able to safely delete your Samourai wallet. To do this, go to: `Settings > Wallet > Secure erase the wallet`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*If you have never used Samourai and are installing the application from scratch, you can resume the tutorial at this step.*

Your Samourai application is now reset. Open the application and proceed with the setup steps as if you were using it for the first time.

![coinjoin](assets/notext/23.webp)

In the next step, you will access the page dedicated to configuring your Dojo. Select the `Dojo` option, then enter your Dojo's login information. To do this, you have the option to scan the information by pressing `Scan QR`.

![coinjoin](assets/notext/24.webp)

*For new users of Samourai, it will then be necessary to create a wallet from scratch. If you need assistance, you can consult the instructions for setting up a new Samourai wallet [in this tutorial, specifically in the section "Creating a software wallet"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*

If you are proceeding with the restoration of an already existing Samourai wallet, select `Restore existing wallet`, then choose `I have a Samourai backup file`.

![coinjoin](assets/notext/25.webp)
Normally, you should always have your recovery file in your clipboard. Then click on `PASTE` to insert your file into the designated location. In order to decrypt it, it will also be necessary to enter the BIP39 passphrase of your wallet in the corresponding field, located just below. To finish, click on `FINISH`.
![coinjoin](assets/notext/26.webp)

You will then be redirected to your Samourai Wallet which, this time, will be connected to your own Dojo.

![coinjoin](assets/notext/27.webp)

### Installing Whirlpool GUI
It is now time to install Whirlpool GUI, the graphical user interface that will allow you to manage your coinjoin cycles from your usual PC. For RoninDojo users, this step is not necessary since the management of coinjoins can be done directly via the web interface in `Apps > Whirlpool`. However, if you are using another Bitcoin "node-in-box" solution, it is imperative to proceed with this installation.
![coinjoin](assets/notext/28.webp)
Go to your personal computer and download the Whirlpool software from the official Samourai Wallet website, selecting the version that corresponds to your operating system.

![coinjoin](assets/notext/29.webp)

Before launching Whirlpool GUI, it is necessary to install JAVA 8 or a higher version on your machine. For this, [you can install OpenJDK](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
It is also necessary to have Tor Daemon or Tor Browser operational in the background on your computer. Make sure to start Tor before each Whirlpool GUI usage session. If Tor is not yet installed on your machine, [you can download and install it from the official project website](https://www.torproject.org/download/), then make sure to launch it in the background.

![coinjoin](assets/notext/31.webp)

Once JDK is installed on your system and Tor is launched in the background, you can start Whirlpool GUI.

![coinjoin](assets/notext/32.webp)

From Whirlpool GUI, click on `Advanced: Remote CLI` to connect your Whirlpool CLI which is on your Dojo. You will need the Tor address of your Whirlpool CLI.

![coinjoin](assets/notext/33.webp)

To locate your Tor address on Umbrel and other "node-in-box" solutions, simply start the Samourai Server or Dojo application (the name may vary depending on the software used). The Tor address will be directly visible on the application's page.
![coinjoin](assets/notext/34.webp)
In Whirlpool GUI, enter the Tor address you obtained earlier in the `CLI address` field. Keep the `http://` prefix, but do not add the `:8899` port at the end. Paste only the address as it was provided to you.
![coinjoin](assets/notext/35.webp)

In the Tor Proxy field, enter `socks5://127.0.0.1:9050` if you are using Tor Daemon, or `socks5://127.0.0.1:9150` if it's Tor Browser. When you first connect to Whirlpool CLI via Whirlpool GUI, it is possible to leave the API key field empty. If this is not your first connection, please enter your API key in the dedicated space. This key can be located on the same page as your Tor address.

![coinjoin](assets/notext/36.webp)

Once you have filled in everything, click on the `Connect` button. Please wait, the connection may take a few minutes.

![coinjoin](assets/notext/37.webp)

### Pairing your Samourai Wallet with Whirlpool GUI
*For RoninDojo users, you can resume the tutorial here.*

We will now pair the Samourai wallet we configured earlier with the Whirlpool GUI software, or directly with RoninDojo for those using this software. Whether you are using Whirlpool GUI or RoninDojo, you will be asked to paste or scan the pairing information of your Samourai wallet.

![coinjoin](assets/notext/38.webp)

To find this information, go to your wallet's settings.

![coinjoin](assets/notext/39.webp)

Click on `Transactions`, then on `Pair to Whirlpool GUI`.

![coinjoin](assets/notext/40.webp)

Samourai will then provide you with the necessary information to establish the connection. Be careful, this data is sensitive! You can transfer it to your PC either by copying it directly or by scanning the QR code displayed, using your computer's webcam after clicking on the QR code symbol.

![coinjoin](assets/notext/41.webp)

After performing this operation, in Whirlpool GUI, select `Initialize GUI`. Please wait, as this step may take a moment.

![coinjoin](assets/notext/42.webp)

Whether you are using Whirlpool GUI or RoninDojo, you will be asked to enter the passphrase of your Samourai wallet. Insert it in the dedicated field, then press the `Login` button to continue.

![coinjoin](assets/notext/43.webp)

You will then arrive at the homepage of Whirlpool CLI

![coinjoin](assets/notext/44.webp)

### Initiating coinjoins from Whirlpool GUI
*For RoninDojo users, the process to follow is identical. The Whirlpool app interface integrated into RoninDojo offers the same options and functionalities as the Whirlpool GUI software on desktop. Therefore, you can follow these instructions in the same way.*
Now that everything is set up, you are ready to start mixing your bitcoins. To do this, transfer the bitcoins you wish to mix to the **Deposit** account of your Samourai Wallet. This operation can be carried out either directly via the Samourai Wallet app or on Whirlpool GUI. From the main page, click on the `+ Deposit` button located at the top left.

![coinjoin](assets/notext/45.webp)

Whirlpool GUI will generate a receiving address. It will also display the minimum amount needed to participate in each coinjoin pool. This amount varies depending on the fee market. It is advisable to deposit an amount slightly higher than the minimum required, as if the mining fees do not decrease, your UTXO might not be accepted in the desired pool. Therefore, send your bitcoins to the provided address. To get a new address, simply click on the `Renew address` button.

![coinjoin](assets/notext/46.webp)

Once the deposit is confirmed, you will be able to see it appear in the **Deposit** account on Whirlpool GUI.

![coinjoin](assets/notext/47.webp)

To start the coinjoin cycles, select the UTXOs you wish to mix and press the `Premix` button. Be careful: if you select several different UTXOs at the same time, they will be combined during the `TX0` preparation transaction. This merging can lead to a decrease in privacy, especially if the UTXOs come from different sources, because of the Common Input Ownership Heuristic (CIOH).

![coinjoin](assets/notext/48.webp)

The Whirlpool configuration page opens. You can choose the pool you wish to enter. Also select the mining fees dedicated to the `TX0` and the first coinjoins. At the bottom of this page, a summary will present you with the amount of doxxic change as well as the amount and number of UTXOs that will be equalized and included in the coinjoin cycles. If you are satisfied with this configuration, press the `Premix` button to start the coinjoin cycles.
![coinjoin](assets/notext/49.webp)

Once the `TX0` is created, you will be able to see your equalized UTXOs in the **Premix** account, waiting for confirmation. To allow your coins to remix automatically 24 hours a day, 7 days a week, I recommend activating the `Automatically mix premix & postmix` option. You will find this feature in the `Configuration` tab, located to the left of your Whirlpool GUI window.
![coinjoin](assets/notext/50.webp)
After starting the coinjoins, you can exit Whirlpool GUI as well as Samourai Wallet. Only your node needs to remain connected to be able to participate in continuous coinjoins. However, it is advisable to periodically check the progress of your coinjoin cycles. If you notice that your UTXOs are no longer being selected for a coinjoin for some time, this may indicate a bug. In this case, go to Whirlpool CLI and select `Start` to restart your availability for coinjoins.

![coinjoin](assets/notext/51.webp)

Your mixed UTXOs are visible from the **Postmix** account on Whirlpool GUI. Additionally, you have the option to view and spend them directly via the Whirlpool interface on your Samourai Wallet. To access this menu, click on the blue `+` at the bottom of your screen, then select `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Whirlpool accounts are easily identifiable on Samourai Wallet by their blue color. This allows you to spend your mixed UTXOs from anywhere and at any time, directly from your smartphone.

![coinjoin](assets/notext/53.webp)

To keep track of your automatic coinjoins, I also recommend setting up a watch-only wallet via the Sentinel app. Add the ZPUB of your **Postmix** account and monitor the progress of your coinjoin cycles in real-time. If you want to understand how to use Sentinel, I recommend consulting this other tutorial on PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)