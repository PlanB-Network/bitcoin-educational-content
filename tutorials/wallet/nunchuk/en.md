---
name: Nunchuk
description: Mobile wallet suitable for everyone
---
![cover](assets/cover.webp)


## A powerful Wallet

Nunchuk was published in late 2020 with a clear philosophy: to make multi-signature a standard. It was therefore designed to perform very advanced functions, with the valuable choice of building the design directly on Bitcoin Core, the reference software for the Bitcoin ecosystem.


After more than 4 years of development and use, it is ready to be tried at scale. If you are a beginner and you are unfamiliar with Nunchuk, this guide will help you take your first steps and discover this tool, learning about its advanced functions after you get past the first impact. The tutorial itself is dedicated to intermediate users who possess the necessary skills to follow all the steps, but it can be an inspiration for everyone to find out how to improve their skills. We will start with the mobile version: it's important to point this out since the Nunchuk software can also run on computers.

## Download

The first step is definitely deciding where to download the app. Go to the [official site](https://nunchuk.io/) where you can find some documentation (not much but it's a start). The feature presentation is also there as well, and toward the end of the page, you will see all the download links.


📌 For this tutorial, I decided to show you how to download the Software Wallet from the Github repository and how to verify the release before installing it on your cell phone. **The following procedure can only be done from your computer**, so I recommend you do all these steps from your desktop or laptop and - after all the verifications - transfer the `.apk` file to your cell phone.


![image](assets/en/01.webp)


If your skills are not very advanced, you may decide to download the `.apk` from the official stores and skip directly to the configuration part of this tutorial. On the other hand, keep following this guide step by step if you want to take the leap.


From your desktop, click on _Visit our open source repository_


The link will take you to Nunchuk's Github page, where you will find a number of repos. We will focus on the _nunchuk-android_ one


![image](assets/en/02.webp)


On the next screen, find the section on _Releases_ and choose _Latest_ on the right.


![image](assets/en/03.webp)


Under _Assets_, download the release (in this example 1.67.apk), along with the SHA256SUMS file and SHA256SUMS.asc.


![image](assets/en/04.webp)


To find the developer's GPG key, go back to the _Releases_ section of the repository and look for the 1.9.53 (or earlier) version, which carries the link to obtain and download the _GPG Key_.


![image](assets/en/05.webp)


We will verify the signatures by using a handy tool offered by Sparrow Wallet, which has a dedicated window for this purpose, and supports PGP signatures and SHA256 Manifests.


Thus, launch Sparrow and from the _Tools_ menu choose _Verify Download_.


![image](assets/en/06.webp)


In the window that pops up, you will find fields to "fill in": choose the _Browse_ button on the right and select, the corresponding files you have just downloaded from Github for each field. When you have completed all the steps, the window will look as follows, with green checkmarks and the Hash confirmation of the manifest.


![image](assets/en/07.webp)

**N.B. the screenshot is from a computer running Windows: be aware that the same practice can be used for any operating system that has Sparrow Wallet installed and verified!**


If you need to download and install Sparrow Wallet, you can find a guide here below.

https://planb.network/en/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

After this process is done, you can transfer the `.apk` file from your computer to your phone.


![image](assets/en/08.webp)


and install Nunchuk


![image](assets/en/09.webp)


Before launching Nunchuk on your phone, open Orbot and put the it in the list of apps to be routed under Tor.


![image](assets/en/11.webp)


Now, you can run Nunchuk. Due to its project features - which are not the subject of this tutorial - Nunchuk, once opened, will invite you to log in via an email or a Google profile. If you don't need to take advantage of Nunchuk Inc's advanced plans, **avoid logging in** and proceed by choosing the _Continue as guest_ option.


![image](assets/en/12.webp)


## Settings

From the _Home_ window of Nunchuck, it is already easy to understand its operating philosophy that we will explain on in a moment.


At the bottom of the page, you can find the menus. As the first step, choose _Profile_ to access the settings.


![image](assets/en/10.webp)


Then choose _Display settings_, and keep ignoring the invitation to create an account.


![image](assets/en/14.webp)


In the screen below, you can check if the Wallet is online and you can connect your server, paying close attention to the instructions you can find in the link on _this guide_.


![image](assets/en/15.webp)


Save the settings with the _Save network settings_ command, then return to the _Profile_ menu and select _Security settings_.


![image](assets/en/16.webp)


From this menu, you can set how to defend yourself when opening the app. To prevent unwanted access, you can protect Nunchuk with the phone's biometric, and/or add a security PIN.


![image](assets/en/17.webp)


Besides, please take a look at the _About_ menu, which you will always find in the _Profile_ window.


![image](assets/en/18.webp)


It will allow you to check the version of the app, or to contact the developers if needed.


![image](assets/en/19.webp)


## Key generation and Wallet

As it is easy to guess from Nunchuk's philosophy, the software is intended as a useful tool for managing multi-signature Wallets. To perform this function, Nunchuk allows the creation of Wallets by separating them from the keys needed to insert the digital signatures.


In fact, the ideal use of Nunchuk involves the creation of Wallets that can be watch-only, i.e. dependent on "Cold" keys.


In the previous screens, you may have noticed that there is a menu at the bottom called _Keys_. If you've just downloaded Nunchuk, in both _Home_ and _Keys_ you'll see a big button inviting you to add a key, _Add Key_.


![image](assets/en/20.webp)

![image](assets/en/21.webp)


**This is just how Nunchuk works:** first, you generate/import keys, and then you create a Wallet, configuring it to choose which keys will authorize the unlocking of funds stored on it.


Even in the case of a singlesig Wallet, you need to first create the key, and then the Wallet. And that is exactly what we will do now, starting with a singlesig Wallet to break the ice and discover the functions of Nunchuk.


Click on _Add Key_


![image](assets/en/22.webp)


Nunchuk shows a number of supported signature devices but, to start, let's choose _Software_.


![image](assets/en/23.webp)


As a consequence, Nunchuk will generate a mnemonic seedphrase that will be stored on the device. You will then need to write down the sequence of words for the backup, creating the best environmental conditions and making sure you have the time to do it well and quietly. The software shows the mnemonic only once, whether you prefer to see it at this stage or later, so choose _Create and backup now_.


![image](assets/en/24.webp)


Nunchuk generates a 24-word mnemonic, which appears immediately on the next screen.


![image](assets/en/25.webp)


Then, it procedes to run a quick check, asking you to select the correct word among 3 choices, corresponding to the number in the mnemonic sequence.

If you have written the mnemonic correctly, the _Continue_ button becomes operational. Press it to move on.


![image](assets/en/26.webp)


Name your key and press _Continue_.


![image](assets/en/27.webp)


At the end of these steps, you will be asked whether to add a [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) to your mnemonic seedphrase. If you do not have the necessary awareness of how to use the passphrase, amd how to back it up, I recommend you choose _I don't need a passphrase_.


![image](assets/en/28.webp)


The key is finally created and it is shown to you in the menu:


- _Key Spec_ indicates the master fingerprint
- The three dots at the top right open up the settings, where you can delete the key or sign a message
- Next to the name of the key, you will find a nib icon, which allows you to edit the name of the Key, to keep your keys in order in the future.
- As a last command, you can check the health status of the key: by pressing _Run health check_ you can have the app check if a key is compromised.


When you are done, click on _Done_


![image](assets/en/29.webp)


You will see your first key appear in the _Keys_ menu.


![image](assets/en/30.webp)


By going to the _Home_ menu, the option to create a Wallet appears. Click _Create new wallet_.


![image](assets/en/31.webp)


Nunchuk shows you a number of possibilities that have to do, for the most part, with services the company offers that are not the subject of this tutorial.


The purpose of this guide is to create a _Hot Wallet and a _Custom wallet_ by diving into the related details.

Let's start with the _Custom wallet_.


![image](assets/en/32.webp)


In a simple way, the app will ask you to name this new Wallet and choose the address script. For the scope of this tutorial, I chose to leave the default setting, _Native segwit_. When you are finished, choose _Continue_.


![image](assets/en/33.webp)


The system then asks you to set which keys to use to unlock the funds of this Wallet. Should there be multiple keys, you will be shown a list from which to choose. For the moment, we have created only one, so let's put a check mark on it. In the lower right corner, Nunchuk will ask you to set up your future multi-signature Wallets, increasing the number of _Required keys_.


![image](assets/en/34.webp)


Since we are creating a singlesig, let's leave `1` and click _Continue_.


Lastly, a verification screen appears, where you can check the characteristics of the Wallet:


- the name
- the `1/1 Multisig` tage, which is how Nunchuk names singlesig Wallets 
- the script type, `Native SegWit`
- the `Keys` key, with its fingerprint and derivation path


When you are satisfied, press _Create wallet_


![image](assets/en/35.webp)


The Wallet has been created and you can download the [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) file as a backup. To return to the main menu, click on the arrow at the top left.


![image](assets/en/36.webp)


When you go back to _Home_, you are shown the newly created Wallet, its balance and the status of the connection. By clicking in the blue space, you can access the main functions of the Wallet.


![image](assets/en/37.webp)



- The lens icon in the upper right-hand corner allows you to do a transaction search;
- `View Wallet config` gives access to the configuration menu, where you can edit the name of the Wallet and enable advanced options on the top right (of which you cannot get screenshots). Here you can export the Wallet configuration, labels, replace keys, change the [gap limit](https://planb.network/en/resources/glossary/gap-limit) and more.


## Transactions with Nunchuk


Click on _Receive_


![image](assets/en/38.webp)


The app is programmed to show the QR Code of the address or copy/share the scriptPubKey to receive onchain funds.


![image](assets/en/39.webp)


We sent an UTXO to this first address.


![image](assets/en/40.webp)


Let's click on _Receive_ to receive another one.


![image](assets/en/41.webp)


The purpose of it is to see that Nunchuk reports this new address to you as an _Unused address_ but also shows you that you have _Used addresses_ and the count thereof.


### Spending transaction with coin control


When this second UTXO has also arrived, go back to the main Wallet screen to check the status of the two incoming transactions and, most importantly, click on the _View coins_ option.


![image](assets/en/42.webp)

 You will be shown individual UTXOs. Here you can choose to view more details by clicking the little arrow next to the amount.


![image](assets/en/43.webp)


You can check when the UTXO arrived, the transaction description, and you can also block the UTXO so that it is not spent (and more).


![image](assets/en/44.webp)


But if you go back to the _Coins_ menu by clicking the arrow in the upper right corner, you can turn on "Coin Control" to spend your UTXOs in a more controlled way.


In the following example, I chose to select a UTXO of 21,000 Sats and then click on the symbol in the lower left corner.


![image](assets/en/45.webp)


Nunchuk automatically opens the _New transaction_ window to spend this UTXO. In the spending transaction, you must first set the amount manually or by selecting _Send all selected_ to use all the coin control balance, without generating remainders. Once the amount is set, choose _Continue_


![image](assets/en/46.webp)


Now Nunchuk shows where to paste the address where to transfer these funds, where to create a description and finalize the transaction.


![image](assets/en/47.webp)


Choosing _Create transaction_ delegates automatic fee and transaction management to the app. I would recommend choosing _Custom transaction_ for more control over this part.


In this new screen:


- _Subtract fee from send amount_, to prevent fees from being taken from another UTXO present in Wallet, by spending it and generating a change (which is an avoidable loss of privacy);
- Set the fees manually after checking the amount on a block explorer.


Having done all these steps, click on _Continue_


![image](assets/en/48.webp)


The next screen is the complete summary of the transaction. If everything is okay, confirm by selecting _Confirm and create transaction_.


![image](assets/en/49.webp)


With _Pending signatures_ Nunchuk alerts you that the transaction is waiting for your signature to approve the expenditure, which you add by clicking on _Sign_.


![image](assets/en/50.webp)


The _Broadcast_ command will appear at the bottom to propagate the finalized and signed transaction.


![image](assets/en/51.webp)


### Spending transaction from menu _Send_


While on the Wallet main page we can see the transaction going out and waiting for some confirmation, we can use the _Send_ menu to simulate a daily purchase.


![image](assets/en/52.webp)


Clicking _Send_, in fact, opens up the screen for sending the transaction, which is the same as the one just seen but without going through coin control.


In this second example, I also decided to select _Custom transaction_ and send the entire amount, but I could have set it manually. Once you have decided on the amount to send, press _Continue_.


![image](assets/en/53.webp)


Always pay attention to whether the fees are subtracted from the UTXO in question (in this example the choice is forced, because there is only one), and manually adjust the fees according to the situation on the Mempool, and press _Continue_.


![image](assets/en/54.webp)


If the summary screen is satisfactory, choose _Confirm and create transaction_.


![image](assets/en/55.webp)


Sign the transaction with _Sign_.


![image](assets/en/56.webp)


Then propagate it to the network.


![image](assets/en/57.webp)


The Wallet is at this point with the balance at zero and the history being updated.


![image](assets/en/58.webp)


## Creation of a "Hot Wallet"


Lastly, to cover all the steps from the initial stages of Nunchuk mobile, let's see how to create what the app calls a "Hot Wallet."


In the _Home_ menu of Nunchuk, where the list of Wallets appears, click the `+` in the upper right corner.


![image](assets/en/59.webp)


Choose _Hot wallet_ from the options.


![image](assets/en/60.webp)


Nunchuk will give you some advice on managing Hot Wallets on the presentation page, where you will select _Continue_ to proceed.


![image](assets/en/61.webp)


After a few moments, the Wallet is created and appears in brownish color in the list. Nunchuk uses this color to alert you that the Wallet has not been backed up.


![image](assets/en/62.webp)


Click on the name of the Wallet, to access its configurations, and you may notice an invitation to back up the mnemonic seedphrase immediately.


![image](assets/en/63.webp)


The procedure is the same as we discussed earlier, so we won't go over it again. Once completed, Nunchuk will direct you to the relevant key page, which you can edit just like the one you created using the Custom procedure.


![image](assets/en/64.webp)


You can also try _Run health check_.


![image](assets/en/65.webp)


This way, you will see how to display all your Wallets in the _Home_ of the app.


![image](assets/en/66.webp)


## Important considerations to continue independently

Just as there is an order for creation, that is, first the generation of the keys and then the Wallet, you will need to maintain the reverse order for deleting these items from your app.


If you need to delete one of the keys, you should first delete the Wallet, or the Wallets which employ one of the signature keys for transactions: eliminate the Wallets first, and only then, delete the keys. If you do not follow this order, you will be unable to remove the key.


Now that you know how to get started with Nunchuk, you can continue exploring the app and uncovering its features. In this tutorial, we've only scratched the surface; keep in mind that there are more advanced applications and sophisticated needs that this software wallet can help you address