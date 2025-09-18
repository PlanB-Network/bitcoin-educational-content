---
name: Blockstream App - Desktop
description: How to use your Hardware Wallet with Blockstream App on a computer?
---
![cover](assets/cover.webp)


## 1. Introduction


### 1.1 Tutorial objective



- This tutorial explains how to use the **Blockstream App** on a computer to manage a Bitcoin **onchain** wallet with a **Hardware Wallet**, enabling secure transactions recorded on the main Blockchain Bitcoin.
- It covers installation, initial configuration, connecting a Hardware Wallet, and receiving and sending onchain bitcoins.
- Note: Other tutorials in the Appendices cover Liquid, Watch-Only and the mobile application.


### 1.2 Target audience



- **Beginners**: Users wishing to manage their bitcoins with secure desktop software and a Hardware Wallet.
- **Intermediate users**: People looking to understand how to use a Hardware Wallet for onchain transactions and privacy options like Tor or SPV.


### 1.3. Background on hardware wallets



- **Hardware Wallet**, **Cold Wallet**: A physical device that stores private keys offline, offering a high level of security against cyber-attacks, unlike **Hot wallets** (software wallets on connected devices).
- **Recommended use**:
    - Ideal for securing large amounts or long-term savings.
    - Suitable for security-focused users who want to protect their funds from the risks associated with connected devices.
- **Limitations**: Requires software such as Blockstream App to view balances, generate addresses, and broadcast Hardware Wallet-signed transactions.


## 2. Introducing Blockstream App



- **Blockstream App** is a mobile (iOS, Android) and desktop application for managing Bitcoin wallets and assets on the Liquid network. Acquired by Blockstream in 2016, it was called *GreenAddress*, was renamed *Blockstream Green* (2019), and is now called *Blockstream app* (2025).
- **Key features**:
- **Onchain** transactions on Blockchain Bitcoin.
    - Transactions on the **Liquid** network (Sidechain for fast, confidential exchanges).
- **Watch-only** portfolios for monitoring funds without access to keys.
    - Privacy options: connection via **Tor**, connection to a **personal node** via Electrum, or **SPV** verification to reduce dependency on third-party nodes.
    - Functions **Replace-by-fee (RBF)** to speed up unconfirmed transactions.
- **Compatibility**: Integrates hardware wallets such as **Blockstream Jade**.
- **Interface**: Intuitive for beginners, with advanced options for experts.
- **Note**: This guide focuses on onchain use with a Hardware Wallet on the desktop version. Other tutorials provided as appendices cover use on mobile application, for onchain, Liquid, and Watch-Only features.


## 3. Installing and setting up Blockstream App Desktop


### 3.1. download



- Go to the [official website](https://blockstream.com/app/) and click on "_Download Now_". Download the version corresponding to your operating system (Windows, macOS, Linux).
- **Note**: Be sure to download from the official source to avoid fraudulent software.


### 3.2. initial configuration



- **Home screen**: When first opened, the application displays a screen without a configured wallet. Created or imported portfolios will appear here later.


![image](assets/fr/02.webp)



- **Customize settings**: Click on the settings icon at bottom left, adjust the options below, then exit the Interface to continue.


![image](assets/fr/03.webp)


#### 3.2.1. General parameters



- In the Settings menu, click on "**General**".
- **Function**: Change the software language and activate experimental functions if required.


![image](assets/fr/04.webp)


#### 3.2.2. Connection via Tor



- In the Settings menu, click on "**Network**".
- **Function**: Route network traffic via **Tor**, an anonymous network that encrypts your connections.
- **Why?**: Hide your IP address and protect your privacy, ideal if you don't trust your network (public Wi-Fi, for example).
- **Disadvantage**: May slow down the application due to encryption.
- **Recommendation**: Activate Tor if confidentiality is a priority, but test connection speed.


![image](assets/fr/05.webp)


#### 3.2.3. Connecting to a personal node



- In the Settings menu, click on "**Custom servers and validation**".
- **Function**: Connects the application to your own **complete Bitcoin node** via an **Electrum server**.
- **Why?**: Provides total control over Blockchain data, eliminating dependency on Blockstream servers.
- **Prerequisite**: A configured Bitcoin node.
- **Recommendation**: Advanced users who want maximum sovereignty.


![image](assets/fr/06.webp)


https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV verification



- In the Settings menu, click on "**Custom servers and validation**".
- **Function**: Uses **Simplified Payment Verification (SPV)** which downloads block headers and verifies your transactions by proof of inclusion (Merkle), without storing the complete Blockchain.
- **Why?**: Reduces dependency on Blockstream's default node, while remaining lightweight for devices.
- **Disadvantage**: Less secure than a full node, as it relies on third-party nodes for some information.
- **Recommendation**: Activate SPV if you can't use a personal node, but prefer a full node for optimum security.


![image](assets/fr/07.webp)


## 4. Connecting a Hardware Wallet to Blockstream App


### 4.1. Preliminary considerations


#### 4.1.1. For Ledger users



- Blockstream Green only supports the **Bitcoin Legacy** application on Ledger devices (Nano S, Nano X).
- Steps to follow in **Ledger Live** before connecting your device :

1. Go to **"Settings "** → **"Experimental features "** and activate **developer mode**.

2. Go to **"My Ledger"** → **"App Catalogue "**, then install the **Bitcoin Legacy** application

3. Open the **Bitcoin Legacy** application on your Ledger before launching Blockstream Green to establish the connection.


- **Note**: Make sure your Ledger is unlocked with your PIN code and that the Bitcoin Legacy application is active when you connect.


#### 4.1.2 Initializing a Hardware Wallet



- If your Hardware Wallet (Ledger, Trezor, or Blockstream Jade) has never been used (either with Blockstream Green, or with other software such as Ledger Live), you will first need to initialize it. This step involves, in a secure environment, without cameras or observers:

1. **seed phrase generation / mnemonic phrase** (12, 18 or 24 words): Write it down carefully on a piece of paper.

2. **seed phrase verification**: Test the Wallet import from the noted words, e.g. by verifying the extended public key. To be carried out before sending funds to Wallet and permanently securing the seed phrase.

3. **Securing the seed phrase**: Store the phrase on a physical medium (paper or metal) and in a safe place. Never store it digitally (no screenshots, cloud, or email).


- **Important**: The seed phrase is your only means of recovering your funds if the device is lost or malfunctions. Anyone with access can steal your bitcoins.
- **Resources** for backing up and checking the seed sentence:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Configuration for this tutorial :



- We'll assume that the Hardware Wallet has already been initialized with a seed phrase and a locking PIN code.
- We assume that the Hardware Wallet has never been connected to Blockstream App, which requires the creation of a new account. If the Hardware Wallet has already been used with Blockstream App, the account will automatically appear when the application is opened.


### 4.2. Start connection



- From the home screen, click on "**Setup a New Wallet**", then validate the terms and conditions and click on "**Get Started**" :


![image](assets/fr/08.webp)



- Select the "**On Hardware Wallet**" option:


![image](assets/fr/09.webp)



- If you're using a **Blockstream Jade**, click on the corresponding button. Otherwise, select "**Connect a different Hardware Device**" :


![image](assets/fr/10.webp)



- Connect your Hardware Wallet to the computer via USB and select it in Blockstream App :


![image](assets/fr/22.webp)



- Please wait while Blockstream App imports your portfolio information:


![image](assets/fr/23.webp)


### 4.3. Create an account



- If your Hardware Wallet has already been used with Blockstream App, your account will automatically appear in the Interface after import. Otherwise, create an account by clicking on "**Create Account**" :


![image](assets/fr/24.webp)



- Choose "**Standard**" to configure a classic Bitcoin portfolio:


![image](assets/fr/25.webp)



- Once your account has been created, you can access your main Interface portfolio:


![image](assets/fr/26.webp)




## 5. Using the onchain wallet with a Hardware Wallet


### 5.1. Receive bitcoins



- From the main portfolio screen, click on "**Receive**" :


![image](assets/fr/27.webp)



- The application displays a **blank reception address**. Using a new address for each reception improves your confidentiality. Click on "**Copy Address**" to copy the address, or let the sender scan the QR code displayed:


![image](assets/fr/12.webp)


**Options** :


- (1) Click on the arrows to generate a new address linked to your portfolio.
- (2) To request a specific amount, click on "**More options**" and then on "**Request Amount**". The QR will be updated, and the address will be replaced by a Bitcoin payment URI such as: `Bitcoin:bc1q...?amount=0.00001`


![image](assets/fr/13.webp)



- (3) To reuse a previous address, click on "**More options**" then on "**List of addresses**" :


![image](assets/fr/14.webp)



- **Verification**: Carefully check the shared address to avoid errors or attacks (e.g. malware modifying the clipboard).
- Once the transaction has been broadcast on the network, it will appear in your wallet. Wait for 1 to 6 confirmations to consider the transaction unchangeable.


![image](assets/fr/28.webp)


### 5.2. send bitcoins



- From the main portfolio screen, click on "**Send**".


![image](assets/fr/29.webp)



- Enter details:
    - (1) Check that the asset selected is **Bitcoin** (onchain).
    - (2) Enter the **address of the recipient** by pasting it or scanning a QR code with your webcam.
    - (3) Indicate the **amount** to be sent (in BTC, satoshis, or other units).



![image](assets/fr/16.webp)



- Select **transaction fees** (optional) :
 - Choose from the suggested options (fast, medium, slow) according to urgency, with an estimated confirmation time.
 - For customized charges, manually adjust the number of satoshis per vbyte. These are shown on the home screen. See also [Mempool.space](https://Mempool.space/).


![image](assets/fr/17.webp)



- **Manual selection of UTXOs** (optional): Click on "**Manual Coin selection**" to choose the specific UTXOs to be used in the transaction.


![image](assets/fr/18.webp)



- **Preliminary verification**: Check the address, amount and fees on the summary screen, then click on "**Confirm transaction**". In reality, the transaction will not be released to the network until you have signed it with your Hardware Wallet, which alone has the secret keys associated with the addresses from which UTXOs (satoshis) will be debited.


![image](assets/fr/19.webp)



- **Final check and signature**: Make sure all transaction parameters are correct **on your Hardware Wallet** screen, then sign the transaction using it. An address error may result in irreversible loss of funds.



- **Broadcast**: Once signed, Blockstream App automatically broadcasts the transaction on the Bitcoin network.


![image](assets/fr/20.webp)



- **Follow-up**:
 - The transaction appears in the Wallet home screen as "pending" until confirmed.
 - As long as the transaction has not been confirmed, the **Replace-by-fee (RBF)** function can be used to speed up confirmation by increasing the fee (see Appendix).


![image](assets/fr/21.webp)


## Appendices


### A1. Other Blockstream tutorials



- Using the Liquid network :


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a


- Import and track a portfolio in "Watch-Only" :


https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb


- Using the Blockstream App on cell phones (Hot Wallet) :


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Explanation of Replace-by-fee (RBF)



- **Definition**: Replace-by-fee (RBF) is a feature of the Bitcoin network that allows the sender to accelerate the confirmation of an **onchain** transaction by increasing the fee.
- **Limits**:
    - RBF is not available for Liquid or Lightning transactions.
    - The initial transaction must be marked as RBF-compatible, which Blockstream App does automatically.
- For more information, see [our glossary](https://planb.network/resources/glossary/rbf-replacebyfee).


### A3. Best practices



- **Secure your recovery phrase**:
    - Save your Hardware Wallet's mnemonic phrase on a physical medium (paper, metal) in a safe place.
    - Never store it digitally (cloud, email, screenshot).
    - Tutorial : Save your mnemonic phrase :


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


- **Protect your privacy**:



    - Generate a new address for each onchain reception.
    - Activate **Tor** or **SPV** to limit tracking.
    - Connect to your own Bitcoin node via Electrum for maximum sovereignty.
- **Always check shipping addresses**:



    - Check the address on your Hardware Wallet screen before signing.
    - Use copy/paste or a QR code to avoid manual errors.
- **Optimize costs**:



    - Adjust charges according to urgency and network congestion (see [Mempool.space](https://Mempool.space/)).
    - Use Liquid or Lightning for fast, low-cost transactions that do not require onchain security.
- Update the software:



    - Keep your Blockstream App and Hardware Wallet firmware up to date with the latest features and security patches.


### A4. Additional resources



- **Official links**:
    - [Official website](https://blockstream.com/)
    - [Support for Blockstream App](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentation and chat
    - [GitHub](https://github.com/Blockstream/green_qt)



- **Block Explorers**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Lightning : [1ML (Lightning Network)](https://1ml.com/)



- **Securing your recovery phrase:**


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


- **Liquid Network** :


[Glossary](https://planb.network/fr/resources/glossary/liquid-network)


https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727


- **Lightning Network**:


[Glossary](https://planb.network/fr/resources/glossary/lightning-network)


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb