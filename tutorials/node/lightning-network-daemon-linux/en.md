---
name: Lightning Network Daemon (Linux)
description: Installing and running Lightning Network Daemon on Linux
---

![cover-lightning-network-daemon](assets/cover.webp)


The Lightning network is a second layer of Bitcoin, enabling it to take on lightning dimensions, thanks in particular to the speed and low cost of the transactions it offers.


In this tutorial, we'll install the Lightning Network Daemon implementation on our Linux machine (Ubuntu 24.04 distribution).


## What is Lightning Network Daemon?


Lightning Network Daemon is a complete Go implementation of the Lightning network. It was created by Lightning Labs and lets you run a full instance of a Lightning node on your machine.

In other words, with this implementation, you can :



- Interact with the Lightning network**: You can use command lines to create Lightning portfolios, manage payment channels and routes, and much more, directly from your machine terminal.
- Linking a remote Bitcoin node or your own Bitcoin Core instance**: LND lets you link a Bitcoin instance and use it as your backend. To use this implementation, you don't need to run a Bitcoin Core instance on your machine.



https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Why have your own Lightning node?

Lightning is a Bitcoin overlay that optimizes the transfer process and reduces transaction costs.


By rotating your Lightning node, you gain sovereignty and autonomy. You're in control of your funds, so keep in mind:


"Not your keys, not your bitcoins."


In this sense, running a Lightning node increases the security and integrity of your data in the following ways:



- Total control**: Manage your own payment channels, become your own bank and be master of your assets.
- Confidentiality**: Transact without relying on third parties to protect your privacy.
- Learning and autonomy**: Thanks to `lncli` commands, you can better understand Lightning's underlying processes by applying yourself from your terminal.
- Decentralization**: Play an active part in strengthening and decentralizing the Bitcoin / Lightning network.


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


You have two options for running an instance of the LND implementation on our machine. We can either set up the environment on our own machine to run locally, or install LND from a Docker container. Here, we'll concentrate on the first option, and see how to proceed with Docker in a later tutorial.

## Install LND from source code


### Prerequisites

As LND is written in Go, you need to make sure you have the GoLang environment and the necessary dependencies on your Linux machine.



- Hardware requirements:**

For a smooth, seamless experience, your machine will need to have the necessary capacity to run your LND Lightning node.


You will need :

1. **8 GB RAM** for optimum fluidity,

2. **A multi-core processor (quad-core or more)** to efficiently manage your node's actions,

3. **At least 5GB disk space** for pruned node mode and 1TB to run Bitcoin Core (optional if using a remote node)



- Install useful dependencies:**

The command below will allow you to install on your machine the tools you need to run LND. Among other things, you'll need to install `Git`, a versioning tool, and `make`, which can execute and build the LND implementation from source code.


```bash
sudo apt install -y build-essential git make
```


![installation-dependances](assets/fr/01.webp)



- Install GoLang on your Linux machine**


As of the date of this tutorial, LND requires version 1.23.6 of Go*** for installation.


If you had a previous version already installed, remove it for the new Go installation.

```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```


![go-install](assets/fr/02.webp)



- Go** environment configuration

In your `~/.bashrc` file, initialize the following environment variables to add Go to your Linux system.


```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```



- Checking the installation** (in French)

```bash
go version
```


![go-version](assets/fr/03.webp)

### Clone the LND GitHub repository


Use git to get a copy of LND source code locally on your machine

```bash
git clone https://github.com/lightningnetwork/lnd.git
```

![clone-lnd](assets/fr/04.webp)

### Build and install


The `make` tool, previously installed, will enable you to build an executable from the LND source code and proceed with your installation.


```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```


Install LND on your machine


```bash
# installer LND
make install
```


![make-lnd](assets/fr/06.webp)


- Checking your installation** (in French)


To make sure everything went smoothly, running this command should give you the version of LND you're currently running.


```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```

![lnd-version](assets/fr/05.webp)


- Maintenance and upgrades


```bash
cd lnd
git pull
make clean && make && make install
```

⚠️ **IMPORTANT**: LND updates may require more recent versions of Go, so be sure to update your system to avoid dependency problems during installation.

### Configuring Lightning Network Daemon


The configuration of a Lightning LND node is similar to that of Bitcoin, and is carried out in a configuration file containing all the parameters of your node. To do this, at the root of your machine you can create a hidden folder `.LND` and then create your configuration file `LND.conf` in this folder.


```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```




In the configuration file, you can set up your LND node.


```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```


## Understanding your configuration


It's important for you to understand the minimum configuration you need for a correct and complete installation of your LND node.


Based on the contents of the `~/.LND/LND.conf` file, here are the details of the fields:



- noseedbackup**: Allows you to choose whether you want LND to perform automatic backups of your portfolios.  Setting this property to `0` allows you to manually save restore information in a personally chosen secure location.



- debuglevel**: Allows you to define the level of detail of errors and logs in the event of errors occurring during an action.



- Bitcoin.active**: Instructs LND to operate as a Bitcoin node and interact with the Bitcoin network.



- Bitcoin.Mainnet**: Specifies LND to connect to Bitcoin's main network (Mainnet), you can set the values `bitcoind.signet` and `bitcoind.regtest` respectively for the Bitcoin Signet and Bitcoin Regtest networks



- Bitcoin.node**: Specifies the type of Bitcoin node to which LND should connect.



- Bitcoin.rpcuser** and **Bitcoin.rpcpassword** : Represent.

respectively the logins (user, password) to connect to your Bitcoin node



- bitcoind.zmqpubrawblock** and **bitcoind.zmqpubrawtx**: respectively define ZeroMQ endpoints to receive notifications about new blocks and transactions on the Bitcoin network.



## Checking your installation with LND


You'll probably want to make sure that the process has been successful, and that you're synchronizing with the Lightning network to keep your node information up to date.


To start the LND implementation and obtain information about your node, simply type the command :

```bash
lnd getinfo
```

![lnd-getinfo](assets/fr/07.webp)

## Performing actions on LND


Once your installation has been completed and checked, you can start using it.

Here are the essential commands to get you started.


### Create a portfolio

Your Lightning portfolio is the first step in any action to manage your funds.


⚠️ **IMPORTANT**: Take careful note of your 24-word **seed phrase**. You'll need it to recover your funds in the event of problems.


Also save your wallet password so that you can unlock it with the `lncli unlock` command when you restart your LND node.


```bash
lncli create
```

![créer-portefeuille](assets/fr/08.webp)

### Check your balance


Consult your accounts directly from your terminal:


```bash
lncli walletbalance
```

![solde](assets/fr/09.webp)

### Information about your node


Use the command below to find out which channels are active on your node.


```bash
lncli listchannels
```


You can also obtain a list of the nodes to which you are connected.


```bash
lncli listpeers
```


### Channel management


A Lightning channel allows you to have a **direct, pair-by-pair connection with another node on the Lightning network**. In this channel, you can freely exchange Satoshis up to the channel's capacity.


### Connect to a node


Connecting to other Lightning nodes is a fundamental action if you want to actively participate and benefit from the power of Lightning.


To connect to a peer (Lightning node), you'll need three pieces of information:


- The node's public key**: This is the node's unique identifier in the Bitcoin network;
- IP** : The IP of the machine on which the node is installed;
- PORT** :  The port open on the machine that allows communication with this node.


You can find nodes to connect to on [amboss](https://amboss.space/), a platform that lists information on Lightning nodes.


```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```



Make sure you connect to **reliable nodes** to preserve the integrity of your own system. Here are some recommendations for choosing the right connections.



- Geographic diversification**: Connect to nodes in different regions.



- Reputation**: Choose nodes with good availability.



- Capacity**: Choose knots with good liquidity.



- Charges**: Check routing charges.

### Open a payment channel

To open a payment channel, make sure you are **connected** to the peer node, then define the **capacity** (the amount of satoshis) you wish to block in this channel.


```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```

### Create a Lightning invoice


A Lightning invoice represents a string of characters expressing your wish to receive satoshis in your Lightning wallet.

Creating Lightning invoices with your own node allows you to protect your data (geographical and personal) and gives you 100% autonomy over the management of your funds.


```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```


### Paying a Lightning invoice


```bash
lncli payinvoice <FACTURE>
```

### Close a channel


There are two ways to close an active channel on your current node.



- Cooperative closure**: This signals your node's wish to withdraw from the payment channel, ensuring that ongoing tasks are completed and that data is backed up to avoid loss of funds.

```
lncli closechannel <ID_CANAL>
```


- Forced closure**: ⚠️ To be avoided if possible, this action interrupts ongoing processes in your payment channel and increases the risk of losing funds.

```
lncli closechannel --force <ID_CANAL>
```

## Best practices and safety for your LND node.

Safety is paramount when using a Bitcoin/ Lightning node. Here are a few points to reinforce the safety of your installation:



- Keep your `seed phrase` in a secure, off-line location.



- Make regular backups of the `~/.LND/channel.backup` file: This file saves your channel states every time a new channel is opened (or an old channel is closed) on your node.

⚠️ Allows you to restore channels and recover funds blocked in payment channels in the event of data loss or node failure


You can restore your funds with the command below by specifying the backup path of this file:

```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```


- Make sure you've saved your Lightning wallet's restore words and password.
- Keep your system up to date.


## Current troubleshooting

### Frequent problems


- bitcoind connection error** : Check your RPC login details
- Synchronization blocked** : Check your Internet connection
- Permission error**: Check the rights of the folder `~/.LND`



So you've come to the end of this tutorial. If you'd like to learn more about Lightning, we offer this introductory course to give you a better understanding of the concepts and practices behind the Lightning network.



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb