---
name: Jade - Electrum
description: How to use your Jade or Jade Plus with Electrum (desktop)
---

![cover](assets/cover.webp)


_This guide is taken from a [Bitcoin Workshops lesson](https://officinebitcoin.it/lezioni/jadeele/index.html)_


The tutorial is made with Jade Classic, but the operations are also valid for those who have Jade Plus.


After initializing Jade, you can start using it and--to do so--choose a wallet display.


Jade is a device that can be used with several wallet, or companion apps as Blockstream specifies them on its site.


In this tutorial you will see the steps for using Electrum Wallet, via USB cable connection.


## Public key transfer


Take and turn on your initialized Jade. As soon as you turn it on it looks like this:



![img](assets/en/32.webp)


If you select _Unlock Jade_, you will get the menu where you have to choose how to connect your device to the companion app.


With Electrum you can only connect Jade via USB, so choose this method.


Launch Electrum, which will open proposing as a default option to open the last wallet used.


If this is the first time you are connecting Jade to Electrum, select _Create New Wallet_ and then _Finish_.


![img](assets/en/34.webp)


Name wallet.


![img](assets/en/35.webp)


Select Standard Wallet.


![img](assets/en/36.webp)


When choosing the keystore, it is essential to select _Use a hardware device_.


![img](assets/en/37.webp)


Electrum starts scanning for the hardware device.


![img](assets/en/38.webp)


By connecting USB to the computer (already connected on the USB C side to Jade), the wallet hardware appears to you in lock mode. Jade unlocks by putting in the six-digit PIN set during setup.



![img](assets/en/39.webp)


Unlocked Hardware device, Electrum detects Jade. Continue by clicking _Next_.


![img](assets/en/40.webp)


At this point Electrum asks you to set the policy script: choose _Native Segwit_.


![img](assets/en/41.webp)


The phase of public key transfer from wallet from Jade to display Electrum begins.


When the public key export is completed, the process is finished.


The watch-only is ready and Electrum alerts of completion with the following screen.


![img](assets/en/42.webp)


wallet is actually created and you can start exploring it: you can see the _addresses_, the _wallet information_, and-most importantly-you can see in the lower right-hand corner the indication that it is Blockstream's device. The green dot next to the Blockstream logo indicates that the device is turned on and properly connected to the local network.


![img](assets/en/43.webp)


## Receiving and spending transactions


From the _Receive_ menu of Electrum, generate a `scriptPubKey` (address) to receive funds. Always start with a small amount and do a receive+spend test.


![img](assets/en/44.webp)


Having received satss, you can check their arrival in the _History_ menu.


![img](assets/en/45.webp)


![img](assets/en/46.webp)


Once the transaction is confirmed, you can spend this UTXO and finish the test.


The expense involves using Jade to sign.


Go to the _Send_ menu of Electrum, paste a scriptPubKey, and check it well.


![img](assets/en/47.webp)


When finished, press _Pay_.


The transaction window opens, in which it is important to set the correct transaction fees. When you have finished all the settings click on _Preview_ in the lower right corner.


![img](assets/en/48.webp)


The transaction window shows some important details, first and foremost the status: `Unsigned`.


At this stage you can also see the _Sign_ command, which you must click to affix the signature with Jade.


![img](assets/en/49.webp)


Now begins a communication phase between the display wallet and the hardware device, in which Electrum alerts you to follow the instructions on the hardware device, turned on and ready to sign.


![img](assets/en/50.webp)


**First, though, you'd better verify what you're signing: all the parameters of the transaction you just set up, also appear on Jade** and you can verify them all.


![img](assets/en/51.webp)


To continue make sure you always place the cursor on the `→` arrow that leads to the next steps and never on the `X` unless you want to end the operation without completing it.


The verification part ends with the fee display. At this point confirmation is equivalent to putting your signature.


![img](assets/en/52.webp)


For a brief moment Jade processes the operation, when it is finished it returns to the home menu.


![img](assets/en/53.webp)


While on Electrum you can see the status of the transaction, which has changed from `Unsigned` to `Signed` and now it is possible, for you, to propagate it by clicking _Broadcast_.


![img](assets/en/54.webp)


wallet, thus tested, can be used to receive UTXO intended for safe storage.


![img](assets/en/55.webp)


This guide is an example of how to use your Jade, connected via USB, to a wallet watch-only. Electrum is a classic example, but you may prefer other wallet software. Jade exports the public key to many other wallets: find the similar functions you read about in this tutorial, to guide you and find how to employ it your favorite companio app.