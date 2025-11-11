---
name: Ashigaru
description: The fork from Samourai Wallet to secure, manage and mix your bitcoins
---

![cover](assets/cover.webp)


Ashigaru is a Bitcoin mobile wallet application that follows on from the Samourai Wallet project, but in a new form. This software was born in a particular context: in April 2024, the founders of Samourai Wallet were arrested by the American authorities, and their servers were seized. Although the Samurai application itself remained usable, it is currently no longer maintained. Ashigaru is a free fork version of Samurai Wallet, maintained by an anonymous team to guarantee the continuity of Samurai's functionality and safeguard its original philosophy: to defend the privacy and sovereignty of Bitcoin users.


Ashigaru takes up much of Samourai's DNA: a similar interface, an obviously self-custodial approach, open source and a focus on privacy. The code is distributed under the GNU GPLv3 license, which ensures that anyone can audit, modify or redistribute the software.


The Ashigaru application integrates a set of advanced tools for confidentiality and management of your UTXOs:


- Whirlpool**, a coinjoin protocol based on Zerolink, enabling you to break the deterministic links between transaction entries and exits, without losing sovereignty over your funds.
- PayNym**, which implements reusable payment codes (BIP47), now represented via a "*Pepehash*" avatar system.
- Ricochet**, a feature that adds intermediate jumps to transactions to make them more difficult to trace.
- And of course ***Coin Control*** to select, freeze and label your UTXOs precisely.
- Batch Spending***, to reduce costs by grouping several payments into a single transaction.
- The **Stealth Mode**, which hides the application on your mobile behind a dummy launcher to go unnoticed during a physical inspection of your phone.
- Advanced spending tools to optimize your confidentiality (payjoin, stonewall...).
- An optimized recovery system using Passphrase BIP39.
- A system for automatically optimizing the choice of transaction fees.


![Image](assets/fr/01.webp)


Ashigaru is therefore aimed at users who are aware of the issues surrounding transaction traceability on Bitcoin. Whether you're a privacy-conscious user, a seasoned bitcoiner committed to self-custody, or an individual exposed to the risks of increased surveillance, this wallet application provides you with the tools you need to regain control of your activity on Bitcoin.


Ashigaru is available in a mobile version via its app, which we'll explore in this tutorial. But it can also be used on the PC with ***Ashigaru Terminal***, which we'll introduce in a future tutorial.


![Image](assets/fr/02.webp)


In this tutorial, I'd like to introduce you to the basic use of Ashigaru: installation, connection to the Dojo, backup, receiving and sending bitcoins. Advanced tools will be presented in other dedicated tutorials.


## 1. Prerequisites for Ashigaru


The application requires a few prerequisites to work properly. First of all, it's not an application available on classic stores like the Google Play Store or App Store. It installs manually on your phone only from its `.apk` file, downloadable via the Tor network. So if you're using an iPhone, this method won't work: you'll need an Android device.


To download the `.apk` file via Tor, you'll need a browser capable of accessing `.onion` sites. The easiest way is to install the Tor Browser application on your phone, available from the [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) or directly [via its `.apk`](https://www.torproject.org/download/#android).


![Image](assets/fr/03.webp)


Most recent smartphones block the installation of applications from unknown sources by default. You'll need to temporarily activate this option for Tor Browser in your device settings to allow installation. Once the application has been installed, remember to deactivate this function to reinforce your phone's security.


Another essential prerequisite for using Ashigaru is a Bitcoin Dojo node. For reasons of security and sovereignty, the Ashigaru team does not maintain a centralized server to connect your application. So you'll need to run your own Dojo instance, or connect to a trusted one.


The Dojo enables your Ashigaru application to consult blockchain information, view your address balances and broadcast your transactions on the Bitcoin network.


To find out more about Dojo and learn how to install it, I invite you to follow this dedicated tutorial :


https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

If you really can't afford to run your own Dojo, you can find people willing to share their instance for free at [dojobay.pw](https://www.dojobay.pw/mainnet/). This may be a temporary solution, but in the long term, I recommend you use your own Dojo to guarantee your sovereignty and confidentiality.


## 2. Check and install the Ashigaru application


### 2.1. Download the Ashigaru application


On your phone, open Tor Browser and go to [the official Ashigaru website](https://ashigaru.rs/download/), in the `Download` section. Then click on the `Download for Android` button to download the installation file.


![Image](assets/fr/04.webp)


Before installing the application on your device, we'll check its authenticity and integrity. This is a very important step, especially when installing an application directly from an `.apk' file.


### 2.2. Check Ashigaru application


Go back to [the official Ashigaru website](https://ashigaru.rs/download/) in the `Download` section, then copy the message displayed under the title `SHA-256 Hash of the APK file`. Copy the entire block, from `BEGIN PGP SIGNED MESSAGE` to `END PGP SIGNATURE`.


![Image](assets/fr/05.webp)


Still on your phone, open a new tab in Tor Browser and go to [the Keybase verification tool](https://keybase.io/verify). Paste the message you've just copied into the field provided, then click on the `Verify` button.


![Image](assets/fr/06.webp)


If the signature is genuine, Keybase will display a message confirming that the file has been signed by the Ashigaru developers. You can also click on the `ashigarudev` profile indicated by Keybase and check that their key fingerprint corresponds exactly to : `A138 06B1 FA2A 676B`.


However, if an error appears at this stage, it means that the signature is invalid. In this case, **do not install the APK**. Start again from the beginning, or ask the community for help before continuing.


![Image](assets/fr/07.webp)


Keybase has provided you with the hash of the application. We'll now check that the hash of the `.apk` file you've downloaded matches the one verified on Keybase. To do this, go to [HASH FILE ONLINE](https://hash-file.online/).


![Image](assets/fr/08.webp)


Click on the `BROWSE...` button and select the `.apk` file downloaded in step 2.1.

Then choose the hash function `SHA-256`, and click `CALCULATE HASH` to calculate the hash of your file.


![Image](assets/fr/09.webp)


The site will display the hash of your `.apk` file. Compare it with the hash you verified on Keybase.io. If the two hashes are identical, the authenticity and integrity check has been successful. You can now proceed to install the application.


![Image](assets/fr/10.webp)


### 2.3. install the Ashigaru application


To install the application, open your phone's file manager and go to the downloads folder. Then click on the `.apk` file you've just checked, and confirm installation when prompted.


![Image](assets/fr/11.webp)


Ashigaru is now installed on your phone.


## 3. Initialize the app and create a Bitcoin wallet


When launching the application for the first time, select `MAINNET`.


![Image](assets/fr/12.webp)


Then click on `Get Started`.


![Image](assets/fr/13.webp)


We will now create a new Bitcoin wallet. Press the `Create a new wallet` button.


![Image](assets/fr/14.webp)


### 3.1. create a Bitcoin wallet


Ashigaru requires a passphrase BIP39. Choose your passphrase and enter it in the appropriate fields. It must be as long and random as possible to resist a brute-force attack.


Make a physical backup of this passphrase immediately. This is a very important step: if you lose your phone, **if you no longer have this passphrase, you will no longer be able to access your bitcoins** stored with your Ashigaru wallet. This same passphrase is also used to encrypt the wallet recovery file.


If you don't know what a passphrase is, or don't fully understand how it works, I strongly recommend that you read this additional tutorial. This is important, because the passphrase is a critical element of your security: misunderstanding its use could result in the permanent loss of your funds.


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Once you've entered your passphrase, click `NEXT`.


![Image](assets/fr/15.webp)


Then choose a PIN code. This code will be used to unlock your Ashigaru wallet, protecting it against unauthorized physical access. It is not involved in the cryptographic derivation of your wallet keys. This means that, even without knowing the PIN code, anyone with your mnemonic phrase and passphrase will be able to regain access to your bitcoins.


Opt for a long, random PIN code. Remember to keep a backup copy in a separate location from your phone, to prevent them from being compromised simultaneously.


![Image](assets/fr/16.webp)


Once the PIN code has been created, Ashigaru displays your wallet's mnemonic phrase. Warning: this phrase, combined with your passphrase, gives full access to your bitcoins. Anyone holding it can take possession of your funds, even if they don't have access to your phone. This 12-word sequence can be used to restore your wallet in the event of loss, theft or breakage of your phone. It is therefore important to save it with the utmost care on a physical medium (paper or metal).


Never save this phrase in digital form, or you risk exposing your funds to theft. Depending on your security strategy, you may create several physical copies, but never divide it. Keep the words in their exact order, and make sure they are numbered.


Finally, never store the mnemonic and passphrase in the same place. If both were compromised simultaneously, an attacker could gain access to your wallet.


![Image](assets/fr/17.webp)


To learn more about how to secure your mnemonic phrase, please consult this complementary tutorial :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru then asks you to reconfirm your passphrase. Take this opportunity to check that your physical backup is correct.


![Image](assets/fr/18.webp)


### 3.2. connect a dojo


Next comes the step of connecting to your Dojo. As explained in the introduction, Ashigaru must be connected to a Dojo in order to interact with the Bitcoin network.


Log on to your Dojo's "Maintenance Tool" and open the `PAIRING` menu.


![Image](assets/fr/19.webp)


On Ashigaru, press the `Scan QR` button, then scan the connection QR code displayed by your DMT. Then click `Continue` to confirm.


![Image](assets/fr/20.webp)


Enter your PIN code to unlock the wallet. This will take you to the synchronization page. It's normal to see *PayNym* errors at this stage, as the wallet is new. Simply click `Continue`.


![Image](assets/fr/21.webp)


You will then be taken to the home page of your wallet.


![Image](assets/fr/22.webp)


Before going any further, I recommend that you carry out a test recovery while the wallet still contains no bitcoin. This will enable you to check that your paper backups are working properly. To find out how, follow this tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Setting up the Ashigaru application


To access the application settings, click on the image of your *PayNym* in the top left-hand corner, then select `Settings`.


![Image](assets/fr/23.webp)


Here you'll find several options for adapting Ashigaru's operation to your needs. However, I strongly recommend that you activate 2 important parameters right from the start.


Start by opening the `Security > Stealth mode` menu, then activate this feature if you need it. It hides the Ashigaru application behind the name, logo and interface of an ordinary application installed on your phone. The aim is to prevent anyone from identifying Ashigaru in the event of a physical inspection of your phone.


![Image](assets/fr/24.webp)


Each fake application on offer has a specific method for unlocking the real Ashigaru interface. For example, if you choose the calculator, the Ashigaru application disappears from your home screen and is replaced by a fake calculator. When you open it, you see a classic working calculator interface, but to access Ashigaru, all you have to do is tap the `=` symbol five times quickly.


The second important parameter to activate is [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). This option allows you to increase the cost of a transaction if it gets stuck in the mempools because the cost is too low. You can activate it via the `Transactions > Spend using RBF` menu.


![Image](assets/fr/25.webp)


Tip: You can change the display unit of your wallet from `BTC` to `sat` simply by clicking on the total balance displayed on the home page.


## 5. Receive bitcoins on Ashigaru


Now that your wallet is operational, you can receive satss. To do so, press the `+` button at the bottom right of the interface, then the green `Receive` button.


![Image](assets/fr/26.webp)


Ashigaru then shows you the first unused receiving address in your wallet, to prevent address reuse (address reuse is a very bad practice for your privacy). You can then forward this address to the person or service who needs to send you bitcoins.


![Image](assets/fr/27.webp)


Once the transaction has been broadcast on the network, it will automatically appear on the application's home page.


![Image](assets/fr/28.webp)


## 6. Send bitcoins with Ashigaru


Now that you have bitcoins in your Ashigaru wallet, you can also send them. To do so, press the `+` button at bottom right, then select the red `Send` button.


![Image](assets/fr/29.webp)


Then choose the account from which you wish to make the expenditure. For the moment, we haven't yet tackled the `Postmix` account, reserved for coinjoins, which we'll look at in a later tutorial. So we're going to send funds from the main deposit account.


![Image](assets/fr/30.webp)


Enter your transaction details: the amount to be sent and the recipient's Bitcoin address.


![Image](assets/fr/31.webp)


By clicking on the three small dots in the top right-hand corner, then on `Show unspent outputs`, you can also choose precisely which UTXOs you wish to spend, to enhance your privacy.


![Image](assets/fr/32.webp)


Once you've filled in all the details, click on the white arrow at the bottom of the interface to continue.


You will then be taken to a summary page showing all the details of your transaction. Several important elements are displayed:


- In the `Destination` block, check one last time that the recipient address and the amount sent are correct;
- In the `Fees` block, you can view the fee rate automatically selected by Ashigaru and, if necessary, modify it by clicking on `MANAGE` ;
- The `Transaction` block indicates the type of transaction you are about to perform. Here, we're talking about a simple transaction, but Ashigaru also supports other types of privacy-optimized transactions, which we'll cover in detail in a future tutorial;
- The red `Transaction Alert` block warns you if your transaction shows patterns that can be recognized by the chain analysis tools, and which could compromise your privacy. By clicking on it, you can view the details. For example, in my case, Ashigaru tells me that the amount sent is round (`3000 sats`), allowing me to deduce which output corresponds to the expense and which is the exchange. To find out more about these chain analysis heuristics, I invite you to follow my BTC 204 training on Plan ₿ Academy ;
- Finally, you can add a label to your transaction to keep a record of its purpose.


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Once you've checked all the information, use the green arrow to send the bitcoins. Hold down the arrow, then drag it to the right to confirm the upload.


![Image](assets/fr/33.webp)


Your transaction has been broadcast on the Bitcoin network.


![Image](assets/fr/34.webp)


## 7. Recovering your Ashigaru wallet


Recovery of an Ashigaru wallet differs slightly from that of a classic Bitcoin wallet, as the application uses the same methods as Samurai Wallet. If you lose access to your wallet (whether because you've forgotten your PIN, uninstalled it or lost your phone), there are several ways to recover your bitcoins.


If you still have access to your phone, or if you had made a backup of this file, the simplest method is to use the backup file `ashigaru.txt`. This file contains all the information you need to restore your wallet on a new instance of Ashigaru (or on Sparrow Wallet), but it's encrypted with the passphrase you defined in step 3.1 of this tutorial. You must therefore have both the `ashigaru.txt` file and your passphrase to use this method.


With these two elements, you can, for example, restore your wallet on Sparrow Wallet.


![Image](assets/fr/35.webp)


If you don't have access to the `ashigaru.txt` file, you can still regain access to your funds using your passphrase mnemonic phrase, just as you would for any other Bitcoin wallet. I recommend that you perform this restore either on a new Ashigaru instance, or directly on Sparrow Wallet, to easily recover the bypass paths from Whirlpool if you were using it. Alternatively, you can import this information into any other BIP39-compatible software by manually entering the derivation paths.


For more information on this process, please consult the complete tutorial I've written on recovering a Wallet Samurai wallet. Since Ashigaru is a fork, the procedure is identical:


https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

As you can see, whatever restoration method you use, the passphrase is indispensable. So be sure to back it up carefully. You can also make several copies, depending on your security strategy.


## 8. Update application


To update the Ashigaru app, since you installed it from an `.apk` file and not via the Play Store like a regular app, you'll need to download the new `.apk` file corresponding to the updated version, then install it manually.


Repeat the steps described in section 2 of this tutorial, except that when you click on the `.apk` file to launch the installation, **your Android phone should offer you the `Update` option, not `Install`**.


![Image](assets/fr/41.webp)


This is a very important point: if Android displays `Install` instead of `Update`, you are probably installing a fraudulent version. In this case, interrupt the installation procedure immediately.


As with the first installation, please check the authenticity and integrity of the `.apk` file before proceeding with the update.


To find out when a new version is available, check the official Ashigaru website from time to time. Rest assured, Ashigaru is a stable, mature application, inherited from Samourai Wallet, and updates are relatively infrequent compared with younger software.


## 9. Donate to the Ashigaru project


Ashigaru is an open-source project. If you'd like to support its development, you can make a donation directly from the application via PayNym.


To do this, click on your PayNym at the top right of the interface, then select your payment code starting with `PM...`.


![Image](assets/fr/36.webp)


Then press the `+` button at the bottom right of the screen.


![Image](assets/fr/37.webp)


Select `Ashigaru Open Source Project` as the recipient.


![Image](assets/fr/38.webp)


Click on the `CONNECT` button to establish the BIP47 communication channel (more about this protocol in the tutorial below).


https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)


Once the notification transaction has been confirmed, you can send your donations to the project by clicking on the small white arrow in the top right-hand corner of the interface.


![Image](assets/fr/40.webp)


You now know how to use the basic features of the Ashigaru application. In future tutorials, we'll look at how to take advantage of advanced spending transactions, as well as Whirlpool, the coinjoin implementation inherited from Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
