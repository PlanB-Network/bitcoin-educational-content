---
name: Heritage
description: A Bitcoin wallet with integrated inheritance mechanism via Taproot scripts
---

![cover](assets/cover.webp)


Passing on bitcoins in the event of death or incapacity represents a major challenge for any crypto-asset holder. Without a suitable inheritance plan, these assets become irrecoverable for your loved ones.


Heritage provides an elegant answer by implementing a dead-man switch mechanism directly on the Bitcoin blockchain. This open-source wallet enables on-chain succession conditions to be configured: if the owner makes no further transactions for a defined period, pre-designated alternative keys can release the funds.


## What is Heritage?


Heritage is a Bitcoin wallet natively integrating an inheritance mechanism via Taproot scripts. Developed under MIT license by Jérémie Rodon, this open-source software guarantees transparency and durability.


Heritage uses Taproot scripts encoded in Bitcoin addresses. Each UTXO integrates two types of spending conditions:



- Primary path** : The owner can spend his bitcoins at any time with his primary key
- Alternative paths**: For each designated heir, a script combines its public key with a timelock


Each owner transaction automatically postpones the activation date of the inheritance clauses. In the event of prolonged inactivity (death, incapacity), the conditions are automatically triggered.


## Heritage service (optional)


Heritage offers two usage options:


**Do it yourself (free)**: The open-source application alone. You manage everything autonomously with your own node. This option offers built-in backup access, built-in inheritance and exclusive control of your bitcoins. However, you need to create your own alerts (calendar, reminders) so you don't forget to renew your timelocks, and there are no automatic notifications for your heirs.


**Use the service (0.05% per year)** : The btc-heritage.com service adds features to simplify management:


- Automatic reminders before your deadlines expire
- Automatic notifications to heirs to guide them through the recovery process
- Priority support
- Simplified descriptor management


Fee: 0.05% of amount managed per year, minimum 0.5 mBTC/year. First year free.


The service remains non-custodial: your private keys never leave your device. Heritage cannot access your funds.


## Heritage CLI


For advanced users preferring the terminal, Heritage offers a command-line tool (CLI) for granular control and air-gapped machine operation.


![Page Heritage CLI](assets/fr/03.webp)


Full CLI documentation is available at [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Here you'll find instructions for downloading, connecting to the service, creating wallets (with Ledger or local keys), managing heirs and transactions.


This tutorial focuses on the Desktop application, which is more accessible to most users.


## Heritage Desktop


Heritage Desktop is a graphical application with an intuitive interface that guides the user through every step of the configuration process.


### Download


Go to [btc-heritage.com](https://btc-heritage.com) and click on "Download application".


![Page d'accueil Heritage](assets/fr/01.webp)


Choose the version corresponding to your operating system (Linux 64bits or Windows 64bits). Binaries are not digitally signed, which may trigger security warnings.


![Page de téléchargement](assets/fr/02.webp)


### Installation on Linux


On Linux, the application is distributed in AppImage format. Before you can run it, you need to install the `libfuse2` dependency:


```bash
sudo apt install libfuse2
```


![Installation libfuse2](assets/fr/04.webp)


Then make the file executable and run it:


```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```


### First launch


On first launch, the onboarding wizard offers you three choices:


![Onboarding initial](assets/fr/05.webp)



- Setup an Heritage Wallet**: Create a new wallet with heritage plan
- Inherit bitcoins**: Recover bitcoins as an heir
- Explore by myself**: Explore functions without assistance


Select "Setup an Heritage Wallet" to create your first wallet.


### Bitcoin network connection


Choose how to connect to the Bitcoin network:


![Choix connexion](assets/fr/06.webp)



- Using the Heritage Service**: Managed infrastructure, simpler for heirs
- Using my own node**: Connect to your own Bitcoin Core or Electrum node


For this tutorial, we're using our own node.


### Private key management


Select how to manage your private keys:


![Gestion des clés](assets/fr/07.webp)



- With a Ledger Hardware Device** : Maximum safety with wallet hardware (recommended)
- Local storage with password**: Locally stored keys with password protection
- Restore an existing wallet** : Restore from an existing seed


### Node configuration


If you're using your own node, the application guides you through its configuration. Make sure your Bitcoin or Electrum node is :


- Installed and running
- Synchronized with Bitcoin network
- Configured to accept RPC connections (for Bitcoin Core)


![Configuration nœud](assets/fr/08.webp)


Click on "My Bitcoin node is up and running" when your node is ready.


### Status panel


Click on "Status" in the top right-hand corner, then "Open Configuration" to access the connection parameters.


![Panneau Status](assets/fr/09.webp)


Set the URL of your Electrum server (e.g. `umbrel.local:50001` if you're using Umbrel).


![Configuration Electrum](assets/fr/10.webp)


### Creation of wallet


Once the connection has been established, click on "Create Wallet" in the WALLETS tab.


![Créer wallet](assets/fr/11.webp)


A popup explains the split architecture of Heritage :


![Architecture split](assets/fr/12.webp)


1. **Key Provider (Offline)**: Manages your private keys and signs transactions. Can be a Ledger or a wallet software.

2. **Online Wallet**: Handles synchronization with the Bitcoin network, address creation and transaction broadcasting.


Fill in the creation form :


![Formulaire création wallet](assets/fr/13.webp)



- Wallet Name**: A unique name to identify your wallet
- Key Provider**: Choose Local Key Storage for this tutorial
- New/Restore**: Select "New" to generate a new seed
- Word Count**: 24 words recommended for maximum security


Enter a strong password and choose options for Online Wallet :


![Options Online Wallet](assets/fr/14.webp)



- Local Node**: Uses your own Electrum or Bitcoin Core node
- Heritage Service**: Uses the Heritage service (recommended for notification functions)


Click on "Create Wallet" to finalize creation.


### Interface from wallet


Your wallet is now created. The interface displays :


![Interface wallet](assets/fr/15.webp)



- Balance
- SEND and RECEIVE buttons
- Transaction history
- Heritage configuration history
- wallet addresses


### Creating heirs


Go to the "HEIRS" tab to create your heirs.


![Page Heirs](assets/fr/16.webp)


The information popup explains:


- Heirs are Bitcoin public keys associated with individuals
- Every heir has his own mnemonic phrase
- The first heir should be a "Backup" for yourself (in case of loss of your main wallet)


#### Backup heir creation


Click on "Create Heir" and name it "Backup".


![Création héritier Backup](assets/fr/17.webp)


The popup explains why a 12-word sentence without passphrase is safe for heirs:

1. **No immediate access**: Heir keys cannot access funds until the timelock has expired

2. **Compromise detection**: If someone accesses the phrase, you can update the Heritage configuration

3. **Long-term accessibility**: A passphrase could be forgotten after many years


Configure the heir :


![Configuration héritier](assets/fr/18.webp)



- Key Provider** : Local Key Storage
- New**: Generate a new seed
- Word Count**: 12 words


Finalize the creation :


![Finalisation héritier](assets/fr/19.webp)



- Heir Type**: Extended Public Key
- Export to Service**: Optional, enables automatic notification of heirs


The Backup heir is now created:


![Héritier créé](assets/fr/20.webp)


#### Saving the heir's mnemonic phrase


Click on the Backup heir and then on "Show Mnemonic" :


![Afficher mnemonic](assets/fr/21.webp)


**IMPORTANT: Make a note of these 12 words and keep them in a safe place. This is the key to recovering the funds.


![Phrase mnémotechnique](assets/fr/22.webp)


#### Removing seed from the application


Once you've written down the phrase, access the heir parameters (cogwheel icon):


![Paramètres héritier](assets/fr/23.webp)


Use "Strip Heir Seed" to remove the private key from the application. Confirm that you have saved the phrase.


![Strip Heir Seed](assets/fr/24.webp)


This is a security measure: only the public key remains in the application, sufficient to configure inheritance.


#### Creation of a second heir


Repeat the process to create a second heir (e.g. "Satoshi"). You will now have two heirs:


![Deux héritiers](assets/fr/25.webp)



- Backup**: Your personal emergency key
- Satoshi**: A designated heir


### Heritage configuration


Return to your wallet and click on the Settings icon:


![Paramètres wallet](assets/fr/26.webp)


In the "Heritage Configuration" section, click on "Create":


![Heritage Configuration](assets/fr/27.webp)


Set time limits for each heir:


![Configuration délais](assets/fr/28.webp)



- Backup**: 180 days (6 months) - Maturity Date: 2026-06-18
- Satoshi**: 455 days (15 months) - Maturity Date: 2027-03-20


**Important**: Each heir must have a longer delay than the previous one. The first heir (Backup) will have access to the funds first.


Also configure :


![Configuration finale](assets/fr/29.webp)



- Reference Date**: Starting date for calculating lead times
- Minimum Maturity Delay**: Minimum delay after a transaction (10 days recommended)


Click on "Create" to validate the configuration.


The Heritage configuration is now active:


![Configuration active](assets/fr/30.webp)


It displays both heirs with their respective deadlines and expiry dates.


### Saving descriptors


**Important**: Save your wallet descriptors. Without them, even with the mnemonic phrase, fund recovery is impossible.


Click on "Backup Descriptors" :


![Bouton Backup](assets/fr/31.webp)


Save the JSON file containing your Bitcoin descriptors:


![Backup descripteurs](assets/fr/32.webp)


This file should be passed on to your heirs, along with their respective mnemonic phrases.


### Receive bitcoins


Click on "RECEIVE" to generate a reception address:


![Recevoir bitcoins](assets/fr/33.webp)


Congratulations! Your Heritage Wallet is ready to receive bitcoins. Each generated address automatically incorporates your Heritage conditions.


After receiving a transaction, your balance is updated:


![Solde mis à jour](assets/fr/34.webp)


The history displays the transaction and the associated Heritage configuration.


---

## Recovery by an heir


Once the set time has elapsed, the heir can reclaim the funds.


### Prerequisites


The heir needs :

1. His 12-word mnemonic phrase

2. The original wallet descriptor backup file (JSON)


### Creating a Heir Wallet


In the "INHERITANCES" tab, a popup reminds you of these prerequisites:


![Page Heir Wallets](assets/fr/35.webp)


**Please note**: Without the descriptor backup file, access to the funds is IMPOSSIBLE, even with the correct mnemonic phrase.


Click on "Create Heir Wallet" :


![Créer Heir Wallet](assets/fr/36.webp)


Please fill in the form:


![Formulaire Heir Wallet](assets/fr/37.webp)



- Heir Wallet Name**: A name to identify this heir wallet
- Key Provider** : Local Key Storage
- Restore**: Select this option to enter an existing phrase


Enter the 12 words of the heir's mnemonic phrase and configure the Heritage Provider:


![Entrée mnemonic](assets/fr/38.webp)



- Heritage Provider**: "Local" to use your own node with the backup file


Load the JSON backup file and click on "Create Heir Wallet" :


![Chargement backup](assets/fr/39.webp)


### Interface Heir Wallet


The Heir Wallet is created. Initially, if the timelock has not yet expired, no inheritance is available:


![Pas d'héritage disponible](assets/fr/40.webp)


Once the delay has elapsed and the funds have been synchronized with the Bitcoin network, they appear in the list of inheritances:


![Héritage disponible](assets/fr/41.webp)


The interface displays :


- Key type and fingerprint
- Total inheritable funds
- Current spendable amount (0 sat if timelock has not yet expired)
- Maturity and expiry dates


When the maturity date is reached, the "Spend" button transfers the bitcoins to a personal wallet.


---

## Best practices


### Saving descriptors


wallet descriptors are essential for reconstructing your Heritage addresses. **Without the descriptors, even with your mnemonic phrase, you won't be able to find your funds.


### Key security



- Use a Ledger for the main key if possible
- Never store heirs' sentences in the same place as your own
- Spread information across multiple media and locations


### Documentation for your loved ones


Write clear instructions explaining each step of the recovery process. Your heirs may not be familiar with Bitcoin at the critical moment.


## Alternatives


Other solutions exist to manage the transmission of your bitcoins, including Liana and Bitcoin Keeper. You'll find our tutorials below:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Conclusion


Heritage allows you to plan your Bitcoin succession in a sovereign way via the Desktop application. Implementation requires thoughtful consideration of appropriate timeframes and securing secrets. Don't forget to pass on to your heirs:


- Their 12-word mnemonic phrase
- The descriptor backup file
- Recovery instructions


## Resources



- [Heritage official website](https://btc-heritage.com)
- [Documentation CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)