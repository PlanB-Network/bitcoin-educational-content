---
name: Electrum Airgap
description: A first step towards security, a cold wallet with Electrum
---
![cover](assets/cover.webp)


## Cold Wallet


In this tutorial I will explain how to make your first airgap signing device, disconnected from the Internet, even without having a dedicated Hardware Wallet. All you need is to have two computers available:


- an old device to be forever prevented from connecting to the Internet;
- your daily-use computer.


This configuration allows for a greater degree of security than the classic `Hot Wallet`: the old computer--without network connection--is the keeper of your private keys, which are never exposed on the Internet, but stored offline ("airgap" or "Cold").


Instead, you will install a Wallet display ("watch-only") on your daily computer, which is connected to the network and with which you can, for example, check balances and prepare receipt transactions.


## Wallet Airgap: What and How


By performing the steps in this guide, we will install two Software Wallet Electrum on the two different computers and finally create two Wallets with different keystores: the Wallet airgap will use the entire hierarchy of the Wallet HD, while the Wallet display will be generated with the master public key.


These two Wallets will be, in all respects, very different from each other. The only thing they will have in common, as we shall see, are the addresses:


- gW-13 on the airgap computer can only sign but, disconnected from the network, does not know the balance and addresses used;
- the Wallet on the daily computer will only be able to prepare and propagate transactions, without being able to dispose of the expenditure, in the absence of the private keys.


## Preliminary Preparation


To download Electrum, I recommend you follow the first steps in this tutorial:


https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

After downloading always verify the release before installing it, then proceed to "One Server" configuration, as you will find in the help section, under `Start with a Dummy Wallet`.


The "One Server" configuration operation is only necessary for the Wallet installed on the daily computer, as the other computer will always be offline.


The following operations involve practicing on two different computers (and Wallets), so-for convenience and focus-I chose to set the Wallet airgap with the light theme, while the Wallet display has the dark theme.


## Wallet Airgap Creation


After downloading and verifying the download of Electrum, take a copy of the executable and bring it to your computer offline. Then launch it and install Electrum.


Double-click to start Electrum: the computer where you will use this Wallet is offline, ignore the network settings and go to the creation of the Wallet which, in this guide, we will call `airgap`.


![image](assets/en/01.webp)


Choose _Standard wallet_.


![image](assets/en/02.webp)


And then select _Create a new seed_ to have the software generate the mnemonic.


![image](assets/en/03.webp)


Accurately transcribe the 12 generate words from Electrum onto a paper backing and proceed with the verification step, re-entering the words in order when Electrum requests it.


![image](assets/en/04.webp)


![image](assets/en/05.webp)


After the Wallet creation is complete, set a complex password (`Strong`) to encrypt the Wallet file on the airgap device. This step is very delicate and important, as the password chosen now, prevents access to the Wallet which has dispositive power, being able to spend funds sign transactions.


![image](assets/en/06.webp)


By clicking _Finish_ the Wallet is defined and appears on the screen. Of course, the network connection indicator, i.e., the colored dot in the lower right corner, is red, as the computer is disconnected and does not allow Wallet to expose the online keys.


![image](assets/en/07.webp)


## Creation Wallet of Visualization


Now that your Wallet has offline private keys, you need to set up a display Wallet, or `watch-only`, which will allow you to view the balance, as well as prepare receipt transactions to continue to accumulate Sats safely.


From the Wallet located on the offline device, choose the _Wallet_ -> _Information_ menu


![image](assets/en/08.webp)


The window containing all your Wallet information will appear, where you can check `derivation path` and `master fingerprint`, for example to mark them next to the words in the mnemonic sentence (strongly recommended).


![image](assets/en/09.webp)


Remember that you are taking this data from an unconnected computer, so you will have to copy/paste the `zpub` to a text file and save it to a usb stick.


Now you can move to the computer connected to the Internet, to launch Electrum and create a new Wallet.


From the _File_ menu, choose _New/Restore_.


![image](assets/en/10.webp)


The new Wallet is view-only, so for this guide we will call it `watch-only`.


![image](assets/en/12.webp)


On the next screen choose _Standard wallet_ and proceed by clicking _Next_.


![image](assets/en/13.webp)


In choosing the `Keystore` be careful: to create the display Wallet select _Use a master key_. Then proceed with _Next_.


![image](assets/en/14.webp)


Paste here the `zpub` copied from Wallet offline and which you brought to this computer via usb media.


![image](assets/en/15.webp)


Conclude by setting a strong password for this Wallet as well, possibly different from the one chosen for its corresponding Cold.


You will see the display Wallet appear, with a warning. The message reminds you that this is a display-only Wallet and that you cannot, with it, spend the associated funds.


**Note Well**: **you will therefore need to always possess the private keys to dispose of the UTXOs of this Wallet**. With a good backup system, it will not be difficult for you to remain in full possession of your Bitcoins.


![image](assets/en/16.webp)


This warning will appear every single time you open this Wallet. Click _Ok_ and let's move on to the verification step.


## Verification of the Two Wallet


As we learned at the beginning of this guide, a Wallet airgap and its display Wallet are two wallets that have different faculties but **share the same addresses**.


If we look at the two Wallets side by side, visually we notice that in the Wallet airgap there is a "seed" symbol, while in the watch-only there is not. Even this detail will help you remember that the Wallet display Wallet does not have private keys.


![image](assets/en/17.webp)


To make an accurate first check, however, select in both Wallets the `Addresses` menu: since they share the same addresses, the list of addresses should be identical for both.


![image](assets/en/18.webp)


⚠️ **ATTENTION**: **there can be no middle ground; the addresses must be the same. In case they are different, it is necessary to delete all the work done so far and start over**.


Now you can proceed to do two different checks. First, try deleting the two Wallets and restoring them from scratch, each on the appropriate computer. In case you proceed to do this verification, the procedures for the display Wallet are identical to those set out above.


For the Wallet airgap, however, on the `keystore` screen you will have to choose _I already have a seed_ and enter the words by copying them from your paper backup.


After the "no-load" trial is over, you can try to make a transaction of a small amount and spend it immediately.


## Receiving and Spending Transactions


To begin using your Electrum airgap, you can make a receipt transaction with a small amount, then spend it toward an address of your own. You can then familiarize yourself with the procedure, verifying that you are in full control of the funds.


**Note**: I do not recommend that you deposit a large amount of funds on Wallet before you are confident that you can perform all operations smoothly.


The steps explained below may, at first glance, seem complicated. Don't let this get you down: when you have given them your first try, you will find that they take only a few minutes to complete.


To receive funds, you must necessarily use the display Wallet located on your computer connected to the Internet. From the `Receive` menu click on _Create request_ to have Electrum generate the first available address and use it to send us a few Satss.


![image](assets/en/19.webp)


![image](assets/en/20.webp)


Once the transaction has been propagated you can already see that-as is natural- it is visible only on the display Wallet and not on the Wallet airgap.


![image](assets/en/21.webp)


After your transaction has received some confirmation, you can prepare the expense and thus try the signing procedure from the Wallet out-of-network. Then prepare the transaction on the watch-only and press _Preview_ to check it


![image](assets/en/22.webp)


You get the advanced transaction window where you can see that:


- the transaction is not signed (`Status: Unsigned);
- `Sign` and `Broadcast` commands are inhibited.


The only thing you can do is to export the transaction as is, to take it to the Wallet airgap and sign it.


Introduce a USB flash drive into your computer and, from the menu at the bottom left, choose _Share_.


![image](assets/en/23.webp)


After that select _Save to file_.


![image](assets/en/24.webp)


Save the transaction to the usb stick.


You will notice that Electrum gives the file a name bearing the first digits of transaction ID, and the file extension is `.PSBT`, meaning `Partially Signed Bitcoin Transaction`.


Extract the media with the `.PSBT` file and connect it to the computer offline.


From the Wallet airgap, now choose the _Tools_ menu, then _Load transaction_ and following From file_.


![image](assets/en/25.webp)


With the file manager, choose `.PSBT` from its location.


![image](assets/en/29.webp)


The off-network computer software will automatically open the advanced transaction window, completely identical to how you saw it on the Wallet display. The status is `Unsigned`, but the difference is that the `Sign` command here is active. And that is precisely what you will have to execute.


![image](assets/en/26.webp)


![image](assets/en/27.webp)


Now that the transaction is signed, remember that your Wallet is on an offline machine. Therefore-even if you see the `Broadcast` command active-your Wallet will not be able to propagate the transaction to the Bitcoin network.


What you need to do now is to repeat the operation of exporting the signed transaction to the usb stick, so that you can import it to a computer connected to the Internet and propagate it.


From the bottom left menu, choose _Share_ again and then _Save to file_.


![image](assets/en/28.webp)


Now the file has a different extension: **instead of `.PSBT` now the transaction has extension `.txn`. From now on this is how Electrum will let you recognize signed transactions from unsigned ones**.


![image](assets/en/30.webp)


For the final propagation of the transaction, take the usb stick out of the off-line computer and insert it into the computer connected to the Internet.


From the watch-only, repeat the import procedure, that is, from the _Tools_ menu select _Load transaction_ and finally _From file_.


![image](assets/en/31.webp)


Electrum will open the transaction window for you, markedly different from the one shown earlier on this Wallet, in that it is now signed (`Status: Signed`) and the `Broadcast` command accessible.


The last operation you need to do is just that:


![image](assets/en/32.webp)


## Conclusions


Your tests are now finished. If you followed the guide and got the same results, you have created a Wallet Cold with Electrum, on two different computers, which you can use in airgap fashion to store your Bitcoins.


The only things you will have to pay close attention to are two:

1) **never use Wallet airgap to generate receiving addresses**. Since it is offline, it will always offer you the first address, which coincides with the one you just used to make the test transaction;


![image](assets/en/33.webp)


_As you can see from the image above, the offline Wallet does not know its own address history. It is totally blind in this respect. **The only task it can do for you is to store your offline keys and sign your transactions**_.


2) Use a USB flash drive dedicated only for this purpose, **don't use a medium you use frequently**. Everyday tools are more likely to be cyber-attacked, and unintentionally, you could attack even the computer you are keeping disconnected from the network. A USB stick that you use only for this purpose has very few opportunities to make contact with your PC online, especially if you are a hodler who doesn't have to spend, thus reducing the likelihood of receiving and then transmitting viruses, malware, etc.