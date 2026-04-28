---
name: ArkadeOS
description: Complete guide to the Arkade wallet and Ark Protocol
---

![cover](assets/cover.webp)

The Bitcoin network faces a major challenge: scalability. While the main layer (layer 1) offers unrivalled security and decentralization, it can only handle a limited number of transactions per second. Lightning Network has emerged as a promising second-layer (layer 2) solution, enabling fast, low-cost payments. However, Lightning imposes its own constraints: channel management, the need for incoming liquidity and a technical complexity that may put off new users.


This is the background to **Ark**, a new layer 2 protocol designed to offer a simplified user experience without sacrificing sovereignty. **ArkadeOS** (or Arkade) is the first major implementation of this protocol, offering a next-generation Bitcoin wallet.


This tutorial will guide you through the world of Arkade. We'll explore how the Ark protocol works, how to install and configure the Arkade wallet, and how to use it to send and receive bitcoins instantly, confidentially and without the usual Lightning Network frictions.

![video](https://www.youtube.com/watch?v=HdKeXV_vZZM)

## Understanding the Ark protocol


Before diving into the use of Arkade, it's essential to grasp the key concepts of the Ark protocol that drives it. Ark is not a separate blockchain, but an intelligent coordination mechanism on top of Bitcoin.


### The VTXO concept

At the heart of Ark is the **VTXO** (Virtual UTXO). A VTXO is a UTXO not yet published on the Bitcoin blockchain: it exists outside the main chain (off-chain) but is backed by transactions pre-signed on the blockchain.


Unlike a balance on a centralized exchange, a VTXO really belongs to you. You hold a cryptographic proof that allows you, at any time, to claim the corresponding real bitcoins on the blockchain, even if the Ark server disappears. VTXOs enable you to transfer value instantly between users without waiting for block confirmations.


### The role of the ASP (Ark Service Provider)

The Ark protocol operates on a client-server model. The server is called **ASP** (Ark Service Provider). The ASP plays the role of conductor:


- It provides the necessary liquidity for the network.
- It coordinates transactions between users.
- It organizes settlement "rounds" on the blockchain.


It's crucial to note that ASP is **non-custodial**. It never holds your private keys, nor can it steal your funds. Its role is purely technical and logistical. If an ASP censors your transactions or goes down, you can always recover your funds via a unilateral exit procedure.


### Rounds and privacy

Transactions on Ark are finalized in batches called **Rounds**. Periodically (e.g. every few seconds), the ASP gathers all pending transactions and anchors them on the Bitcoin blockchain in a single optimized transaction.

This mechanism offers two major advantages:


- Scalability**: A single on-chain transaction can validate thousands of off-chain payments, drastically reducing costs for users.
- Confidentiality**: Each round acts as a **CoinJoin**. Funds from all participants are mixed into a common pool before being redistributed in the form of new VTXOs. This breaks the link between sender and receiver, making it extremely difficult, if not impossible, for an outside observer to trace payments.


## ArkadeOS presentation


ArkadeOS is the concrete application that makes the Ark protocol available to the general public. Developed by Ark Labs, it's a complete ecosystem comprising a wallet (Wallet), a server (Operator) and developer tools.


For the end user, Arkade takes the form of an elegant, intuitive web wallet (PWA - Progressive Web App). It hides the cryptographic complexity of VTXOs and rounds behind a familiar interface. With Arkade, you have an address to receive, a button to send, and a transaction history, just like a classic wallet, but with the power of Ark's immediacy and confidentiality.


## Installation and configuration


As Arkade is a Progressive Web App, it's particularly easy to install, and doesn't necessarily involve traditional application stores.


### Access and installation

You can access Arkade directly from any modern web browser (Chrome, Safari, Brave) on computer or mobile.



- Visit the application's official website: **[arkade.money](https://arkade.money)**.


![arkade homepage](assets/fr/01.webp)


You'll be greeted by a series of introductory screens introducing you to Arkade's key concepts: a new ecosystem for Bitcoin, the importance of self-custody and the benefits of batch transactions.


![arkade onboarding](assets/fr/02.webp)



- On Android (Chrome/Brave)** : Press the browser menu (three dots) and select "Install application" or "Add to home screen".
- On iOS (Safari)**: Press the share button (square with an upward arrow) and choose "On home screen".


Once installed, Arkade launches like a native application, full-screen and without an address bar.


### Portfolio creation

On first launch, you will be asked to configure your wallet.



- Click on **"Create New Wallet"**.


![create wallet](assets/fr/03.webp)



- The wallet is created instantly. Unlike traditional Bitcoin wallets, **Arkade doesn't use a 12- or 24-word recovery phrase**. Instead, Arkade automatically generates a **private key** in Nostr (nsec) format, which will be used to back up and restore your wallet. Remember to save this key immediately (see next section).



- You'll see the "Your new wallet is live!" screen, confirming that your wallet is ready to use. Click on **"GO TO WALLET "** to access the main interface.


Once in your wallet, you're taken to Arkade's main interface. Here you'll find your balance, buttons for sending and receiving funds, and an "Apps" tab that gives access to integrated applications such as Boltz (Lightning exchange), LendaSat and LendaSwap (lending services), and Fuji Money (synthetic assets).


![wallet interface](assets/fr/04.webp)


### Connection to ASP

By default, the wallet is automatically configured to connect to the official Arkade Labs ASP. You can check which server you're connected to by going to **Settings** > **About** where you'll see the server address (currently `https://arkade.computer`).


In the current version of Arkade (Beta), it is not possible to manually modify the ASP server. The application automatically connects to the official Arkade Labs ASP. In the future, users may be able to choose between different ASPs according to their preferences, but this feature is not yet available.


### Backing up your private key

**Arkade uses a private key in Nostr (nsec) format as a backup and recovery method. To back up your private key :



- Go to **Settings** from the main screen.
- Select **"Backup and privacy "**.
- You'll see your **private key** displayed in `nsec...` format. This long string of characters is your only means of restoring your wallet.
- Press **"COPY NSEC TO CLIPBOARD "** to copy your private key.
- Keep this key in a safe place**: write it down on paper, store it in a secure password manager, or use any other backup method that suits you.
- Arkade also offers the **"Enable Nostr backups "** option. This feature uses the Nostr protocol (a decentralized network) to automatically back up certain data from your wallet in encrypted form to Nostr relays. This facilitates synchronization between multiple devices and offers simpler recovery of your wallet's status.


**Important**: Nostr backups are a **comfort** feature only. They do not replace the backup of your nsec key. Nostr relays do not guarantee permanent data storage. Your nsec private key remains your only guaranteed means of recovering your funds.


![backup private key](assets/fr/05.webp)



## Using Arkade


Once you've set up your wallet, you're ready to explore Arkade's capabilities. The interface is designed to unify the different types of Bitcoin payments (On-chain, Lightning, Ark) seamlessly.


### Receiving funds


To fund your wallet, press **"Receive "**. Arkade offers three methods of receipt:



- Ark payment**: If the sender also uses Arkade, share your Ark address for an instant, confidential and virtually free transfer.
- On-chain deposit (Boarding)**: Use the Bitcoin address (`bc1p...`) to receive from a classic wallet or an exchange. Allow for confirmation (~10 min) before funds are converted into VTXOs.
- Lightning swap**: Generate a Lightning invoice and pay it from an external wallet Lightning. Funds arrive instantly via an automatic swap.


![receive amount](assets/fr/06.webp)


The receipt screen displays all available options: QR code, Ark address, Bitcoin (BIP21) address and Lightning invoice. For Lightning payments, keep the application open during the transaction.


![receive confirmation](assets/fr/07.webp)


### Sending funds


To send funds, press **"Send "** and paste the recipient's address or scan the QR code. Arkade automatically detects the type of payment required:



- Ark** payment: To an Ark address, the transfer is instant, private and virtually free (0 SATS fee). The recipient does not need to be online.
- Lightning** payment: Scan a Lightning invoice (`lnbc...`) and Arkade automatically performs a swap. The ASP pays the invoice for you and debits your Arkade balance.
- On-chain payment**: Towards a classic Bitcoin address (`bc1q...` or `bc1p...`), Arkade initiates a "Collaborative Output" which will be included in the next on-chain round.


Check the details on the "Sign transaction" screen, then confirm with **"TAP TO SIGN "**.


![send payment](assets/fr/08.webp)


**Current limitation (Beta)**: VTXOs created less than 24 hours ago cannot be used for on-chain outputs. If you encounter an error, please wait until your VTXOs are "mature".


**on-chain output confidentiality**: The example below shows an [Ark output transaction on mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). We observe a distributed input to 4 different outputs, like a CoinJoin. For an external observer, it is impossible to determine which amount belongs to which user.


![transaction ark mempool](assets/fr/11.webp)


## Advanced features


### VTXO expiration management

A technical feature of the Ark protocol is that VTXOs have a **limited lifetime**. This time constraint is inherent in the design of the protocol. The expiration time is configurable by each ASP server; on the official Arkade Labs ASP, this period is around **4 weeks (≈30 days)**.


**This limitation allows the Ark server to efficiently manage liquidity and clean up VTXOs from inactive users. After expiration, the Ark server can technically claim the remaining funds in the VTXO tree.


**To keep your VTXOs active, they need to be "refreshed" before they expire. Refreshing consists of participating in a new "round" where your VTXOs close to expiration are exchanged for new VTXOs with a new full validity period (≈30 days on Arkade Labs ASP).


The Arkade wallet manages this process automatically: the application constantly monitors the status of your VTXOs and automatically refreshes them a few days before they expire. As long as you open your application regularly (at least once a week), your VTXOs will automatically be kept active.


**If you don't open your wallet for more than 4 weeks, your VTXOs will expire. However, you don't lose your funds: you retain the option of recovering them via a **unilateral exit** (see next section). This procedure is more costly and slower, but it ensures that your funds remain recoverable.


The need to open the application regularly makes Arkade a **"Hot Wallet"** designed for day-to-day spending, not a safe for long-term savings. To store bitcoins without using them for long periods, prefer a cold wallet hardware.


**Check the status of your VTXOs**: You can monitor the status of your VTXOs in **Settings** > **Advanced**. See "Next Renewal" to see when the next automatic renewal will take place, and "Virtual Coins" to see a detailed list of all your VTXOs with their expiry date.


![vtxo management](assets/fr/09.webp)


### Sortie Unilatérale (Unilateral Exit)


Unilateral exit is a **fundamental cryptographic guarantee** of the Ark protocol that ensures you get your funds back, even if the ASP disappears, censors your transactions or refuses to cooperate. Technically, your VTXOs are **pre-signed Bitcoin transactions** that you own. In an absolute emergency, you can broadcast these transactions on the Bitcoin blockchain to recover your funds without anyone's authorization.


**How does it work? The process takes place in two stages. First, **Unrolling**: you sequentially broadcast the pre-signed transactions that make up your VTXOs in the transaction tree. Then the **Finalization**: once the timelocks have expired (usually 24 hours), you collect your bitcoins from a standard address.


**Current status in Arkade**: In the Beta version, there is not yet a button or simple user interface for one-sided output. This functionality currently requires the use of the Arkade SDK and technical knowledge of TypeScript programming.


**Even if the procedure isn't accessible at the touch of a button, the cryptographic guarantee is there. Your VTXOs contain pre-signed transactions that legitimately belong to you. It's this technical guarantee that makes Ark a **non-custodial** protocol: even in the worst-case scenario, your funds remain technically recoverable. A simplified interface will probably be added in future versions of Arkade.


## Advantages and limitations


To put Arkade in the right context, let's summarize its current strengths and weaknesses.


### Highlights


- User Experience (UX)**: No channel management, incoming capacity or complex channel backups as with Lightning. Just install and use.
- Privacy** : The default CoinJoin architecture offers a much higher level of anonymity than standard on-chain or Lightning transactions.
- Interoperability**: Pay any Bitcoin QR code (On-chain or Lightning) from a single interface.


### Constraints


- Young protocol**: Ark is a very recent technology. Bugs may exist. It is advisable not to use Ark to store sums whose loss would be critical.
- ASP dependency**: Although non-custodial, the system relies on ASP availability for fluidity. If the ASP is offline, you can no longer transact instantly (only output your on-chain funds).
- Hot Wallet only** : The need to open the application regularly to refresh VTXOs is not suitable for cold storage (Cold Storage).


## Comparison: Arkade vs Lightning vs Cashu


To better understand Arkade's positioning, let's compare it to the other two major scalability solutions.



| Criterion | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Model** | Shared UTXO coordinated by server (ASP) | P2P network of payment channels | Blind tokens issued by a bank (Mint) |
| **Custody** | **Non-custodial** (you hold the keys) | **Non-custodial** (you hold the keys) | **Custodial** (the Mint holds the funds) |
| **Privacy** | **High** (Native CoinJoin, blind to the public) | **Medium** (Onion routing, but channels are visible) | **Very High** (Blind even to the Mint) |
| **Scalability** | Excellent (Massive on-chain batching) | Excellent (Infinite off-chain transactions) | Excellent (Simple server signatures) |
| **Experience** | Simple (close to an on-chain wallet) | Complex (channel management, liquidity) | Very simple (like digital cash) |
| **Main risk** | ASP availability & Expiration | Channel management & Backups | Trust in the Mint (risk of theft) |

**Arkade** is the ideal compromise: the simplicity and confidentiality of Cashu, but with the sovereignty (non-custodial) of Lightning.


## Support & Assistance


If you encounter any problems or have any questions while using Arkade, the application offers several support options:



- Go to **Settings** > **Support**.
- You'll find several options:
  - Customer support**: Get help with your wallet, report bugs or ask questions.
  - Secure Chat**: Your conversations are secure and private, with history maintained between sessions.
  - Bug Reports**: Report any problems you encounter, including steps to reproduce them.
  - Track Progress**: Keep track of your support tickets and conversations at all times.


![support](assets/fr/10.webp)


The Arkade team is also active on Telegram via the @arkade_os channel for support and integration opportunities.


## Important note: Application in Beta


**⚠️ Arkade is currently in Public Beta on the mainnet Bitcoin**. Although the application is functional with real bitcoins, it is important to take certain precautions.


### Recommendations for use


- Use small amounts**: Avoid storing large sums on Arkade. Use this wallet for your day-to-day expenses and keep your savings on a cold wallet hardware.
- Possible bugs and limitations**: As with any application under active development, Arkade may present bugs or unexpected behavior. Report any problems via integrated support.
- Rapid evolution** : The application and protocol are constantly being improved. Some features may change or be added in future versions.


### Current known limitations


- 24-hour delay on VTXOs** : Newly created VTXOs cannot be used immediately for on-chain outputs.
- ASP unique**: It is not yet possible to change the ASP server in the application.
- Technical unilateral output**: No simplified interface for unilateral output yet (requires SDK).


The Arkade Labs team is actively working to relax these limitations in future versions.


## Conclusion


ArkadeOS represents a major breakthrough in the Bitcoin ecosystem. By implementing the Ark protocol, it proves that it is possible to reconcile simplicity of use with the fundamental principles of Bitcoin: don't trust, verify.


Although still in its infancy, Arkade offers a fascinating glimpse of what the future of Bitcoin payments could look like: instant, private and accessible to all with no technical prerequisites. It's the perfect tool for your daily expenses, complementing your secure savings solution (Cold Wallet).


We encourage you to test Arkade with small amounts to discover this new protocol for yourself. The ecosystem is evolving fast, and Arkade is at the forefront of this innovation.


## Resources


To find out more, consult the official resources:



- Arkade** website: [arkadeos.com](https://arkadeos.com)
- Documentation**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark** protocol: [ark-protocol.org](https://ark-protocol.org)
- Source Code** : [GitHub Arkade](https://github.com/arkade-os)