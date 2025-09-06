---
name: Blockstream App - Liquid
description: How to configure Blockstream App and use the Liquid network
---
![cover](assets/cover.webp)

## 1. Introduction

### 1.1 Tutorial objective



- This tutorial explains how to use the **Blockstream App** mobile application to manage a **Bitcoin Liquid** portfolio, i.e. transactions recorded directly on the Bitcoin "Liquid" side chain.
- It covers installation, initial configuration, creation of a software wallet, and operations for receiving and sending bitcoins on Liquid.
- Note: Other tutorials in the Appendices cover Onchain, Watch-Only and the desktop version.


### 1.2 Target audience



- Beginners**: Users wishing to manage their bitcoins with an intuitive mobile application, integrating the Liquid network.
- Intermediate users**: People seeking to understand onchain functionalities and privacy options such as Tor or SPV.


### 1.3 Introducing Liquid


**Liquid** is a **Sidechain** of Bitcoin, developed by **[Blockstream](https://blockstream.com/Liquid/)**, designed to offer faster, more confidential transactions and advanced functionality, while remaining connected to the main Blockchain Bitcoin.


A Sidechain is an independent Blockchain that operates in parallel with Bitcoin, using a mechanism known as **two-way peg**. This system locks bitcoins onto the main Blockchain to create **Liquid-Bitcoins (L-BTC)**, tokens that circulate on the Liquid network while retaining parity of value with the original bitcoins. Funds can be returned to Blockchain Bitcoin at any time.


![image](assets/fr/17.webp)




- (1) Peg-in**: Bitcoins (BTC) are locked onto the main Blockchain by the Liquid federation. In return, an equivalent amount of Liquid-Bitcoins (L-BTC), ensuring parity between the two chains, is issued on the Blockchain Liquid and sent to the user.



- (2) Independent transactions** : Transactions can run simultaneously and independently on the main Blockchain (BTC) and Sidechain Liquid (L-BTC), depending on user requirements.



- (3) Peg-out**: The user sends Liquid-Bitcoins (L-BTC) back to the Liquid federation. The federation then unlocks an equivalent amount of bitcoins (BTC) on the main Blockchain and transfers them to the user.


Liquid relies on a **federation** of trusted participants (exchanges, recognized Bitcoin companies) who manage block validation and bilateral anchoring. Unlike Blockchain Bitcoin, which is decentralized and relies on miners, Liquid is a **federated** network, meaning that its security and governance depend on these participants. Although this implies a compromise on decentralization, it enables optimized performance and advanced functionality.


![image](assets/fr/18.webp)


##### Why use Liquid?



- Speed**: Transactions on Liquid are confirmed in around **1 minute**, compared with 10 minutes or more for onchain transactions, thanks to blocks generated every minute by a federation of validators.
- Enhanced confidentiality**: Liquid uses **Confidential Transactions**, which hides the amount and type of asset transferred, making transactions more private (although addresses remain visible).
- Low fees** : Transactions on Liquid are generally less expensive, making them ideal for frequent transfers or small amounts.
- Multiple assets**: In addition to L-BTCs, Liquid supports the issuance of other digital assets, such as stablecoins or tokens, for use in specific applications.
- Use cases**: Liquid is particularly suitable for cross-platform exchanges, fast payments, or applications requiring smart contracts, while remaining linked to the security of Bitcoin.


**Note: This tutorial focuses on using Liquid via the Blockstream App. For an in-depth understanding of the Liquid network, you'll find resources in the appendix.


### 1.4. Hot wallet reminder



- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **software wallet**: all names for an application installed on a smartphone, computer or any device connected to the Internet, enabling private keys from a Bitcoin wallet to be managed and secured.
- Unlike **hardware wallets**, also known as **Cold wallets**, which isolate keys offline, software wallets operate in a connected environment, making them more vulnerable to cyber-attacks.



- Recommended use** :
    - Ideal for managing moderate amounts of bitcoin, especially for daily transactions.
    - Suitable for beginners or users with limited assets, for whom a Hardware Wallet may seem superfluous.



- Limitations**: Less secure for storing large funds or long-term savings. In this case, choose a Hardware Wallet.



## 2. Introducing Blockstream App



- Blockstream App** is a mobile (iOS, Android) and desktop application for managing Bitcoin wallets and assets on the Liquid network. Acquired by [Blockstream](https://blockstream.com/) in 2016, it was previously named *Green Address* and then *Blockstream Green*.
- Key features** :
    - Onchain** transactions on Blockchain Bitcoin.
    - Transactions on the **Liquid** network (Sidechain for fast, confidential exchanges).
    - Watch-only** portfolios for monitoring funds without access to keys.
    - Privacy options: connection via **Tor**, connection to a **personal node** via Electrum, or **SPV** verification to reduce dependency on third-party nodes.
    - Functions **Replace-by-fee (RBF)** to speed up unconfirmed transactions.
- Compatibility**: Integrates hardware wallets such as **Blockstream Jade**.
- Interface**: Intuitive for beginners, with advanced options for experts.
- Note**: This guide focuses on onchain use. Other tutorials in the Appendices cover Onchain, Watch-Only and the desktop version.



## 3. Installing and configuring the Blockstream App


### 3.1. download



- For Android** :
    - Download [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) from the Google Play Store.
    - Alternative: Install via the APK file available on [Blockstream's official GitHub](https://github.com/Blockstream/green_android).
- For iOS** :
    - Download [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) from the App Store.
- Note**: Be sure to download from official sources to avoid fraudulent applications.


### 3.2. initial configuration



- Home screen**: When first opened, the application displays a screen without a configured wallet. Created or imported portfolios will appear here later.


![image](assets/fr/02.webp)



- Customize settings**: Click on "Application settings", adjust the options below, click on "Save", restart the application and create your portfolio.


![image](assets/fr/03.webp)


#### 3.2.1. Enhanced privacy (Android only)



- Function**: Disables screenshots, hides application previews in the task manager, and locks access when the phone is locked.
- Why?** : Protects your data against unauthorized physical access or screen-capturing malware.


#### 3.2.2. Connection via Tor



- Function**: Route network traffic via **Tor**, an anonymous network that encrypts your connections.
- Why?**: Hide your IP address and protect your privacy, ideal if you don't trust your network (public Wi-Fi, for example).
- Disadvantage**: May slow down the application due to encryption.
- Recommendation**: Activate Tor if confidentiality is a priority, but test connection speed.


#### 3.2.3. Connecting to a personal node



- Function**: Connects the application to your own **complete Bitcoin node** via a **Electrum server**.
- Why?**: Provides total control over Blockchain data, eliminating dependency on Blockstream servers.
- Prerequisite**: A configured Bitcoin node.
- Recommendation**: Advanced users who want maximum sovereignty.


#### 3.2.4. SPV verification



- Function**: Uses **Simplified Payment Verification (SPV)** to directly verify certain Blockchain data without downloading the entire chain.
- Why?**: Reduces dependency on Blockstream's default node, while remaining lightweight for mobile devices.
- Disadvantage**: Less secure than a full node, as it relies on third-party nodes for some information.
- Recommendation**: Activate SPV if you can't use a personal node, but prefer a full node for optimum security.




## 4. Creating a Bitcoin onchain portfolio


### 4.1. Start creation



- Caution**: Set up your portfolio in a private environment, without cameras or observers.
- From the home screen, click on "Get Started" :


![image](assets/fr/04.webp)



- If you want to manage a **Cold Wallet** (offline wallet): click on **"Connect Jade "** to use the Hardware Wallet Blockstream Jade or other compatible Cold wallets.


![image](assets/fr/05.webp)




- The next screen appears:


![image](assets/fr/06.webp)




- (1) **"Setup Mobile Wallet"** : Create a new hot wallet (Hot Wallet).
- (2) **"Restore from Backup "**: Import an existing portfolio using a mnemonic phrase (12 or 24 words). Warning: Do not import the phrase from a Cold Wallet, as it will be exposed on a connected device, invalidating its security.
- (3) **"Watch-Only "**: Import an existing read-only portfolio, to view the balance (e.g. of your Cold Wallet) without exposing the mnemonic phrase. See the "Watch Only" tutorial in the appendix.


**In this tutorial**: Click on **"Setup Mobile Wallet"** to create a Hot Wallet.

Your Wallet is automatically created and the Wallet home page, here called "My Wallet 5", is displayed:


![image](assets/fr/07.webp)


**Important**: Blockstream App has simplified the creation of a Wallet by not automatically displaying the 12-word seed phrase. *Even though the portfolio is now created in one click, you risk losing access to your funds if you don't save your seed phrase*.


### 4.2. Save seed phrase



- On the Wallet home screen, click on the "Security" tab, then on the "Back Up" prompt or the "Recovery Phrase" menu:


![image](assets/fr/08.webp)


The seed 12-word phrase will be displayed for you to save.



- Write down your recovery phrase with the utmost care. Write it down on paper or metal and keep it in a safe place (safe, offline location). This phrase is your only means of accessing your bitcoins in the event of loss of your device or deletion of the application.
- It's also important to note that anyone with this phrase can steal all your bitcoins. Never store it digitally:
 - No screenshot
 - No cloud, email or messaging backups
 - No copy/paste (risk of saving to clipboard)


**! This point is critical**. For more information on backup :


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Check seed sentence


Before sending funds to an address associated with this seed phrase, you must test the backup of your 12 words.

To do this, we'll write down a reference, delete the Wallet, restore it with the backup, and check that the reference is unchanged.



- On the Wallet home screen, click on the "Settings" tab, then on "Wallet Details", and copy the zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):


![image](assets/fr/09.webp)


Note: a zpub address can be imported into your Blockstream application for the "Watch Only" function (see Appendix).



- Delete the application, then restore the wallet via **"Restore from Backup "** by entering the mnemonic phrase, and check that the zpub is unchanged. If yes, then your backup is correct, and you can send funds to the Wallet.



- To learn more about how to perform a recovery test, here is a dedicated tutorial :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Securing access to the application


Lock access to the application with a strong PIN code:


- From the Wallet home screen, go to **"Security "** then click on **"PIN "**
- Enter and confirm **a random 6-digit PIN code**.


**Biometric option**: Available for added convenience, but less secure than a robust PIN code (risk of unauthorized access, e.g. fingerprint or face scan during sleep).


**Note**: The PIN secures the device, but only the seed phrase can be used to recover funds.




## 5. Using the Liquid wallet


### 5.1. Receive "L-BTC" bitcoins


To receive Liquid-Bitcoins (L-BTC), several options are available. You can ask someone to send you some directly by sharing a Liquid receiving address, which is detailed below.


Alternatively, exchange your bitcoins onchain or via the Lightning network for L-BTC using [a bridge such as Boltz](https://boltz.Exchange/): enter your Liquid receiving address, make payment as you prefer, and receive your L-BTC.



- From the portfolio home screen, click on '"**Transact**" then **"Receive "**.


![image](assets/fr/19.webp)



- By default, the application displays a blank **receipt address, onchain** (SegWit v0 format, starting with `bc1q...`). Click on "Bitcoin" to select **Liquid Bitcoin** :


![image](assets/fr/20.webp)



- Options** :
 - (1) Click on the arrows to select another new address linked to this seed sentence.
    - (2) You can also choose an address from among those already used/displayed, by clicking on the three dots at top right and then on "List of Addresses"
    - (3) To request a specific amount, click on the three dots at top right, select "Request amount", and enter the desired amount. The QR will be updated, and the address will be replaced by a Bitcoin payment URI.


![image](assets/fr/21.webp)



- Share the address/URI by clicking on "**Share**", copying the text or scanning the QR code.
- Verification**: Check the address shared with the recipient as far as possible to avoid errors or attacks (e.g. malware modifying the clipboard).


### 5.2. send bitcoins



- From the portfolio home screen, click on "**Transact**" then **"Send "** :


![image](assets/fr/22.webp)



- Enter details** :
    - (1) Enter the **address of the recipient** by sticking it on or scanning a QR code.
    - (2) Check the assets and the account from which the funds are being sent.
    - (3) Indicate the **amount** to be sent. You can choose the unit: L-BTC, L-satoshis, USD, ...


![image](assets/fr/23.webp)



- Check** :
    - Check the address, amount and charges on the summary screen.
    - An address error can result in irreversible loss of funds. Beware of malware that modifies the clipboard.


![image](assets/fr/24.webp)



- Confirmation**: Slide the "Send" button to sign and distribute the transaction.
- Follow-up**: In the Wallet "Transact" tab, the transaction appears as "Unconfirmed", then "Confirmed", then "Completed":


![image](assets/fr/25.webp)



- The time between 2 blocks is 1 minute on Liquid, so the transaction is quickly confirmed and completed.



## Appendices


### A1. Other Blockstream App tutorials


Using the Onchain network


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importing and tracking a Wallet in "Watch Only" mode


https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop version


https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Best practices


To use **Blockstream App** securely and efficiently, follow these recommendations. They will help you protect your funds, optimize your transactions, and preserve your confidentiality on the **Bitcoin (onchain)**, **Liquid**, and **Lightning** networks.



- Secure your recovery phrase** :
 - Tutorial: Saving your mnemonic phrase


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- Use secure authentication** :
 - Activate a **strong PIN** or **biometric authentication** (fingerprint or facial recognition) to protect access to the application.
 - Never share your PIN or biometric data.



- Protect your privacy** :
 - Generate a new address for each onchain reception or Liquid to limit tracing on the Blockchain.
 - Activate the "Enhanced Privacy", "Tor" and "SPV" functions.
 - For maximum confidentiality, connect your Wallet to your own Bitcoin node via an Electrum server instead of using the public node



- Choose the network best suited to your needs** :
 - Onchain**: Preferred for long-term custody or large-value transactions (fees negligible in relation to amount).
 - Liquid**: Use for fast, low-cost transfers with enhanced confidentiality.
 - Lightning**: Choose instant, low-cost transfers for small amounts.



- Always check shipping addresses** :
 - Before sending funds, check the address carefully. Funds sent to the wrong address are lost forever. Use copy/paste or QR code scanning, never copy/modify an address by hand.



- Optimize costs** :
 - For onchain transactions, choose appropriate fees (slow, medium, fast) according to urgency and network congestion.
 - Use Liquid, or Lightning for small amounts.



- Keep the application up to date



### A3. Additional resources



- Official links:**
 - [Official website](https://blockstream.com/)**
 - [Support for the mobile application](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentation and chat
 - [GitHub](https://github.com/Blockstream/green_android)**



- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lightning: **[1ML (Lightning Network)](https://1ml.com/)**



- Learning and tutorials:** **[Plan ₿ Network](https://planb.network/)** :
 - Securing your recovery phrase


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- Liquid Network** :
 - [Glossary](https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- Lightning Network** :
 - [Glossary](https://planb.network/fr/resources/glossary/lightning-network)**


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
