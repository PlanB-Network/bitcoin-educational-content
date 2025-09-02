---
name: Blockstream App - Watch-Only
description: How do I configure a Watch-only wallet on Blockstream App?
---

![cover](assets/cover.webp)

## 1. Introduction

### 1.1 Objective of the tutorial



- This tutorial explains how to set up and use the **Watch-Only** feature of the **Blockstream App** mobile application to monitor a Bitcoin wallet without accessing its private keys.
- It covers installation, initial configuration, importing an extended public key, and using it to track balances and generate receiving addresses.
- Note: Other tutorials, provided in the appendix, cover Onchain, Liquid and the desktop version.


### 1.2. Target audience



- Beginners**: Users wishing to monitor a Bitcoin portfolio (often associated with a Hardware Wallet) via an intuitive mobile application.
- Intermediate users**: People looking to manage read-only portfolios while using privacy options such as Tor or SPV.
- Hardware wallet owners**: To check their balances and generate addresses without connecting their device.
- Businesses and shops** :
 - Track your transactions for accounting purposes without exposing your private keys.
 - Verify transactions received without entering their private keys in online payment systems.
 - Enable employees to generate new reception addresses without having access to private keys.
- Organizations and crowdfunding**: Display the balance transparently to donors without allowing access to funds.


### 1.3. Introducing Watch-Only


A **Watch-Only** wallet allows you to monitor the transactions and balance of a Bitcoin wallet without having access to the private keys. Unlike a conventional wallet, it stores only public data, such as the **extended **public key** (which gave rise to "**xpub**", then "zpub", "ypub", etc.), which enables it to obtain receiving addresses and track transaction history on the Blockchain Bitcoin. The absence of private keys makes it impossible to disburse funds from the application, guaranteeing enhanced security.


![image](assets/fr/10.webp)


**Why use a Watch-Only wallet?



- Security**: Ideal for monitoring a portfolio secured by a **Hardware Wallet** without exposing private keys on a connected device.
- Convenience**: Allows you to check the balance and generate new recipient addresses without connecting the Hardware Wallet.
- Confidentiality**: Compatible with options such as **Tor** or **SPV** to limit dependency on third-party servers.
- Use cases**: Tracking funds on the move, generating addresses to receive payments, or verifying transactions without risking private keys.


![image](assets/fr/01.webp)


### 1.4. Extended public keys


An **extended public key** (xpub, ypub, zpub, etc.) is a piece of data derived from a Bitcoin wallet that generates all child public keys and their associated receive addresses, without giving access to the private keys.



- How it works** : The extended public key is generated from the seed phrase via a deterministic process (BIP-32). It creates a hierarchical tree of child public keys, each of which can be converted into a receive address. Using the same derivation path (e.g. `m/44'/0'/0'`) as the watched wallet, the Watch-Only wallet generates the same addresses, enabling funds to be tracked and new receive addresses to be created.


![image](assets/fr/11.webp)



- Extended public key types
 - xpub**: Used for Legacy portfolios (addresses starting with "1", BIP-44) and Taproot portfolios (addresses starting with "bc1p", BIP-86).
 - ypub**: Designed for compatible SegWit wallets (addresses starting with "3", BIP-49).
 - zpub**: Associated with native SegWit portfolios (addresses starting with "bc1q", BIP-84).
 - Others (tpub, upub, vpub, etc.)**: Used for alternative networks (such as Testnet) or specific standards. For example, tpub is for the Testnet network.



- Distinction** : The choice between xpub, ypub, or zpub depends on the address type (legacy, SegWit, Taproot or nested SegWit) and the BIP standard used by the wallet. Check the format required by your source portfolio to ensure compatibility with Blockstream App.



- Security and confidentiality** : The extended public key is not sensitive in terms of security, as it does not allow funds to be spent (no access to private keys). However, it is sensitive in terms of confidentiality, as it reveals all public addresses and associated transaction history.


**Recommendation**: Protect your extended public key as sensitive information.


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot wallet reminder



- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **software wallet**: all names for an application installed on a smartphone, computer or any device connected to the Internet, enabling private keys from a Bitcoin wallet to be managed and secured.
- Unlike **hardware wallets**, also known as **Cold wallets**, which isolate keys offline, software wallets operate in a connected environment, making them more vulnerable to cyber-attacks.



- Recommended use** :
    - Ideal for managing moderate amounts of bitcoin, especially for daily transactions.
    - Suitable for beginners or users with limited assets, for whom a Hardware Wallet may seem superfluous.



- Limitations**: Less secure for storing large funds or long-term savings. In this case, choose a Hardware Wallet.



## 2. Introducing Blockstream App



- Blockstream App** is a mobile (iOS, Android) and desktop application for managing Bitcoin portfolios and assets on the Liquid network. Acquired by [Blockstream](https://blockstream.com/) in 2016, it was previously named *Green Address* and then *Blockstream Green*.
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



- Function**: Connects the application to your own **complete Bitcoin node** via an **Electrum server**.
- Why?**: Provides total control over Blockchain data, eliminating dependency on Blockstream servers.
- Prerequisite**: A configured Bitcoin node.
- Recommendation**: Advanced users who want maximum sovereignty.


#### 3.2.4. SPV verification



- Function**: Uses **Simplified Payment Verification (SPV)** to directly verify certain Blockchain data without downloading the entire chain.
- Why?**: Reduces dependency on Blockstream's default node, while remaining lightweight for mobile devices.
- Disadvantage**: Less secure than a full node, as it relies on third-party nodes for some information.
- Recommendation**: Activate SPV if you can't use a personal node, but prefer a full node for optimum security.




## 4. Creating a Bitcoin "Watch-only" portfolio


### 4.1. Recover extended public key


To set up a Watch-Only wallet, you must first obtain the extended public key (xpub, ypub, zpub, etc.) of the wallet to be monitored. This information is generally available in the settings or "wallet information" section of your software or Hardware Wallet.



- Example with Blockstream App: From the wallet home screen, go to "Settings", then "Wallet Details", and copy the zpub :


![image](assets/fr/09.webp)



- Alternative 1: Generate a QR code containing the extended public key for scanning in the next step.
- Alternative 2: Use a output descriptor if your wallet provides it.


### 4.2. import Wallet Watch-only



- Caution**: Set up your portfolio in a private environment, without cameras or observers.
- From the home screen, click on "Set up a new portfolio" and then on "Get Started" :


![image](assets/fr/04.webp)



- The next screen appears:


![image](assets/fr/06.webp)




- (1) **"Setup Mobile Wallet"** : Create a new Hot Wallet. See the "Blockstream App - Onchain" tutorial in the appendix.
- (2) **"Restore from Backup "**: Import an existing portfolio using a mnemonic phrase (12 or 24 words). Caution: Do not import the phrase from a Cold Wallet, as it will be exposed on a connected device, invalidating its security.
- (3) **"Watch-Only "**: the option we're interested in for this tutorial.



- Then select "**Single signature**" and the "**Bitcoin**" network:


![image](assets/fr/12.webp)



- Paste the extended public key (xpub, ypub, zpub, etc.), scan the corresponding QR code, or enter a output descriptor. Even if the application specifies "xpub", the keys ypub, zpub, etc. are also authorized. Then click on "Connect":


![image](assets/fr/13.webp)



### 4.3. Using the Wallet Watch-only


Once imported, the Watch-Only wallet displays the total balance and transaction history of addresses derived from the extended public key. Only onchain transactions are visible (Liquid transactions are ignored). To monitor a Liquid wallet, repeat the import by selecting "Liquid" in the previous step.



- View balance and history**: from the home screen, view total balance and onchain transaction history:


![image](assets/fr/14.webp)



- Generate a receiving address**: Click on "Transact", then "Receive", to create a new onchain address. Share it via QR code or copy to receive funds:


![image](assets/fr/15.webp)



- Send funds**: Click on **"Transact "**, then **"Send "**. You can enter :
 - The recipient's address.
 - The amount of the transaction.
 - Transaction fees.


However, as the Watch-Only wallet does not hold the private keys, you cannot send funds directly. To sign the transaction, connect your Hardware Wallet or exchange PSBTs by scanning the QR codes (an option available on the Coldcard Q, for example).


![image](assets/fr/16.webp)



- Note**: Always check the receiving address and transaction details to avoid errors. Funds sent to the wrong address cannot be recovered.



## Appendices


### A1. Other Blockstream App tutorials



- Using the Onchain network :


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143


- Using the Liquid network :


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a


- Desktop version :


https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Extended public keys



- Glossary :
 - [Extended public keys](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Course :
 - [Les clés publiques étendues](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/les-cles-etendues-8dcffce1-31bd-5e0b-965b-735f5f9e4602)



### A3. Best practices


To use **Blockstream App** securely and efficiently, follow these recommendations. They will help you protect your funds, optimize your transactions, and preserve your confidentiality on the **Bitcoin (onchain)**, **Liquid**, and **Lightning** networks.



- Secure your recovery phrase** :
 - Tutorial: Saving your mnemonic phrase


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- Use secure authentication** :
 - Activate a **strong PIN** or **biometric authentication** (fingerprint or facial recognition) to protect access to the application.
 - Never share your PIN or biometric data.



- Protect your privacy** :
 - Generate a new address for each onchain or Liquid reception to limit tracing on the Blockchain.
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



### A4. Additional resources



- Official Blockstream links:**
 - [Official website](https://blockstream.com/)**
 - [Support for the mobile application](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentation and chat
 - [GitHub](https://github.com/Blockstream/green_android)**



- Block Explorers :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lightning: **[1ML (Lightning Network)](https://1ml.com/)**



 - Learning and tutorials:** **[Plan ₿ Network](https://planb.network/)** :
  - Securing your recovery phrase


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- Liquid Network** :
 - [Glossary](https://planb.network/fr/resources/glossary/Liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- Lightning Network** :
 - [Glossary](https://planb.network/fr/resources/glossary/lightning-network)**


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb