---
name: Coin Control
description: Get started with Coin Control, a key tool to protect your privacy on Bitcoin
---
![cover](assets/cover.webp)

*This tutorial is imported from [a lesson by Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*


## Introduction


The robustness of the Bitcoin protocol is guaranteed by simple key concepts. Among these, transparency stands out: all Bitcoin transactions are public and easily verifiable by anyone. Although this feature is a cornerstone of the protocol, as it prevents fraud and guarantees the authenticity of funds, it can also pose a challenge to confidentiality. **Have you ever wondered if such transparency could undermine your privacy?**


You should. While accumulating Satoshi non-kyc is rather easy, your privacy is most at risk right at the spending stage.


### What happens when you spend a UTXO


Spending Bitcoin is not simply the transfer of value to someone else.


By consuming one of your UTXOs, you must in fact meet the conditions imposed for protocol transparency, because you have an obligation to prove that you own those funds. You therefore make yourself responsible for :


- expose your public key;
- produce a digital signature.


The time of spending is therefore the most critical: **spending Bitcoin is an act to be done consciously and with as much control as possible**.


## Coin Control


In the Bitcoin protocol, items such as _account_ or _monetary units_ do not exist. The concept of UTXO is explained excellently in the following course, which I highly recommend:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

With Bitcoin what you accumulate and later spend are small or large units of account measured in Satoshi, represented by `unspent transaction outputs`, the **UTXO**, also called `coins`. When you use UTXOs to create a transaction, they are completely destroyed and other UTXOs are created in their place.


Software Wallets are developed to make this choice automatically, using "randomly" selected coins, adopting certain algorithms provided by the protocol. The only criterion that these algorithms meet, is to cover the amount needed for spending.


They may mix together UTXOs of different ages, or favor spending the newest or "oldest," depending on the algorithm chosen by the developers. The best Software Wallets, also plan to leave the user with an important choice.


The `Coin Control`manual, which you can also find referred to as `Coin Selection`, is a feature of some Software Wallets that allows you to **manually select UTXOs to spend when you build your transaction**.


Suppose we have a Wallet with 3 UTXOs of 21,000, 42,000 and 63,000 Satoshi, respectively.


![img](assets/en/01.webp)


If you have to spend 24,000 Sats and let an algorithm do the automatic selection, a good Software Wallet might choose to combine UTXO 1 + UTXO 2 to pay the 24k Sats and Miner fees, creating a remainder that goes back to an internal address of the starting Wallet.


![img](assets/en/02.webp)


After the transaction, the new situation in Wallet, counting only UTXOs, can be summarized as follows.


![img](assets/en/03.webp)


With the right software and your awareness, however, you could have made a different, in some ways more correct choice. For example, by selecting only the UTXO2 (from 42,000 Sats).


![img](assets/en/04.webp)


With an end situation in your Wallet, at the level of UTXO, that looks different from before.


![img](assets/en/05.webp)


## Why manual coin control?


![img](assets/en/06.webp)


In the two examples above, the balance is actually the same `108,280 Sats`. After spending 24,000 Sats, without manual selection we would have 2 UTXO in Wallet; with Coin manual control we have 3 total.


The question we might ask ourselves is the following: **why do all this?** There are, or could be, several reasons why we did not use `UTXO1` **and they are all at the core of why—when spending—activating manual coin control is one of the best practices to follow**.


Selecting UTXOs allows you to favor some aspects over others. The choice really depends on the goals you want to achieve.


### Privacy


One of the main advantages, when it comes to manual Coin control, is a **greater privacy for the spender**. Let us always take our example: the expenditure of 24,000 Satoshi _without manual Coin selection_. Since Blockchain of Bitcoin is a public record, an outside observer can declare, without a shadow of a doubt, that the inputs `UTXO1 of 21,000 Sats` and `UTXO2 of 42,000 Sats`, as well as the rest, the `UTXO5 from 38,280 Sats` **all three belong to the same user**.


By manually selecting `UTXO2`, on the other hand, `UTXO1` remains completely reserved, sitting in the UTXO set waiting to be spent at a more appropriate time.


The `UTXO1` could come from a KYC source, such as a payment received in exchange for goods and services, while the other UTXOs do not. Mixing a UTXO-kyc with others that are more confidential compromises the anonymity set of non-kyc funds.


**KYC funds would inevitably lead back to the payer’s identity. If it were your wallet, would you want an external observer to be able to trace your identity with such absolute certainty?**


Try then to consider that Wallets that implement manual selection of UTXOs, for example, allow **segregation of one or more UTXOs**, a function to be used when such situations arise.


Although I am convinced that KYC funds should be kept in a separate Wallet than Bitcoin purchased without kyc, if this is your case the segregation of some of your addresses is a key help, which you could take advantage of by learning to manually select your spending inputs.


### Saving on fees


Selecting the correct UTXO to make an expenditure, **allows for fee optimization**. Again starting from our initial example, Software Wallet selected two UTXOs to cover the expense to be made. Two UTXOs imply two signatures to be shown to the network. It follows that the transaction has a greater "weight" in terms of vBytes.


Using the Coin manual control, on the other hand, you can select only one that is sufficient to cover the amount, saving fees by decreasing the "weight" of the transaction.


In times when fees are high, but you are forced to spend Bitcoin On-Chain (e.g., to open a Lightning Network channel), that's when the Coin control turns out to be the right economic incentive to turn to.


### Aggregation of the remains


When you make a payment and use Bitcoin On-Chain, the possibility of receiving change almost always becomes a certainty. Each remainder is itself a small loss of privacy, as it reveals to the network (and especially to the recipient of the payment) an address of yours that can be associated with your source input.


Considering that the best Wallet HDs generate special addresses for the remnants, you can easily recognize them and "segregate" all the remnants of the various transactions made; when they have reached a certain amount you can select them manually and consolidate them, or swap to Lightning Network (my preferred method) and process them so as to regain the privacy lost in spending.


### Expenditure from a Cold Wallet


The Cold Wallet is an instrument with which one can reasonably obtain a good degree of security, to store any amount of funds to keep aside for a long period of time. However, unforeseen events may happen, so the need arises to get a hand on savings and meet some unexpected expenses.


I don't know how many can share my approach, but my advice is to **never make the expenditure directly from Cold Wallet, to avoid receiving the change between the addresses of the same**. Learn to manually select the UTXOs needed to cover the expense, transfer them to a Wallet Hot and prepare your transaction from the latter. Any change, then, you can send it back to a Cold Wallet address (if the amount is adequate), use it for other expenses, or still segregate it as we have just seen.


## Practical presentation

After the technical introduction of the `why`, let`s see how to put the Coin manual control into practice with different software, desktop and mobile. We will always use the same Wallet BIP39, imported into each of the chosen tools, so as to show you the small differences between them.


## Wallet Desktop


### Sparrow


If you use Sparrow, open your Wallet and select _UTXOs_ from the menu on the left. You will see a list of all UTXOs associated with your Wallet.


Simply click with the mouse on one of them and then choose _Send Selected_. Sparrow also shows you the total available for spending after the selection, right next to the command. Graphically Sparrow shows you the selected UTXO by highlighting it in blue.


![img](assets/en/07.webp)


You can also select more than one. Help yourself with the _CTRL_ key to select non-adjacent UTXOs in the list.


![img](assets/en/08.webp)


After manually selecting UTXO, you can start to build the transaction, and Sparrow will show you well, graphically, how it is constituted.


![img](assets/en/09.webp)


#### Segregation of UTXO


Segregating funds means "locking" them within Wallet so that they cannot be used as input to a transaction. Sparrow allows this functionality, which is always accessed from the _UTXOs_ menu: you place the mouse over the UTXO to be "locked" and click the right mouse button. Among the features of this procedure will appear _Freeze UTXO_. This is how you will be able to segregate Coins with Sparrow wallets.


![img](assets/en/29.webp)


### Electrum


If your Wallet desktop is Electrum, you should know that you can manually select UTXOs either from the _Addresses_ menu or from the _Coins_ menu. In both menus, selection is done by pointing the mouse to the desired UTXO and choosing _Add to Coin control_ after right-clicking.


![img](assets/en/10.webp)


Even with this software you can select more than one UTXO, helping with the _CTRL_ key on your keyboard if they are not adjacent to each other.


![img](assets/en/11.webp)


Graphically Electrum will show you the selection by highlighting the selected UTXOs in green, while a bar appears at the bottom, highlighted in the same color, showing the available balance after the Coin control.


![img](assets/en/12.webp)


Once you have selected the output, or outputs, you can build your transaction as you usually do from the _Send_ menu.


#### Segregation of UTXO


Electrum provides this functionality by going to the _Coins_ menu, where you will go to select a particular UTXO and then choosing _Freeze_ with a right-click. You can "freeze" the address even without funds from the _Addresses_ menu, or the "Coin" to not spend it.


![img](assets/en/28.webp)


### Nunchuk


Nunchuk allows you to manually select UTXOs from the main menu once it is open. Launch Nunchuk and click _View coins_.


![img](assets/en/13.webp)


This opens the window that contains all the UTXOs in your Wallet, where you can select one or more by activating the check mark next to each amount. After making your selection, continue with _Create transaction_.


![img](assets/en/14.webp)


After that you can enter the destination address and set the amount and fees.


![img](assets/en/15.webp)


#### Segregation of UTXO


For the sake of completeness, Nunchuk also allows among its features, to segregate one (or more) UTXOs and does so in two different ways. Access the _View coins_ menu and manually choose from the list of coins. Then click the _More_ menu at the bottom right: a list of options will appear, from which you can choose _Lock coins_.


![img](assets/en/39.webp)


![img](assets/en/40.webp)


You can also click in the space reserved for UTXO, to access the _Coin details_ window. Here the command to lock/unlock the UTXO in question appears in the upper right corner.


![img](assets/en/41.webp)


### Blockstream App


Blockstream App desktop, formerly known as Green, allows you to make Coin selection when you have already started building the transaction. Therefore, open your Wallet and click on _Send_.


![img](assets/en/16.webp)


Paste the destination address into the appropriate field and then select _Manual Coin selection_.


![img](assets/en/17.webp)


This opens the window where you can select one or more UTXO coins. In the example below, we have selected two coins. After that, confirm your choice by clicking on _Confirm Coin Selection_.


![img](assets/en/18.webp)


Set the amount and fees and then proceed normally with your transaction.


![img](assets/en/19.webp)


⚠️ N.B. In the _Coins_ menu of Green there are _Lock_/_Unlock_ items that foreshadow the possibility of segregating UTXO. This feature is activated only in so-called Multisig accounts; it is also activated only by selecting UTXO of very small amount, close to the threshold of `Dust`.


## Wallet mobile


Wallets can also be chosen from mobile, which allow UTXOs to be selected manually. Let us see Blue Wallet as the first example.


### Blue Wallet


If you are a user of this Wallet, open it and click to enter the control screens related to one of your Wallets. To access the Coin control manual you must enter the spending phase, then click _Send_.


![img](assets/en/21.webp)


On the next screen choose the menus indicated by the three dots in the upper right corner. A drop-down window opens with a series of commands. Choose the last one: _Coin Control_.


![img](assets/en/22.webp)


At this point Blue Wallet shows all your UTXOs. In addition to amounts, they are differentiated graphically by different colors.


![img](assets/en/27.webp)


Choose the UTXO to select after which select _Use Coin_.


![img](assets/en/23.webp)


Blue Wallet takes you back to the _Send_ window to continue building the transaction. Adjust the amount and fees, after which you choose _Next_.


![img](assets/en/24.webp)


At this point you can end the transaction, as you usually do.


#### Segregation of a UTXO


Blue Wallet also allows you to segregate UTXOs, making them unavailable for spending which is not a bad function for a Wallet from a mobile device. You access the Coin control with the procedure just explained and, after selecting the UTXO, choose _Freeze_ instead of _Use Coin_.


![img](assets/en/26.webp)


### Nunchuk


The mobile version of Nunchuk also provides the ability for the user to do Coin control. If you use this app from mobile, open it and go to the _Wallet_ menu. From there choose _View coins_.


![img](assets/en/30.webp)


In the window where the list of UTXOs appears, click _Select_.


![img](assets/en/38.webp)


A selection function appears next to each UTXO. As in the desktop version, manual selection on Nunchuk mobile is done by checking the little square next to the amount. The screen shows the number of UTXOs selected and the total amount available. When finished, click the ₿ symbol in the lower left corner, which is the command to start building the transaction.


![img](assets/en/31.webp)


Now you can complete the transaction, choosing the amount and clicking _Continue_.


![img](assets/en/32.webp)


Continue as you always do, pasting a destination address, description, and customizing fee settings.


#### Segregation of UTXO


You can also segregate UTXOs with mobile Nunchuk. Access the dedicated coins list window and select the arrow next to the UTXO you want to segregate.


![img](assets/en/42.webp)


You will see the space reserved for _Coin details_, where you can select _Lock this coin_.


![img](assets/en/43.webp)


### Bitcoin Keeper


Bitcoin Keeper is the last Wallet we will see in this guide. We see its functionality applied to Coin control with a Wallet single-sig, although such a use is not the purpose of this very particular app. After setting up Keeper on your phone, launch it and open a Wallet containing some funds. In the center of the main screen click _View All Coins_.


![img](assets/en/34.webp)


Keeper shows an overview of the UTXOs. To access the selection screen click _Select To Send_.


![img](assets/en/35.webp)


You can select coins by checking them off by clicking on the appropriate command. When finished, click _Send_.


![img](assets/en/36.webp)


Bitcoin Keeper takes you directly to the _Send_ menu, where you can build the transaction with the selected UTXOs.


![img](assets/en/37.webp)


## Hardware Wallet


Each of the Software Wallets seen in this guide can be the watch-only interface to one of your Hardware Wallets. It means the Coin control for offline signing device is performed with the steps seen so far.


### General recommendations


Coin control is a very effective practice for selecting your transaction inputs. Manual selection is even more efficient if, when buying/receiving your funds, you have labeled the source of your Satoshis well. If you wish to learn this technique well, I recommend the following tutorial:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

We have talked previously about `segregation of remains`. If you want to lock remnants for later processing and regain privacy (swap on Layer 2), you must take care to `label` them each time you receive one. Of the Software Wallets seen so far, only Electrum graphically colors UTXO remainders to make them visible at a glance. Others, such as Sparrow, show you the chain in the derivation path of the individual UTXO (`m/84'/0'/0'/1/11`).


To apply this technique effectively, remember to always add a description on the change you receive: the person to whom you sent your funds (a payment, a tutorial, or other), knows the address associated with the change and knows that it belongs to you, since it comes from the transaction you did together!