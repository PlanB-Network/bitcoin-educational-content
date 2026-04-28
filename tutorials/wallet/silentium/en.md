---
name: Silentium
description: Progressive web wallet with Silent Payments support (BIP-352)
---

![cover](assets/cover.webp)


The reuse of Bitcoin addresses is one of the most direct threats to user confidentiality. When a recipient shares a single address to receive multiple payments, any observer can trace all associated transactions and reconstruct their financial history. This problem particularly affects content creators, charities or activists who wish to publicly display a donation address without compromising their privacy.


Silentium responds to this problem with an elegant solution accessible directly from your browser. This open-source progressive web application (PWA), launched in May 2024 by Louis Singer, implements Silent Payments (BIP-352): a reusable static address where each payment ends up on a separate blockchain address, with no prior interaction or observable link between transactions.


**Important warning**: Silentium is an experimental project serving as a *proof-of-concept* for Silent Payments' lightweight wallets. It should not be used as a daily wallet or for storing significant amounts. The developers explicitly state:


> Use at your own risk.

Note that this wallet can be used as a testnet or regtest.


## What is Silentium?


### Philosophy and objectives


Silentium serves as a technical demonstration for implementing Silent Payments in a lightweight wallet browser. Although it also supports conventional Bitcoin addresses, the emphasis is on Silent Payments to enable users to experiment with this privacy technology in a straightforward way.


### How do Silent Payments work?


Silent Payments (BIP-352) use Elliptic Curve Diffie-Hellman Key Exchange (ECDH). The recipient generates a static address (`sp1...` on mainnet, `tsp1...` on testnet) consisting of two public keys: a scan key to detect payments, and a spend key to use them.


The sender combines his private input keys with the recipient's scan key to calculate a shared secret generating a cryptographic "tweak". This tweak, added to the spending key, creates a unique Taproot address for each transaction. The recipient reproduces this calculation with his private scan key to detect and spend the funds without any prior interaction.


Advantages: enhanced confidentiality for sender and receiver, no third-party server required, transactions indistinguishable from conventional Taproot payments. Main disadvantage: intensive scanning of the blockchain to detect payments.


To find out more about the theoretical workings of Silent Payments, see the last part of the BTC,204 course on Plan ₿ Academy :


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Supported platforms


Silentium is a Progressive Web App (PWA) accessible from any modern browser (mobile or desktop). Use it directly on `app.silentium.dev`, install it as a native application via your browser, or deploy it locally. Installation is done directly from the browser, without going through the official stores.


## Using the Web App


### Access and installation


[Go to `https://app.silentium.dev/` from your browser](https://app.silentium.dev/). The application loads instantly and displays the home screen.


To install it as a native application on iOS, press the share button (square with upward arrow) then select "On home screen". On Android, the browser usually offers an "Add to home screen" notification directly. Once installed, Silentium appears with its dedicated icon and works as a native application, but requires an internet connection to synchronize transactions.


![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)


### Portfolio creation


On first launch, choose "Create Wallet" to generate a new wallet, or "Restore Wallet" to restore from an existing recovery phrase.


Select "Create Wallet". The application generates a 12-word phrase that you must write down carefully. This phrase is the only way to recover your funds. Even on testnet, adopt good backup practices. Press "Continue" after saving your phrase.


The application then asks you to set a password to secure access to the wallet. Choose a strong password and confirm it.


![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)


Once the phrase has been confirmed and the password set, you'll be taken to the main interface.


### Interface main and parameters


The main interface displays your balance in satoshis (initially 0 sats), with three buttons at the bottom:


- Sync**: synchronizes wallet with blockchain
- Receive**: to receive funds
- Send**: to send bitcoins


Access Settings via the icon at top right (three horizontal bars). The Settings menu offers several options:



- About**: application information
- Backup**: backup of recovery phrase
- Explorer**: select blockchain explorer (Mempool by default) and Silentiumd server
- Network**: network selection (mainnet/testnet)
- Password**: change password
- Reload**: reloading the wallet
- Reset**: complete reset
- Theme**: change theme


![Interface principale et paramètres avec Explorer](assets/fr/03.webp)


The **Explorer** section is particularly important: it lets you choose the blockchain explorer used (Mempool by default) and also displays the URL of the Silentiumd server (`https://bitcoin.silentium.dev/v1` for mainnet). If you host your own Silentiumd server or wish to use testnet, this is where you configure these parameters.


### Receiving funds


From the main interface, press the "Receive" button. By default, Silentium displays a Silent Payment address with its QR code. The address starts with `sp1...` on mainnet or `tsp1...` on testnet.


You can switch between Silent Payment and classic Bitcoin addresses using the "Switch to classic address" / "Switch to silent address" button at the bottom of the screen.


![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)



Once the transaction has been broadcast, please wait a few minutes. For Silent Payments, Silentium automatically scans the blockchain for transactions intended for you. Transactions appear with the status "Unconfirmed" before being progressively confirmed.


### Send a payment


From the main interface, press the "Send" button. The send screen will ask you :


1. **Address**: paste a Silent Payment address (`sp1...` or `tsp1...`) or a classic Bitcoin address. You can use the QR scan icon to scan an address.

2. **Amount**: enter the amount in satoshis to be sent. A numeric keypad is displayed for easy entry. Your available balance is displayed at the top for reference.


![Envoi de fonds depuis Silentium](assets/fr/05.webp)


Once you've entered the address and amount, press "Proceed" to continue. The application will ask you to select the desired fee level before confirming the transaction.


## wallet self-hosting


### Why self-host?


Silentium's local hosting offers total sovereignty, code verification, a development environment and resilience in the face of official site failures.


### Prerequisites


Node.js (version 14+), npm or yarn, Git, and around 500 MB disk space.


### Local installation


Clone the repository and install the :


```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```


### Launch and use


Start the application in development mode:


```bash
yarn start
```


Go to `http://localhost:3000` in your browser. For an optimized production version :


```bash
yarn build
```


Files generated in `build/` can be served with nginx, Apache or any web server. By default, Silentium connects to the public `bitcoin.silentium.dev` server. Modify this setting in the parameters to use testnet or your own server.


## The Silentiumd server


### Role and operation


Silentium uses a **Silentiumd** indexing server to optimize payment detection. Scanning all Taproot transactions would be too cumbersome for a browser or cell phone.


Silentiumd pre-calculates intermediate data (tweaks) for each Taproot transaction. Your wallet downloads these tweaks (a few bytes per transaction) and performs the final calculation locally, verifying the ownership of the payment. The server never knows your keys or can identify your transactions, unlike conventional Electrum servers.


Compact BIP158 filters allow your wallet to determine which blocks to scan without revealing your addresses, thus preserving your confidentiality.


### Public server


The public server `bitcoin.silentium.dev` (mainnet), sponsored by Vulpem Ventures, offers a simple and immediate experience. Although confidentiality is preserved, this approach implies relative trust in the third-party infrastructure.


### Host your own Silentiumd server


For total sovereignty, host your own Silentiumd server. Prerequisites: Bitcoin Core non-elagged node with `txindex=1` and `blockfilterindex=1`, Go 1.21+, 10-20 GB disk space, system administration skills.


**Installation:**


```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```


Configure via environment variables (see the repository's `config.md` for details). The server indexes the blockchain and exposes a API that can be queried by your wallet.


No packaged solutions for Umbrel or Start9 currently exist, limiting accessibility to non-technical users.


## Advantages and limitations


### Highlights



- Maximum accessibility**: use from any browser, no heavy installation required
- Multi-platform**: works on mobile (Android/iOS) and desktop thanks to PWA technology
- Simple self-hosting**: local installation possible with a few commands
- Open-source**: fully auditable code on GitHub
- Privacy-focused**: no tracking, no analytics, local cryptographic calculations
- Separate architecture**: clear separation between wallet (client) and indexing server
- Without account**: no registration or personal data required


### Constraints to consider



- Experimental project**: proof of concept only, not intended for daily use or production
- No guarantees**: risk of bugs, vulnerabilities, possible loss of funds
- Limited support**: little user documentation, small community, no official support
- Server dependency**: requires a working Silentiumd server (public or self-hosted)
- Intensive scanning**: Silent Payments detection consumes bandwidth
- Reduced functionality**: no coin control, no Lightning, no multi-signatures


## Best practices


### seed safety


Even on testnet, treat your recovery phrase seriously. Write it down and keep it in a safe place. Keep separate wallets for testnet and mainnet: never use a test seed on a wallet intended for real funds.


### Source code verification


One of the advantages of self-hosting is the ability to check the source code before running it. If you're planning to use Silentium with real funds, take the time to audit the code or get a trusted developer to do it. Also compare the hash of the code deployed on `app.silentium.dev` with that of the GitHub repository to ensure authenticity.


### Backup and restoration


Silent Payments fund recovery requires a wallet compatible with the BIP-352 protocol. A standard wallet cannot scan the blockchain to retrieve your UTXO Silent Payments. Keep Silentium installed or make sure you have access to another compatible wallet (such as Cake Wallet or other future implementations) to restore your funds if necessary.


## Conclusion


Silentium provides an accessible testing ground for understanding Silent Payments without technical friction. As a proof of concept, it demonstrates how this privacy technology can be integrated into a wallet browser while preserving self-custody. Experiment on testnet to discover this promising breakthrough for on-chain privacy.


## Resources


### Official documentation


- Silentium GitHub repository (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub repository (server): https://github.com/louisinger/silentiumd
- Web application: https://app.silentium.dev/
- Silent Payments community site: https://silentpayments.xyz
- Specification BIP-352: https://bips.dev/352


### Articles and resources


- Official announcement (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Silent Payments: https://bitcoinops.org/en/topics/silent-payments/


### Testnet tools


- Testnet faucet: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet