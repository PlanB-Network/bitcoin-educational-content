---
name: Mostro
description: KYC-free Bitcoin P2P exchange platform via Lightning and Nostr
---

![cover](assets/cover.webp)


How do you acquire or sell bitcoins without compromising your financial sovereignty? Centralized platforms impose invasive KYC procedures exposing your personal data, with the possibility of arbitrary account freezes or state surveillance.


**Mostro P2P** offers a decentralized alternative combining Lightning Network, the Nostr protocol and hold invoices. Its major innovation: an automated escrow system where your bitcoins remain under your control throughout the exchange, eliminating the risk of theft, exchange bankruptcy or arbitrary confiscation.


## What is Mostro P2P?


Mostro P2P is an open source Bitcoin exchange protocol created by **grunch**, developer of the popular Telegram bot **lnp2pbot** launched in 2021. While lnp2pbot already enabled KYC-free P2P exchanges via Lightning, it presented a major vulnerability: **Telegram constitutes a centralized point of failure** susceptible to censorship by governments.


Mostro represents the **decentralized evolution** of this concept: by replacing Telegram with the **Nostr** protocol (an incensurable network of distributed relays), Mostro eliminates this systemic risk. The protocol combines Lightning Network for instant transactions, Nostr for censorship-resistant communication, and **hold invoices** to create a truly non-custodial automated escrow.


### Technical architecture


Mostro works through three components:


- Daemon Mostrod**: coordinates exchanges between users and Lightning Network
- Lightning** node: creates hold invoices (~24h cryptographic escrow)
- Mostro** customers: user interfaces (CLI, Mobile, Web)


Orders are published on Nostr as public events (type 38383), while private trades are transmitted via end-to-end encrypted messages (NIP-59, NIP-44). Each Mostro instance defines its own fees (generally between 0.3% and 1%) and transaction limits (ranging from a few thousand to several hundred thousand sats, depending on the instance).


### Decisive advantages


**Censorship-resistant**: No government can shut down Mostro as long as Nostr relays exist somewhere in the world. Unlike the vulnerable lnp2pbot via Telegram, Mostro allows exchanges that are **censorship-proof**.


**Escrow non-custodial**: Lightning hold invoices lock your bitcoins without transferring them permanently. Your funds remain under your control and are automatically returned to you in the event of a problem (~24h).


**Confidentiality by design**: Two modes available to suit your needs. Reputation Mode** links your reputation to your Nostr key to build lasting trust. Full Private Mode** favors absolute anonymity with single-use ephemeral keys.


## Main features


**Decentralized communication**: All orders are published on Nostr via cryptographically signed events. Private negotiations are transmitted via end-to-end encrypted messages, guaranteeing absolute confidentiality.


**Reputation system**: 5-star rating with iterative calculation permanently stored on Nostr. Allows you to gradually build a reputation as a reliable trader.


**Decentralized arbitration**: In the event of a dispute, an impartial arbitrator examines the evidence and makes a decision based on transparent criteria. Each dispute generates a unique token for traceability.


**Payment flexibility**: Support for many fiat currencies via the yadio.io exchange rate service. Accepts SEPA transfers, PayPal, Revolut, cash, and any method agreed between parties.


## Mostro customers available


Mostro offers two main operational clients for your P2P exchanges.


### Mostro CLI - Command Line Client


The **Mostro CLI** is the most mature and functional client. Written in Rust, it offers the full range of Mostro features via a command-line interface. Compatible with macOS, Linux and Windows.


**Main controls** :


- `listorders`: Display all available orders
- `neworder` : Create a new buy or sell order
- `takesell` / `takebuy`: Take a buy or sell order
- `fiatsent`: Confirm sending of fiat payment
- `release`: Release the escrow and finalize the exchange
- `getdm`: View direct messages
- `rate` : Evaluate your counterparty after an exchange


Ideal for technical users, automation and environments requiring maximum safety.


### Mostro Mobile - Smartphone application


The **mobile app** in alpha version enables P2P trading directly from your smartphone. Intuitive graphical Interface with tabbed navigation, order viewing, advanced filters and integrated chat to communicate with your counterparties.


Available for **Android** (via APK on GitHub), it's the optimal choice for users favoring simplicity and occasional mobile trading.


### Mostro-web - Interface web (in development)


Interface advanced JavaScript web application under active development. Designed to offer a complete user experience with extensive trading and wallet management functionalities. Access via browser with no installation required.


## Installation and configuration


This tutorial will guide you through the installation and use of the two main Mostro clients: CLI and the mobile application.


### Essential prerequisites


Before you begin, you will need :



- A working Lightning Network** wallet with sufficient liquidity (or Lightning-compatible)
 - Recommended: Phoenix, Breez, Wallet of Satoshi...
 - Minimum 1000 satoshis of liquidity to test


https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- A Nostr** private key (format `nsec1...`)
 - Create a dedicated trading key on [nostrkeygen.com](https://nostrkeygen.com/)
 - Important**: Never use your main personal Nostr key
 - Keep your private key in a safe place (password manager)



- Optional but recommended**: VPN or Tor connection to mask your IP address


https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI installation


#### On macOS


**Step 1: Rust check**


Check that Rust is installed (version 1.64+ required):


```bash
rustc --version
```


If Rust is not installed :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```


**Step 2: Cloning the repository**


```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```


![Vérification Rust et clonage](assets/fr/01.webp)


**Step 3: Configuration**


Copy and edit the :


```bash
cp .env-sample .env
```


Open `.env` and configure your settings:


```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```


**Important for CLI/Mobile** synchronization: To access the same orders on the CLI and the mobile app, you must use the **same Mostro Pubkey** and the **same Nostr relays** in both clients. Check these settings in Settings on the mobile app.


![Configuration .env](assets/fr/02.webp)


**Step 4: Installation**


Compile and install the CLI :


```bash
cargo install --path .
```


Compilation takes 1-2 minutes. The `mostro-cli` executable will be installed in `~/.cargo/bin/`.


![Installation du CLI](assets/fr/03.webp)


**Step 5: Check**


Check that everything works:


```bash
mostro-cli --help
```


You should see the complete list of orders.


![Vérification avec --help](assets/fr/04.webp)


#### On Linux (Ubuntu/Debian)


Installation identical to macOS, with the addition of :


```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```


Then follow steps 3 and 4 in the macOS section.


#### On Windows


First install Rust via [rustup.rs](https://rustup.rs/), then use PowerShell :


```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```


Identical configuration: copy `.env-sample` to `.env` and fill in your parameters.


### Installing Mostro Mobile


#### On Android


**Step 1**: Go to the [GitHub releases page](https://github.com/MostroP2P/mobile/releases) and download the **app-release.apk** file (approx. 65 MB).


![Page GitHub Releases](assets/fr/10.webp)


**Step 2: Once downloaded, open the APK file from your downloads. Android will ask you to authorize installation from this source.


![Téléchargement et installation APK](assets/fr/11.webp)


**Step 3**: Follow the onboarding screens, which present the functionalities:


- Trade Bitcoin freely - no KYC** : Trade without identity verification thanks to Nostr
- Privacy by default**: Choose between Reputation mode and Full privacy mode
- Security at every step**: Protection with non-custodial hold invoices


![Écrans d'accueil Mostro](assets/fr/12.webp)


**Step 4**: Continue onboarding to discover :


- Fully encrypted chat**: End-to-end encrypted communication
- Take an offer**: Browse the order book and choose an offer
- Can't find what you need?** : Create your own customized order


![Suite onboarding](assets/fr/13.webp)


**Step 5: Once onboarding is complete, the app automatically generates a pair of Nostr keys. Go to the menu (☰) then **Account** to save your **Secret Words** (recovery phrase). It's also on this screen that you have the option of changing the privacy mode previously mentioned.


![Menu et sauvegarde des clés](assets/fr/15.webp)


**Important**: Write down your recovery phrase in a safe place (password manager, paper safe).


### Initial security configuration


Whatever platform you use :



- Dedicated key**: Use a separate Nostr identity for trading
- Small amounts**: Start with less than sats 10,000 to get started
- Multiple relays**: Configure 3-5 geographically diverse relays
- Network protection**: Activate VPN or Tor to hide your IP address
- Wallet secure**: Activate automatic locking of your wallet Lightning


## Use with CLI


This section demonstrates the purchase of bitcoins via Mostro CLI following a real-life use case.


### Step 1: List available orders


The `listorders` command displays all active orders:


```bash
mostro-cli listorders
```


You'll see a table with details of each order: ID, type (buy/sell), amount, currency, payment method.


![Liste des ordres disponibles](assets/fr/05.webp)


In this example, an order to sell 5 EUR via Revolut is visible (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).


### Step 2: Taking the order


To buy these bitcoins, take the order with `takesell` :


```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```


Mostro will ask you to provide a **Lightning invoice** to receive the BTC. The exact amount in satoshis is indicated (here: 4715 sats).


![Prise d'ordre de vente](assets/fr/06.webp)


### Step 3: Provide your Lightning invoice


Generate a Lightning invoice from your wallet (Phoenix, Breez, etc.) for the exact amount, then send it :


```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```


The system confirms the shipment and tells you to wait for the seller to pay the hold invoice before activating the escrow.


![Envoi de la Lightning invoice](assets/fr/07.webp)


### Step 4: Contact the seller


Once the escrow has been activated, use `dmtouser` to request payment details from the seller:


```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```


![Communication avec le vendeur](assets/fr/08.webp)


### Step 5: Retrieve the answer


Check direct messages to see the seller's response:


```bash
mostro-cli getdm
```


The seller gives you his payment ID (here his Revtag: `@satoshi`).


![Réception de la réponse](assets/fr/09.webp)


### Step 6: Making the fiat payment


Send the payment via the agreed method (Revolut in this example) to the contact details provided. **Keep all supporting documents** (screenshots, transaction references).


### Step 7: Confirm payment dispatch


Once payment has been made, notify Mostro :


```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```


### Step 8: Receipt of bitcoins


As soon as the seller confirms receipt of the fiat and releases the escrow with the `release` command, you instantly receive your bitcoins on the Lightning invoice you provided.


### Step 9: Evaluation


Rate the seller to contribute to the decentralized reputation:


```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```


### Useful commands


**Cancel an order** (before it is taken) :

```bash
mostro-cli cancel -o <order-id>
```


**Create a new sales order** :

```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```


**Open a dispute** :

```bash
mostro-cli dispute -o <order-id>
```


## Use with the mobile application


This section demonstrates the sale of bitcoins via Mostro Mobile by following a real-life use case.


### Interface main


The application has 3 main tabs:



- Order Book**: Browse available buy (BUY BTC) and sell (SELL BTC) orders
- My Trades**: View your active and historical orders
- Chat**: Communicate with your counterparties using figures


![Interface principale](assets/fr/14.webp)


### Recommended configuration


Before trading, configure a few settings via the menu (☰) > **Settings** :



- Lightning Address** (optional): To receive payments directly
- Relays**: Add several Nostr relays for resilience (e.g. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Check the public key of the Mostro instance you're using


![Paramètres de l'application](assets/fr/16.webp)


**Important for CLI/Mobile synchronization**: If you're using both the CLI and the mobile app, configure **exactly the same Nostr relays and Mostro Pubkey** in both clients. Without this identical configuration, you won't see the same orders available on both interfaces. The relays and Mostro Pubkey visible in Settings (screenshot above) must match those in your CLI `.env' file.


### Step 1: Create a sell order


Press the green **"+"** button at bottom right, then select **SELL** (red button).


![Boutons de création d'ordre](assets/fr/17.webp)


Fill in the creation form :


1. **Currency**: Select the currency you wish to receive (EUR, USD, etc.)

2. **Amount** : Enter the amount in fiat (e.g. 1 to 3 EUR)

3. **Payment methods** : Choose the method (e.g. "Revolut")

4. **Price type**: Select "Market Price"

5. **Premium**: Adjust premium (slider from -10% to +10%, recommended: 0% to sell quickly)


Press **Submit** to publish your order.


### Step 2: Publication confirmation


Your order is now published! It will be available for 24 hours. You can cancel it at any time before a buyer takes it by executing the `cancel` command.


![Ordre publié](assets/fr/18.webp)


The order appears in the **My Trades** tab with the status "Pending" and the badge "Created by you".


### Step 3: A buyer takes your order


When a buyer takes your order, you receive a notification. See details in **My Trades**.


![Ordre pris par un acheteur](assets/fr/19.webp)


**Important instruction**: You must now **pay the hold invoice** displayed to lock your bitcoins (here 4674 sats for 1-5 EUR) in the escrow. You have **15 minutes maximum** otherwise the exchange will be cancelled.


Copy the hold invoice and pay it from your wallet Lightning (Phoenix, Breez, etc.).


### Step 4: Communicate with the buyer


Once the escrow has been activated, press **CONTACT** to open the encrypted chat with the buyer.


The buyer (here "anonymous-gloriaZhao") will contact you to request your payment details. Please reply with your details (Revtag, IBAN, etc.).


![Chat avec l'acheteur](assets/fr/20.webp)


### Step 5: Receipt of fiat payment


Wait until you receive the fiat payment in your Revolut account (or other agreed method). **Check carefully**:


- The exact amount
- The sender
- The reference if requested


The buyer will inform you via chat that he has sent the payment. Mostro will also display a message confirming that the fiat has been sent to you.


![Confirmation d'envoi du paiement](assets/fr/20.webp)


### Step 6: Release the escrow


Once you have **confirmed receipt** of the fiat payment on your account, press the green **RELEASE** button and confirm to send the satss to the buyer.


![Libération de l'escrow](assets/fr/20.webp)


Bitcoins are instantly transferred to the buyer via his Lightning invoice.


### Step 7: Evaluate the consideration


After release, press **RATE** to rate the buyer. Select from 1 to 5 stars (here 5/5) and press **Submit Rating**.


![Évaluation de la contrepartie](assets/fr/21.webp)


The exchange is over!


### Buy bitcoins with the mobile app


The process to **buy** bitcoins is similar but reversed:


1. Browse the **Order Book** > **BUY BTC** tab to view sell orders

2. Click on an interesting order to view details

3. Press **Take Order**

4. Provide your Lightning invoice (generated from your wallet)

5. Wait for the seller to activate the escrow

6. Contact the seller via **CONTACT** for payment details

7. Send fiat payment (keep proof)

8. Seller releases escrow after verification

9. Receive bitcoins instantly on your Lightning invoice

10. Rate the seller (1-5 stars)


### Problem management


**Cancel an order**: In **My Trades**, press your order and then the **CANCEL** button (available only before it is taken).


**Open a dispute**: If a disagreement arises, press **DISPUTE** in the order details. Attach all evidence (chat screenshots, bank transaction references).


## Advantages and limitations


### Benefits


**Financial sovereignty**: Your bitcoins never leave your direct control thanks to the hold invoice mechanism, eliminating the risk of exchange bankruptcy or piracy.


**Censorship-resistant**: No authority can shut down the network or censor your orders. The system works as long as Nostr relays are operational.


**Default anonymity**: Only a pseudonymous Nostr key identifies you, without KYC or personal data. End-to-end encrypted communications.


**Payment flexibility**: Any mutually accepted payment method is possible (transfers, mobile apps, cash, barter).


### Limitations


**Early development**: Rudimentary interfaces and technical learning curve required.


**Limited liquidity**: Limited number of orders, particularly for large amounts or rare currencies.


**Technical requirements**: Basic understanding of Lightning and Nostr required.


**Individual responsibility**: No centralized support in case of problems, caution required.


## Conclusion


Mostro P2P represents a promising alternative to centralized exchanges, combining Lightning Network, Nostr and automated escrow for truly decentralized trading. Despite its early development and limited liquidity, the platform already offers financial sovereignty, censorship resistance and default anonymity.


For bitcoiners who prefer autonomy and confidentiality, Mostro is a viable option worthy of progressive exploration. Its decentralized architecture guarantees community rather than commercial evolution, paving the way for a future of truly free Bitcoin exchanges.


## Resources


### Official documentation


- [Mostro official website](https://mostro.network)
- [Technical documentation](https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)


### Source code and development


- [Main GitHub repository](https://github.com/MostroP2P/mostro)
- [Web client](https://github.com/MostroP2P/mostro-web)
- [Customer CLI](https://github.com/MostroP2P/mostro-cli)


### Community


- [Nostr Protocol](https://nostr.com)
- [Lightning Network Guides](https://lightning.network)