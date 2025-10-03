---
name: Nunchuk
description: Wallet mobile suitable for all
---
![cover](assets/cover.webp)


## A powerful Wallet

Nunchuk arrived in late 2020 with a clear philosophy: to make multi-signature a standard. It was therefore designed to perform very advanced functions, with the valuable choice of building the design directly on Bitcoin Core, the reference software for the Bitcoin ecosystem.


After more than 4 years of development and use, it is ready to be tried at scale. If you are a beginner and unfamiliar with Nunchuk, this guide will help you take your first steps and discover this software, whose advanced functions you will be able to learn about after you get past the first impact. The tutorial itself is dedicated to intermediate users who possess the necessary skills to follow all the steps, but it can be an inspiration for everyone to find out how to increase skills. We will start with the mobile version, and this pointing out is necessary, since Nunchuk has the software to run on computers as well.


## Download

The first step is definitely deciding where to download the app. Go to the [official site](https://nunchuk.io/) where you can find some documentation (not much but it's a start), the feature presentation as well as, toward the end of the page, all the download links.


📌 For this tutorial I decided to show you how to download Software Wallet from the Github repository and how to verify the release before installing it on your cell phone. **The following procedure can only be done from your computer**, so I recommend you do all these steps from your desktop or laptop and - after all the verifications - transfer the `.apk` file to your cell phone.


![image](assets/en/01.webp)


If your skills are not very advanced, you may decide to download the `.apk` from the official stores and skip directly to the configuration part of this tutorial. If, on the other hand, you want to take the leap, keep following step by step.


So from your desktop computer click _Visit our open source repository_


The link will take you to Nunchuk's Github page, where you will find a number of repos. We will focus on the _nunchuk-android_ one


![image](assets/en/02.webp)


On the next screen, locate to the right the section on _Releases_ and choose _Latest_


![image](assets/en/03.webp)


Under _Assets_, download the release (in this example 1.67.apk), along with the SHA256SUMS file and SHA256SUMS.asc.


![image](assets/en/04.webp)


To find the developer's GPG key, go back to the _Releases_ section of the repository and look for 1.9.53 (or earlier) which carry the link to obtain and download the _GPG Key_


![image](assets/en/05.webp)


We will proceed with verification through a handy tool offered by Sparrow wallet, which has a dedicated window for this purpose and supports PGP signatures and SHA256 Manifests.


Then launch Sparrow and from the _Tools_ menu choose _Verify Download_.


![image](assets/en/06.webp)


In the window that pops up, you will find fields to "fill in": choose the _Browse_ button on the right and select, for each field, the corresponding files you have just downloaded from Github. When you have completed all the steps, the window will look as follows, with green checkmarks and Hash confirmation of the manifest.


![image](assets/en/07.webp)

**N.B. the screenshot is from a Windows PC, the same practice can be used for any operating system on your computer, just have Sparrow wallet installed. And verified!**


You can find the guide to Sparrow wallet to download this Software Wallet

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

You can then transfer the `.apk` file from your computer to your phone


![image](assets/en/08.webp)


and install Nunchuk


![image](assets/en/09.webp)


Before launching Nunchuk on your phone, open Orbot and put the newcomer in the list of apps to be routed under Tor.


![image](assets/en/11.webp)


Now run Nunchuk. For project features-which are not the subject of this tutorial-Nunchuk, once opened, will invite you to log in via an email or Google profile. Until you plan to take advantage of Nunchuk Inc's advanced plans, **avoid logging in** and proceed by choosing the _Continue as guest_ option.


![image](assets/en/12.webp)


## Settings

Nunchuk presents itself with a _Home_ window of presentation, where it is easy to understand its operating philosophy and which we will elaborate on in a moment.


At the bottom you can find the menus, and as the first step, choose _Profile_ to access the settings.


![image](assets/en/10.webp)


Then choose _Display settings_, continuing to ignore the invitation to create an account.


![image](assets/en/14.webp)


In the screen below you can check if Wallet is online and you can connect your server, paying close attention to the instructions at the link that is offered by clicking on _this guide_.


![image](assets/en/15.webp)


Save the settings with the _Save network settings_ command, return to the _Profile_ menu and select _Security settings_.


![image](assets/en/16.webp)


From this menu you set how to defend the opening of the app. To prevent unwanted access you can protect Nunchuk with the phone's biometric, and/or add a security PIN.


![image](assets/en/17.webp)


Also take a look at the _About_ menu, which you will always find in the _Profile_ window


![image](assets/en/18.webp)


which will allow you to check the version of the app, or to contact the developers if needed.


![image](assets/en/19.webp)


## Key Generation and Wallet

As is easy to guess from Nunchuk's philosophy, the software is intended as a useful tool for managing multi-signature Wallets. To perform this function, Nunchuk allows the creation of Wallet by separating them from the keys needed to arrange digital signatures.


In fact, the ideal operation of Nunchuk involves the creation of Wallets that can be watch-only, dependent on keys that can be "Colds."


In the previous screens you may have noticed that there is a menu at the bottom called _Keys_. If you've just downloaded Nunchuk, in both _Home_ and _Keys_ you'll see a big button inviting you to add a key, _Add Key_.


![image](assets/en/20.webp)

![image](assets/en/21.webp)


**This is just how Nunchuk works:** first you generate/import the keys and then you create the Wallet, configuring it to choose which keys will authorize the unlocking of the funds stored on it.


Even in the case of Wallet singlesig, you create the key first and only then the Wallet. And that is exactly what we will do now, starting with a Wallet singlesig to break the ice and discover the functions of Nunchuk.


Click _Add Key_


![image](assets/en/22.webp)


Nunchuk shows a number of supported signature devices but, to start, choose _Software_.


![image](assets/en/23.webp)


Nunchuk will generate a mnemonic that will be stored on the device. You then need to write down the sequence of words for the backup, creating the best environmental conditions and making sure you have the time to do it well and quietly. The software shows the mnemonic only once, whether you choose to show it now or later, so choose _Create and backup now_.


![image](assets/en/24.webp)


Nunchuk generates 24-word mnemonic sentences, which appear immediately on the next screen


![image](assets/en/25.webp)


and then proceeded to do a quick check, asking you to select the correct word, from 3 choices, corresponding to the number in the mnemonic sequence.

If you have written the mnemonic correctly, the _Continue_ button becomes operational. Press it to move on.


![image](assets/en/26.webp)


Name your key and press _Continue_.


![image](assets/en/27.webp)


At the end of these steps, you will be asked whether to add a [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) to your mnemonic phrase. If you do not have the necessary awareness of how to use passphrase, arrange for its backup, or how it works, I recommend that you choose _I don't need a passphrase_.


![image](assets/en/28.webp)


The key is finally created and is shown to you in the menu:


- With _Key Spec_ the master fingerprint is indicated
- You have settings, the three dots at the top right, where you can delete the key or sign a message
- Next to the name of the key you will find a nib icon, clicking on which you can edit the name of the Key, for example to keep your keys in order in the future.
- As a last command, you can check the health status of the key: by pressing _Run health check_ you can have the app check if a key is compromised.


When you are good, click _Done_


![image](assets/en/29.webp)


In the _Keys_ menu you will see your first key appear.


![image](assets/en/30.webp)


By going to the _Home_ menu, the option to create Wallet appears. Click _Create new wallet_.


![image](assets/en/31.webp)


Nunchuk shows you a number of possibilities that have to do, for the most part, with services the company offers that are not the subject of this tutorial.


In this guide we will create a _Hot Wallet and a _Custom wallet_ by detailing the details.

Let's start with _Custom wallet_.


![image](assets/en/32.webp)


In a simple way, the app will ask you to name this new Wallet and choose the script for the addresses. For the tutorial I chose to leave the default setting, _Native segwit_. When you are finished, choose _Continue_


![image](assets/en/33.webp)


The configuration of Wallet goes on to ask you to set with which key the funds of this Wallet will be unlocked. Should there be multiple keys, you will be shown a list from which to choose. We for the moment have created only one, so we choose to put a check mark on that one. In the lower right corner you can see how Nunchuk will ask you to set up your future Wallet multi-signatures, increasing the number of _Required keys_.


![image](assets/en/34.webp)


Since we are creating a singlesig, we leave `1` and click _Continue_.


Last, a verification screen appears, where you can check the features of Wallet:


- the name
- the `1/1 Multisig` tage, which is how Nunchuk names the Wallet singlesig
- the script type, `Native SegWit`
- the `Keys` key, with its fingerprint and derivation path


When you are satisfied, press _Create wallet_


![image](assets/en/35.webp)


Wallet has been created and you can download the [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) file as a backup. To return to the main menu click the arrow in the upper left corner.


![image](assets/en/36.webp)


You are in _Home_, where you are shown the newly created Wallet reporting the balance and status of the connection. By clicking in the blue space, you can access the main functions of Wallet.


![image](assets/en/37.webp)



- The lens icon in the upper right-hand corner allows you to do a transaction search;
- `View Wallet config` gives access to the configuration menu, where you can edit the name of the Wallet and enable advanced options, top right (of which you can't get screenshots). Here you can export the Wallet configuration, labels, replace keys, change the [gap limit](https://planb.network/en/resources/glossary/gap-limit) and more.


## Transactions with Nunchuk


Awards _Receive_


![image](assets/en/38.webp)


The app is programmed to show the QR Code of the address or copy/share the scriptPubKey to receive onchain funds.


![image](assets/en/39.webp)


We had a UTXO arrive on this first address,


![image](assets/en/40.webp)


but we still click _Receive_ to receive another one.


![image](assets/en/41.webp)


The purpose is for you to find out that Nunchuk reports this new address to you as an _Unused address_ but also shows you that you have _Used addresses_ and the count thereof.


### Spending transaction with coin control


When this second UTXO has also arrived, go back to the Wallet main screen to check the status of the two incoming transactions and, most importantly, click on the _View coins_ option


![image](assets/en/42.webp)


where you will be shown individual UTXOs. Here you can choose to view one in particular by clicking the little arrow next to the amount


![image](assets/en/43.webp)


and check when it arrived, the description, block UTXO so that it is not spent and more.


![image](assets/en/44.webp)


But if you go back to the _Coins_ menu by clicking the arrow in the upper right corner, you can turn on "Coin Control" to spend your UTXOs in a more controlled way.


In the following example, I chose to select UTXO of 21,000 Sats and then click the symbol in the lower left corner.


![image](assets/en/45.webp)


Nunchuk automatically opens the _New transaction_ window to spend this UTXO. In the spending transaction, first, you must set the amount manually or by selecting _Send all selected_ to send all the coin control balance, without generating remainders. Once the amount is set, choose _Continue_


![image](assets/en/46.webp)


Now Nunchuk shows where to paste the address to which to transfer these funds, detail a description, and finalize the transaction.


![image](assets/en/47.webp)


Choosing _Create transaction_ delegates automatic fee and transaction management to the app. I recommend choosing _Custom transaction_ for more control.


In this new screen it is important to select


- _Subtract fee from send amount_, to prevent fees from being paid by another UTXO present in Wallet, spending it and generating a remainder (which is an avoidable loss of privacy);
- and then set the fees manually after checking on the explorer.


Having done all these steps, click on _Continue_


![image](assets/en/48.webp)


The next screen is the complete summary of the transaction. If everything is okay, confirm by selecting _Confirm and create transaction_.


![image](assets/en/49.webp)


With _Pending signatures_ Nunchuk alerts you that the transactionp is waiting for your signature to approve the expenditure, which you affix by clicking _Sign_.


![image](assets/en/50.webp)


The _Broadcast_ command appears at the bottom to propagate the finalized and signed transaction.


![image](assets/en/51.webp)


### Spending transaction from menu _Send_


While on the main page of Wallet we see the transaction going out and waiting for confirmation, we use the _Send_ menu to simulate a daily expense.


![image](assets/en/52.webp)


Clicking _Send_, in fact, brings up the screen for sending the transaction, which is the same as the one just seen but without going through coin control.


Also in this second example I decided to select _Custom transaction_ and send the entire amount, but I could have set it manually. Once you have decided on the amount to send press _Continue_.


![image](assets/en/53.webp)


Then always make a case whether the fees are subtracted from the UTXO in question (in this example the choice is forced, because there is only one), manually adjust the fees according to the situation at the time in Mempool, and press _Continue_.


![image](assets/en/54.webp)


If the summary screen is satisfactory, choose _Confirm and create transaction_.


![image](assets/en/55.webp)


Sign the transaction with _Sign_


![image](assets/en/56.webp)


and propagate it to the network.


![image](assets/en/57.webp)


Wallet is at this point with the balance at zero and the history being updated.


![image](assets/en/58.webp)


## Creation of a "Hot Wallet"


Last and not to leave out anything from the initial stages of Nunchuk mobile, let's see how this creates what the app calls "Hot Wallet."


In the _Home_ menu of Nunchuk, where the list of Wallets appears, click the `+` in the upper right corner.


![image](assets/en/59.webp)


Choose _Hot wallet_ from the options


![image](assets/en/60.webp)


Nunchuk dispenses some advice on handling Hot Wallets on the presentation page, where you will select _Continue_ to proceed.


![image](assets/en/61.webp)


After a few moments the Wallet is created and appears in the list in brownish color. This is the color with which Nunchuk alerts you that you have not yet backed up Wallet.


![image](assets/en/62.webp)


Click on the name of the Wallet, to access its configurations, and you may notice an invitation to back up the mnemonic phrase immediately.


![image](assets/en/63.webp)


The procedure is the same as we have seen before, so we won't stand over it again. Once it's done, Nunchuk will take you to the relevant key page, which you can edit as the one you created with the _Custom_ procedure.


![image](assets/en/64.webp)


Also try _Run health check_


![image](assets/en/65.webp)


or to see how to display all your Wallets in the _Home_ of the app.


![image](assets/en/66.webp)


## To keep in mind to continue independently

Just as there is an order for creation, that is, first generating the keys and then the Wallet, you will need to maintain the reverse order for deleting these items from your app.


If you have a need to delete one of the keys, you should first have the foresight to delete Wallet, or Wallets, which employ one of the signature keys for transactions: first you delete Wallets and only then the keys. If you do not follow this order, you will find yourself unable to remove the key.


Now that you know how to get started with Nunchuk, you can continue to study this app and discover its secrets. In this tutorial we have only taken the first steps, but there are more sophisticated applications and advanced needs that this Software Wallet can help you meet.