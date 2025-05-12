---
name: Trezor Model One
description: Setting up and using the Hardware Wallet Model One
---
![cover](assets/cover.webp)


*Image credit: [Trezor.io](https://trezor.io/)*


The Trezor Model One is the very first Hardware Wallet ever released, launched in 2014 by SatoshiLabs. After more than ten years in existence, it remains an interesting choice, particularly for users looking for a Hardware Wallet that's accessible both technically and in terms of budget. In fact, it's priced at €49 on the official Trezor website. It's one of the only hardware wallets in this price range. It lies midway between entry-level devices at around €20, such as the Tapsigner, which often lack a screen, and mid-range devices at around €80, such as the Ledger Nano S Plus or the Trezor Safe 3.


The Model One features a 0.96-inch monochrome OLED display and two physical buttons. It operates without a battery, using only a micro-USB connection for power and data exchange.


![Image](assets/fr/01.webp)


The main drawback of the Model One is its lack of Secure Element, which makes it vulnerable to a variety of physical attacks, some of which are relatively simple to execute. These attacks can include the analysis of auxiliary channels to determine the device PIN, or more advanced techniques to extract the encrypted seed in order to brute-force it later. Note that these attacks require physical access to the device. However, this vulnerability can be considerably reduced by using a solid passphrase BIP39. If you opt for this Hardware Wallet, I strongly advise you to configure a passphrase.


The Model One offers two important advantages:


- It is based on a completely open-source architecture. Unlike more recent models with Secure Element, all Model One hardware and software components are auditable;
- It is equipped with a screen. To my knowledge, this is the only Hardware Wallet on the market in this price range with a display. This is a very important feature, as it enables signed information and reception addresses to be verified, thus preventing many digital attacks.


The Trezor Model One may therefore represent a wise choice for beginners and intermediate users on a limited budget. However, it's important to remain aware of its limitations in terms of physical protection, due to the absence of Secure Element. If your budget is limited, this is a good option, but if you can afford to opt for a superior model, such as the Trezor Safe 3 at €79, it's preferable, as it includes a Secure Element.


## Unboxing the Trezor Model One


When you receive your Model One, make sure the box and seal are intact to confirm that the package has not been opened. A software verification of the device's authenticity and integrity will also be carried out when it is set up later.


Box contents include :


- The Trezor Model One;
- Cardstock to record your mnemonic phrase, stickers and instructions;
- USB-A to micro-USB cable.


![Image](assets/fr/02.webp)


Navigating the device is very simple:


- Right-click to confirm and proceed to the next steps;
- Use the left button to go back.


## Prerequisites


For this tutorial, I'm going to show you how to use the Trezor Model One with [Sparrow Wallet portfolio management software](https://sparrowwallet.com/download/). If you haven't yet installed this software, please do so now. If you need help, we also have a detailed tutorial on configuring Sparrow Wallet :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

You'll also need the Trezor Suite software to configure the Model One, check its authenticity and install the firmware. We'll only be using this software for that, and afterwards it will only be needed for firmware updates. For day-to-day management of the wallet, we'll be using Sparrow Wallet exclusively, as it's optimized for Bitcoin and easy to use, even for beginners (Sparrow only supports Bitcoin, not altcoins).


[Download Trezor Suite from the official website](https://trezor.io/trezor-suite)


![Image](assets/fr/03.webp)


For both these programs, I strongly recommend that you check both their authenticity (with GnuPG) and their integrity (via Hash) before installing them on your machine. If you don't know how to do this, you can follow this other tutorial :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Starting the Trezor Model One


Connect your Model One to your computer where Trezor Suite and Sparrow Wallet are already installed.


![Image](assets/fr/04.webp)


Open Trezor Suite, then click on "*Set up my Trezor*".


![Image](assets/fr/05.webp)


Select "*Bitcoin-only firmware*", then click on "*Install Bitcoin-only*".


![Image](assets/fr/06.webp)


Trezor Suite will then install the firmware on your Model One. Please wait during installation.


![Image](assets/fr/07.webp)


Click on "*Continue*".


![Image](assets/fr/08.webp)


## Creating a Bitcoin portfolio


On Trezor Suite, click on the "*Create new Wallet*" button.


![Image](assets/fr/09.webp)


Accept the terms of use on the Hardware Wallet.


![Image](assets/fr/10.webp)


In Trezor Suite, click on "*Continue to backup*".


![Image](assets/fr/11.webp)


The software provides instructions on how to manage your mnemonic phrase.


This mnemonic gives you full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to your Trezor Model One.


The 24-word phrase restores access to your bitcoins in the event of loss, theft or breakage of your Hardware Wallet. It is therefore very important to save it carefully and store it in a safe place.


You can write it on the cardboard supplied in the box, or for added security, I recommend engraving it on a stainless steel base to protect it from fire, flood or collapse.


Confirm the instructions, then click on the "*Create Wallet backup*" button.


![Image](assets/fr/12.webp)


The Model One will create your mnemonic phrase using its random number generator. Make sure you're not being watched during this operation. Write down the words provided on the screen on the physical medium of your choice. Depending on your security strategy, you may consider making several complete physical copies of the phrase (but above all, don't divide it). It's important to keep the words numbered and in sequential order.


***Obviously, you must never share these words on the Internet, as I do in this tutorial. This example wallet will be used only on the Testnet and will be deleted at the end of the tutorial


For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

To move on to the next words, right-click. Once you've written down all the words, click the right button again to move on to the next step.


![Image](assets/fr/13.webp)


Your Hardware Wallet again shows you all your words. Check that you've written them all down.


![Image](assets/fr/14.webp)


## Setting the PIN code


Next comes the PIN code step. The PIN code unlocks your Trezor. It therefore provides protection against unauthorized physical access. This PIN code is not involved in the derivation of your wallet's cryptographic keys. So even without access to the PIN code, possession of your 12-word mnemonic phrase will enable you to regain access to your bitcoins.


On Trezor Suite, click on "*Continue to PIN*", then on the "*Set PIN*" button.


![Image](assets/fr/15.webp)


Confirm on the Model One.


![Image](assets/fr/16.webp)


We recommend choosing a PIN code that is as random as possible. Be sure to save this code in a separate location from where your Trezor is stored (e.g. in a password manager). You can define a PIN code of between 8 and 50 digits. I recommend that you choose a PIN code as long as possible to enhance security.


The PIN code must be entered in Trezor Suite on your computer by clicking on the dots corresponding to the digits, according to the keyboard configuration displayed on the Trezor Model One.


This specific PIN entry method is required every time you unlock your Trezor Model One, whether via Trezor Suite or Sparrow Wallet.


![Image](assets/fr/17.webp)


Once finished, click on the "*Enter PIN*" button.


![Image](assets/fr/18.webp)


Write down your PIN again to confirm.


![Image](assets/fr/19.webp)


On Trezor Suite, click on the "*Complete setup*" button.


![Image](assets/fr/20.webp)


The configuration of your Model One is now complete. If you wish, you can change the name and home page of your Hardware Wallet.


![Image](assets/fr/21.webp)


We won't be needing the Trezor Suite software any more, except to carry out regular firmware updates on your Hardware Wallet, or if you'd like to run a recovery test. We're now going to use Sparrow to manage the portfolio, as this software is perfectly suited to Bitcoin-only use.


## Setting up the portfolio on Sparrow Wallet


Start by downloading and installing Sparrow Wallet [from the official website](https://sparrowwallet.com/) on your computer, if you haven't already done so.


Once you've opened Sparrow Wallet, make sure that the software is connected to a Bitcoin node, which is indicated by the tick in the bottom right-hand corner of Interface. If you're having trouble connecting Sparrow, I recommend you consult the beginning of this tutorial:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Click on the "*File*" tab, then on "*New Wallet*".


![Image](assets/fr/22.webp)


Name your portfolio, then click on "*Create Wallet*".


![Image](assets/fr/23.webp)


In the "*Script Type*" drop-down menu, select the type of script that will be used to secure your bitcoins. I recommend "*Taproot*", or failing that, "*Native SegWit*".


![Image](assets/fr/24.webp)


Click on the "*Connected Hardware Wallet*" button. Your Model One must of course be connected to the computer.


![Image](assets/fr/25.webp)


Click on the "*Scan*" button. Your Model One should appear.


When you connect your Model One to a computer with Sparrow Wallet open, you will then be prompted to enter a passphrase BIP39 on Sparrow. This advanced option will be covered in a future tutorial. For now, you can simply select "*Toggle passphrase Off*" to prevent your Trezor from prompting you to enter a passphrase every time you start up.


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)


Click on "*Import Keystore*".


![Image](assets/fr/27.webp)


You can now see the details of your wallet, including the extended public key of your first account. Click on the "*Apply*" button to finalize wallet creation.


![Image](assets/fr/28.webp)


Choose a strong password to secure access to Sparrow Wallet. This password will ensure secure access to your Sparrow wallet data, protecting your public keys, addresses, labels and transaction history from unauthorized access.


I advise you to save this password in a password manager so you don't forget it.


![Image](assets/fr/29.webp)


And now your portfolio has been imported into Sparrow Wallet!


![Image](assets/fr/30.webp)


Before you receive your first bitcoins in your wallet, **I strongly advise you to perform an empty recovery test**. Write down some reference information, such as your xpub, then reset your Trezor Model One while the wallet is still empty. Then try to restore your wallet on the Trezor using your paper backups. Check that the xpub generated after the restore matches the one you originally wrote down. If it does, you can rest assured that your paper backups are reliable.


To learn more about how to perform a recovery test, I suggest you consult this other tutorial:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## How to receive bitcoins with the Trezor Model One?


On Sparrow, click on the "*Receive*" tab.


![Image](assets/fr/31.webp)


Before using the address proposed by Sparrow Wallet, check it on your Trezor's screen. This practice allows you to confirm that the address displayed on Sparrow is not fraudulent, and that the Hardware Wallet does indeed hold the private key needed to subsequently spend the bitcoins secured with this address. This helps you to avoid several types of attack.


To perform this check, click on the "*Display Address*" button.


![Image](assets/fr/32.webp)


Check that the address displayed on your Trezor matches the one on Sparrow Wallet. It's also advisable to carry out this check just before communicating your address to the sender, to be sure of its validity. You can press the right button to confirm.


![Image](assets/fr/33.webp)


You can also add a "*Label*" to describe the source of bitcoins that will be secured with this address. This is a good practice that allows you to better manage your UTXOs.


![Image](assets/fr/34.webp)


You can then use this address to receive bitcoins.


![Image](assets/fr/35.webp)


## How to send bitcoins with the Trezor Model One?


Now that you've received your first Satss in your Model One-secured wallet, you can spend them too! Connect your Trezor to your computer, launch Sparrow Wallet, then go to the "*Send*" tab to build a new transaction.


![Image](assets/fr/36.webp)


If you wish to *Coin Control*, i.e. choose specifically which UTXOs to consume in the transaction, go to the "*UTXOs*" tab. Select the UTXOs you wish to spend, then click on "*Send Selected*". You will be redirected to the same screen in the "*Send*" tab, but with your UTXOs already selected for the transaction.


![Image](assets/fr/37.webp)


Enter the destination address. You can also enter multiple addresses by clicking on the "*+ Add*" button.


![Image](assets/fr/38.webp)


Write down a "*Label*" to remember the purpose of this expense.


![Image](assets/fr/39.webp)


Select the amount to be sent to this address.


![Image](assets/fr/40.webp)


Adjust the fee rate of your transaction according to the current market. For example, you can use [Mempool.space](https://Mempool.space/) to choose a suitable fee rate.


Make sure all your transaction parameters are correct, then click on "*Create Transaction*".


![Image](assets/fr/41.webp)


If everything is to your satisfaction, click on "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Click on "*Sign*".


![Image](assets/fr/43.webp)


Click on "*Sign*" next to your Trezor Model One.


![Image](assets/fr/44.webp)


Check the transaction parameters on your Hardware Wallet screen, including the recipient's receiving address, the amount sent and the fee. Once the transaction has been verified on the Trezor, right-click to sign it.


![Image](assets/fr/45.webp)


Your transaction is now signed. Check one last time that everything is OK, then click on "*Broadcast Transaction*" to broadcast it on the Bitcoin network.


![Image](assets/fr/46.webp)


You can find it in the "*Transactions*" tab of Sparrow Wallet.


![Image](assets/fr/47.webp)


Congratulations, you're now up to speed on the basic use of the Trezor Model One with Sparrow Wallet! To take things a step further, I recommend this comprehensive tutorial on using a Hardware Wallet Trezor with a passphrase BIP39 to reinforce your safety :


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!