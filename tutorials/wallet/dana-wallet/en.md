---
name: Dana Wallet
description: Minimalist wallet for Silent Payments (BIP-352)
---

![cover](assets/cover.webp)


The reuse of Bitcoin addresses is one of the most direct threats to user confidentiality. When a recipient shares a single address to receive multiple payments, any observer can trace all associated transactions and reconstruct their financial history. This problem particularly affects content creators, charities or activists who wish to publicly display a donation address without compromising their privacy or that of their donors.


Dana Wallet responds to this problem with an elegant solution: Silent Payments. This minimalist, open-source wallet, launched in 2024, generates a reusable static address while guaranteeing that each payment received ends up on a separate address on the blockchain. The sender needs no prior interaction with the recipient, and no external observer can link individual transactions together. On the blockchain, these payments look like perfectly ordinary Taproot transactions.


Dana Wallet is available on Mainnet and Signet, but the developers still consider it experimental and recommend not depositing funds you're not prepared to lose. In this tutorial, we'll use the Signet version to discover Silent Payments without risking any real funds.


## What is Dana Wallet?


### Philosophy and objectives


Dana Wallet adopts an "SP-first" approach: the wallet generates Silent Payments addresses exclusively, and accepts only this type of payment. You won't be able to create a classic Bitcoin address (legacy, SegWit or Taproot standard) with this application. This deliberate restriction allows you to concentrate fully on learning the BIP-352 protocol without being distracted by other features. The uncluttered interface deliberately favors ease of use over a profusion of options, making the tool accessible even to users new to on-chain confidentiality concepts.


The project is entirely open-source, developed with Flutter for the mobile interface and Rust for the internal cryptographic logic. This architecture combines a fluid user experience with optimum performance for intensive scanning operations.


### How do Silent Payments work?


Silent Payments (BIP-352) are based on a sophisticated cryptographic mechanism using Elliptic Curve Diffie-Hellman Key Exchange (ECDH). The recipient generates a static address (starting with `sp1...` on mainnet or `tsp1...` on Signet) consisting of two distinct public keys: a scan key ($B_{scan}$) to detect incoming payments, and a spend key ($B_{spend}$) to spend funds received. This separation makes it possible to keep the spend key on wallet hardware while using the scan key on a connected device.


When a sender wishes to make a payment, his wallet combines the sum of his inputs' private keys with the recipient's public scan key to calculate a shared ECDH secret. This secret generates a cryptographic "tweak" which, added to the recipient's spending key, creates a unique Taproot address for that transaction.


The recipient can reproduce this calculation using his private scan key and the public keys visible in the transaction (Diffie-Hellman mathematical property). This enables him to detect and spend the funds without any prior interaction with the sender.


This approach offers several advantages:


- Recipient confidentiality**: each payment ends up at a different address
- Sender confidentiality**: no persistent identifier linking payments
- No third-party server**: protocol operates autonomously
- Indistinguishable transactions**: Silent Payments look like ordinary Taproot transactions


The main drawback is the cost of scanning: the recipient has to analyze each new Taproot transaction to detect those intended for him.


If you would like to learn more about the technical operation of Silent Payments, we recommend the BTC204 course on confidentiality in Bitcoin, which includes a chapter dedicated to Silent Payments:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Supported platforms


Dana Wallet is available as an Android application. The APK can be downloaded via the dedicated F-Droid repository provided by the developers, via Obtainium, or directly from GitHub. For Linux users, it is technically possible to compile the Flutter application for desktop.


The app is not available on iOS or via the official stores (Google Play, App Store), reflecting its experimental status and its focus on a technical audience.


## Installation


### Essential prerequisites


To install Dana Wallet on Android, you'll need an Android device with the "Unknown sources" option enabled in the security settings. No account or registration is required.


### Add F-Cold deposit


The recommended method is to add Dana Wallet's dedicated F-Droid repository. Go to `fdroid.silentpayments.dev` where you'll find the repository link and a QR code to scan. The repository currently offers 3 applications: the Mainnet version, Development and Signet.


![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)


### Installation via F-Droid


Open the F-Droid application on your Android device, then access Settings via the icon at bottom right. Select "Repositories" to manage app sources. Press the "+" button to add a new repository, then scan the QR code or paste the `https://fdroid.silentpayments.dev/fdroid/repo` link. Once the repository has been added, you'll see the three versions of Dana Wallet available. Select "Dana Wallet - Bookmark" and press "Install".


![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)


## Initial configuration


### Portfolio creation


On first launch, Dana Wallet displays a welcome screen introducing its mission: "Send and receive donations without middlemen". Press "Begin" to continue. The next screen presents the application's three key benefits:


- Effortless donations**: start receiving donations in seconds
- Privacy by default**: no need for servers or complex infrastructure
- Email-like experience**: send and receive bitcoins as simply as an email


You can choose between "Restore" to restore an existing wallet or "Create new wallet" to create a new one. Press "Create new wallet".


![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)


The application then generates a recovery phrase, which you should carefully note down on a physical medium. Even for test funds of no real value, adopt good backup practices.


### Interface and parameters


Once the wallet has been created, you're taken to the main interface, divided into two tabs: "Transact" and "Settings".


The **Transact** tab displays your bitcoin balance (and its conversion to dollars), a list of recent transactions, and two action buttons: "Pay" to send funds, and a receive button (download icon).


The **Settings** tab offers four options:


- Show seed phrase**: displays your recovery phrase for safekeeping
- Change fiat currency**: change display currency (USD by default)
- Set backend url**: configure Blindbit server URL (see next section)
- Wipe wallet**: completely wipes the wallet from the device


![Interface principale Transact et menu Settings](assets/fr/04.webp)


### The Blindbit server


Dana Wallet uses an indexing server called **Blindbit** to detect your Silent Payments. Understanding how it works is important for evaluating the application's trust model.


**Why do we need a server?


To detect a Silent Payment, your wallet must theoretically scan all Taproot transactions in each block and perform a cryptographic calculation (ECDH) for each one. On a cell phone, this operation would be too computationally and bandwidth-intensive.


The Blindbit server solves this problem by pre-calculating intermediate data (called "tweaks") for all Taproot transactions. Your wallet then downloads these tweaks (33 bytes per transaction) and performs the final calculation **locally** to check whether a payment belongs to you.


**Preserved confidentiality**


Unlike a conventional Electrum server where you reveal your addresses, the Blindbit server doesn't know which payments belong to you. It provides the same data to all users, and it's your phone that performs the final verification. Your confidentiality is therefore preserved vis-à-vis the server.


**Default server


Dana Wallet uses the public server `silentpayments.dev/blindbit/signet` (for Signet) or `silentpayments.dev/blindbit/mainnet` (for Mainnet). You can change this URL in the settings if you host your own server.


**Host your own Blindbit server**


For users wishing total sovereignty, it is possible to host their own Blindbit Oracle server. This requires :


- A complete Bitcoin Core node **non-eagled** (non-pruned)
- Installing Blindbit Oracle (available on GitHub: `setavenger/blindbit-oracle`)
- Approx. 10 GB of additional disk space
- Technical skills (Go compilation, server configuration)


No packaged application is yet available for Umbrel or Start9. Installation remains manual for the time being. This is a field in active evolution, and more accessible solutions may emerge in the future.


## Daily use


### Receiving funds


To receive bitcoins, press the receive button (download icon) from the main screen. Dana Wallet then displays your complete Silent Payment address in the format `tsp1q...` on Bookmark. The interface offers several options:


- Show QR code**: displays your address's QR code for easy scanning
- Share**: share the address via your phone's applications
- Copy**: copies address to clipboard


As shown on the screen, you can share this address publicly on your social networks without compromising your privacy.


![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)


To obtain your first test funds on Signet, use the dedicated Silent Payments faucet accessible at `silentpayments.dev/faucet/signet`. Copy your address `tsp1...`, paste it in the field provided on the faucet, then validate the request. Wait for a block to be mined (about 10 minutes on Signet).


### Send a payment


To send funds, press the "Pay" button from the main screen. The "Choose recipient(s)" screen appears with three options for specifying the recipient:


- Enter payment information manually
- Paste from clipboard**: paste an address from the clipboard
- Scan QR Code**: scan a QR code containing the address


Once the recipient's address has been validated, the "Enter amount" screen lets you enter the amount to be sent in satoshis. Your available balance is displayed for reference. Press "Proceed to fee selection" to continue.


![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)


The next screen shows three levels of charges, depending on the urgency required:


- Fast** (10-30 minutes): higher fees for fast confirmation
- Normal** (30-60 minutes): moderate costs
- Slow** (1+ hour): minimum fee for non-urgent transactions


After selecting the fee level, the "Ready to send?" confirmation screen summarizes all the details: destination address, amount, estimated time and transaction fee. Check this information carefully, then press "Send" to send the transaction.


Once sent, the transaction appears in your history with the status "Unconfirmed" until it is included in a block. Your balance is updated accordingly.


![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)


## Advantages and limitations


### Highlights



- Pedagogical**: simplified interface focused on learning Silent Payments
- Bidirectional**: supports both sending and receiving, unlike other wallets
- Open-source**: fully auditable code on GitHub
- Dedicated Faucet**: makes it easier to obtain test funding
- Without account**: no registration or personal data required


### Constraints to consider



- Experimental**: unaudited software, use with caution on Mainnet
- Limited platform**: mainly Android, no iOS version
- Reduced functionality**: no coin control, no sub-accounts, no Lightning
- Intensive scanning**: payment detection consumes significant resources


## Best practices


### seed safety


Even for Signet tests with worthless backgrounds, treat your recovery phrase seriously. Use the "Show seed phrase" option in the settings to write it down carefully. As a matter of good practice, maintain completely separate wallets for Signet and Mainnet: never use a seed created for testing on a wallet intended to receive real funds.


### Warning about experimental status


Dana Wallet is still considered experimental by its developers. As they clearly state: "Don't use funds you aren't willing to lose". For learning purposes, opt for the Signet version. If you use the Mainnet version, limit yourself to token amounts.


### Backup and restoration


Silent Payments fund recovery requires a wallet compatible with the BIP-352 protocol. A standard wallet cannot scan the blockchain to retrieve your UTXO Silent Payments. Keep Dana Wallet installed or use the "Restore" option at first launch to recover an existing wallet.


## Comparison with BIP-47 and PayJoin


| Criterion                  | Silent Payments (BIP-352) | BIP-47 PayNyms      | PayJoin (BIP-78)    |
|---------------------------|---------------------------|---------------------|---------------------|
| Static address            | Yes (`sp1...`)            | Yes (payment code)  | No                  |
| Interaction required       | None                      | Initial notification transaction | For each payment     |
| On-chain footprint         | None (normal transactions) | Visible OP_RETURN    | Modified transaction |
| Receiver-side scanning     | Intensive (every block)   | Light (after notification) | None                |
| Sender privacy             | Excellent                 | Limited (link after notification) | Good (mixing)       |


Silent Payments eliminate the BIP-47 notification transaction at the cost of a more expensive scan. PayJoin solves a different problem (input correlation) and can be combined with Silent Payments.


## Conclusion


Dana Wallet is a valuable educational tool for learning about Silent Payments in a risk-free environment. Its minimalist approach allows you to understand the fundamental mechanisms of the BIP-352 protocol without being distracted by secondary features. By experimenting with Signet, you'll develop a practical understanding of this promising technology for Bitcoin transaction confidentiality.


Silent Payments represent a significant step forward in reconciling ease of use and respect for privacy. The enthusiasm of the community and the first integrations into various wallets (Cake Wallet, BitBox02, BlueWallet for sending) point to a future where publishing a donation address will no longer compromise the financial privacy of its owner.


## Resources


### Official documentation


- Dana Wallet GitHub repository: https://github.com/cygnet3/danawallet
- F-Cold deposit: https://fdroid.silentpayments.dev
- Silent Payments community site: https://silentpayments.xyz
- Specification BIP-352: https://bips.dev/352


### Signet test tools


- Faucet Silent Payments: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet


### Blindbit server (self-hosted)


- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle