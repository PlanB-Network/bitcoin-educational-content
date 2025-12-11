---
name: Ginger Wallet
description: Open-source, self-custody Bitcoin wallet software, fork from Wasabi Wallet, integrating Coinjoins
---
![cover](assets/cover.webp)


Ginger Wallet is an open source, non-custodial Bitcoin wallet focused on confidentiality and privacy. It started life as fork from Wasabi Wallet (after version 2.0.7.2 - MIT license).


Ginger Wallet retains Wasabi's technical architecture while adding a few specific features. According to the [Ginger Wallet documentation](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi emphasizes **autonomy and control**, while Ginger focuses on **ease of use, security and a simplified experience**, making it accessible to those less familiar with technical aspects.


Ginger Wallet is wallet software for computers only (no mobile application).


## What is Coinjoin?


The **coinjoin** is a special Bitcoin transaction structure which brings together several participants in a single collaborative transaction. This mechanism mixes the entries of different users into a common transaction, making it extremely difficult - if not often impossible, if done properly - to trace funds. As a result, it becomes almost impossible for an outside observer to identify with certainty the origin and destination of the bitcoins involved, unlike in conventional Bitcoin transactions.


For you, as a user, coinjoin helps preserve your confidentiality. For example, if you receive a donation of 10,000 sats on a Bitcoin address, the sender can trace these funds and, in some cases, deduce that you hold a larger quantity of bitcoins, or observe your activities. By making a coinjoin after this 10,000 sats donation, you break the traceability: the sender will no longer be able to derive any information about you from this payment.


The Chaumian coinjoin offers a high level of security, as the funds remain under the exclusive control of the user at all times. Even the operators of the coordinating servers cannot divert participants' bitcoins under any circumstances. Neither users nor coordinators need to trust each other: each retains control of his or her private keys, and remains solely authorized to validate transactions. No third party can therefore appropriate your bitcoins during a coinjoin, nor establish a direct link between your inputs and outputs.


To learn more about coinjoin, check out Plan ₿ Academy's BTC 204 course :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Install Ginger Wallet


To install Ginger Wallet, visit the website [Ginger Wallet](https://gingerwallet.io).


Press **Download** to download the right version for your computer (Windows / MacOs / Linux).


![screen](assets/fr/03.webp)


Another option is to go to the project's [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) to download it.


![screen](assets/fr/04.webp)


Then run the installation program.


![screen](assets/fr/05.webp)



## Parameter settings


### Preliminary configurations


Open Ginger Wallet, choose your preferred language.


![screen](assets/fr/06.webp)


Right from the start, Ginger reminds you of the costs involved in the coinjoin process.


![screen](assets/fr/07.webp)


Then press **Start**, then **New** to create a new wallet.


![screen](assets/fr/08.webp)


Next, save and confirm your seedphrase.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)


![screen](assets/fr/10.webp)


For added security, Ginger Wallet gives you the option of adding a passphrase.


![screen](assets/fr/11.webp)


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

This passphrase, once added, will be requested every time you try to access your wallet.


![screen](assets/fr/12.webp)


Ginger automatically activates the default **Coinjoin** when you create your wallet. You are informed of this and can then customize the setting to suit your needs.


![screen](assets/fr/13.webp)



### General settings


Once you've created your first wallet, you'll be taken to the Ginger Wallet interface.


![screen](assets/fr/14.webp)


Activate the **Discreet mode**, if you want to hide the balances in your wallets.


![screen](assets/fr/15.webp)


You can create multiple wallets on Ginger Wallet. Just click on **Add a wallet**.


![screen](assets/fr/16.webp)


Ginger supports the use of hardware wallets via the standard Bitcoin Core interface, although direct integration from or to a hardware wallet is not yet available.


Compatible hardware wallets include (but are not limited to) :


- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- etc.


Now click on **Settings**.


![screen](assets/fr/17.webp)


These settings are those of the application in general, and the configurations you make there will apply to all wallets.


In **Settings**, you have the tabs :



- General**


![screen](assets/fr/18.webp)



- Appearance


In this tab, you can change the language, currency and fee display unit (BTC/Satoshi), among others.


![screen](assets/fr/19.webp)



- Bitcoin**


This tab lets you enable Bitcoin Knots to run at application startup, choose your network (Main/RegTest), and your charge rate provider (Mempool Space/Blockstream info/Full Node), etc.


![screen](assets/fr/20.webp)



- Safety features**


In the Security tab, you can enable two-factor authentication, activate or deactivate Tor and even disable it once the Ginger application is closed.


![screen](assets/fr/21.webp)


**NB** :


- For two-factor authentication, make sure your authentication application supports the SHA256 protocol and 8-digit codes. Ginger Wallet requires an 8-digit 2FA code to enhance security. This longer format makes the code much harder to guess or compromise, offering greater protection against unauthorized access.
- By default, all Ginger network traffic passes through Tor, eliminating the need for manual configuration. If Tor is already active on your system, Ginger will automatically give it priority.


But once you deactivate Tor in the settings, your privacy remains generally preserved, except in two situations:


- during a Coinjoin, the coordinator could link your inputs and outputs to your IP address;
- when broadcasting a transaction, a malicious node to which you connect could associate your transaction with your IP.


Don't forget to press **Done** (in the bottom right-hand corner) each time, to save your settings. Some settings require Ginger Wallet to be restarted to take effect.


In addition, the search bar at the top of the wallets lets you search for and access any parameter, etc...


![screen](assets/fr/22.webp)



### Portfolio configuration


Several wallets can be created in the application, so each wallet can be configured to suit your needs. To do so, click on the **three dots** in front of the wallet name, then on **Portfolio settings**.


![screen](assets/fr/23.webp)


As you can see, apart from the wallet parameter, you'll be able to see your UTXOs (list of tokens you own), statistics and wallet information (the extended public key, for example).


To return to our wallet configuration, once you click on wallet parameters, you will be taken to the following tabs:


- General** (where you can change the wallet name) ;


![screen](assets/fr/24.webp)



- Coinjoin** (where you can customize the coinjoin settings for this wallet) ;


![screen](assets/fr/25.webp)



- Tools** (where you can check your seedphrase, synchronize your wallet again, or delete it).


![screen](assets/fr/26.webp)



## Receive bitcoins


![video](https://youtu.be/cqv35wBDWMQ)


To receive bitcoins in your wallet on Ginger Wallet:


- press **Receive** ;


![screen](assets/fr/27.webp)



- Enter the name of the source to which you wish to associate the address. This is labeling to keep track of your payments. This has no on-chain implications; it's simply traceability information stored locally in your application;


https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)



- click on the little arrow to the left of **Generate** to choose your address format (**SegWit** /**Taproot**) , then click on **Generate**, to generate an address and QR code.


![screen](assets/fr/29.webp)


This address or QR code will be used by your sender to send you bitcoins.


![screen](assets/fr/30.webp)



## Send bitcoins



![video](https://youtu.be/2nf5aAimfhg)


To do this :


- Press the **Send** button;
- enter the recipient's address, the amount to be sent and a label;
- check the transaction overview and confirm to send.


![screen](assets/fr/31.webp)



## Spend bitcoins


It's easy to buy and sell Bitcoin with Ginger Wallet. In just a few steps, you can spend your bitcoins.


### Buy bitcoins


![video](https://youtu.be/lEqTBzm5MEA)


Ginger Wallet users can buy bitcoins.



- Press the **Buy** button. This button remains visible even if the wallet is empty.


![screen](assets/fr/32.webp)



- Select your country, or even your state (in some regions, such as Canada), before proceeding with a bitcoin purchase. In fact, when you click on the **Buy** function for the first time, you'll also need to specify your region.


![screen](assets/fr/33.webp)


Press **Continue** to progress through the purchasing process.



- Then enter the amount of bitcoins you wish to purchase in the dedicated field. You can also choose the transaction currency.


![screen](assets/fr/34.webp)


Each currency has a minimum and maximum purchase limit. For example, in USD, the maximum limit is $30,000.


If you have already made a purchase, you can view your transaction history by clicking on the **Previous orders** button. A list of past transactions and their status will be displayed.



- Choose the offer that's right for you.


At this point, you'll see a list of all available offers. For each offer, you have :


 - supplier name (1) ;
 - the number of bitcoins equivalent to the amount previously entered, the payment method and the purchase fee (2) ;
 - the **Accept** button (3).


![screen](assets/fr/35.webp)


The fees indicated in the offer do not constitute an additional cost. They are already included in the total amount of the offer.


The top right-hand corner of the screen, labelled **All**, lets you filter offers by payment method. Your selected payment method will be set by default, but can be changed at any time.


![screen](assets/fr/36.webp)


If you find a suitable offer, click on the **Accept** button to proceed with the purchase. You will then be redirected to the seller's page, where you can finalize the transaction.


### Selling bitcoins


Ginger Wallet users can sell Bitcoin. The **Sell** button is only visible when there are funds available in the wallet.



- Click on **Sell**.


![screen](assets/fr/37.webp)



- As with the **Buy** option, when you use the Sell function for the first time, you must select your country before proceeding with a bitcoin sale.



- Next, you need to enter the amount of Bitcoins you wish to sell. You can enter this amount in BTC or in a fiat currency such as the US dollar (USD).



- Once you've done this, you'll see a list of available offers. Choose a sales offer that suits you, then click **Accept** to continue.



- Now you need to finalize the transaction:
 - Once you have accepted an offer, you will be redirected to the supplier's page;
 - Follow the instructions on the supplier page ;
 - At some point, you will receive a recipient address and the exact amount to send;
 - Then return to Ginger Wallet to continue the process;
 - Once back in Ginger Wallet, a dialog box will appear, allowing you to continue by clicking **Send**.


This will open the **Send** screen with the recipient's address and amount pre-filled. You can also use the **Send** button on the home screen. Although you can send the transaction manually, we recommend you complete it via the dialog box for an optimized process.


## Making a coinjoin on Ginger Wallet


![Vidéo](https://youtu.be/AJe67RDfB1A)


Protect the confidentiality of your bitcoins with **Coinjoin**, integrated directly into Ginger Wallet. The wallet uses **WabiSabi**, a Chaumian coinjoin protocol designed to facilitate more accessible and efficient coinjoins.


It's up to you to choose the coinjoin strategy (automatic or manual) that suits you best.


Ginger Coinjoin is ready to use as soon as you download it (no additional steps required). Automatically, Ginger Coinjoin runs in the background to protect your privacy with every transaction. In practice, the Coinjoin player will appear whenever you have a balance that can be anonymized.


As for manual coinjoin start-up, it's a one-click operation. Start the round and wait for the coinjoin transaction to be built and confirmed. You'll see the anonymization score in the interface.


Several mixes can be performed until the desired level of anonymity is reached. You can also exclude certain parts from the mix.


By default, Ginger uses its own coordinator with all preconfigured parameters and guaranteed fees. Coinjoins of tokens worth more than 0.03 BTC incur a 0.3% coordinator fee in addition to the mining fee. Entries of 0.03 BTC or less, as well as remixes, are exempt from coordinator fees, even after a single transaction. Therefore, a payment made with Coinjoin funds allows both sender and receiver to remix their coins without incurring coordinator fees.


Ginger prefers coinjoins with more participants to smaller, faster rounds. Larger coinjoins offer more anonymity, lower costs and greater efficiency of block space.



## Safety and best practices


The desire for decentralization and the preservation of privacy require the adoption of several best practices:


- Always keep your seedphrase in a safe place off-line;
- If you lose your computer or suspect unauthorized access, create a new wallet immediately. Transfer your funds to this new wallet and delete the old one;
- Use a different address for each reception to avoid reusing addresses;
- Always download your wallet applications exclusively from the official GitHub account or the official website.


Now you're familiar with using the Ginger Wallet application to send, receive and spend your bitcoins.


If you found this tutorial useful, please leave me a green thumb below. Please feel free to share this article via your social media platforms. Thank you so much!


I also suggest you check out this tutorial on how to use the Liana computer application to send and receive bitcoins, as well as implement an automated estate plan.


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04