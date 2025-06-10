---
name: Trezor Shamir Backup
description: Single-share and multi-share mnemonic phrases on Trezor
---
![cover](assets/cover.webp)


*Image credit: [Trezor.io](https://trezor.io/)*


## New backup options on Trezor


Since 2023, Trezor has been offering a new backup format called ***Single-share Backup***, gradually replacing the classic BIP39-based approach found on most wallets. Unlike traditional 12- or 24-word mnemonic phrases, this new format is based on a single 20-word phrase derived from a standard developed by SatoshiLabs: **SLIP39**. The aim is to improve backup robustness and readability, while enabling smooth migration to a distributed backup model.


This distributed model is called ***Multi-share Backup***. It's based on the same principle, but instead of generating a single mnemonic phrase, it splits it into several fragments called ***shares***, each of which is a mnemonic phrase in its own right. To restore the wallet, a certain number of these *shares* (defined by a *threshold*) must be reunited. For example, in a 3-of-5 scheme, any 3 *shares* out of the 5 will restore the wallet. Please note that Trezor's distributed backup system is different from multisig wallets. To spend your bitcoins, only your Hardware Wallet Trezor is required. Only one signature is required. Distribution applies only at the level of the mnemonic phrase, i.e. the backup.


![Image](assets/fr/01.webp)


This system solves the problem of the single point of failure of the mnemonic phrase without the disadvantages associated with managing a Multisig or passphrase BIP39. The recovery process is no longer based on a single piece of information, but on several, with the added benefit of loss tolerance thanks to the threshold.


Users who have created a wallet with *Single-share Backup* can switch to *Multi-share Backup* at any time without having to migrate their wallet. Receiving addresses and accounts will remain identical. The *Multi-share* system only affects the backup, while the rest of the wallet remains unchanged.


Multi-share Backup* is available on the Trezor Model T, Safe 3 and Safe 5. This feature is not supported by the Trezor Model One.


**Important note:** Trezor's *Multi-share* system is cryptographically secure, as it uses the *Shamir's Secret Sharing* scheme for distribution. We strongly advise against applying a similar system manually, by dividing a classic mnemonic phrase yourself. It's a bad practice that significantly increases the risk of theft and loss of your bitcoins, so don't do it. A classic mnemonic phrase is stored in its entirety.


## Shamir's Secret Sharing in SLIP39


The cryptographic mechanism underlying *Multi-share* backups on Trezor is the *Shamir's Secret Sharing Scheme* (SSSS). Its principle is as follows: secret information (in this case, the seed of the wallet) is transformed into a mathematical polynomial. Several points of this polynomial are then calculated, each of which becomes a share. The original secret is reconstructed by polynomial interpolation, by gathering a minimum number of points (the threshold).


No secret information can be deduced from a number of shares below the threshold, guaranteeing perfect theoretical security of the secret information. In other words, even an attacker with unlimited computing power cannot guess seed if the threshold is not reached.


SLIP39 uses this scheme to distribute the seed wallet. Each share is a 20-word sentence, built from a list of 1024 words (different from the BIP39 list).


## Setting up a Multi-share Backup on a Trezor


When creating your wallet on Trezor, you have three different options:


- Use a classic BIP39 mnemonic phrase of 12 or 24 words;
- Use a single-share mnemonic phrase (SLIP39);
- Configure multiple mnemonic phrases in Multi-share (SLIP39).


If you opt for a Single-share SLIP39 mnemonic phrase, you'll be able to upgrade to a Multi-share at a later date without having to reset the wallet. On the other hand, if you start with a classic BIP39 wallet (12- or 24-word phrase), you won't be able to convert it directly to a Multi-share. You'll have to create a new Multi-share wallet from scratch and transfer your funds from the old wallet to the new one via one or more Bitcoin transactions. This is a more complex and costly operation. If you want to make this migration, I recommend you buy a new Hardware Wallet Trezor to avoid having to enter your seed on a wallet software.


In this tutorial, we'll first look at how to set up a Multi-share when creating a wallet, then, in a subsequent section, we'll see how to convert a Single-share to a Multi-share on an existing wallet.


If you need help with the initial setup of your device, we also have a detailed tutorial for each Trezor model:


https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### On a new wallet


You've now completed the initial configuration of your Trezor and are ready to create the wallet. In Trezor Suite, click on the "*Create new Wallet*" button.


![Image](assets/fr/02.webp)


Choose the "*Multi-share Backup*" option, then click on "*Create Wallet*".


![Image](assets/fr/03.webp)


Accept the terms of use on your Trezor and confirm the creation of the wallet.


![Image](assets/fr/04.webp)


In Trezor Suite, click on "*Continue to backup*".


![Image](assets/fr/05.webp)


Read the instructions carefully, confirm them, then click on "*Create Wallet backup*".


![Image](assets/fr/06.webp)


For more information on the proper way to save and manage your mnemonic phrases, I highly recommend following this other tutorial, especially if you're a beginner:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

On the Trezor, select the total number of shares you wish to configure. The most common configurations are 2-de-3 and 3-de-5. For this example, I'll create a 2-de-3, so I'll select 3 shares. Each share will represent a 20-word mnemonic phrase.


*For Safe 5 users, although the screen will say "*Tap to continue*", you'll actually need to swipe up to confirm


![Image](assets/fr/07.webp)


Then confirm the threshold, i.e. the number of shares required to regain access to the wallet and the bitcoins it contains.


![Image](assets/fr/08.webp)


The Trezor will create your various shares (mnemonic phrases) using its random number generator. Make sure you're not being watched during this operation. Write down the words provided on the screen on the physical medium of your choice. It's important to keep the words numbered and in sequential order.


I recommend that you note down each share on a separate medium and carefully manage their storage to avoid several being accessible in the same place. For example, for a 2-of-3 configuration like mine, one option would be to keep one share at my home, another with a trusted friend, and the last in a bank safe. The choice of storage locations will depend on your personal security strategy.


You can see at the top of the screen which share you are currently viewing.


of course, you must never share these words on the Internet, as I'm doing in this tutorial. This example wallet will be used only on the Testnet and will be deleted at the end of the tutorial.**_


![Image](assets/fr/09.webp)


To move on to the next words, click on the bottom of the screen. You can go backwards by sliding down. Once you've written down all the words, keep your finger on the screen to move on to the next share, and repeat the operation.


![Image](assets/fr/10.webp)


At the end of each share recording, you'll be asked to select the words in your mnemonic phrase in order to confirm that you've written them down correctly.


![Image](assets/fr/11.webp)


And that's it, you've successfully backed up your wallet using the Multi-share option. You can now continue with the rest of the configuration instructions.


### On an existing single-share wallet


If you already have a Trezor wallet with a single-share backup (a SLIP39 mnemonic phrase, not the classic BIP39 phrase), and would like to improve the availability and security of your wallet backup, you can set up a multi-share system without having to transfer your bitcoins.


To do this, connect and unlock your Hardware Wallet. In Trezor Suite, go to Settings.


![Image](assets/fr/12.webp)


Go to the "*Device*" tab.


![Image](assets/fr/13.webp)


Then click on "*Create Multi-share Backup*".


![Image](assets/fr/14.webp)


Read the instructions, then click on "*Create Multi-share Backup*".


![Image](assets/fr/15.webp)


You'll then need to enter your current mnemonic phrase (single-share) on your Trezor screen. Select the number of words (default is 20).


![Image](assets/fr/16.webp)


Then use the Trezor's on-screen keyboard to enter each word of your current mnemonic phrase.


![Image](assets/fr/17.webp)


You can then choose the configuration of your Multi-share Backup by following the instructions provided in the previous section.


![Image](assets/fr/18.webp)


Once you've created your Multi-share Backup, you'll need to decide what to do with your original Single-share mnemonic phrase. As the Bitcoin wallet remains the same, this single phrase will always allow access to it. This will depend on your security strategy, but in general, it's advisable to destroy this phrase to eliminate this single point of failure, which is precisely the aim of Multi-share Backup. If you decide to destroy it, make sure you do so securely, as **it still gives access to your bitcoins**.


Congratulations, you're now up to speed on the use of Single-share and Multi-share Backups on Trezor hardware wallets. If you'd like to take your wallet security a step further, take a look at this tutorial on BIP39 passphrases:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!


## Additional resources



- [SLIP-0039: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).