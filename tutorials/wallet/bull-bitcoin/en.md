---
name: Bull Bitcoin Wallet
description: Find out how to use the Wallet Bull Bitcoin
---

![cover](assets/cover.webp)

![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)

*This video tutorial from BTC Sessions walks you through the process of setting up and using Bull Bitcoin Wallet!*

This guide takes you through the installation, configuration and use of Bull Bitcoin Wallet. You'll learn to send and receive funds on the Bitcoin On-Chain, Liquid, and Lightning networks, as well as how to move Bitcoin between them. The wallet's extensive features make it a powerful, all-in-one tool for managing your Bitcoin. Let's get started.

## Introduction

Bull Bitcoin Wallet, developed by [Bull Bitcoin](https://www.bullbitcoin.com/), is a **self-custodial** Bitcoin wallet, which means you have full control over your private keys and therefore your funds, without depending on a third party. Open-source and rooted in a Cypherpunk philosophy, this Wallet combines simplicity, confidentiality and advanced features such as cross-network swaps and PayJoin support. It lets you manage your bitcoins on three networks: **Bitcoin onchain**, **Liquid** and **Lightning**, each tailored to specific uses. On the [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), you can check out current topics and upcoming developments. As the project is 100% open-source and "built in public", you can also send your suggestions and any bugs you encounter. While some wallets now support multiple networks, the Bull Bitcoin Wallet stands out by deeply integrating privacy features across all of them, making it a powerful tool for managing your Bitcoin across all major networks

## 1️⃣ Prerequisites

Before you start using **Bull Bitcoin Wallet**, make sure you have the following items:

- **Compatible Smartphone**: A **iOS** (iPhone or iPad) or **Android** device
- Internet connection
- **Secure backup media**: Write down your **recovery phrase** (12 words) on paper or metal and store it in a safe place.
- **Basic knowledge**: A minimum understanding of Bitcoin concepts (addresses, transactions, fees) is useful, although this tutorial explains each step for beginners.

## 2️⃣ Installation

You can install the application through:

- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(for iOS devices)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (for Android devices)

Android users also have alternative options:

- Download the APK directly from [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) page or
- Install through the Nostr-compatible [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)

After installing the application, follow up on the welcome screen to configure your account.

## 3️⃣ Initial configuration

On opening, you are prompted with the following options: 

- `Create New Wallet`
- `Recover Wallet` and
- `Advanced Options`

Let's start by tapping on `Advanced Options`.

Here, we can configure the advanced settings before creating or recovering a wallet:

1. Enable the `Tor proxy` to route traffic over the Tor network.
        1. [Orbot app](https://orbot.app/en/) needs to be installed and running before enabling
        2. Tor Proxy only applies to Bitcoin (not Liquid) and may result in a slower connection.
2. Setup a `Custom Electrum Server`, or
3. Adjust the `Recover Bull` settings. We will learn more about the [Recover Bull](https://recoverbull.com/) later.

After making all the optional adjustments, tap `Done`. If you wish to re-use an existing Wallet, click on `Recover Wallet` and fill in the 12 words of your recovery phrase.

Otherwise, click on  `Create a New Wallet`. 

![image](assets/en/01.webp) 

## 4️⃣ Home Screen

Before we dive deeper, let's take a look at the `Home Screen` to get oriented:

- the `transaction overview` and `settings menu` is located at the top.
- The `Available Balance` has a privacy option that can be `turned on or off`.
- Access the `Bitcoin Bull Exchange` to `Buy, Sell, or Pay` (this depends on the jurisdiction and may require KYC).
- `Transfer` of funds between wallets
- `Secure Bitcoin` equals Onchain Bitcoin Wallet
- `Instant payments` via the Lightning- / Liquid Network *(Note: Bull Bitcoin Wallet enables payments to be made and received via Lightning. Funds received via Lightning are stored on the [*Liquid network](https://liquid.net/) (in the Wallet Instant Payments) thanks to an automatic swap via [*Boltz exchange](https://boltz.exchange/). This gives you the ability to interact with Lightning without having to manage liquidity channels, while remaining in self-custody.)*
- `Send` and `Receive` of funds

![image](assets/en/02.webp) 

First, let's make some important configurations and start with the `Backup`. 

## 5️⃣ Backup

To begin the backup process, tap the `gear icon (⚙)` in the top right corner of the app and select `Wallet Backup`. You will be presented with two methods for securing your wallet: `Encrypted Vault` and `Physical Backup`. Let's explore each one. 

![image](assets/en/03.webp) 

### Physical Backup

Tap on `Physical Backup` to see a list of 12 words that represent your recovery or seed phrase. Please consider the following:

- Write down your `recovery phrase` with the utmost care. Write it down on paper or metal and keep it in a safe place (safe deposit box, offline location). This phrase is your only means of accessing your bitcoins in the event of loss of your device or deletion of the application.
- It's also important to note that anyone with this phrase can steal all your bitcoins. Never store it digitally:
- No screenshot
- No cloud, email or messaging backups
- No copy/paste (risk of saving to clipboard)

![image](assets/en/25.webp) 

The next screen will have you put the word in the right order to make sure you got the seed phrase correct. You'll get a confirmation when the test is done and it's successful.

! **This point is critical**. For further assistance :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Encrypted vault

There is also the option of an encrypted, anonymous backup in the cloud. But didn't we mention in the last paragraph that cloud backups are risky and should be avoided? However, the Bull Bitcoin team has developed a clever way to make the process safe. Here's how it works: 

`Recoverbull` is a backup protocol that simplifies securing your Bitcoin wallet by splitting the backup into two parts. First, your wallet's backup file is encrypted on your device using a strong encryption key. You can save this encrypted file wherever you want, such as Google Drive or your device. Second, the encryption key needed to unlock the file is stored by the Recoverbull Key Server. To recover your wallet, you need both the encrypted backup file and the key, which you access with your PIN or password. This design ensures that your cloud backup alone is useless and that the key server alone is useless without your specific backup file. This keeps your funds safe even if one part is compromised.

Think of it like a safe deposit box. The encrypted backup file is the *box*, which you can store anywhere (like Google Drive). Your Recovery PIN is the *key*, which is stored separately by the Recoverbull Key Server. A thief would need to get both your specific box and your specific key to open it. This design ensures that even if someone gets your backup file, it's useless without the key from the server, and the server's key is useless without your unique backup file. 

Learn more about the `Recoverbull` wallet backup protocol [here](https://recoverbull.com/).

Tap on `Encrypted vault` and then `Continue` to confirm using the Default Server. The connection will be routed through the `Tor` Network to ensure privacy and anonymity.

**Understanding Your PINs**

- `App Unlock PIN`**:** The optional PIN set in `Settings > Security PIN` to lock the app on your phone.
- `Recovery PIN`**:** The mandatory PIN created during the `Encrypted Vault` backup process, used to decrypt your backup file during recovery. 

These are two separate PINs. Do not forget your Recovery PIN, as it is essential for restoring your wallet."

**Recovery PIN Setup:** 

- You must create a PIN or Password to recover access to your wallet.
- The PIN / Password must be at least 6 digits long (e.g., avoid simple sequences like 123456, which are not accepted).
- Without this PIN, wallet recovery is impossible.

Next, select a vault provider:

- `Google Drive` or 
- a `custom location` (e.g. your device)

![image](assets/en/04.webp) 

Now, save the `backup file`. Next, tap `Test Recovery`, select your saved backup file or vault, and then tap `Decrypt Vault`. Enter your `PIN` or `Password`. If everything worked, the `Test completed successfully` screen will appear.

### Import / Export Labels

Now that we created our Backup let's have a look on `Labels`.  The Bull Bitcoin wallet enhances privacy and organization by allowing users to create custom labels for their receiving addresses and transactions. These labels help you categorize your funds, as transactions sent to a labeled address will inherit that label, and you can also label outbound transactions to track their change. The wallet fully supports the [BIP-329](https://bip329.org/) standard, which means you can export all your labels to a file and import them into another wallet. This feature ensures you can seamlessly back up your transaction history and categorizations, or migrate them between different instances of the wallet, without losing your personalized organization.

![image](assets/en/05.webp)

##  6️⃣ Settings

With your primary backup secured, let's explore the other features available in the settings.

### A - Securing access

To secure the app, navigate to `Settings` and choose `Security PIN` to select PIN Code. Create a strong PIN to lock access to your wallet. While this step is optional, it is highly recommended to prevent unauthorized access if someone else uses your phone.

![image](assets/en/06.webp)

### B - Connection to a personal node (optional)

The Wallet BullBitcoin connects to Electrum servers by default: the first managed by Bull Bitcoin and a secondary server from Blockstream, both of which are considered to keep no logs, reducing the risk of tracking.

For greater confidentiality, you can connect the application to your own Bitcoin node via an Electrum server. To do so, tap `Settings` > `Bitcoin Settings` > `Electrum Server Settings`, then tap `+ Add Custom Server` to enter your server's address and credentials. 

![image](assets/en/07.webp)

### C - Currency

The available balance is displayed on the main screen in both `sats` and `USD`. To change this, navigate to `Settings` > `Currency`. There, you can toggle between `sats/BTC` and select your `default fiat currency`.

![image](assets/en/08.webp)

### D - Bitcoin Settings

The `Bitcoin Settings` menu offering deep access to your wallet's core configurations and data. Here, you can inspect the fundamental details of your `Secure Bitcoin` and `Instant payments wallets`, giving you full transparency and control. Key features within this menu include:

- **Wallet Details:** Navigate to your Secure Bitcoin or Instant payments wallet to view specific information.
- **Wallet Fingerprint:** A unique identifier for your wallet.
- **Public Key (Pubkey):** The key used to generate your Bitcoin receiving addresses.
- **Descriptor:** A technical summary of your wallet's structure.
- **Derivation Path:** The specific path used to generate all addresses from your master private key.
- **Address View:** Access a list of your unused receiving addresses and change addresses (coming soon)

Furthermore, you have the option to:

- `Enable Auto Transfer` settings to set a maximum instant wallet balance, which will then be automatically transferred to the secure bitcoin wallet.
- Import Generic wallets via `Mnemonic` Phrase or import `watch-only`
- Connect `Hardware wallets`: currently supported devices are ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade and Foundation Passport

##  7️⃣ Bull Bitcoin Exchange

Directly from the wallet, you have access to the [Bull Bitcoin exchange](https://www.bullbitcoin.com/), allowing you to buy, sell and pay Bitcoin without leaving the app. This integration provides a convenient solution for managing your Bitcoin needs. Please be aware that access to the exchange and its services may be restricted based on your jurisdiction, and completing Know Your Customer (KYC) verification may be required to comply with regulatory standards and use the platform's full features.

To get started, tap on `Exchange` in the bottom right corner, then `Sign up` or `Login` to your account. 

The exchange offers the following [features](https://www.bullbitcoin.com/):

- Buy Bitcoin with self-custody from your bank account
- Non-custodial
- Individuals or corporations
- Instant withdrawal
- No hidden fees
- Lightning Network available
- No transaction limits
- Recurring buy options

![image](assets/en/09.webp)

To learn more please visit this tutorial: 

https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Receiving funds

Receiving funds with **Bull Bitcoin Wallet** is straightforward and flexible, supporting three distinct networks tailored for different use cases:

- The `Bitcoin (onchain)` network for secure, long-term storage.
- The `Liquid` network for fast, more confidential transactions.
- The `Lightning` network for instant, low-cost payments.

The app automatically generates the appropriate address or invoice based on your selected network. Here's how to proceed for each network.

### Receiving via Onchain (Bitcoin network)

To receive on-chain funds, you can either select the `Secure Bitcoin Wallet` from the Home screen and tap `Receive`, or tap the main `Receive` button and then choose the `Bitcoin network`.

You have two primary modes for generating a receive address:

**Default Mode (URI with additional input parameters)

By default, the wallet generates a [BIP21 URI](https://bips.dev/21/). This is a standardized format that packages more information than a simple address, including an amount, a personal note, and PayJoin parameters to enhance privacy. This comprehensive URI is encoded into a QR code and made available to copy. The format looks like this: `bitcoin:<address>?<parameter1>=<value1>&<parameter2>=<value2>`.

- **Additional Input Parameters:**
    - **Amount:** Specify a requested amount in BTC, sats, or a fiat currency.
    - **Message:** Add a personal note that will be visible to the sender.
    - **PayJoin:** Enable this option to improve privacy by combining inputs from both the sender and receiver in the transaction.

Example URI:

```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```

*Important Note: Please do not send any funds to the addresses in this tutorial, the wallet will be deleted.* 

![image](assets/en/10.webp)

**Copy or scan Address only option enabled

With the `Copy or scan Address only option` enabled, the application generates a simple Bitcoin address in SegWit (bech32) format.

Example:

```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```

Even if you enter an amount or a note, they will not be included in the QR code or the copied address.

![image](assets/en/11.webp)

### Receiving via the Liquid Network

You can receive a payment on the Liquid Network. Once on the `Receive` screen, you have the same two options for generating a payment request:

**1. Simple Address:** Copy the standard `Liquid address`. This is a unique identifier for your wallet on the Liquid network and does not include any specific amount or message.

Example Address:

```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```

**2. Detailed Payment Request (URI):** For a more structured request, you can specify an amount and a personal note. This information is automatically encoded into a shareable URI and its corresponding QR code.

- **Amount:** You can set the amount in Bitcoin (BTC), Satoshis (Sats), or a fiat currency.
- **Note:** Add a personal message to identify the transaction.

**Example URI:**

```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```

To complete the transaction, provide the sender with the `address` or `URI`. You can do this by copying it to your clipboard or by having them scan the QR code directly from your screen.

![image](assets/en/12.webp)

### Receiving via Lightning


The Bull Bitcoin Wallet also allows you to send and receive payments via the Lightning Network. A key feature is that funds received via Lightning are automatically swapped and stored on the `Liquid Network` within your `Instant Payments Wallet`. This service is powered by `Boltz`. This design enables you to enjoy the speed and low cost of Lightning without the complexity of managing liquidity channels, all while maintaining full self-custody of your funds. While this hybrid approach is self-custodial and avoids the complexity of managing channels, it introduces a third-party service (Boltz), a small swap fee, and reliance on the Liquid Network's federation of functionaries as keyholders, which is different from a traditional, non-custodial Lightning wallet where you manage your own channels. You can learn more about Liquid and there governance model here:

https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306

- **Limits:**
    - **Minimum Amount:** A minimum invoice amount is required. Please check the app for the current limit
    - **Fees:** You, the receiver, are responsible for a small swap fee. This fee is deducted from the amount the sender transfers and is subject to change
- **Benefits:**
    - **Self-Custodial:** Your funds are always under your control, secured on the Liquid network.
    - **Avoid High On-Chain Fees:** By using Lightning and storing on Liquid, you bypass the on-chain fees associated with opening a traditional Lightning channel. You can choose to move funds to an on-chain channel later, when the accumulated amount justifies the expense.
    - **Tip:** For the most cost-effective transaction between two Bull Bitcoin users, use the **Liquid network directly** to avoid the Lightning swap fees entirely.

To receive a payment, you must generate a `Lightning invoice`:

1. `Enter an Amount`**:** Specify the amount you wish to receive in Bitcoin (BTC), Satoshis (Sats), or a fiat currency.
2. `Add a Note` **(Optional):** Include a memo or note. This will be embedded in the invoice and displayed in your transaction history once the payment is complete, making it easier to identify.
3. `Invoice Validity`**:** The Lightning invoice is time-sensitive and expires after **12 hours**. If it is not paid within this period, it becomes invalid, and you will need to generate a new one.

Provide the sender with the invoice by copying it to your clipboard or by letting them scan the QR code displayed on your screen.

![image](assets/en/13.webp)

## 9️⃣  Sending funds

You can access the send screen directly from the home page or from within any of your wallets. Bull Bitcoin Wallet simplifies the process by automatically detecting the destination network—`Bitcoin`, `Liquid`, or `Lightning`—based on the address or invoice you enter, whether pasted or scanned via QR code.

### On-Chain Transmission via the Bitcoin Network

Sending funds on-chain means your transaction is recorded directly on the Bitcoin blockchain. This method is best for larger transfers or non-time-sensitive transfers. To begin, you can tap on the `Send Button` down right, and scan or enter a `standard Bitcoin address`.

If the address you provide does not include a specific amount, you will be prompted to fill in the details on the send screen. You can specify the amount in your preferred unit, such as BTC, satoshis, or a fiat equivalent. You also have the option to add a personal note, which is a private memo for your own reference to help you identify the transaction later. This note is not shared with the recipient.

Conversely, if the payment request you scan or paste already contains all the necessary details, such as a BIP21 URI with a pre-defined amount, the wallet will bypass the data entry screen and take you directly to the confirmation screen to authorize the payment.

![image](assets/en/14.webp)

Before your transaction is broadcast, you will be presented with a confirmation screen. It is crucial to take a moment and carefully review every parameter, paying close attention to the recipient address, the amount being sent, and the network fees. This screen also provides powerful tools for customizing your transaction.

You can control the fees in two primary ways. The first method is to select a desired transaction speed, such as low, medium, or high, and the wallet will automatically calculate the appropriate fee for you. The second method allows for more precise control by letting you set a specific fee, either as an absolute total in satoshis or as a relative rate per byte, which then provides an estimated confirmation time.

For advanced users, the wallet offers several settings to fine-tune the transaction. `Replace-by-Fee` (RBF) is enabled by default, which is a valuable feature that allows you to accelerate a transaction if it becomes stuck in the mempool by re-broadcasting it with a higher fee. You can also manually select which `Unspent Transaction Outputs` (UTXOs) to spend from. This is a powerful tool for UTXO consolidation, a strategy where you combine multiple small inputs into a single larger one. While this may cost more in fees for the current transaction, it can significantly reduce fees on future transactions, especially if network fees are expected to rise.

![image](assets/en/15.webp)

PayJoin is automatically attempted when you scan a recipient's payment request (a BIP21 URI) that includes a `pj=` parameter. If you simply paste a plain address with no extra parameters, this feature will not be activated. This collaborative method enhances privacy by combining inputs from both the sender and the receiver, breaking the common-input-ownership heuristic and allowing for better scaling and fee savings in some circumstances as well.

### Sending to the Liquid Network

The `Liquid Network` is designed for fast, confidential transactions with minimal fees. When you send funds via Liquid, they are withdrawn from your `Instant Payments Wallet`. The process is straightforward: you simply enter or scan the recipient's `Liquid address`.

If the address does not specify an amount, you will be asked to provide one on the send screen. You can enter the amount in BTC, satoshis, or fiat. A key advantage of Liquid is its low minimum threshold. As with on-chain transactions, you can add an optional personal note for your own records. If the payment request already includes an amount, the wallet will proceed directly to the confirmation screen.

On the confirmation screen for a Liquid transaction, you will review the details. The fees are notably low and are calculated based on the complexity of the transaction. They are typically around 0.1 sat/vB, which for a simple transaction amounts to just 20-40 satoshis (for example, 26 satoshis as of December 21, 2025).

![image](assets/en/16.webp)

### Sending to the Lightning Network

You can either scan an Lightning Address (e.g. `runningbitcoin@rizful.com`) which allows you to set the amount and an optional note for the recipient, or scan a invoice with a pre-defined amount, which takes you directly to the confirmation screen. 

*Note that minimum amounts and fees apply.*

The Bull Bitcoin Wallet sends Lightning payments by withdrawing funds from your `Instant Payments Wallet` (on Liquid) and swapping them via `Boltz`. This hybrid approach is fully self-custodial and avoids the high on-chain fees of managing a dedicated Lightning channel, but it requires paying a `swap fee`. For the lowest cost, send directly to a recipient's Liquid address if they also use a Bull Bitcoin wallet.

## 🔟 Transferring Funds Between Your Wallets

Bull Bitcoin allows you to move your Bitcoin between your `Secure Bitcoin` wallet and your `Instant Payments Wallet` on the Liquid Network or to an `external Wallet`. To perform a transfer, simply navigate to the `Transfer` section, select the source and destination wallets, enter the amount you wish to move, and confirm the transaction.

![image](assets/en/17.webp)

## 1️⃣1️⃣ Recovering Your Bull Bitcoin Wallet

This section explains how to regain access to your Bull Bitcoin Wallet funds if you lose your device, uninstall the app, or simply need to switch to a new one. As already explained, there are two primary methods for recovery: using the unique `Recoverbull` method and using a standard `BIP39 seed phrase`.

### Method 1: Recoverbull

Recap: Wallet backups are encrypted locally. The encrypted file can be stored in cloud storage, or on another device. The encryption key is stored by the Recoverbull Key Server. Both are kept separate and must be combined to recover a wallet.

To start I will delete the Wallet with all funds on it and reinstall the wallet. We will land on the `Welcome screen` again. This time, select the `Recover Wallet` option. Then, navigate to the `Encrypted Vault` method, confirm using the `Default Key server`, and select the location or `Vault provider` where you stored the backup file.

![image](assets/en/18.webp)

It states that the vault was successfully imported. Tap `Decrypt Vault` button and enter the `PIN`. The next screen will show your `balances` and the `number of transactions` that were recovered.

![image](assets/en/19.webp)

### Method 2: Seed Phrase

This method uses your wallet's master recovery phrase, a standard 12  word list that serves as the ultimate backup for your funds. It is the most universal way to recover a Bitcoin wallet, as it is not tied to any specific service or server. As long as you have this phrase, you can restore your wallet on any compatible device, even without access to the Bull Bitcoin Key Server.

From the Welcome screen, select `Recover Wallet`. This time, choose the `Physical backup` method. The app will present a grid of words. Carefully select each word of your 12 -word seed phrase in the correct order. Be meticulous, as a single mistake will result in an incorrect wallet.

## 1️⃣2️⃣ Connecting a Hardware Wallet

For the highest level of security, many Bitcoin users choose to store their funds in `cold storage`. This means keeping the `private keys` that control your Bitcoin on a device that is never connected to the internet. A `hardware wallet`  (or Signing device) is a specialized physical device designed for this exact purpose. It acts like a digital vault for your keys, ensuring they are never exposed to the potential threats of an online computer or smartphone.

By connecting a hardware wallet to the Bull Bitcoin app, you get the best of both worlds: the uncompromising security of cold storage for your private keys, combined with the powerful features and user-friendly interface of the Bull Bitcoin wallet for viewing balances and managing transactions. In this final chapter, we will show you how to connect a hardware wallet, such as a [Coldcard Q](https://coldcard.com/q), to your Bull Bitcoin wallet. This tutorial will not cover setting up a Coldcard Q in depth; you can learn about that here: 

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importing a Wallet

![image](assets/en/26.webp)

First, from the main menu on your Coldcard Q, select `Export Wallet`, then choose `Bull Wallet`. Your Coldcard will generate a QR code. 

![image](assets/en/20.webp)

Open the Bull Bitcoin Wallet and navigate to `Settings` > `Bitcoin Settings` > `Import wallet` and select `Coldcard Q` on your phone and tap `Open the camera` to scan this QR code to import your hardware wallet's public keys.

![image](assets/en/21.webp)

### Receiving with Coldcard Q

To receive Bitcoin using your connected Coldcard Q, you do not need the device to be physically connected to your phone. The Bull Bitcoin Wallet has already imported the necessary public keys, allowing it to generate addresses on its own.

1. Tap on your imported Coldcard Q signing device and select `Receive`.
2. The app will automatically display a fresh Bitcoin address from your Coldcard's wallet.
3. Use this address to receive funds. The Bitcoin will be secured directly to the hardware wallet's keys, even though the device was offline during the process.

![image](assets/en/22.webp)

### Sending with Coldcard Q

Sending Bitcoin with your Coldcard Q requires your physical confirmation to authorize any transaction. While the Bull Wallet app is used to build the transaction, the final signature can only be created on the hardware wallet itself.

To begin, open your `Coldcard Q` wallet and tap on `Send`. Then, `open the camera` to scan the QR code for the receiving address. After scanning, enter the `amount` you want to send and adjust the `fee priority` as needed.

For more options, you can look under Advanced Settings. Here you will find the `Replace by Fee` (RBF) option, which is activated by default and allows you to speed up a stuck transaction later. You also have the `Coin Control` option, which lets you manually select the specific UTXOs you wish to spend.

Once you have reviewed all the details, tap `Show PSBT` to prepare the transaction. 

![image](assets/en/23.webp)

Tap the `Scan` button on your Coldcard Q and use its camera to scan the QR code displayed on your phone. The Coldcard screen will then show you all the transaction details. Carefully verify the amount, the recipient address, and your change address. If everything is correct, press the `Enter` button on the Coldcard Q to sign the transaction. Next, a QR code of the signed transaction will appear on the screen. 

![image](assets/en/24.webp)

On the Bull wallet, tap `I'm done`, then tap the `Camera` button to scan the QR code of the `signed transaction` from your Coldcard Q. The Bull Wallet will now display a summary screen of the signed transaction. Review it one last time, then tap `Broadcast` Transaction. This finalizes the process by sending the transaction to the Bitcoin network, and your funds will be on their way.

## 🎯 Conclusion

You have now completed your journey through the Bull Bitcoin Wallet. The app puts powerful privacy and security tools right at your fingertips, making advanced features simple to use. It helps you stay private with features like `PayJoin`, which hides your transactions on the blockchain, and `Tor integration`, which masks your network activity from prying eyes. For those who want ultimate control, you can connect to your `own personal Bitcoin node` to stop relying on third-party servers, and use a `Hardware wallet` to keep your private keys completely offline and safe. With smart backup options and seamless support for Bitcoin, Liquid, and Lightning, the Bull Bitcoin Wallet is a strong, all-in-one choice for anyone who is serious about keeping their funds private, secure, and fully under their own control.

## 📚 Bull Wallet Resources

[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)