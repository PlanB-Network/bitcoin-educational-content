---
name: Umbrel
description: Discover and install Umbrel - Your Bitcoin node and home server
---

![cover](assets/cover.webp)

![video](https://youtu.be/qFfhr4sApso)

## Introduction


### What is a Bitcoin node?


A Bitcoin node is a computer that participates in the Bitcoin network by running Bitcoin Core software or an alternative client. Its role is essential to the operation and security of the network:



- Blockchain storage**: Maintains a complete, up-to-date copy of the Blockchain Bitcoin
- Transaction verification**: validates each transaction and block according to protocol rules
- Information dissemination**: Shares new transactions and blocks with other nodes
- Consensus-building**: Contributes to the application of network rules


Running your own Bitcoin node is a crucial step towards financial sovereignty, offering several key benefits:



- Confidentiality**: Share your transactions without revealing your information to third parties
- Resistance to censorship**: No one can stop you from using Bitcoin
- Independent verification**: No need to trust other people's nodes to verify your transactions
- Consensus building**: Contribute to the application of Bitcoin network rules
- Network support**: Become an active participant in network distribution and decentralization


### Umbrel: A simple solution for running a Bitcoin node


Umbrel is an open source operating system that simplifies the installation and management of a Bitcoin node. It also transforms your computer into a personal and private home server, making it easy to host :



- A complete Bitcoin node
- Bitcoin essential applications (Electrs, Mempool.space)
- Other personal services (cloud storage, streaming, VPN, etc.)


With its elegant and intuitive Interface user interface, Umbrel makes self-hosted services accessible to all, while retaining total control over your data.


## Umbrel installation options


Umbrel offers two main ways to use their solution: a turnkey option (Umbrel Home) and a free open source version (UmbrelOS).


![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)


### Umbrel Home: The turnkey solution


Umbrel Home is a pre-configured home server, specially designed for an optimal experience. This all-in-one hardware solution includes:


**Hardware features**


- High-performance processor optimized for self-hosting
- Pre-installed high-speed SSD storage
- Quiet cooling system
- Compact, elegant design
- Integrated USB and Ethernet ports


**Exclusive benefits**


- Plug-and-play installation: plug in and go
- Premium support with dedicated assistance
- Guaranteed automatic updates
- Integrated migration wizard
- Full hardware warranty
- Full support for all functionalities


**Price**: €399 (price may vary according to season)


### UmbrelOS: The open source version


UmbrelOS is the free, open source version of the Umbrel operating system. This flexible solution lets you use your own hardware while benefiting from Umbrel's essential features.


**Benefits**


- Totally free of charge
- Open, verifiable source code
- Freedom of choice
- Advanced customization options


**Supported platforms**


- Raspberry Pi 5: A popular and affordable solution
- X86 systems: For standard PCs or servers
- Virtual machine: For testing or use on existing infrastructure


**Limitations


- Community support only
- Some advanced features reserved for Umbrel Home
- More technical initial configuration
- Performance depends on hardware selected


This version is ideal for :


- Technical users
- Those who already own compatible equipment
- People who want to learn and experiment
- Developers wishing to contribute to the project


Official installation links :


- [Installation on Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installation on x86 systems (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Virtual machine installation](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)


In this tutorial, we'll concentrate on installing UmbrelOS on a Raspberry Pi 5, but the basic principles remain similar for other platforms.


## Installing Umbrel OS on Raspberry Pi 5


### Required components


For this installation you will need :



- Raspberry Pi 5 (4 GB or 8 GB RAM)
- An official Raspberry Pi power supply (crucial for stability!)
- MicroSD card (32 GB minimum)
- A microSD card reader
- An external SSD for data storage
- Ethernet cable
- A USB cable to connect the SSD


### Installation steps


**Download UmbrelOS**


![Téléchargement UmbrelOS](assets/fr/01.webp)


- Visit the [official website](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Download the latest version of UmbrelOS for Raspberry Pi 5


**Balena Etcher** installation


![Téléchargement Balena Etcher](assets/fr/02.webp)


- Download and install [Balena Etcher](https://www.balena.io/etcher/) on your computer


**Preparing the microSD** card


![Insertion carte microSD](assets/fr/03.webp)


- Insert your microSD card into your computer's card reader


**Image flashing**


![Flashage UmbrelOS](assets/fr/04.webp)


- Launch Balena Etcher
- Select the downloaded UmbrelOS image
- Choose your microSD card as destination
- Click on "Flash!" and wait for the process to finish
- Safely eject the card


**microSD card installation


![Installation microSD](assets/fr/05.webp)


- Insert the microSD card into your Raspberry Pi 5


**Peripheral connection**


![Connexion périphériques](assets/fr/06.webp)


- Connect the external SSD to an available USB port
- Connect the Ethernet cable between the Pi and your router


**Power on


![Démarrage du Pi](assets/fr/07.webp)


- Connect the official Raspberry Pi power supply
- Wait a few minutes for the system to start up


**First access**


![Accès interface web](assets/fr/08.webp)


- On a device connected to the same network, open your browser
- Access Umbrel's Interface web site at: `http://umbrel.local`


![Page d'accueil Umbrel](assets/fr/09.webp)


If `umbrel.local` doesn't work, you'll need to find the IP address of your Raspberry Pi on your local network. You can :


- Consult your router's Interface
- Using a network scanner like nmap
- Use the `arp -a` command in your computer's terminal


## First step on Umbrel


Once your Umbrel is started and accessible via your browser, follow these steps to get started:


### Initial configuration


**Create your account**


![Création compte](assets/fr/10.webp)


- Choose a user name
- Set a secure password
- You will need these credentials to access your Umbrel


**Account confirmation


![Confirmation compte](assets/fr/11.webp)


- Click on "Next" to access your dashboard


**Discovery of the Interface**


![Interface Umbrel](assets/fr/12.webp)


- Access the Umbrel App Store
- Discover the many applications available
- Let's start by installing the essential applications for Bitcoin


### Installing Bitcoin applications


**Bitcoin Node**


![Bitcoin Node](assets/fr/13.webp)


- First application to install
- Download and check the entire Blockchain Bitcoin


**Electrs**


![Installation Electrs](assets/fr/14.webp)


- Electrum server for connecting Bitcoin wallets
- Synchronizes with your Bitcoin node


**Mempool**


![Installation Mempool](assets/fr/15.webp)


- Interface display for Blockchain
- Tracks transactions and blocks in real time


## Tracking a transaction with Mempool.space


Mempool.space is an open-source Blockchain explorer that provides real-time visualization of the Bitcoin network. It lets you track your transactions and understand how transactions propagate on the network.


### Understanding Mempool and confirmations


The "Mempool" (memory pool) is like a virtual waiting room where all unconfirmed Bitcoin transactions are stored before being included in a block. Here's how a transaction is processed:


1. **Broadcast**: When you send a transaction, it is first broadcast on the Bitcoin network

2. **Waiting in Mempool**: Waiting to be selected by a miner on the basis of costs

3. **First confirmation**: A minor includes it in a block (1st confirmation)

4. **Additional confirmations**: Each new block mined after the one containing your transaction adds a confirmation


The recommended number of confirmations depends on the amount :


- For small amounts: 1-2 confirmations may suffice
- For large amounts: 6 confirmations are generally considered very secure


### Explore Interface from Mempool.space


1. **The home page** gives you an overview of the Bitcoin network:


   - Recently mined blocks
   - Cost estimates for different priorities
   - The current state of Mempool


![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)


2. **Search for a transaction**: To track a specific transaction, paste its identifier (txid) into the search bar at the top of the page.


![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)


### Analyze transaction details


Once your transaction has been found, Mempool.space presents you with a complete analysis:


1. **Essential information** :


   - Status (confirmed or not)
   - Expenses paid (in Sats/vB)
   - Estimated confirmation time


![Détails des frais et statut de la transaction](assets/fr/25.webp)


2. **Transaction structure** :


   - Visual representation of inputs and outputs
   - Detailed list of addresses involved
   - Amounts transferred


3. **Technical data** :


   - Transaction weight
   - Virtual size
   - Format and version used
   - Other specific metadata


![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)


### Advantages of using Mempool.space on Umbrel


1. **Confidentiality**: Your requests go through your own node

2. **Independence**: No need to rely on a third-party service

3. **Reliability**: Access to data even when public browsers are down


With this application, you can efficiently monitor your transactions, understand how fees affect confirmation speed, and gain a better understanding of how the Bitcoin network works.


## Connecting a Wallet Bitcoin to your node


### Electrs configuration


**Local connection


![Connexion locale](assets/fr/18.webp)


- For use on your local network
- Quicker and easier to set up


**Remote connection via Tor**


![Connexion Tor](assets/fr/19.webp)


- To access your node from anywhere
- More secure and private


### Connection with Sparrow Wallet


**Access to parameters


![Paramètres Sparrow](assets/fr/20.webp)


- Open Sparrow Wallet
- Go to Preferences > Server
- Click on "Modify existing connection"


**Choice of connection type


Sparrow offers three connection modes:


***Public Server***


- Connection to public servers (e.g. blockstream.info, Mempool.space)
- Simple but less private


***Bitcoin Core***


- Direct connection to a Bitcoin node
- Private but slower


***Private Electrum***


- Connect to your Electrs server
- Combines privacy and performance


**Electrs** configuration


Choose your connection type using the information displayed in the Electrs application we saw earlier:


In both cases, leave the "Use SSL" and "Use proxy" options unchecked.


**Local connection

Host: umbrel.local

Port number: 50001


**Remote connection (Tor)**

Host : [your-address-onion]

Port number: 50001


The Tor connection is necessary if you want to access your node outside your local network.


![Configuration connexion](assets/fr/21.webp)

For more information on Sparrow Wallet software, we have a comprehensive tutorial :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Conclusion


Your Umbrel is now ready to use. You participate actively in the Bitcoin network while retaining full control of your data. Feel free to explore the many other applications available in the Umbrel App Store to extend the capabilities of your home server.


## Useful resources


### Official documentation


- [Official Umbrel website](https://umbrel.com)
- [Umbrel documentation](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)


### Bitcoin applications


- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)


### Community


- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)