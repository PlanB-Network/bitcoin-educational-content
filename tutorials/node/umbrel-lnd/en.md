---
name: Umbrel LND
description: Advanced tutorial on installing and configuring Lightning Network Daemon (LND) on Umbrel
---
![cover](assets/cover.webp)



## Introduction


This advanced tutorial takes you step-by-step through the installation, configuration and use of the Lightning Node (LND) application on your Umbrel node. You'll learn how to open channels, manage your liquidity and synchronize your node with a mobile application.


## 1. Prerequisite: functional Bitcoin Umbrel node


Before deploying Lightning, you need to have a fully operational Bitcoin node on Umbrel. This involves installing Umbrel (on Raspberry Pi, NAS or other machine) and fully synchronizing the Blockchain Bitcoin.


To install Umbrel and configure your Bitcoin node, we recommend you follow our dedicated tutorial :


https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Make sure your Bitcoin node is up to date and working properly, as Lightning Network relies on it for all off-chain transactions.


## 2. Introduction to Lightning Network


Lightning Network is a second-layer protocol designed to speed up and reduce the cost of Bitcoin transactions by carrying them out outside the main Blockchain.


In concrete terms, Lightning uses a network of payment channels between nodes: two users open a channel by blocking On-Chain BTC (initial transaction), then can instantly exchange payments within this channel. These off-chain transactions are not recorded on the Blockchain, hence their speed and virtually zero cost.


Payments can be routed through multiple channels (thanks to intermediary nodes) to reach any recipient on the network, enabling an almost unlimited scale of instant transactions. Lightning thus offers very fast, low-cost transactions, ideal for everyday payments or micro-transactions, while lightening the load on the Blockchain Bitcoin.


To operate, a Lightning node must be permanently connected to the network and interact with other Lightning nodes. Various software implementations exist (LND, Core Lightning, Eclair, etc.), all of which are compatible with each other. Umbrel uses LND (Lightning Network Daemon) as part of its official Lightning Node application. This tutorial focuses on LND.


For a complete theoretical introduction to Lightning Network, we recommend that you take our dedicated course :


https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

This course will give you a thorough grounding in the fundamental concepts of Lightning Network, before moving on to practice with your LND node.


## 3. Why self-host LND?


Operating your own Lightning node (LND) on Umbrel gives you total sovereignty over your funds and channels, compared with custodial or semi-custodial solutions.


### Comparison of Lightning solutions :


**Solutions custodiales (ex: Wallet of Satoshi)** :


- Your Lightning bitcoins are managed by a trusted third party
- Easy to use, no technical complexity
- The operator holds your funds and can trace your transactions
- You sacrifice control and confidentiality


**Non-commodity consumer portfolios (e.g. Phoenix, Breez)** :


- Users retain their private keys and thus ownership of their BTC
- No complete node management - application manages channels in the background
- Compromise between simplicity and sovereignty
- Dependence on supplier infrastructure for liquidity
- Technical limitations (one smartphone cannot route payments for others)


**Self-hosted LND node (Umbrel)** :


- Maximum sovereignty: your On-Chain and off-chain BTCs are entirely under your control
- No third parties are involved in opening channels or managing your payments
- Increased confidentiality (your channels and transactions are known only to you and your direct peers)
- Freedom of use: connect to your own services and wallets
- Possibility of routing transactions for others (micro-fee remuneration)
- Increased technical responsibilities (maintenance, liquidity management, backups)


In short, self-hosting LND gives you maximum control, but requires more technical skill. It's a trade-off between convenience and sovereignty.


## 4. Step-by-step tutorial


### 4.1 Installing and configuring the Lightning Node application on Umbrel


Once your Umbrel node (Bitcoin) has been synchronized, follow these steps :


![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)


Install the Lightning Node application from the "App Store" section of the Interface Umbrel.


![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)


LND (Lightning Network Daemon) will be deployed on your Umbrel as an application. When you first open it, you'll see a warning message informing you that Lightning is an experimental technology.


![Création ou restauration d'un nœud LND](assets/fr/03.webp)


You can choose between creating a new node or restoring one from a backup/seed. For a first-time installation, choose to create a new node. The Lightning Node app will generate a 24-word mnemonic phrase (your seed Lightning): write it down very carefully (ideally offline, on paper), as it will be used to restore your Lightning funds if necessary.


**Note: On recent versions of Umbrel, installation of the Lightning app provides this 24-word seed (the Bitcoin Umbrel node itself does not).


![Interface principale de Lightning Node](assets/fr/04.webp)


After initialization, you'll access Lightning Node's main Interface.


![Paramètres de l'application](assets/fr/05.webp)


In the application settings, you'll find a number of important options:


   - Consult your Node ID (your node's unique identifier)
   - Connecting an external wallet (Connect Wallet)
   - View secret words
   - Access Advanced Settings
   - Recover channels
   - Download channel backup file
   - Enable automatic backups
   - Configure backup via Tor (Backup over Tor)


These options are essential for the security and management of your Lightning node. Make sure you activate automatic backups and keep your secret words safe.


**Useful resources:**


- [Umbrel Community](https://community.umbrel.com) - Discussion forum for users to share problems and solutions concerning Umbrel and its ecosystem

> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Description of Lightning Node app features on Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Official LND documentation

### 4.2 Opening a Lightning channel


Once LND is up and running, you can open your first Lightning channel. To find quality nodes to connect to:


![Page d'accueil Amboss.space](assets/fr/06.webp)


[Amboss.space](https://amboss.space/) is an explorer for finding reliable nodes to open channels.


![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)


For example, the [ACINQ node](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) is a recognized node with excellent availability and liquidity statistics.


![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)


For this tutorial, we'll open a channel with [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). The information required for connection (pubkey@ip:port) is given on their Amboss page.


To open the channel :


![Bouton d'ouverture de canal](assets/fr/09.webp)


On the Lightning Node home page, click on the "+ OPEN CHANNEL" button


![Configuration du canal](assets/fr/10.webp)


In the channel configuration page :


   - Paste the node ID copied from Amboss (format: pubkey@ip:port)
   - Define the amount of channel capacity (some nodes like ACINQ have minimums, e.g. 400k Sats)
   - Adjust opening transaction fees if necessary


![Canal en cours d'ouverture](assets/fr/11.webp)


Once the transaction has been sent, the channel will appear as "opening" on the home page. Wait for confirmation of the On-Chain transaction.


![Détails du canal](assets/fr/12.webp)


Click on the channel to view its details:


   - Current status
   - Total capacity
   - Breakdown of liquidity (incoming/outgoing)
   - Public key of remote node
   - And other technical information


### Using Lightning Network+ to obtain incoming liquidity


![Lightning Network+ dans l'App Store](assets/fr/13.webp)


Lightning Network+ is available in the Umbrel App Store to make it easier to obtain incoming cash.


![Interface principale de LN+](assets/fr/14.webp)


The main Interface offers three important options:


- "Liquidity swaps: explore the available swap offers
- "Open For Me": filter the swaps for which you are eligible
- "To Docs": access documentation


![Message d'erreur LN+](assets/fr/15.webp)


Note: If you don't have a channel open yet, you'll see this error message when you click on "Open For Me".


![Liste des swaps disponibles](assets/fr/16.webp)


The "Liquidity Swaps" page shows all the swap offers available on the network.


![Swaps éligibles](assets/fr/17.webp)


"Open For Me" filters only those swaps for which your node meets the required conditions.


![Détails d'un swap](assets/fr/18.webp)


Example of swap details :


- Pentagon configuration (5 participants)
- Capacity of 300k Sats per channel
- Prerequisite: minimum 10 open channels with 1M Sats total capacity
- Places available: 4/5


### 4.3 Synchronization with a mobile application (Zeus)


To control your Lightning node remotely (smartphone), you can use Zeus (open-source application available on iOS/Android).


**Zeus configuration with Umbrel :**


![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)


Make sure your Umbrel node is accessible (by default via Tor).

In the Interface Umbrel, open the Lightning Node app, then click on the "Connect Wallet" button as indicated by the arrow.


![Page de connexion avec QR code](assets/fr/20.webp)


A QR code appears, containing your LND access data in lndconnect format. This QR code is particularly dense with information, so don't hesitate to enlarge it for easier reading.


![Configuration initiale de Zeus](assets/fr/21.webp)


On your phone :


   - Open Zeus
   - On the home page, click on "Advanced setup" to connect your own Lightning node
   - In the parameters, select "Create or connect a Wallet"


![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)


In Zeus:


   - Choose "LND (REST)" as connection type
   - You can either scan the QR code (recommended method) or enter the information manually. (Don't hesitate to zoom in on the Umbrel QR code, as it is very dense)
   - Important: activate the "Use Tor" option if your Umbrel is only accessible via Tor (the default)
   - Save configuration


Your Zeus is now connected to your Umbrel node and allows you to make Lightning payments, view your channels, balances, etc., while remaining completely self-managed.


**Advanced connection options:**


By default, the Zeus ↔ Umbrel connection is via Tor. For a faster connection, there are two alternatives:


**Lightning Node Connect (LNC)** :


   - Lightning Labs' encrypted connection mechanism
   - Install the Lightning Terminal app on Umbrel (includes LNC access)
   - Generate a connection QR code in Lightning Terminal (Connect → Connect Zeus via LNC)
   - Scan it into Zeus (choose "LNC" as connection type)


**VPN Tailscale**:


   - Easy-to-configure mesh VPN
   - Install Tailscale on Umbrel (App Store) and on your cell phone
   - Connect Zeus via Tailscale private IP instead of Tor address


These options are not mandatory, and the Tor + Zeus solution works well in most cases.


> **Useful resources:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Official guide to connecting Zeus to Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus open-source project
> - [Umbrel Community - Connecting Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guide to connecting Zeus to Umbrel using Tailscale

## 5. Safety and best practices


Managing a self-hosted Lightning node requires particular attention to security.


### Backup and security for your node


**Essential types of backups**


Your Lightning Umbrel node requires two types of backups:


**The seed sentence (24 words)**


- Recovers On-Chain funds
- Necessary to recreate your Wallet Lightning
- For ultra-secure storage (offline, on paper)


**Static Channel Backup (SCB)** file


- Contains Lightning channel information
- Enables forced channel closure in the event of a crash
- Important:** Never save the `channel.db` file manually (risk of penalties)


**Manual backup procedure


To save your channels manually :

1. Access the Lightning Node menu (three dots "⋮" next to "+ Open Channel")

2. Download the channel backup file

3. Export a new SCB after each channel modification

4. Store SCB securely (encrypted media, off-site copy)


**Umbrel** automatic backup system


Umbrel features a sophisticated automatic backup system that ensures :


*Data protection:*


- Client-side encryption before transmission
- Sending via the Tor network
- Data supplemented by random filling
- Encryption key unique to your device


*Enhanced security:*


- Instant backups on status changes
- Decoy" backups at random intervals
- Hide backup size changes
- Protection against time analysis


*Restoration process:*


- Identifier and key derived from your seed Umbrel
- Complete restoration possible with mnemonic phrase only
- Automatic recovery of latest backups
- Restore channel settings and data


### Crash restoration


If your node is lost (hardware failure, corrupted SD card) :


- Reinstall Umbrel
- Enter your 24-word seed in the Lightning app
- Import the SCB file during restoration


LND will contact each partner of your old channels to close them and recover your share of On-Chain funds. The channels will be permanently closed (to be reopened if necessary).


### Availability and fraud protection


Ideally, leave your knot online as often as possible. In case of prolonged absence:


- A malicious peer could attempt to broadcast an old channel state
- Lightning provides for a "protest period" (about 2 weeks on LND)
- If you are going to be away for a long time, set up a Watchtower


**Watchtower configuration:**


- In LND advanced settings, add the URL of a trusted Watchtower server
- You can use a public service or install your own Watchtower



To find out more about configuring and using watchtowers, we recommend you take a look at our dedicated tutorial :


https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Other best practices



- Software updates:** Keep Umbrel and LND up to date (security fixes)
- Hardware protection:** Use a stable system (Raspberry Pi with SSD, mini-PC) and a UPS
- Network security:** Keep default Tor configuration, change Umbrel admin password (default: "moneyprintergobrrr")
- Encryption:** Enable disk encryption if possible


## 6. Additional tools


Umbrel's Lightning Node app provides the essentials for managing your channels, but third-party tools offer advanced functionality.


### ThunderHub


Interface modern web-based Lightning node management system installable via the Umbrel App Store.


**Features:**


- Real-time visualization of channels (capacities, balances)
- Integrated rebalancing tools
- Support for multi-path billing (MPP)
- QR code generation LNURL
- Transaction management On-Chain


ThunderHub is ideal for monitoring an active routing node and performing simple rebalancing.


### Ride The Lightning (RTL)


Interface web compatible with several Lightning implementations (LND, Core Lightning, Eclair).


**Highlights:**


- Multi-node management
- Context-sensitive dashboards
- Support for submarine swaps (Lightning Loop)
- 2-factor authentication
- Export/import channel backups


RTL is a complete "Swiss army knife" for administering a Lightning node with a more expert-oriented approach.


### Other useful tools



- Lightning Shell** : Command line (lncli) via browser
- BTC RPC Explorer & Mempool** : Monitoring Blockchain
- LNmetrics & Torq**: Routing performance analysis
- Amboss & 1ML**: "Social" management of your node (aliases, contacts, network analysis)


These tools can be installed in just a few clicks via the Umbrel App Store, without any complex configuration.


**Additional tool resources:**


- [ThunderHub.io - Features](https://thunderhub.io) - Overview of ThunderHub features
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL documentation
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - A practical guide to rebalancing
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - Advanced documentation for power-users


## Conclusion


Running your own LND node on Umbrel is an important step towards financial sovereignty. Although it requires more technical involvement than a custodial solution, the benefits in terms of control, confidentiality and active participation in the Lightning network are considerable.


By following this guide, you should now be able to install LND, open channels, manage your liquidity and access your node remotely. Feel free to gradually explore advanced features and additional tools as you become more familiar with the ecosystem.


Remember that the security of your funds depends on your safeguards and practices. Take the time to understand every aspect before committing large sums.