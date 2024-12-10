---
name: Coinjoin - Samourai Wallet
description: How to perform a coinjoin on Samourai Wallet?
---
![cover](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, the Whirlpool tool no longer functions, even for individuals who have their own Dojo or are using Sparrow Wallet. However, it remains possible that this tool could be reinstated in the coming weeks or relaunched in a different manner. Moreover, the theoretical part of this article remains relevant for understanding the principles and objectives of coinjoins in general (not just Whirlpool), as well as understanding the effectiveness of the Whirlpool model.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

"*a bitcoin wallet for the streets*"

In this tutorial, you will learn what a coinjoin is and how to perform one using the Samourai Wallet software and the Whirlpool implementation.

## What is a coinjoin on Bitcoin?
**Coinjoin is a technique that breaks the traceability of bitcoins on the blockchain**. It relies on a collaborative transaction with a specific structure of the same name: the coinjoin transaction.

Coinjoins enhance the privacy of Bitcoin users by complicating chain analysis for external observers. Their structure allows merging multiple coins from different users into a single transaction, thus obscuring the trails and making it difficult to determine the links between input and output addresses.

The principle of coinjoin is based on a collaborative approach: several users who wish to mix their bitcoins deposit identical amounts as inputs of the same transaction. These amounts are then redistributed as outputs of equal value to each user. At the end of the transaction, it becomes impossible to associate a specific output with a known user in input. No direct link exists between the inputs and outputs, breaking the association between users and their UTXO, as well as the history of each coin.
![coinjoin](assets/notext/1.webp)

Example of a coinjoin transaction (not from me): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

To perform a coinjoin while ensuring that each user maintains control over their funds at all times, the process begins with the construction of the transaction by a coordinator, who then transmits it to the participants. Each user then signs the transaction after verifying that it suits them. All collected signatures are finally integrated into the transaction. If an attempt to divert funds is made by a user or the coordinator, by modifying the outputs of the coinjoin transaction, the signatures will prove invalid, leading to the rejection of the transaction by the nodes.

There are several implementations of coinjoin, such as Whirlpool, JoinMarket, or Wabisabi, each aiming to manage coordination among participants and increase the efficiency of coinjoin transactions.
In this tutorial, we will delve into the implementation of **Whirlpool**, which I consider to be the most efficient solution for performing coinjoins on Bitcoin. Although available on several wallets, in this tutorial, we will exclusively explore its use with the Samourai Wallet mobile application, without Dojo.

## Why perform coinjoins on Bitcoin?
One of the initial problems with any peer-to-peer payment system is double spending: how to prevent malicious individuals from spending the same monetary units multiple times without resorting to a central authority to arbitrate?

Satoshi Nakamoto provided a solution to this dilemma through the Bitcoin protocol, a peer-to-peer electronic payment system that operates independently of any central authority. In his white paper, he highlights that the only way to certify the absence of double spending is to ensure the visibility of all transactions within the payment system.

To guarantee that each participant is aware of the transactions, they must be publicly disclosed. Therefore, the operation of Bitcoin relies on a transparent and distributed infrastructure, allowing any node operator to verify the entirety of the electronic signature chains and the history of each coin, from its creation by a miner.

The transparent and distributed nature of Bitcoin's blockchain means that any network user can follow and analyze the transactions of all other participants. As a result, anonymity at the transaction level is impossible. However, anonymity is preserved at the level of individual identification. Unlike the traditional banking system where each account is linked to a personal identity, on Bitcoin, funds are associated with pairs of cryptographic keys, thus offering users a form of pseudonymity behind cryptographic identifiers.

Thus, confidentiality on Bitcoin is compromised when external observers manage to associate specific UTXOs with identified users. Once this association is established, it becomes possible to trace their transactions and analyze the history of their bitcoins. Coinjoin is precisely a technique developed to break the traceability of UTXOs, thereby offering a certain layer of confidentiality to Bitcoin users at the transaction level.

## How does Whirlpool work?
Whirlpool stands out from other coinjoin methods by using "_ZeroLink_" transactions, which ensure that there is strictly no technical link possible between all the inputs and all the outputs. This perfect mixing is achieved through a structure where each participant contributes an identical amount in input (except for mining fees), thus generating outputs of perfectly equal amounts.
This restrictive approach to inputs gives Whirlpool coinjoin transactions a unique feature: the total absence of deterministic links between inputs and outputs. In other words, each output has an equal probability of being attributed to any participant, compared to all other outputs in the transaction.
Initially, the number of participants in each Whirlpool coinjoin was limited to 5, with 2 new entrants and 3 remixers (we will explain these concepts further on). However, the increase in on-chain transaction fees observed in 2023 prompted the Samourai teams to rethink their model to improve privacy while reducing costs. Thus, taking into account the market situation of fees and the number of participants, the coordinator can now organize coinjoins including 6, 7, or 8 participants. These enhanced sessions are referred to as "_Surge Cycles_". It is important to note that, regardless of the configuration, there are always only 2 new entrants in Whirlpool coinjoins.

Thus, Whirlpool transactions are characterized by an identical number of inputs and outputs, which can be:
- 5 inputs and 5 outputs;
![coinjoin](assets/notext/2.webp)
- 6 inputs and 6 outputs;
![coinjoin](assets/notext/3.webp)
- 7 inputs and 7 outputs;
![coinjoin](assets/notext/4.webp)
- 8 inputs and 8 outputs.
![coinjoin](assets/notext/5.webp)
The model proposed by Whirlpool is thus based on small coinjoin transactions. Unlike Wasabi and JoinMarket, where the robustness of the anonsets relies on the volume of participants in a single cycle, Whirlpool bets on the chaining of several small-sized cycles.

In this model, the user pays the fees only upon their initial entry into a pool, allowing them to participate in a multitude of remixes without additional fees. It is the new entrants who cover the mining fees for the remixers.

With each additional coinjoin in which a coin participates, along with its peers encountered in the past, the anonsets will grow exponentially. The goal is therefore to take advantage of these free remixes which, with each occurrence, contribute to strengthening the density of the anonsets associated with each mixed coin.

Whirlpool was designed taking into account two important requirements:
- The accessibility of implementation on mobile devices, given that Samourai Wallet is primarily a smartphone application;
- The speed of the remixing cycles to promote a significant increase in anonsets.
These imperatives guided the developers of Samourai Wallet in the design of Whirlpool, leading them to limit the number of participants per cycle. Too few participants would have compromised the efficiency of the coinjoin, drastically reducing the anonsets generated each cycle, while too many participants would have posed management issues on mobile applications and would have hindered the flow of cycles.
**Ultimately, there is no need to have a high number of participants per coinjoin on Whirlpool since the anonsets are achieved through the accumulation of several coinjoin cycles.**

[-> Learn more about Whirlpool anonsets.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### The pools and coinjoin fees
For these multiple cycles to effectively increase the anonsets of the mixed coins, a certain framework must be established to restrict the amounts of UTXO used. Whirlpool thus defines different pools.

A pool represents a group of users wishing to mix together, who agree on the amount of UTXO to use to optimize the coinjoin process. Each pool specifies a fixed amount for the UTXO, which the user must adhere to in order to participate. Thus, to perform coinjoins with Whirlpool, you need to select a pool. The pools currently available are as follows:
- 0.5 bitcoins;
- 0.05 bitcoin;
- 0.01 bitcoin;
- 0.001 bitcoin (= 100,000 sats).

By joining a pool with your bitcoins, they will be divided to generate UTXOs that are perfectly homogeneous with those of the other participants in the pool. Each pool has a maximum limit; thus, for amounts exceeding this limit, you will be forced either to make two separate entries within the same pool or to orient yourself towards another pool with a higher amount:

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


These fees essentially act as an entry ticket for the chosen pool, regardless of the amount you put in coinjoin. Thus, whether you join the 0.01 pool with exactly 0.01 BTC or enter it with 0.5 BTC, the fees will remain the same in absolute value.

Before proceeding to coinjoins, the user thus has a choice between 2 strategies:
- Opt for a smaller pool to minimize service fees, knowing that they will receive several small UTXOs in return;
- Or prefer a larger pool, agreeing to pay higher fees to end up with a reduced number of UTXOs of greater value.

It is generally advised against merging several mixed UTXOs after the coinjoin cycles, as this could compromise the acquired confidentiality, especially due to the Common-Input-Ownership Heuristic (CIOH). Therefore, it may be wise to choose a larger pool, even if it means paying more, to avoid having too many small-value UTXOs as output. The user must weigh these compromises to choose the pool they prefer.

Besides the service fees, the mining fees inherent to any Bitcoin transaction must also be considered. As a Whirlpool user, you will be required to pay the mining fees for the preparation transaction (`Tx0`) as well as those for the first coinjoin. All subsequent remixes will be free, thanks to Whirlpool's model which relies on the payment of new entrants.

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

Each of these accounts fulfills a specific function within the coinjoin process.

All these accounts are linked to a single seed, which allows the user to recover access to all their bitcoins using their recovery phrase and, if applicable, their passphrase. However, it is necessary to specify to the software, during this recovery operation, the different account indexes that were used.

Let's now look at the different stages of a Whirlpool coinjoin within these accounts.

### The different stages of coinjoins on Whirlpool
**Stage 1: The Tx0**
The starting point of any Whirlpool coinjoin is the **deposit** account. This account is the one you automatically use when you create a new Bitcoin wallet. This account must be credited with the bitcoins that one wishes to mix.
The `Tx0` represents the first step in the Whirlpool mixing process. It aims to prepare and equalize the UTXO for the coinjoin, by dividing them into units corresponding to the amount of the selected pool, to ensure the homogeneity of the mix. The equalized UTXO are then sent to the **premix** account. As for the difference that cannot enter the pool, it is separated into a specific account: the **bad bank** (or "doxxic change").
This initial transaction `Tx0` also serves to settle the service fees due to the mix coordinator. Unlike the following steps, this transaction is not collaborative; the user must therefore assume all the mining fees:
![coinjoin](assets/en/7.webp)

In this example of a `Tx0` transaction, an input of `372,000 sats` from our **deposit** account is divided into several output UTXO, which are distributed as follows:
- An amount of `5,000 sats` intended for the coordinator for service fees, corresponding to the entry into the pool of `100,000 sats`;
- Three UTXO prepared for mixing, redirected to our **premix** account and registered with the coordinator. These UTXO are equalized at `108,000 sats` each, to cover the mining fees for their future initial mix;
- The surplus that cannot enter the pool, being too small, is considered toxic change. It is sent to its specific account. Here, this change amounts to `40,000 sats`;
- Finally, there are `3,000 sats` that do not constitute an output, but are the mining fees necessary to confirm the `Tx0`.

For example, here is a real Whirlpool Tx0 (not from me): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Step 2: The doxxic change**
The surplus that could not be integrated into the pool, here equivalent to `40,000 sats`, is redirected to the **bad bank** account, also referred to as "doxxic change", to ensure a strict separation from the other UTXO in the wallet.

This UTXO is dangerous for the user's privacy, as not only is it still attached to its past, and thus possibly to the identity of its owner, but additionally, it is noted as belonging to a user who has performed a coinjoin.
If this UTXO is merged with mixed outputs, they will lose all the confidentiality gained during the coinjoin cycles, notably because of the Common-Input-Ownership-Heuristic (CIOH). If it is merged with other doxxic changes, the user risks losing confidentiality since this will link the different inputs of the coinjoin cycles. Therefore, it must be handled with caution. The way to manage this toxic UTXO will be detailed in the last part of this article, and future tutorials will cover these methods more in-depth on PlanB Network.

**Step 3: The Initial Mix**
After the `Tx0` is completed, the equalized UTXOs are sent to the **premix** account of our wallet, ready to be introduced into their first coinjoin cycle, also called "initial mix". If, as in our example, the `Tx0` generates multiple UTXOs for mixing, each of them will be integrated into a separate initial coinjoin.

At the end of these first mixes, the **premix** account will be empty, while our coins, having paid the mining fees for this first coinjoin, will be adjusted exactly to the amount defined by the chosen pool. In our example, our initial UTXOs of `108 000 sats` will have been reduced to exactly `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Step 4: The Remixes**
After the initial mix, the UTXOs are transferred to the **postmix** account. This account gathers the already mixed UTXOs and those waiting for remixing. When the Whirlpool client is active, the UTXOs in the **postmix** account are automatically available for remixing and will be randomly chosen to participate in these new cycles.

As a reminder, the remixes are then 100% free: no additional service fees or mining fees are required. Keeping the UTXOs in the **postmix** account thus maintains their value intact and simultaneously improves their anonsets. That's why it's important to allow these coins to participate in multiple coinjoin cycles. It costs you strictly nothing, and it increases their levels of anonymity.

When you decide to spend mixed UTXOs, you can do so directly from this **postmix** account. It is advisable to keep the mixed UTXOs in this account to benefit from free remixes and to avoid them leaving the Whirlpool circuit, which could decrease their confidentiality.

As we will see in the following tutorial, there is also the `mix to` option which offers the possibility to automatically send your mixed coins to another wallet, such as a cold wallet, after a defined number of coinjoins.
After covering the theory, let's dive into practice with a tutorial on using Whirlpool through the Samourai Wallet Android app!
## Tutorial: Coinjoin Whirlpool on Samourai Wallet
There are numerous options for using Whirlpool. The one I want to introduce here is the Samourai Wallet option (without Dojo), an open-source Bitcoin wallet management application on Android.

Mixing on Samourai without Dojo has the advantage of being quite easy to handle, quick to set up, and requires no other device than an Android phone and an internet connection.

However, this method has two notable drawbacks:
- Coinjoins will only occur when Samourai is running in the background and connected. This means that if you want to mix and remix your bitcoins 24/7, you must constantly keep Samourai turned on;
- If you use Whirlpool with Samourai Wallet without taking care to connect your own Dojo, then your application will have to connect to the server maintained by the Samourai teams, and you will reveal the `xpub` of your wallet to them. These anonymous pieces of information are necessary for your application to find your transactions.

The ideal solution to overcome these limitations is to operate your own Dojo associated with a Whirlpool CLI instance on your personal Bitcoin node. This way, you will avoid any information leakage and achieve complete independence. Although the tutorial presented below is useful for certain goals or for beginners, to truly optimize your coinjoin session, using your own Dojo is recommended. A detailed guide on setting up this configuration will soon be available on PlanB Network.

### Installing Samourai Wallet
To start, you will obviously need the Samourai Wallet app. You can download it directly from the official website using the APK, from their GitLab, or from the Google Play Store.

### Creating a Software Wallet
After installing the software, you will need to proceed with creating a Bitcoin wallet on Samourai. If you already have one, you can skip directly to the next step.

Upon opening the application, press the blue `Start` button. You will then be asked to select a location in your phone's files where the encrypted backup of your new wallet will be stored.

![samourai](assets/notext/9.webp)
Activate Tor by clicking on the corresponding notch. At this stage, you also have the option to select a specific Dojo. However, in this tutorial, we will continue with the default Dojo; so you can leave the option disabled. When Tor is connected, press the `Create a new wallet` button.
![samourai](assets/notext/10.webp)

Samourai Wallet then prompts you to set a BIP39 passphrase. This additional password is very important as it directly acts in the derivation of your private keys. A potential loss of this passphrase would result in the inability to access your bitcoins, making them irretrievably lost. To restore your Samourai wallet, it is imperative to have both your 12-word recovery phrase and the passphrase.

It is therefore essential to choose a robust passphrase and to make one or more physical copies, on paper or on a metallic medium, to ensure the security of your bitcoins. After completing these tasks, check the box `I am aware that in case of loss...`, then press the `NEXT` button.

![samourai](assets/notext/11.webp)

You must then define a PIN code consisting of 5 to 8 digits. This code will secure access to your wallet on your phone. It will be requested every time you want to open the Samourai application. Opt for a robust PIN code and make sure to keep a backup copy. After that, you can press the `NEXT` button.

![samourai](assets/notext/12.webp)

Samourai will invite you to enter your PIN code again for confirmation. Enter it, then press `FINALIZE`.

![samourai](assets/notext/13.webp)

You will then access your recovery phrase composed of 12 words. This phrase allows you to recover your wallet with the previously entered passphrase. It is strongly recommended to make one or more copies of this phrase on physical media, such as paper or a metallic material, to ensure the security of your bitcoins in case of a problem.

After making these backups, you will be directed to the interface of your new Samourai wallet.

![samourai](assets/notext/14.webp)

You are offered to obtain your PayNym Bot. You can request it if you wish, although it is not essential for our tutorial.

![samourai](assets/notext/15.webp)
Before proceeding to receive bitcoins on this new wallet, it is strongly recommended to recheck the validity of your wallet backups (the passphrase and the recovery phrase). To verify the passphrase, you can select the icon of your PayNym Bot located at the top left of the screen, then follow the path:
```plaintext
Settings > Troubleshooting > Passphrase/backup test
```

Enter your passphrase to perform the verification.

![samourai](assets/notext/16.webp)

Samourai will confirm if it is valid.

![samourai](assets/notext/17.webp)

To verify your backup of the recovery phrase, access the icon of your PayNym Bot, located at the top left of the screen, and follow this path:
```plaintext
Settings > Wallet > Show 12-word recovery phrase
```

Samourai will display a window with your recovery phrase. Make sure it matches exactly with your physical backup.

To go further and perform a complete recovery test, note a witness element of your wallet, such as one of the `xpubs`, then proceed to delete your wallet (provided it is still empty). The goal is to try to restore this empty wallet using only your physical backups. If the restoration is successful, this indicates that your backups are valid and reliable.

### Receiving bitcoins
After creating your wallet, you will start with a single account, identified by the index `0'`. This is the **deposit** account we talked about in the previous parts. It is to this account that you will need to transfer the bitcoins intended for coinjoins.

To do this, click on the blue `+` symbol located at the bottom right of the screen.

![samourai](assets/notext/18.webp)

Then click on the green `Receive` button.

![samourai](assets/notext/19.webp)

Samourai will automatically generate a new blank address to receive bitcoins.

![samourai](assets/notext/20.webp)

You can send the bitcoins to be mixed there.

![samourai](assets/notext/21.webp)

### Making the Tx0
When the transaction is confirmed, we can start the coinjoins process. To do this, click on the blue `+` button at the bottom right of the screen.

![samourai](assets/notext/22.webp)

Then click on `Whirlpool` in blue.

![samourai](assets/notext/23.webp)

Wait while Whirlpool initializes and Samourai creates the necessary accounts.

![samourai](assets/notext/24.webp)

You will then arrive at the Whirlpool homepage. Click on `Start`.
![samourai](assets/notext/25.webp)
Select the UTXO from the **deposit** account that you wish to send in coinjoin cycles, then click on `Next`.

![samourai](assets/notext/26.webp)

In the next step, you will need to choose the fee level to allocate to the `Tx0` as well as to your first mix. This setting will determine the speed at which your `Tx0` and your initial coinjoin (or initial coinjoins) will be confirmed. Keep in mind that the mining fees for the `Tx0` and the initial mix are your responsibility, but you will not have to pay mining fees for the subsequent remixes. You have the choice between `Low`, `Normal`, or `High` options.

![samourai](assets/notext/27.webp)

In the same window, you have the option to choose the pool you will enter. Given that I initially selected a UTXO of `454,258 sats`, my only possible choice is the `100,000 sats` pool. This page also presents you with the pool's service fees, in addition to the mining fees, which allows you to know the total cost for this coinjoin cycle. If everything suits you, select the appropriate pool and continue by clicking on the blue `VERIFY CYCLE DETAILS` button.

![samourai](assets/notext/28.webp)

You can then see all the details of your coinjoin cycle:
- the number of UTXOs that will enter the pool;
- the various fees incurred;
- the amount of doxxic change...

Verify the information, then click on the green `START CYCLE` button.

![samourai](assets/notext/29.webp)

A window will appear to offer you to mark the toxic change resulting from your entry into the coinjoin cycle as "non-spendable". By selecting `YES`, this UTXO will not be visible in your wallet and cannot be selected for future transactions. However, it will remain accessible in the list of UTXOs in your wallet, where you can manually change its status. It is recommended to opt for this option to avoid any handling error that could compromise your privacy later on. If you choose `NO`, the toxic change will remain available for use in your wallet. If you want to learn more about managing and using this toxic change, I advise you to read the last part of this tutorial.

![samourai](assets/notext/30.webp)

Samourai will then broadcast your Tx0.

![samourai](assets/notext/31.webp)

### Making the coinjoins
Once the Tx0 is broadcasted, you can find it in the `Transactions` tab of the Whirlpool menu.

![samourai](assets/notext/32.webp)
Your UTXOs ready to be mixed are in the `Mixing in progress...` tab, which corresponds to the **Premix** account.
![samourai](assets/notext/33.webp)

Once the `Tx0` is confirmed, your UTXOs will be automatically registered with the coordinator, and the initial mixes will start successively in an automatic manner.

![samourai](assets/notext/34.webp)

By checking the `Remixing` tab, which corresponds to the **Postmix** account, you will observe the UTXOs resulting from the initial mixes. These coins will remain ready for subsequent remixing, which will not incur any additional fees. I recommend consulting this other article to learn more about the remixing process and the efficiency of a coinjoin cycle: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

![samourai](assets/notext/35.webp)

It is possible to temporarily suspend the remixing of a UTXO by pressing the pause button located to its right. To make it eligible for remixing again, simply click on the same button a second time. It is important to note that only one coinjoin can be performed per user and per pool simultaneously. Thus, if you have 6 UTXOs of `100 000 sats` ready for the coinjoin, only one of them can be mixed. After mixing a UTXO, Samourai Wallet proceeds to randomly select a new UTXO from your availability, in order to diversify and balance the remixing of each coin.

![samourai](assets/notext/36.webp)

To ensure continuous availability of your UTXOs for remixing, it is necessary to keep the Samourai application active in the background. You should see a notification on your phone confirming that Whirlpool is running. Closing the application or turning off your phone will pause the coinjoins.

### Completing the coinjoins
To spend your mixed bitcoins, go to the **Postmix** account noted `Remixing` in the Whirlpool menu tabs.

![samourai](assets/notext/37.webp)

Click on the blue Whirlpool logo located at the bottom right.

![samourai](assets/notext/38.webp)

Then click on `Spend Mixed UTXOs`.

![samourai](assets/notext/39.webp)

You can then enter the recipient's address and the amount to send, in the same way as for any other transaction made with Samourai Wallet. The blue background indicates that the funds are being spent from a Whirlpool account, and not from the **deposit** account.

![samourai](assets/notext/40.webp)

By clicking on the 3 small dots at the top right, you have the option to select specific UTXOs.
![samourai](assets/notext/41.webp)
By clicking on the white square at the top right of the window, you can scan the QR code of the receiving address with your camera.

![samourai](assets/notext/42.webp)

Enter the necessary information for your spending transaction, then click on the blue `VERIFY TRANSACTION` button.

![samourai](assets/notext/43.webp)

In the next step, you have the option to modify the fee rate associated with your transaction. You can also enable the Stonewall option by checking the corresponding box. If the Stonewall option is not selectable, it means that your **Postmix** account does not contain a UTXO of sufficient size to support this particular transaction structure.

[-> Learn more about Stonewall transactions.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

If everything is to your satisfaction, click on the green `SEND ... BTC` button.

![samourai](assets/notext/44.webp)

Samourai will then proceed to sign your transaction before broadcasting it on the network. You just need to wait until it is added to a block by a miner.

![samourai](assets/notext/45.webp)

### Using an SCODE
Sometimes, the Samourai Wallet teams offer "SCODEs". An SCODE is a promotional code that provides a discount on the service fees of the pool. Samourai Wallet occasionally offers such codes to its users during special events. I advise you [to follow Samourai Wallet](https://twitter.com/SamouraiWallet) on social media so as not to miss out on future SCODES.

To apply an SCODE on Samourai, before starting a new coinjoin cycle, go to the Whirlpool menu and select the three small dots located at the top right of the screen.

![samourai](assets/notext/46.webp)

Click on `SCODE (promo code) Whirlpool`.

![samourai](assets/notext/47.webp)

Enter the SCODE in the window that opened, then validate by clicking on `OK`.

![samourai](assets/notext/48.webp)

Whirlpool will automatically close. Wait for Samourai to finish loading, then open the Whirlpool menu again.

![samourai](assets/notext/49.webp)

Make sure your SCODE has been correctly registered by clicking once more on the three small dots, then selecting `SCODE (promo code) Whirlpool`. If everything is in order, you are ready to start a new Whirlpool cycle with a discount on the service fees. It is important to note that these SCODEs are temporary: they remain valid for a few days before becoming obsolete.

## How to know the quality of our coinjoin cycles?
For a coinjoin to be truly effective, it is essential that it demonstrates good uniformity between the amounts of inputs and outputs. This uniformity amplifies the number of possible interpretations in the eyes of an external observer, thereby increasing the uncertainty surrounding the transaction. To quantify this uncertainty generated by a coinjoin, one can resort to calculating the transaction's entropy. For an in-depth exploration of these indicators, I refer you to the tutorial: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). The Whirlpool model is recognized as the one that brings the most homogeneity to coinjoins.

Next, the performance of several coinjoin cycles is evaluated based on the extent of the groups in which a coin is concealed. The size of these groups defines what is called the anonsets. There are two types of anonsets: the first assesses the privacy obtained against a retrospective analysis (from the present to the past) and the second, against a prospective analysis (from the past to the present). For a detailed explanation of these two indicators, I invite you to consult the tutorial: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## How to manage postmix?
After performing coinjoin cycles, the best strategy is to keep your UTXOs in the **postmix** account, waiting for their future use. It is even advisable to let them remix indefinitely until you need to spend them.

Some users might consider transferring their mixed bitcoins to a wallet secured by a hardware wallet. This is possible, but it is important to follow the recommendations of Samourai Wallet meticulously so as not to compromise the acquired confidentiality.

The merging of UTXOs constitutes the most frequently made mistake. It is necessary to avoid combining mixed UTXOs with unmixed UTXOs in the same transaction, in order to avoid the CIOH (*Common-Input-Ownership-Heuristic*). This requires careful management of your UTXOs within your wallet, particularly in terms of labeling. Beyond coinjoin, merging UTXOs is generally a bad practice that often leads to a loss of confidentiality when not properly managed.
You should also be vigilant about the consolidation of mixed UTXOs with each other. Moderate consolidations are possible if your mixed UTXOs have significant anonsets, but this will inevitably decrease the privacy of your coins. Ensure that consolidations are neither too large nor carried out after an insufficient number of remixes, as this risks establishing deducible links between your UTXOs before and after the coinjoin cycles. In case of doubt about these operations, the best practice is not to consolidate postmix UTXOs, and to transfer them one by one to your hardware wallet, generating a new blank address each time. Once again, remember to properly label each received UTXO.

It is also advised against transferring your postmix UTXOs to a wallet using uncommon scripts. For example, if you enter Whirlpool from a multisig wallet using `P2WSH` scripts, there's little chance you'll be mixed with other users having the same type of wallet originally. If you exit your postmix to this same multisig wallet, the privacy level of your mixed bitcoins will be greatly diminished. Beyond scripts, there are many other wallet fingerprints that can trick you.

As with any Bitcoin transaction, it is also appropriate not to reuse receiving addresses. Each new transaction must be received on a new blank address.

The simplest and safest solution is to let your mixed UTXOs rest in their **postmix** account, letting them remix and only touching them to spend. Samourai and Sparrow wallets have additional protections against all these risks related to chain analysis. These protections help you avoid making mistakes.

## How to manage doxxic change?
Next, you must be careful in managing doxxic change, the change that could not enter the coinjoin pool. These toxic UTXOs, resulting from the use of Whirlpool, pose a risk to your privacy since they establish a link between you and the use of coinjoin. It is therefore imperative to handle them with caution and not to combine them with other UTXOs, especially mixed UTXOs. Here are different strategies to consider for their use:
- **Mix them in smaller pools:** If your toxic UTXO is large enough to enter a smaller pool on its own, consider mixing it. This is often the best option. However, it is crucial not to merge several toxic UTXOs to access a pool, as this could link your different entries.
- **Mark them as "non-spendable":** Another approach is to stop using them, mark them as "non-spendable" in their dedicated account, and just Hodl. This ensures that you do not accidentally spend them. If the value of bitcoin increases, new pools more suited to your toxic UTXOs could emerge;
- **Make donations:** Consider making donations, even modest ones, to developers working on Bitcoin and its associated software. You can also donate to organizations that accept BTC. If managing your toxic UTXOs seems too complicated, you can simply get rid of them by making a donation;
- **Buy gift cards:** Platforms such as [Bitrefill](https://www.bitrefill.com/) allow you to exchange bitcoins for gift cards that can be used at various merchants. This can be a way to get rid of your toxic UTXOs without losing the associated value;
- **Consolidate them on Monero:** Samourai Wallet now offers an atomic swap service between BTC and XMR. This is ideal for managing toxic UTXOs by consolidating them on Monero, without compromising your privacy via KYC, before sending them back to Bitcoin. However, this option can be costly in terms of mining fees and the premium due to liquidity constraints;
- **Send them to the Lightning Network:** Transferring these UTXOs to the Lightning Network to benefit from reduced transaction fees is an option that can be interesting. However, this method may reveal certain information depending on your use of Lightning and should therefore be practiced with caution.

Detailed tutorials on implementing these different techniques will be offered soon on PlanB Network.

**Additional resources:**
[Samourai Wallet video tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Samourai Wallet Documentation - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter thread on coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog post on coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).
