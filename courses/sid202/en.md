---
name: Building with Elements and Liquid Network
goal: Learn to use and develop with the Elements open-source blockchain platform and its key features
objectives:
  - Understand the foundational concepts of the Elements blockchain platform and Liquid sidechains.
  - Learn to set up and run Elements nodes for standalone and sidechain configurations.
  - Gain practical experience with federated block signing and the Federated 2-Way Peg.
  - Set up and manage secure, efficient blockchain environments for real-world use cases.
---

# Build on Liquid and Elements

Discover the advanced features and capabilities of Liquid and Elements, and learn how to effectively utilize these tools to enhance your development projects. This training provides a complete theoretical and practical foundation, enabling you to master features like Confidential Transactions, Issued Assets, and Federated Block Signing.

Liquid, based on the Elements framework, is designed to improve privacy, scalability, and functionality for financial and technical solutions. In this course, you'll gain hands-on experience with asset issuance and management, the Federated 2-Way Peg, and the use of tools like elementsd and elements-cli, empowering you to create innovative solutions tailored to your needs.

This course is tailored to developers of all experience levels. Beginners and intermediate users will find accessible explanations and practical examples, while advanced users can delve deeper into technical details and lesser-known features of Liquid and Elements.

Join us to elevate your skills, unlock the full potential of Liquid and Elements, and create impactful tools for the future of the Liquid innovation.
+++

# Introduction

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Courses Introduction

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

The purpose of Elements Academy is to introduce and explain the key concepts of Elements, the open-source platform that Liquid is built on. By the end of the course, you should have a good understanding of the main features of Elements, such as Confidential Transactions and Issued Assets, and the processes involved in running Elements Core.

Each section will have lessons with explanatory text and a video that ends with a quiz. The number of questions relate to the size of the preceding topic. Section 10 will summarize the course content and end with a larger quiz.

Any questions, requests for additional information or queries over the quiz answers can be directed to your teacher James Dorfman.

## Elements Overview

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements is an open source, sidechain-capable blockchain platform, providing access to powerful features developed by members of the community, such as Confidential Transactions and Issued Assets.

Elements is, at its core, a protocol that enables consensus to be formed around the transaction history and rules that govern the transfer and creation of assets stored in a distributed blockchain ledger.

More background information on Elements can be found readily on the Elements Project website (https://elementsproject.org/), the official Liquid blog (https://blog.liquid.net/), and developer portal(https://liquid.net/devs).

### Elements

Launched in 2015, Elements reduces internal development and research costs and harnesses the very latest blockchain technology, opening up many new use cases for implementation. An Elements-based blockchain can operate as either a standalone Blockchain or be pegged to another and run as a Sidechain. Running Elements as a Sidechain enables assets to be verifiably transferred between different blockchains.

Built upon and extending Bitcoin's codebase, it lets developers familiar with the bitcoind API quickly and cost-effectively create working blockchains and test proof-of-concept projects. Being built on the Bitcoin codebase also allows Elements to function as a testbed for changes to the Bitcoin protocol itself.

Some of the main features of Elements are listed next.

#### Confidential Transactions

By default, all addresses in Elements are blinded using Confidential Transactions. Blinding is the process by which the amount and type of asset being transferred is cryptographically hidden from everyone, except the participants and those they choose to reveal the blinding key to.

#### Issued Assets

Issued Assets on Elements allows multiple types of asset to be issued and transferred between network participants. An Issued Asset also benefits from Confidential Transactions and can be reissued or destroyed by anyone holding the relevant reissuance token.

#### Federated 2-Way Peg

Elements is a general purpose blockchain platform that can also be “pegged” to an existing blockchain (such as Bitcoin) in order to enable the two way transfer of assets from one chain to the other. Implementing Elements as a sidechain allows you to work around some of the inherent properties of the main chain, while retaining a good degree of the security provided by assets secured on the main chain.

#### Signed Blocks

Elements uses a Strong Federation of signatories, called Block Signers, who sign and create blocks in a reliable and timely manner. This removes the transaction latency of the PoW mining process, which is subject to large block time variance due to its random poisson distribution. The Federated Block Signing process achieves reliable block creation without introducing the need for third party trust or computational `algorithm` based mining.

Elements adds all these features on top of the Bitcoin Core codebase, extending the ability of the mainchain protocol and enabling new business use cases when deployed as a sidechain or as a standalone blockchain solution.

# Element

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## How Elements Works

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements provides a technical solution to problems blockchain users face daily; transaction latency, lack of privacy, and risk to fungibility.

Elements overcomes these problems through its use of Federated Block Signing and Confidential Transactions.

Unlike the Bitcoin network, the process of block signing within Elements is not reliant on Dynamic Membership Multiparty Signatures (DMMS) and Proof of Work (PoW). Instead, Elements uses a Strong Federation of signatories, called Block Signers, who can sign and create blocks in a reliable and timely manner. This removes the transaction latency of the PoW mining process, which is subject to large block time variance due to its random poisson distribution. The Federated Block Signing process achieves reliable block creation without introducing the need for third party trust.

Elements can run as a sidechain to another blockchain, such as Bitcoin, or as a standalone blockchain with no dependencies on other networks.

When used as a sidechain, the Strong Federation also contains members who enable the secure and controlled transfer of assets between a main chain and an Elements sidechain. The controlled transfer of assets is called the Federated 2-Way Peg and members who perform the role of asset transfer are called Watchmen.

The processes involved in the running of an Elements network and the roles of the participants in the network are important to understanding how Elements works.

Whether implemented as a sidechain or a standalone blockchain, Elements makes use of Strong Federations of Block Signers to produce blocks.

### Strong Federations

Elements uses a consensus model first proposed by Blockstream, called Strong Federations. A Strong Federation does not need Proof of Work (PoW) and instead relies on the collective actions of a group of mutually-distrusting participants, called Functionaries.

The roles a Functionary can fulfill within a Strong Federation are: Block Signers and Watchmen. Block Signers are required if you run Elements in either sidechain or standalone blockchain mode, whereas Watchmen are only required in a sidechain setup.

The actions a member of a Strong Federation can perform are split between two distinct roles in order to enhance security and limit the damage an attacker can cause.

When combined, the roles of these participants allows Elements to deliver both rapid block creation (faster and final transaction confirmation) and assured, transferable assets (pegged assets directly linkable to another blockchain).

You can read the Strong Federations whitepaper here: https://blockstream.com/strong-federations.pdf

### Block Signers

A blockchain like Bitcoin's is extended when anyone forming part of a dynamic group of block signers extends the chain by demonstrating proof of work expended. The dynamic nature of the set introduces the latency issues inherent to such systems.

By using a fixed signer set a Federated model replaces the dynamic set with a known set, multi-signature scheme. Reducing the number of participants needed to extend the blockchain increases the speed and scalability of the system, while validation by all parties ensures integrity of the transaction history.

Federated block signing consists of several phases:

- Step 1 - Block Signers propose candidate blocks in a round-robin fashion to all other participating Block Signers.

- Step 2 - Each Block Signer signals their intent by pre-committing to sign the given candidate block.

- Step 3 - If the given threshold for pre-commitment is met, each Block Signer signs the block.

- Step 4 - If the signature threshold (which may be different from that of step 3) is met, the block is accepted and sent to the network. The Strong Federation has reached consensus on the latest block of transactions.

- Step 5 - The next block is then proposed by the next Block Signer in the round-robin and the process repeats.

Because a Strong Federation's block generation is not probabilistic and is based on a fixed set of signers, it will never be subject to multi-block reorganizations. This allows for a significant reduction in the wait time associated with confirming transactions. It also removes the incentive to mine for profit (i.e., the block rewards) and replaces it with an incentive to productively participate in a network where all participants have the same shared goal; ensuring the network continues to function in a manner that is beneficial to all. It does this without introducing a single point of failure or higher trust requirements.

### Elements as a Sidechain - Watchmen and the Federated 2-Way Peg

When run as a sidechain, some members of the Strong Federation have an additional role to fulfill, that of the Watchmen. Watchmen are responsible for the transfer of assets into and out of an Elements sidechain, processes known as `Peg-In` and `Peg-Out`.

In order for a sidechain to operate in a trustworthy manner it must allow participants to verify that the supply of assets is controlled and verifiable. An Elements sidechain uses a 2-Way Federated Peg to enable the two-way transfer of assets in and out of an Elements blockchain. This satisfies the requirements of provable issuance and inter-chain transfers.

The Federated 2-way Peg feature allows an asset to be interoperable with other blockchains and representative of another blockchain's native asset. By pegging your blockchain to another, you can extend the capabilities of the mainchain and overcome some of its inherent limitations.

At a high level, transfers into the sidechain occur when someone sends mainchain assets to an address controlled by a multi-signature Watchmen wallet. This effectively freezes the assets on the mainchain. Watchmen then validate the transaction and releases the same amount of the associated asset within the sidechain. The released assets are sent to a sidechain wallet that can prove claim to the original mainchain assets. This process effectively moves assets from the parent chain to the sidechain.

In order to transfer assets back to the mainchain, a user makes a special peg-out transaction on the sidechain. This transaction is checked by Watchmen who then sign a transaction spending from the multi-signature wallet they control on the mainchain. A threshold number of participants in the federation must sign before the mainchain transaction becomes valid. When the Watchmen send an asset back to the mainchain they also destroy the corresponding amount on the sidechain, effectively transferring the assets between blockchains.

## Setting up and Running Elements

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

As Elements is based upon the Bitcoin codebase, the components that make up a functioning network are very similar.

The Elements node software itself is called `elementsd` and runs as a daemon on a user's machine. A daemon (or service in Windows) is a program that runs as a background service without requiring the direct control of a logged on user.

Note: Throughout this document, we will always refer to elementsd as the daemon version, but everything could be done with elements-qt, provided that the server option is enabled.

The Elements daemon connects to other nodes on the network so it can exchange transaction and block data, validating and extending its local copy of the network's blockchain.

The Elements software also consists of a client program called `elements-cli` which allows you to send Remote Procedure Call (RPC) commands to elementsd from the command line. This can be used to query a wallet balance, view transaction or block data or broadcast a transaction for example. This setup should be familiar to anyone who has used the Bitcoin equivalents; bitcoind and bitcoin-cli.

As an Elements node can be configured by passing parameters in at startup or via a configuration file it is possible to have more than one instance running on the same machine. This is useful for testing and development purposes as you can setup your own local network on a single machine, with each Elements node having its own copy of the blockchain data, managing its own pool of unconfirmed valid transactions and listening to RPC requests on different ports.

### The Elements Code Repository and Community

Elements is an open-source project and its source code can be found in the Elements GitHub repository at https://github.com/ElementsProject/elements. The repository contains the source for the elementsd and elements-cli programs along with supporting installation and build tools, a suite of tests and some instructional documentation.

To complement the code repository, there is also the https://elementsproject.org website, a community-focused resource containing explanations of what Elements is, how it works and a comprehensive tutorial section. The tutorial focuses on learning about Elements by following command line examples and shows you how to build simple desktop and web applications on top of it. The site also lists popular Elements community discussion forums and is itself hosted on GitHub, enabling community contributions to be made to the site's content.

In order to run Elements on your machine you will first need to clone (download a copy of) the source code, install any dependencies the code has and finally build the daemon and client executables. The Elements software is then ready to be configured and run.

## Configuring Nodes and Networking

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Configuration settings can be passed to an Elements node on startup in order to change the way it runs, validates data, connects to other nodes and initializes its blockchain data.

Settings are either loaded from the designated `elements.conf` file or passed in as parameters via the command line.

Some of the things can be changed using these parameters:

- The name of the default asset used in a standalone blockchain implementations.
- The number of the initial asset created.
- The asset to be used when paying transaction fees on the network.
- The storage location of the blockchain data files.
- The RPC credentials used to connect to a Bitcoin node.
- The `n of m` threshold to be met and the valid public keys that can sign blocks.
- The script that needs satisfying in order to transfer assets in and out of a sidechain.
- Whether to connect to a Bitcoin node as a sidechain or not.

Many of these form part of the network's consensus rules, so it is important that they are applied across all nodes on startup. Some can be changed after a chain has been initialized but some need to be fixed after they are used to initialize a chain.

The use of parameters will be covered later in the course as and when they relate to each section.

### Basic Operations Using the Command Line

This course will show examples that use the `elements-cli` program to make RPC calls to one or more Elements nodes. This is done from a terminal session and in order to make the commands briefer an `alias` will be used. By this convention when you see something like the following commands:

```bash
e1-dae

e1-cli getnewaddress
```

The `e1-dae` and `e1-cli` are actually a typographic shortcut that makes use of the terminal's `alias` feature. The `e1-dae` and `e1-cli` will actually be substituted when the command is executed and the command that will run will be similar to:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

What we see above is a call to start the Elements daemon and a call to the elements-cli programs located in the `$HOME/elements/src` directory and a value for the `datadir` parameter. The `datadir` parameter allows us to tell the daemon and client instances where to locate their config files and, in the case of the daemon, where to store its copy of the blockchain. As they share a config file the client will be able to make RPC calls to the daemon.

By running the above command again, but with a different `datadir` value, we can start more than one instance of Elements, each with its own separate copy of the blockchain and config settings. By this convention we will use the alias `e2-dae` and `e2-cli` in the course to refer to a different datadir directory than e1's. So the above example for our second `e2` instance would be:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

This will allows us to perform all manner of operations like transacting assets between nodes, issuing assets and checking the use of blinding in Confidential Transactions between different nodes on the same network.

# Using Element Practical usecase

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Confidential Transactions

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

In this section you will learn how to use the Confidential Transactions feature of Elements.

All addresses in Elements are, by default, blinded using Confidential Transactions, which keep the amount and type of assets transferred visible only to participants in the transaction (and those they choose to reveal the blinding key to), while still cryptographically guaranteeing that no more coins can be spent than are available.

### Confidential Addresses and Confidential Transactions

By default, when you create a new address in Elements using the `getnewaddress` command it is created as a confidential address.

In order to demonstrate confidential transactions we'll have e2 send itself some funds and then try and view the transaction from e1. This will demonstrate the confidential nature of transactions in Elements.

Every new address generated by an Elements node is confidential by default. We can demonstrate this by getting e2 to generate a new address.

```
e2-cli getnewaddress
```

Note that the address starts with e1. This identifies it as a Confidential Address. Examining the address in more detail using the getaddressinfo command shows more details of the address.

```
e2-cli getaddressinfo <address>
```

You can see that there is a confidential_key property that tells us it is a confidential address.

The confidential_key is the public blinding key, which is added to the confidential address itself. This is the reason why a confidential address is so long.

It also has an associated unconfidential address. Should you wish to use regular, non-confidential, transactions within Elements, assets should be sent to this address instead of the one with the lq1 prefix.

We can now have e2 send some funds to the address it generated. This will later demonstrate that e1, as it is not one of the transacting parties, will not be able to view the details of the transaction.

```
e2-cli sendtoaddress <address>
```

Note the transaction ID. Confirm the transaction.

```
e2-cli -generate 101
```

Looking at the transaction where e2 sent some funds to itself from the perspective of e2 itself.

```
e2-cli gettransaction <txid>
```

Scrolling up the transaction details, you can see that e2 can view the amounts sent and received as well as the asset transacted. You can also see the amountblinder and assetblinder properties, which are used to blind the details from other nodes not involved in the transaction.

To check the details of the same transaction from e1 we first we need to get the raw transaction details.

```
e1-cli getrawtransaction <txid>
```

That returns raw transaction details. If you look within the vout section you can see that there are three instances. The first two instances are the receiving and change amounts, and the third is the transaction fee. Of these three amounts, the fee is the only one in which you can see a value, as the fee itself is always unblinded within Elements.

### Blinding Keys

What the first two vout sections show are "blinded ranges” of the value amounts and the commitment data that acts as proof of the actual amount and type of asset transacted.

Even if we were to import e2's private key into e1's wallet, it would still not be able to see the amounts and type of asset transacted because it still has no knowledge of the blinding key used by e2. We'll prove this by importing the private key used by e2's wallet into e1's. First we need to export the key from e2

```
e2-cli dumpprivkey <address>
```

Then import it into e1.

```
e1-cli importprivkey <privkey>
```

Now we can prove that e1 can still not see the values.

```
e1-cli gettransaction <txid>
```

Indeed, it shows 0 as the tx amount when it was actually 1.

To be able to see the actual, unblined value, we need the blinding key. To do this we first export the blinding key from e2.

```
e2-cli dumpblindingkey <address>
```

Then import it into e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Now when we get the transaction details from e1.

```
e1-cli gettransaction <txid>
```

It shows that with the blinding key imported, we can now view the actual value of 1 within the transaction.

In this section we've seen that the use of a blinding key hides the amount and type of assets in a transaction, and that by importing the right blinding key, we can reveal those values. In practical use, a blinding key may, for example, be given to an auditor, should there be a need to verify the amounts and types of assets held by a party. The Confidential Transactions feature of Elements also allows for “range proofs” to be performed. Range proofs can prove that an amount of an asset is held within a given range, without the need to expose the actual amount itself.

We have also seen that Confidential Transactions are optional, but enabled by default when a new address is generated.

That's it for this lesson; good luck on the quiz and see you in the next one!

## Issued Assets

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

In this section you will learn how to use the Issued Assets feature of Elements.

Issued Assets enable multiple types of asset to be issued and transferred between Elements network participants. Any node on the network can issue its own assets. Issuances may represent fungible ownership of any asset including vouchers, coupons, currencies, deposits, bonds, shares, etc. Issued Assets opens the door for building trustless exchanges, options, and other advanced smart contracts involving self-issued assets.

An Issued Asset also benefits from Confidential Transactions and they can be reissued by anyone holding the associated token.

The first step is we'll need access to two Elements nodes, which we'll call e1 and e2. The nodes have had their blockchains reset and the default asset split between them.

The two nodes are on the same local network, and are connected to each other, and therefore share the same transactions in their transaction mempool and identical blockchains. Although they are running on the same machine, it is worth noting that they do not share the same actual blockchain files. Each node manages its own local copy of the blockchain, which contains the same transaction history because they are in consensus and adhere to the same protocol rules as each other.

Let's start by checking each node's view of the existing asset issuances on the network.

This is done using the listissuances command.

```
e1-cli listissuances

e2-cli listissuances
```

As you can see, both nodes show the same issuance history. They both display one asset, the initial issuance of 21 million Bitcoin which were created on chain initialization. You can see the hex id of the asset in the results of running the command above and also the label assigned to the asset, which is 'bitcoin'.

It is worth noting that the default asset is always given a label when the chain is initialized. When you issue your own assets, you can set labels for them yourself, which we'll be doing shortly. Before we can do that, we need to issue our own asset.

We'll have e1 issue the new asset. This is done using the issueasset command.

```
e1-cli issueasset 100 1 false
```

`issueasset` accepts 3 parameters.

The amount of the new asset to issue, we've used 100. The amount of tokens to create (tokens are used to reissue amounts of an asset), of which we chose 1. The final parameter tells Elements to either create the asset issuance as blinded or unblinded. We'll use unblinded as we want to view the issuance amounts from e2 in a minute, so we'll enter false.

Running the command returns data about the issuance. These include the transaction id, which you can take a copy of for later use, the unique hex value of the asset, and the unique hex value of the asset's token.

Generate a block to confirm the issuance transaction.

```
e1-cli -generate 1
```

Run the `listissuances` command against e1 again.

```
e1-cli listissuances
```

That shows us that e1 is now aware of 2 issuances, the initial issuance of Bitcoin and our newly issued asset, of which we can see 100 of. Note the hex value of the new asset and that there is no associated asset label, as there is for the bitcoin issuance.

Check e2's list of known issuances again.

```
e2-cli listissuances
```

That shows us that e2 is not aware of the asset issuance e1 made. It can only see the initial issuance of bitcoin that it could already see.

This is because e2 is unaware of, and is not watching, the address to which the new asset was sent to when it was issued by e1.

It is worth noting that even though e2 can not see the issuance itself, e1 could still send e2 some of the asset. The new asset would then show up as an available balance in e2's wallet, even though it is not aware of the original issuance.

In order to enable e2 to see the actual issuance (and therefore the amount issued), we need to add the address to e2 as a watched address.

In order to do this we need to find out the address that the asset was sent to. For this, we will use the transaction id we copied earlier and have e1 retrieve the details of that transaction so we can find out the correct address to add to the wallet watch list of e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Scrolling up past the hex of the transaction data you will see the address that received 100 of our new asset, identified by its hex value.

Take the address and copy it so we can import it into e2.

Now let's import that address into e2. To do this we use the importaddress command.

```
e2-cli importaddress <the-issued-to-address>
```

If we now check e2's list of issuances.

```
e2-cli listissuances
```

You can see that our newly issued asset is now included in the list. The e2 node is also able to determine the amount of the asset that was issued, along with the amount of the associated token, as the issuance was an unblinded issuance. To enable the use of asset ID to name mapping within Elements, first stop Elements.

```
e1-cli stop
```

Then restart it with an additional parameter that maps an asset's hex to the provided label. This enables the node to display data about the asset to us in a more human-readable format. You can add this to the end of elements.conf if you prefer, then you do not need to add the argument to the daemon each time you start it. For example:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

But we will use the argument method here.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Querying the node for a list of issuances again.

```
e1-cli listissuances
```

That shows us that the mapping of the asset's hex value to its label is working. Checking again on the e2 node's list of issuances.

```
e2-cli listissuances
```

You can see that the e2 node does not have access to this label, because labels are only available to the node that set them. Indeed, we can assign a different label to the same asset hex on e2 than we did on e1. First stop the e2 node.

```
e2-cli stop
```

Restarting with a different label assigned to the hex of our new asset.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Listing issuances from e2.

```
e2-cli listissuances
```

Asset labels are local to each node, only the hex of the asset is recognised by other nodes on the network.

The mapping of label to asset hex is useful when carrying out actions such as transactions and wallet balance queries, as it allows a shorthand way to refer to an asset. For example, if we wanted to send some of our new asset (an amount of 10) from e1 to e2 without the use of the label.

First we need to get an address to send the asset to.

```
e2-cli getnewaddress
```

Then use the sendtoaddress command.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Confirm the transaction by generating a block.

```
generate 1
```

Checking the asset was received on e2.

```
e2-cli getwalletinfo
```

We can see that the asset was indeed received.

Note that e2 maps the hex of the asset received and displays it using its own label. An easier way to do the same thing would be to use e1's asset label when sending.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Behind the scenes, Elements maps local labels to hex values to help simplify the use of issued assets.

In this section we have seen how to issue and label assets. In the next section we will look at reissuing and destroying amounts of an issued asset.

## Reissuing Assets

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

In this section you will learn how to issue more of an already issued asset and also how to destroy a given amount of an issued asset.

The need to reissue (creating more) of an asset or destroy an amount of the asset is something that is likely to occur when the asset represents something that does not have a fixed supply. This could apply to assets that represent gold held in a vault for example; as units of gold move in and out of the vault, the asset representing the vault's supply needs to adjusted up or down accordingly.

Reissuing an amount of an asset requires ownership of the associated token that was created alongside the asset when it was initially issued.

When creating more of an asset, It does not matter which node issued the asset in the first place, as long as the node that is reissuing an amount of an asset it is in possession of what is commonly called the asset's reissuance token. We'll look at how to initially create the reissuance token, how to use it to reissue an amount of an asset and also how to transfer the reissuance token to other nodes, so that they also have permission to reissue the asset.

We'll need access to two Elements nodes, which we'll call e1 and e2. The nodes have had their blockchains reset and the default asset split between them.

We'll have e1 issue an amount of 100 of a new asset and create 1 reissuance token for that same asset. We'll create the issuance as unblinded in order to simplify the example. So let's go ahead and issue the asset and its associated reissuance token.

```
e1-cli issueasset 100 1 false
```

Note the ID of the asset and also that of the (reissuance) token.

As we will later be reissuing more of the asset from e2 we will need to take a note of the transaction ID that the asset was issued in and use that to import the address the asset was sent to.

Confirm the transaction.

```
e1-cli -generate 1
```

We'll now check the transaction's details using the gettransaction command:

```
e1-cli gettransaction <txid>
```

Scrolling up past the hex of the transaction's data you will see that in the transaction e1 received 1 reissuance token and 100 of the associated asset.

Take a copy of the address so we can import it into e2.

And now importing the address into e2's wallet.

```
e2-cli importaddress <address>
```

We can now see that both e1 and e2 are aware of the asset issuance.

```
e1-cli listissuances

e2-cli listissuances
```

Currently e1 holds an amount of the asset and the 1 reissuance token but e2 does not.

```
e1-cli getwalletinfo
```

Also note that e1 has less of the default asset than before because it paid a small amount to cover transaction fees. This amount is due to be collected by e1 when the block created is matured over 100 blocks deep.

```
e2-cli getwalletinfo
```

As e1 holds the reissuance token it can reissue more of it. This is done by using the reissueasset command. Let's have e1 reissue another 100 of the asset.

```
e1-cli reissueasset <asset-id> 100
```

Checking the reissuance worked.

```
e1-cli getwalletinfo
```

You can see that e1 now holds 200 of the asset as expected.

As e2 does not hold an amount of the reissuance token they will receive an error if they try to reissue the asset.

```
e2-cli reissueasset <asset-id> 100
```

Note the error message.

We can view the details of the reissuance from e1 using the listissuances command.

```
e1-cli listissuances
```

Note the `is_reissuance` flag.

If we now send e2 an amount of the reissuance token they will be able to reissue an amount of the asset themselves. First we need an address to send it to. It is worth noting that the reissuance token is treated just the same as any other asset within elements when sending and displaying balances and that it can also be broken down to smaller denominations like any other asset, so we do not need to send the 1 reissuance token to e2 in order for it to be able to reissue the asset. Any denomination will suffice. Generating an address for e2 to receive the reissuance token.

```
e2-cli getnewaddress
```

Then send a fraction of the RIT from e1 to e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirm the transaction.

```
e1-cli -generate 1
```

We can now see that e2 holds the 0.1 it was sent.

```
e2-cli getwalletinfo
```

This means that e2 can now reissue more of the asset associated with the RIT it holds in its wallet. We'll have e2 reissue 500 of the asset.

```
e2-cli reissueasset <asset-id> 500
```

Check the result of the reissuance.

```
e2-cli getwalletinfo
```

You can see that e2 now holds the amount reissued in its wallet balance and that the RIT itself is not consumed in the process of asset reissuance.

Destroying an amount of an asset is something anyone who holds at least the amount being destroyed can do, it is not governed by the reissuance token.

```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```

In this section we have seen how to issue an asset, along with how to make use of the reissuance token that is optionally created as part of asset issuance. We've also seen how transferring a reissuance token is as simple as transferring any other asset, and that holding any amount of a reissuance token grants the holder the right to issue more of the associated asset. It is therefore very important to control who has access to reissuance tokens in your network. We've also seen how to destroy an amount of an asset and that this process is not controlled by the possession of the reissuance token.

# Element Federation

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Block Signing

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements supports a federated signing model which allows you to specify the number of Strong Federation members that must sign a proposed block in order to produce a valid block.

Previously, and for ease of example, we have been creating blocks using the `generate` command, which hasn't had to satisfy a multisignature requirement in order for the blocks created to be accepted by the network as valid.

We'll be setting up our nodes to require 2-of-2 multisig block creation. This will be setup using the signblockscript parameter, which can be added to the config file or passed into the node on startup. In order to initialize a chain with this parameter, we first need to build the script that it made up of.

We'll do this using some existing nodes, save the data they output and then wipe the chain so we can restart it using our signblockscript parameter. This is necessary as the script forms part of the network's consensus rules and will need to be set on chain initialisation. It cannot be added at a later date to an already existing chain.

We'll need access to two Elements nodes, which we'll call e1 and e2. The nodes have had their blockchains reset and the default asset split between them.

Ensure that the con_max_block_sig_size parameter is set to a high value in your elements.conf file otherwise, block signing will fail later on in this section. We have set con_max_block_sig_size=2000 for this tutorial.

As we will be resetting out blockchain and wiping the wallets associated with e1 and e2, we will need to take a copy of the addresses, public keys and private keys we use to generate the block signing script so we can use them later.

First, we need each of what will be the block signing nodes to generate a new address, which you need to take a copy of.

```
e1-cli getnewaddress

e2-cli getnewaddress
```

Then we need to extract the public keys from the addresses and note them for later use.

```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```

Then extract the private keys, which we'll re-import later so the nodes can sign the blocks after we re-initialise our blockchain and wallet data.

```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```

Now we need to generate a redeem script with a 2 of 2 multi-signature requirements. We do this by using the createmultisig command and passing the first parameter as 2 and then providing two public keys. It is these keys that ownership of needs proving later when the block is created.

Either node, e1 or e2, could generate the multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

That gives us our redeemscript, which you can copy for use later.

Now we need to wipe the existing blockchain and wallet data so we can start again with the new signblockscript as part of the chain's consensus rules. This is why we needed to take a copy of some of the data earlier, such as the private keys that will be used in the new chain to sign blocks. You need to do this before proceeding.

With our existing wallet and chain data deleted we can now start our nodes and have them initialize a new chain using the signblockscript parameter. Let's pass in -evbparams=dynafed:0::: to disable dynafed activation, because we don't need that advanced feature for this example.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Now we need to import the private keys that we saved earlier so that our nodes can sign and help complete any proposed blocks.

```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```

The use of the generate command should now error as it fails to meet the required block signing rules now enforced by our nodes.

```
e1-cli -generate 1
```

In order to propose a new block either node can call the getnewblockhex command. This returns the hex of a new block that will need signing before it is accepted by any nodes on our network.

```
e1-cli getnewblockhex
```

Remember that the command just creates a proposed block, it doesn't generate one.

To confirm this we can see that there are currently no blocks in our blockchain.

```
e1-cli getblockcount
```

If we try submitting the block hex without signing it first.

```
e1-cli submitblock <block-hex>
```

We get a message telling us that the block proof is invalid. This is because it has not yet been signed by 2 of the required 2 parties.

So let's get e1 to sign the proposed block.

```
e1-cli signblock <block-hex>
```

Have e2 sign the hex.

```
e2-cli signblock <block-hex>
```

Notice that e2 does not sign the output created from e1 signing the proposed block. They both sign the proposed block hex independently of each other's results.

Now we need to combine the block signatures of e1 and e2. Either node can do this, all they need is the signed block hex from the other node.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

You can see the combineblocksigs command outputs the hex of the signed block as well as a status of complete, telling us the block hex is ready to be submitted.

Now either node can submit the completed block hex. We'll have e1 do it.

```
e1-cli submitblock <combined-signed-hex>
```

Checking that the submission was a valid one.

```
e1-cli getblockcount

e2-cli getblockcount
```

You can see that both e1 and e2 have accepted the block as valid and added it to the tip of their local copies of the blockchain.

To summarize the process. In this section we have:
- Proposed a block.
- Had each node sign it.
- Combined the signatures.
- Checked that the signatures are valid and meet the chain's redeemscript threshold.
- Submitted the block.

Each node on the network validated the block and added it to their local copy of the blockchain.

### Block SIgning

Although the process initially appears complex, the sequence of block signing in Elements is always the same and the initial setup needs to be performed only once:

1. Initial setup (performed once)
2. A multisignature address is created called `signblockscript` using the public keys of Federated Block Signers.
3. The redeem script from this is used to start a new blockchain.
4. Block production (ongoing)
5. Proposed blocks are generated and exchanged for signing.

Once a threshold number of signatories have signed the proposed block it is combined and submitted to the network. If it meets the criteria of the chain's `signblockscript`, nodes accept it as a valid block.

## Element as a Side Chain

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements is an open-source, general purpose blockchain platform that can also be `pegged` to an existing blockchain, such as Bitcoin. When pegged to another blockchain, Elements is said to be operating as a `sidechain`. Sidechains enable the two-way transfer of assets from one chain to another. Implementing Elements as a sidechain allows you to work around some of the inherent limitations of the mainchain, while retaining a good degree of the security provided by assets secured on the mainchain.

While a sidechain is aware of the mainchain and its transaction history, the mainchain has no awareness of the sidechain and none is required for its operation. This enables sidechains to innovate without restriction or the delays associated with mainchain protocol improvement proposals. Rather than trying to alter it directly, extending the main protocol allows the mainchain itself to remain secure and specialized, underpinning the smooth operation of the sidechain.

By extending the functionality of Bitcoin and leveraging its underlying security, an Elements-based sidechain is able to provide new functionality that was previously not available to users of the mainchain. An example of an Elements-based sidechain in production use is the Liquid Network.

In order to initialize an Elements blockchain as a sidechain, we need to use the federated peg script parameter. This parameter can be set in a node's config file or passed in on start up.

The federated peg script defines which members of the strong federation can perform peg-in and peg-out functions. These functionaries are referred to as `Watchmen` as they watch the mainchain and sidechain for valid peg-in and peg-out transactions and action them if valid. To `peg-out` means to move pegged assets out of the sidechain and into the mainchain and to `peg-in` means to move pegged assets into the sidechain from the mainchain. When we say `move into the sidechain`, what we actually mean is the funds get locked in a multi-signature address on the mainchain and a corresponding amount of the asset is created on the Elements sidechain. When we say `move out of the sidechain` what we mean is that assets are destroyed on the Elements sidechain and the corresponding amount are released from the locked funds held on the mainchain. Permission to perform the peg-in and peg-out functions requires that functionaries prove ownership of the public keys used in the federated peg script. This is done with the use of the corresponding private keys.

In order to create a federated peg script we therefore first need to have each of our nodes generate a public key. We also need to store the associated private keys for later use as we'll need to wipe any existing chain data and initialize a new chain using the federated peg script. This is because the federated peg script forms part of the consensus rules of a sidechain, and it cannot be applied to an existing, non-pegged, blockchain at a later date.

So let's generate an address with each of our nodes, store the relevant data for later use and generate the federated peg script which we'll use to initialize our sidechain later.

First we need each of our nodes, which will act as the Watchmen in our network, to generate a new address.

```
e1-cli getnewaddress

e2-cli getnewaddress
```

Then we validate the address to obtain the public keys.

```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```

And then retrieve the private keys associated with each address.

```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```

Store the private and public keys for later use.

Now we need to wipe the existing blockchain and wallet data as we'll be initializing a new chain using a federated peg script. You can do this now. Don't forget to start the Bitcoin daemon, which we'll need to peg-in.

Now we can initialize a new chain with a federated peg script created using the public keys we stored earlier. The numbers that we enter and that surround our public keys define and delimit the number of keys used, and the key ownership that must be proven in order to peg-in and out of our sidechain.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Now we will import the private keys that we saved before, so that our nodes can later sign and complete the transfer of assets between chains and satisfy the requirements of the federated peg script.

```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```

We now need to mature some blocks on both chains. Maturity of blocks is a requirement of the peg process as it protects against block reorganizations on the mainchain leading to an inflation of the pegged asset supply within the sidechain.

To keep this section focused on the federated peg, we will be generating blocks without using the block signing model we looked at in the last section, and return to using the 'generate' command to create new blocks.

```
b-cli generate 101

e1-cli generate 1
```

We don't necessarily need to generate blocks right now for elements. But, let's generate one anyway. It's good practice to avoid potential inconsistencies.

Now our chain is ready to peg-in. In order to peg-in we need to generate a special kind of address using the getpeginaddress command. Note that the duration between generating a peg-in address with getpeginaddress and claiming it with claimpegin should be kept as small as possible. peg-in addresses are not long-term durable and should not be reused.

```
e1-cli getpeginaddress
```

You can see that the command creates a new mainchain address, as well as a new script that will need satisfying in order to claim the peg-in funds. The mainchain address is a `pay to script hash` address that will be used by functionaries performing the Watchmen role within the Elements network.

Like getnewaddress, getpeginaddress adds a new secret to the calling node's wallet, so it is important to factor backup of the wallet file into your node management process.

We'll now send some bitcoin from the mainchain to the sidechain. Our mainchain regression test wallet holds some funds already.

```
b-cli getwalletinfo
```

We can see that the wallet holds 50 bitcoin. We'll send one bitcoin from the mainchain to the sidechain. We need to send funds to the mainchain address our node generated earlier.

```
b-cli sendtoaddress <e1-pegin-address>
```

We need to keep the ID of this transaction as we need it for proof of funding later.

We can now see that the mainchain wallet balance has decreased by the amount we sent, plus an additional small amount to cover the transactions fees.

```
b-cli getwalletinfo
```

We need to mature the transaction again.

```
b-cli generate 101
```

In order to have our Elements node claim the peg-in funds we need to obtain the `proof` that the peg-in transaction has been made. The cryptographic proof uses the funding transaction ID to calculate the merkel path and proves that the transaction is present in a confirmed block.

```
b-cli gettxoutproof '["<tx-id>"]'
```

We also need the raw transaction data.

```
b-cli getrawtransaction <tx-id>
```

With the proof and raw data for the peg-in transaction, our elements node can now claim the peg-in using the raw transaction and the transaction proof.

```
e1-cli claimpegin <raw> <proof>
```

Note that there is an optional third argument which we could have provided to claimpegin. This third parameter can be used to specify the sidechain address to send the claimed funds to. This was not needed in our example as we were calling the command from the same node that owns the address the claimed funds are going to.

Checking the balance of e1.

```
e1-cli getwalletinfo
```

Generating a block to confirm the claim.

```
e1-cli generate 1
```

Checking the balance of e1.

```
e1-cli getwalletinfo
```

We can see that the peg-in has been successfully claimed.

To peg-out, the process is similar. In that an address is generated, funds are sent to it and the funds are released if the transaction is valid. We won't cover the whole peg-out process as it involves work on the mainchain which is beyond the scope of this course. The steps in terms of the Elements events are that an address is generated on the mainchain.

```
b-cli getnewaddress
```

Funds are sent to the mainchain address from an Elements node using the sendtomainchain command.

```
e1-cli sendtomainchain <new-address> 1
```

Generating a block to confirm the transaction.

```
e1-cli generate 1
```

Check the balance of the node's wallet.

```
e1-cli getwalletinfo
```

And see that the balance has decreased.

In this section we have seen how to:
- Generate a federated peg script.
- Initialize a new chain that uses the script as a network consensus parameter rule.
- Send funds from the mainchain to the sidechain.
- Claim the funds within the Elements sidechain.
- Understand how sending funds back to the mainchain is started.

### FederatedPegScript


In order to allow Elements to work as a sidechain, the genesis block in its blockchain must be created with a `fedpegscript` in place. This is done by passing in the `fedpegscript` parameter on node start up. The script will then form part of the Elements blockchain's consensus rules and allow peg-in and peg-out requests to be validated and actioned.

The `fedpegscript` is made up of public keys controlled by those authorized to perform the peg actions. The following shows the example format of a 2-of-2 multisignature fedpegscript:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Note: The characters outside the public keys are delimiters that indicate public key and `n of m` requirements. For example, the template for a 1-of-1 fedpegscript would be '5121<pub key 1>51ae'.

### Peg-in

Before a peg-in can be accepted by an Elements sidechain, it must have sufficient confirmations on the mainchain. This is necessary to avoid inflation in the supply of the pegged asset on the Elements sidechain which could be caused by a re-organization of the mainchain.

Short re-organizations of the tip of the Bitcoin blockchain are expected as part of the normal operation of the Proof of Work (PoW) consensus mechanism. As such, Elements only accepts a peg-in to be valid when it has sufficient depth within the Bitcoin blockchain. This serves to prevent Elements from accepting the same peg-in more than once.

### Peg-Out

A peg-out occurs when an Elements node calls the `sendtomainchain` command, which takes as input a mainchain address (the peg-out destination) as well as the amount of the pegged asset to be `withdrawn`. This creates a peg-out transaction on the sidechain. Once the Functionaries who are acting as Watchmen detect that the peg-out transaction has been confirmed on the sidechain, they take care of actually releasing the asset on the mainchain to the peg-out destination, as we learned in earlier sections of the course.

## Elements as a Standalone Blockchain

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

So far, we have looked at how to run Elements as a sidechain. However, it can also operate as a standalone blockchain solution with its own default native asset. In this setup an Elements blockchain still retains all the features of a sidechain implementation, such as Confidential Transactions and Issued Assets, but does not need peg-in or peg-out to add or remove default asset amounts from circulation.

In this section we will:

Initialize a new Elements blockchain with a default asset named `newasset`.

Specify 1,000,000 `newasset` to be created along with 2 reissuance tokens for it.

Claim all the anyone-can-spend `newasset` coins.

Claim all the anyone-can-spend reissuance tokens for 'newasset'.

Send the asset and its reissuance token to another node's wallet.

Reissue more 'newasset' from both nodes.

In order to initialize an Elements network to operate as a standalone blockchain, each node needs to be started with some basic parameters. They are used to tell the node to not try and validate peg-ins from another blockchain, the name of the network's default asset and the amount of the default asset and associated reissuance token to create.

We'll start a new chain using these parameters on our two connected Elements nodes now. We'll name the default asset `newasset` and issue one million of them and two `newasset` reissueance tokens.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Note that the amounts used here are in the smallest denomination the network can accept, so the two hundred million reissuance tokens actually equate to two whole tokens. The same is true for the denomination of initial free coins.

Check our node's current wallet balances.

```
e1-cli getwalletinfo

e2-cli getwalletinfo
```

We can see that the initialisation worked correctly.

As the initial issuance of assets are created as `anyone can spend`, we'll have e1 claim them all so we can remove e2's access to them.

```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Note that we do not need to specify 'newasset' as the asset to send as it is already the default asset. and therefore also the default asset used to pay network fees.

Within Elements, you can send multiple assets types to the same address, so we can re-use the address we just generated to receive the default asset, and use it as the destination address for the reissuance tokens.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirm the transactions.

```
e1-cli generate 101
```

We'll check that e1 is the only holder of the asset and its reissuance token now.

```
e1-cli getwalletinfo

e2-cli getwalletinfo
```

Which we can see is indeed the case.

Now we'll send some of the 'newasset' to e2, who currently holds a balance of zero.

```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Note that we did not have to specify the type of asset to be sent, as `newasset` has been created as the network's default asset

Let's also send some of the reissuance tokens for `newasset` to e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirm the transactions.

```
e1-cli generate 101
```

We can check that the wallets have updated accordingly.

```
e1-cli getwalletinfo

e2-cli getwalletinfo
```

Now we'll reissue some of the default asset from e1. Note that the ability to do this is enabled by the initialreissuancetokens startup parameter. Which if omitted or set to zero will result in a default asset that cannot be reissued at a later date.

```
e1-cli reissueasset newasset 100
```

We were able to use the label of `newasset` instead of having to provide the hex id value because an Elements chain always labels its default asset.

Checking that the reissuance of the default asset worked:

```
e1-cli generate 101

e1-cli getwalletinfo
```

We will now prove that because e2 holds some of `newasset` reissuance tokens, it can also reissue the default asset.

```
e2-cli reissueasset newasset 100
```

Checking that the reissuance of the default asset by e2 worked.

```
e2-cli generate 101

e2-cli getwalletinfo
```

In this section we have set up Elements as a standalone blockchain and checked that basic functionality works as we would expect.

We used startup parameters to:

Initialize a new Elements blockchain with a default asset named 'newasset'.

Specify the amount of the default asset to create on chain initialization.

Create some reissuance tokens for the default asset and reissued more of the default asset from both nodes.

On our standalone blockchain Elements network, all other transactional operations will operate in the same way as the examples covered in the main sections of the course, but will use 'newasset' instead of `bitcoin` as the default and fee asset.

### Node Startup and Chain Initialization Parameters

In order to tell an Elements node to operate as a standalone blockchain a few parameters must be used together. We'll take a look at each now and find out what they do.

#### `validatepegin=0`
As a standalone blockchain does not need to validate any peg-in or peg-out transactions, we need to disable those checks. With this setting, you do not need to run the Bitcoin client software or store a copy of the Bitcoin blockchain, as the Elements network will operate independently.

#### `defaultpeggedassetname`
This allows you to specify the name of the default asset created upon blockchain initialization.

#### `initialfreecoins`
The number (in the equivalent of Bitcoin's Satoshi unit) of the default asset to create.

#### `initialreissuancetokens`
The number (in the equivalent of Bitcoin's Satoshi unit) of the reissuance tokens for the default asset to create. Without this is would be impossible to create more of the default asset. If you do not want it to be possible to create more of the default asset this can be set to zero or omitted.

Using these parameters, the common to start a node would look something like this:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Basic Operations

The `defaultpeggedassetname` parameter applies a label to the default asset. Without this setting, the default asset will be automatically named `bitcoin`. In previous sections, when we sent assets which we issued ourselves to another node we had to specify either the asset hex or the locally applied asset label to tell Elements which asset we were sending. As `defaultpeggedassetname` applies across all nodes we do not need to name it when we send it, even though its name is not `bitcoin`. Every function that would have sent `bitcoin` before by default will now send whatever you chose to label the default asset as.

So sending 10 of the new default asset to an address is as simple as:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

If you have also provided the node with a value for `initialreissuancetokens` greater than zero then you will also be able to reissue more of the default asset, something that is not possible if you run Elements as a sidechain.

To do this, any node holding an amount of the token associated with the default asset just needs to issue a command in the form:

```
e1-cli reissueasset <default asset name> <amount>
```

By using the above parameters you can operate Elements as a standalone blockchain with its own default asset, decoupled from Bitcoin and other blockchains.

## Conclusion

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

In this course we have learned that Elements is an open-source network protocol that can be implemented as a sidechain to another blockchain, or as a standalone blockchain solution.

We've seen that the source code and website for Elements (https://github.com/ElementsProject/elements) are hosted on GitHub and that there are community discussion forums, such as Build On L2(https://community.liquid.net/c/developers/), or the Liquid Developers Telegram (https://t.me/liquid_devel), that can be used to learn more about deploying and developing applications on Elements and Liquid. Key features such as Confidential Transactions and Issued Assets were covered, along with how members of a Strong Federation enable federated block signing and the 2-Way Peg mechanism.

The next step is to challenge yourself with a cumulative quiz that covers all previous sections, then to begin your Elements journey…good luck!

# Conclusion

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Reviews & Ratings

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusion

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>
Congratulations on completing this course!

We're thrilled that you've successfully reached this milestone in your learning journey. Through your dedication and engagement, you've gained valuable knowledge and skills that will serve you well in your professional development.
