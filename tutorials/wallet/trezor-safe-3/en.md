---
name: Trezor Safe 3
description: Configuring and using Hardware Wallet Safe 3
---
![cover](assets/cover.webp)


*Image credit: [Trezor.io](https://trezor.io/)*


The Trezor Safe 3 is a Hardware Wallet designed by SatoshiLabs and created in 2023. It's a very compact, lightweight model (14 grams) designed for both beginners and intermediate users. It is the successor to the famous Model One, with significant additions, while retaining the brand's open-source approach that sets it apart from its main competitor, Ledger. The Safe 3 is priced at €79. It is therefore positioned in the mid-range hardware wallet segment, in direct competition with the Ledger Nano S Plus.


The Safe 3 has no battery and operates exclusively via a USB-C connection, used for both power and communication. It features a small 0.96-inch monochrome OLED display and two physical buttons.


![Image](assets/fr/01.webp)


The Safe 3 offers all the essential features expected of a good Hardware Wallet, including excellent integration of the passphrase BIP39. However, it does not yet support Miniscript.


This model is particularly suitable for beginners, and might even be the Hardware Wallet I'd recommend to a new user. It's also well suited to intermediate users. On the other hand, it may not meet all the expectations of advanced users looking for more specific features, available on devices like the Coldcard. Nevertheless, if you don't need these advanced options, the Trezor Safe 3 may be an excellent choice.


## The Trezor Safe 3 safety model


The Trezor Safe 3 is now equipped with an EAL6+ certified **Secure Element**, a significant advance on previous models such as the Model One and Model T. This is the OPTIGA Trust M V3 chip, which does not directly store the seed, but acts as a cryptographic component to secure access to it. The Secure Element retains a secret that can only be accessed once the user has entered the PIN correctly. This secret is then used to decrypt the seed, which is stored encrypted in the device's main memory.


This hybrid security system offers improved physical protection, notably against extraction attacks or invasive analysis, problems to which the Model One was prone, particularly in PIN management. These vulnerabilities are now circumvented thanks to the use of the Secure Element. This model also maintains an open-source software architecture: the code that manages the generation and use of private keys remains fully accessible and verifiable. The OPTIGA chip manages only the PIN code, an element external to Bitcoin wallet key management. It only releases a secret that can be used to decrypt the seed. Also, the OPTIGA Trust M V3 chip benefits from a relatively free license, which authorizes SatoshiLabs to freely publish potential vulnerabilities.


This security model represents, in my opinion, one of the best compromises available on the market today. It combines the advantages of a Secure Element with open-source software management. Previously, users had to choose between enhanced physical security with a chip and transparency with open-source; with Trezor Safe 3, it's possible to benefit from both.


In this tutorial, we'll show you how to set up and use your Trezor Safe 3 securely.


## Unboxing the Trezor Safe 3


When you receive your Safe 3, make sure the box and seal are intact to confirm that the package has not been opened. A software verification of the device's authenticity and integrity will also be carried out when it is set up later.


Box contents include :


- Trezor Safe 3;
- A pouch containing cardstock to record your mnemonic phrase, stickers, and instructions;
- USB-C to USB-C cable.


![Image](assets/fr/02.webp)


When opened, your Trezor Safe 3 should be protected by a protective plastic and the USB-C port should be secured by a holographic seal. Make sure it's there.


![Image](assets/fr/03.webp)


Navigation on the device is straightforward: use the right button to scroll to the right, and the left button to scroll to the left. Press both buttons simultaneously to confirm an action.


![Image](assets/fr/04.webp)


## Prerequisites


For this tutorial, I'm going to show you how to use the Trezor Safe 3 with [Sparrow Wallet wallet management software](https://sparrowwallet.com/download/). If you haven't already installed this software, please do so now. If you need help, we also have a detailed tutorial on configuring Sparrow Wallet :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

You'll also need the Trezor Suite software to configure the Safe 3, check its authenticity and install the firmware. We'll only be using this software for that, and afterwards it will only be needed for firmware updates. For day-to-day management of the wallet, we'll be using Sparrow Wallet exclusively, as it's optimized for Bitcoin and easy to use, even for beginners (Sparrow only supports Bitcoin, not altcoins).


[Download Trezor Suite from the official website](https://trezor.io/trezor-suite)


![Image](assets/fr/05.webp)


For both these programs, I strongly recommend that you check both their authenticity (with GnuPG) and their integrity (via Hash) before installing them on your machine. If you don't know how to do this, you can follow this other tutorial :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Starting Trezor Safe 3


Connect your Safe 3 to your computer where Trezor Suite and Sparrow Wallet are already installed.


![Image](assets/fr/06.webp)


Open Trezor Suite, then click on "*Set up my Trezor*".


![Image](assets/fr/07.webp)


Select "*Bitcoin-only firmware*", then click on "*Install Bitcoin-only*".


![Image](assets/fr/08.webp)


Trezor Suite will then install the firmware on your Safe 3. Please wait during installation.


![Image](assets/fr/09.webp)


Click on "*Continue*".


![Image](assets/fr/10.webp)


Then proceed to the authenticity test to make sure your Hardware Wallet is not fake or compromised.


![Image](assets/fr/11.webp)


On your Safe 3, press the right button to confirm.


![Image](assets/fr/12.webp)


If your Trezor is genuine, a confirmation message will appear in Trezor Suite.


![Image](assets/fr/13.webp)


You can then skip the windows with the basic operating instructions.


![Image](assets/fr/14.webp)


## Creating a Bitcoin wallet


On Trezor Suite, click on the "*Create new Wallet*" button.


![Image](assets/fr/15.webp)


For a standard wallet, you can opt for the default backup type. This creates a classic single-sig wallet with a 12-word mnemonic phrase. Click on "*Create Wallet*".


If you would like to learn more about the other backup options available on Trezor, including *Multi-share Backup*, I recommend you also consult this tutorial :


https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)


Accept the terms of use on Hardware Wallet.


![Image](assets/fr/17.webp)


Press the right button again to create a new wallet.


![Image](assets/fr/18.webp)


In Trezor Suite, click on "*Continue to backup*".


![Image](assets/fr/19.webp)


The software provides instructions on how to manage your mnemonic phrase.


This mnemonic gives you full, unrestricted access to all your bitcoins. Anyone in possession of this phrase can steal your funds, even without physical access to your Trezor Safe 3.


The 12-word phrase restores access to your bitcoins in the event of loss, theft or breakage of your Hardware Wallet. It is therefore very important to save it carefully and store it in a safe place.


You can write it on the cardboard supplied in the box, or for added security, I recommend engraving it on a stainless steel base to protect it from fire, flood or collapse.


Confirm the instructions, then click on the "*Create Wallet backup*" button.


![Image](assets/fr/20.webp)


Safe 3 will create your mnemonic phrase using its random number generator. Make sure you're not being watched during this operation. Write down the words provided on the screen on the physical medium of your choice. Depending on your security strategy, you may consider making several complete physical copies of the phrase (but above all, don't divide it). It's important to keep the words numbered and in sequential order.


***Obviously, you must never share these words on the Internet, as I do in this tutorial. This example wallet will be used only on the Testnet and will be deleted at the end of the tutorial


For more information on the proper way to save and manage your mnemonic phrase, I highly recommend following this other tutorial, especially if you're a beginner:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)


To move on to the next words, right-click. You can go backwards by clicking on the left button. Once you've written down all the words, hold down the right button to move on to the next step.


![Image](assets/fr/22.webp)


Select the words in your mnemonic phrase according to their order to confirm that you've written them down correctly. Use the left and right buttons to navigate between proposals, then select the correct word by clicking on the 2 buttons simultaneously.


![Image](assets/fr/23.webp)


Once this verification procedure is complete, click on the button on the right.


![Image](assets/fr/24.webp)


## Setting the PIN code


Next comes the PIN code step. The PIN code unlocks your Trezor. It therefore provides protection against unauthorized physical access. This PIN code is not involved in the derivation of your wallet's cryptographic keys. So even without access to the PIN code, possession of your 12-word mnemonic phrase will enable you to regain access to your bitcoins.


On Trezor Suite, click on "*Continue to PIN*", then on the "*Set PIN*" button.


![Image](assets/fr/25.webp)


Confirm with Safe 3.


![Image](assets/fr/26.webp)


We recommend choosing a PIN code that is as random as possible. Be sure to save this code in a separate location from where your Trezor is stored (e.g. in a password manager). You can define a PIN code of between 8 and 50 digits. I recommend that you choose a PIN code as long as possible to enhance security.


Use the left and right buttons to select each digit. To confirm your choice and move on to the next digit, press both buttons simultaneously.


![Image](assets/fr/27.webp)


When finished, click on the "*ENTER*" checkmark at the beginning of the digits, then confirm your PIN a second time.


![Image](assets/fr/28.webp)


Your PIN code has been registered.


![Image](assets/fr/29.webp)


On Trezor Suite, click on the "*Complete setup*" button.


![Image](assets/fr/30.webp)


The configuration of your Safe 3 is now complete. If you wish, you can change the name and home page of your Hardware Wallet.


![Image](assets/fr/31.webp)


We won't be needing the Trezor Suite software any more, except to perform regular firmware updates on your Hardware Wallet, or if you'd like to run a recovery test. We're now going to use Sparrow to manage the wallet, as this software is perfectly suited to Bitcoin-only use.


## Setting up the wallet on Sparrow Wallet


Start by downloading and installing Sparrow Wallet [from the official website](https://sparrowwallet.com/) on your computer, if you haven't already done so.


Once you've opened Sparrow Wallet, make sure that the software is connected to a Bitcoin node, which is indicated by the tick in the bottom right-hand corner of the Interface. If you're having trouble connecting Sparrow, I recommend that you read the beginning of this tutorial:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Click on the "*File*" tab, then on "*New Wallet*".


![Image](assets/fr/32.webp)


Name your wallet, then click on "*Create Wallet*".


![Image](assets/fr/33.webp)


In the "*Script Type*" drop-down menu, select the type of script that will be used to secure your bitcoins. I recommend "*Taproot*", or failing that, "*Native SegWit*".


![Image](assets/fr/34.webp)


Click on the "*Connected Hardware Wallet*" button. Your Safe 3 must of course be connected to the computer and unlocked.


![Image](assets/fr/35.webp)


Click on the "*Scan*" button. Your Safe 3 should appear. Click on "*Import Keystore*".


![Image](assets/fr/36.webp)


You can now see the details of your wallet, including the extended public key of your first account. Click on the "*Apply*" button to finalize wallet creation.


![Image](assets/fr/37.webp)


Choose a strong password to secure access to Sparrow Wallet. This password will ensure secure access to your Sparrow wallet data, protecting your public keys, addresses, labels and transaction history from unauthorized access.


I advise you to save this password in a password manager so you don't forget it.


![Image](assets/fr/38.webp)


And now your wallet has been imported into Sparrow Wallet!


![Image](assets/fr/39.webp)


Before you receive your first bitcoins in your wallet, **I strongly advise you to perform an empty recovery test**. Write down some reference information, such as your xpub, then reset your Trezor Safe 3 while the wallet is still empty. Then try to restore your wallet on the Trezor using your paper backups. Check that the xpub generated after the restore matches the one you originally wrote down. If it does, you can rest assured that your paper backups are reliable.


To learn more about how to perform a recovery test, I suggest you consult this other tutorial:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## How can I receive bitcoins with Trezor Safe 3?


On Sparrow, click on the "*Receive*" tab.


![Image](assets/fr/40.webp)


Before using the address proposed by Sparrow Wallet, check it on your Trezor's screen. This practice allows you to confirm that the address displayed on Sparrow is not fraudulent, and that the Hardware Wallet does indeed hold the private key needed to subsequently spend the bitcoins secured with this address. This helps you to avoid several types of attack.


To perform this check, click on the "*Display Address*" button.


![Image](assets/fr/41.webp)


Check that the address displayed on your Trezor matches the one on Sparrow Wallet. It's also advisable to carry out this check just before communicating your address to the sender, to be sure of its validity. You can use the buttons to confirm.


![Image](assets/fr/42.webp)


You can then add a "*Label*" to describe the source of bitcoins that will be secured with this address. This is a good practice that allows you to better manage your UTXOs.


![Image](assets/fr/43.webp)


You can then use this address to receive bitcoins.


![Image](assets/fr/44.webp)


## How do I send bitcoins with Trezor Safe 3?


Now that you've received your first Satss on your Safe 3-secured wallet, you can spend them too! Connect your Trezor to your computer, unlock it using the PIN code, launch Sparrow Wallet, then go to the "*Send*" tab to build a new transaction.


![Image](assets/fr/45.webp)


If you wish to *Coin Control*, i.e. choose specifically which UTXOs to consume in the transaction, go to the "*UTXOs*" tab. Select the UTXOs you wish to spend, then click on "*Send Selected*". You will be redirected to the same screen in the "*Send*" tab, but with your UTXOs already selected for the transaction.


![Image](assets/fr/46.webp)


Enter the destination address. You can also enter multiple addresses by clicking on the "*+ Add*" button.


![Image](assets/fr/47.webp)


Write down a "*Label*" to remember the purpose of this expense.


![Image](assets/fr/48.webp)


Select the amount to be sent to this address.


![Image](assets/fr/49.webp)


Adjust the fee rate of your transaction according to the current market. For example, you can use [Mempool.space](https://Mempool.space/) to choose a suitable fee rate.


Make sure all your transaction parameters are correct, then click on "*Create Transaction*".


![Image](assets/fr/50.webp)


If everything is to your satisfaction, click on "*Finalize Transaction for Signing*".


![Image](assets/fr/51.webp)


Click on "*Sign*".


![Image](assets/fr/52.webp)


Click on "*Sign*" next to your Trezor Safe 3.


![Image](assets/fr/53.webp)


Check the transaction parameters on your Hardware Wallet screen, including the recipient's receiving address, the amount sent and the charge. Once the transaction has been verified on the Trezor, click on both buttons simultaneously to sign it.


![Image](assets/fr/54.webp)


Your transaction is now signed. Check one last time that everything is OK, then click on "*Broadcast Transaction*" to broadcast it on the Bitcoin network.


![Image](assets/fr/55.webp)


You can find it in the "*Transactions*" tab of Sparrow Wallet.


![Image](assets/fr/56.webp)


Congratulations, you're now up to speed on the basic use of the Trezor Safe 3 with Sparrow Wallet! To take things a step further, I recommend this comprehensive tutorial on using a Hardware Wallet Trezor with a passphrase BIP39 to enhance your safety:


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!