---
name: Mastering Liquid Engineering
goal: Master the Liquid Network and Elements, from node operations to confidential transactions and asset issuance.
objectives:
  - Understand Liquid's federated architecture, governance model, and ecosystem
  - Set up and operate Elements nodes with CLI and RPC commands
  - Create confidential transactions and manage issued assets
  - Deploy custom Elements-based networks with proper security configurations
---

# Your path to Liquid Operational Engineering

In this course, we will take you through the complete journey of becoming a Liquid operational engineer. Starting with the fundamentals of Liquid's architecture and governance, you will progressively build hands-on expertise in running Elements nodes, creating confidential transactions, issuing and managing assets, and ultimately deploying your own Elements-based networks.

This is a technical course designed for developers and operators who want to work with Bitcoin sidechains. You will learn the practical skills needed to interact with Elements through CLI and RPC, understand the cryptographic foundations of confidential transactions, and configure federated networks with proper security measures including HSM integration and disaster recovery procedures.

+++


# Overview to Liquid and Elements
<partId>6095b7ca-2339-4f67-8971-2bb9b5db1700</partId>

## Liquid Architecture and Governance Model
<chapterId>11bd45f5-fbd6-434c-8831-1730e0d3521a</chapterId>

![video](https://www.youtube.com/watch?v=d0TmI19Lkc8)


### Liquid Network Governance and Architecture

The Liquid Network represents a federated sidechain solution built on top of Bitcoin, designed to extend Bitcoin's capabilities while maintaining a close relationship with its source code and operational principles. Before diving into the technical details, it is essential to understand the relationship between Blockstream and the Liquid Federation, as this is often misunderstood. Blockstream serves as the technical provider for the Liquid Federation, supplying software and hardware, but does not have direct access to or control over the Liquid Network itself. Each operator of the federation maintains their own independent access to their functionality, creating a separation between the technology provider and the network operators.

The Liquid Network runs on Elements, which is essentially Bitcoin Core with specific extensions. The codebases are so closely related that Elements can synchronize a Bitcoin node up until the Taproot activation in November 2021. The slight differences that prevent full synchronization beyond that point stem from Taproot being developed first in Liquid before being ported to Bitcoin, resulting in minor variations like different exact opcodes. Approximately 80 to 90 percent of the Elements code comes directly from Bitcoin Core, making it a true extension rather than a separate implementation. This close relationship serves an important purpose: Liquid acts as a testing ground for new Bitcoin technologies, with both Segwit and Taproot being analyzed within Elements before their Bitcoin deployment.

The federation operates through a consensus mechanism requiring 11 out of 15 signatures for block validity. Block production follows a round-robin system where every minute, one of the 15 functionaries proposes a block, the remaining functionaries validate and sign it, and then everyone combines the signatures to add the block to the chain. If one functionary is unavailable during their turn, that round is simply skipped, and the next functionary continues the process. This built-in redundancy means the network can tolerate temporary outages without significant disruption, as handling such situations is part of the network's designed resilience.

### Confidential Transactions and Asset Issuance

One of the most significant features distinguishing Liquid from Bitcoin is native asset issuance. Users can issue their own assets within the network without requiring smart contracts or specialized programming tools. The network handles all protocols and transactions natively, meaning every wallet that supports one asset can support any asset without additional development. This native handling is particularly valuable for financial applications and securities because it eliminates the need to audit smart contracts for each new asset, addressing one of the major pain points in EVM-based chains where constant auditing still fails to prevent theft.

Confidential transactions represent another cornerstone feature of the Liquid Network. When sending a transaction, observers can only see the UTXOs, sources, and destinations, similar to Bitcoin. However, both the asset type and the amount remain hidden from outside observers. This means a transaction swapping 10 Bitcoin for USDT appears identical to a simple payment between friends. The privacy implications extend beyond personal financial privacy to trading advantages, as no one can front-run transactions or determine address balances. This confidentiality was initially more expensive due to larger transaction sizes, roughly ten times bigger than non-confidential transactions. Recent protocol improvements through the Elements Improvement Proposal process have implemented discount CT, ensuring confidential and non-confidential transactions now cost exactly the same, removing any financial incentive to sacrifice privacy.

The peg-in process allows users to bring Bitcoin into the Liquid Network. Users receive a pegging address, send their Bitcoin to that address, and after 102 blocks can claim the equivalent LBTC within Liquid. The 102-block requirement mirrors the same number of confirmations Bitcoin miners must wait before spending their mining rewards, following the principle that if this security measure is sufficient for miners, it is sufficient for the federation. The peg-out process is more restricted, limited to federation members only, as a security measure against potential unknown vulnerabilities. Regular users can still convert LBTC back to Bitcoin through atomic trustless swaps offered by various companies, often faster than a direct peg-out since these typically occur via Lightning.

### Federation Structure and Security Model

The Liquid Federation comprises several distinct roles with different capabilities. Wallet users can create transactions but cannot verify them independently since they typically use thin clients connecting to block explorers. Node operators run Elements nodes and continuously validate the chain. Federation members form a superset of the 15 functionaries and participate in governance decisions while also having the ability to perform actual peg-outs. Functionary operators run the specialized hardware called HSMs that handle the cryptographic keys for both block signing and the Bitcoin wallet controlling pegged funds.

A common criticism of Liquid suggests that operators could simply extract keys and act maliciously. However, the keys are held within Hardware Security Modules that prevent direct access even with physical possession of the device. While nothing can be declared absolutely impossible, extracting keys from an HSM is extraordinarily difficult and would not go unnoticed. The security model ensures that even if some operators became malicious, they would still lack the ability to access the keys directly. Blockstream deliberately makes its own operations more difficult by maintaining this separation, choosing to do things correctly rather than conveniently.

The federation governance operates through three boards: the membership board deciding who can join, the oversight board handling internal controls and decision-making processes, and the technology board working closely with Blockstream on technical features. Changes to the network protocol follow the Elements Improvement Proposal process, modeled after Bitcoin's BIP system. This structured approach ensures transparency and community input on network modifications while maintaining the stability that financial applications require.

### Block Finality and Emergency Recovery

Liquid provides two-minute transaction finality, meaning once a block has one confirmation on top of it, the transaction can never be replaced or reorganized. Only the topmost block can theoretically be replaced by another block at the same height, though in over three million blocks this has never occurred. This finality guarantee stems from the HSM security model, where each device will never sign a block below the last block it has signed. The federation cannot collude to change this rule because doing so would require modifying the HSM itself, which presents the same level of difficulty as extracting the keys entirely.

The Bitcoin wallet holding pegged funds operates on an 11 out of 15 multisignature scheme with an important addition: after 4,032 blocks, approximately four weeks, the UTXOs become spendable by emergency keys through a two out of three signature. This contingency plan ensures that if a catastrophic event rendered the network unable to produce blocks, the nearly 3,800 Bitcoin currently on the network could be recovered and returned to their owners. However, this emergency mechanism requires constant maintenance, as the federation must continuously sweep these UTXOs on the Bitcoin side regardless of fee rates to prevent them from ever becoming spendable by the emergency keys. The fees collected on Liquid, currently around three and a half Bitcoin after spending on Bitcoin-side transactions, primarily fund this sweeping process rather than generating profit for any party.

## Liquid Ecosystem and Use Cases
<chapterId>6a5d055c-93e5-4ae6-9dd5-d128b06c009e</chapterId>

**No video -- TBD**

# Running an Elements Node
<partId>5dd19f3e-e56c-44d1-ac46-7631469fd06f</partId>

## How Elements Works
<chapterId>94fa27d7-0339-46a1-ab25-df39916a0cee</chapterId>

![video](https://www.youtube.com/watch?v=v0lzmfH81AY&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=3)

### The Elements Framework

Elements represents a sophisticated technical solution designed to address several persistent challenges that blockchain users encounter in their daily interactions with distributed ledger technology. The primary issues that Elements tackles include transaction latency, insufficient privacy protections, and risks to asset fungibility. These problems have long plagued traditional blockchain implementations, creating friction for users who require faster, more private, and more reliable transaction processing. Elements overcomes these limitations through two innovative mechanisms: federated block signing and confidential transactions, which together create a more efficient and secure blockchain environment.

Unlike the Bitcoin network, which relies on dynamic membership multi-party signatures and proof-of-work consensus, Elements employs a fundamentally different approach to achieving network agreement. The system utilizes what is known as a strong federation of signatories, referred to as block signers, who possess the authority to sign and create blocks in a reliable and timely manner. This architectural decision eliminates the transaction latency inherent in proof-of-work mining, which suffers from significant block time variance due to its random Poisson distribution. Elements can operate either as a sidechain connected to another blockchain such as Bitcoin, or as a completely standalone blockchain with no dependencies on external networks.

### Strong Federations and Functionary Roles

The consensus model underlying Elements, proposed by Blockstream, is called strong federations. This model eliminates the need for proof-of-work entirely, instead relying on the collective actions of a group of mutually distrusting participants known as functionaries. The design philosophy recognizes that security can be achieved through carefully structured cooperation among parties who do not inherently trust one another, rather than through computational competition.

Functionaries within a strong federation can fulfill two distinct roles: block signers and watchmen. Block signers are essential regardless of whether Elements operates as a sidechain or standalone blockchain, while watchmen are only necessary in sidechain configurations where assets must be transferred between chains. The separation of these roles into distinct functions serves an important security purpose, as it limits the potential damage any single attacker could cause by compromising one aspect of the system. When these roles work in concert, Elements delivers both rapid block creation with faster and final transaction confirmation, as well as the ability to manage transferable assets that are directly linkable to another blockchain.

### The Block Signing Process

Traditional blockchains like Bitcoin extend their chains when any participant from a dynamic group demonstrates proof-of-work expended. The dynamic nature of this participant set introduces the latency issues that plague such systems. Elements addresses this by replacing the dynamic set with a known set operating under a multi-signature scheme, which dramatically increases the speed and scalability of the system while maintaining transaction history integrity through validation by all parties.

The federated block signing process operates through a carefully orchestrated sequence of phases. Block signers first propose candidate blocks in a round-robin fashion to all other participating block signers, ensuring fair distribution of block creation opportunities. Each block signer then signals their intent by pre-committing to sign the given candidate block. If the predetermined threshold for pre-commitment is achieved, each block signer proceeds to sign the block. Once the signature threshold is met, the block is accepted and broadcast to the network, indicating that the strong federation has reached consensus. The process then repeats with the next block signer in the round-robin sequence proposing the subsequent block.

Because block generation in a strong federation is deterministic rather than probabilistic and relies on a fixed set of signers, the network will never experience multi-block reorganizations. This characteristic allows for dramatically reduced confirmation wait times compared to traditional proof-of-work systems. Additionally, this model removes the profit-driven mining incentive of block rewards, replacing it with an incentive structure where all participants share the common goal of maintaining beneficial network operation, all without introducing single points of failure or elevated trust requirements.

### Sidechain Operations and the Federated Two-Way Peg

When Elements operates as a sidechain, certain federation members take on the additional responsibility of serving as watchmen. These participants manage the transfer of assets into and out of the Elements sidechain through processes called peg-in and peg-out. For a sidechain to function in a trustworthy manner, participants must be able to verify that the asset supply remains controlled and auditable, which the federated two-way peg mechanism ensures.

The transfer process into the sidechain begins when someone sends mainchain assets to an address controlled by a multi-signature watchman wallet, effectively freezing those assets on the mainchain. Watchmen validate this transaction and release an equivalent amount of the associated asset within the sidechain to a wallet that can prove claim to the original mainchain assets. For transfers back to the mainchain, users create a special peg-out transaction on the sidechain. Watchmen verify this transaction and sign a corresponding transaction from their multi-signature mainchain wallet, requiring a threshold number of federation participants to sign before the mainchain transaction becomes valid. When assets return to the mainchain, the corresponding sidechain amount is destroyed, maintaining consistent total supply across both chains.


## Setting Up and Running Elements, Elements CLI Basics
<chapterId>e51d03ce-ec08-43a4-b9ad-39d677944119</chapterId>

![video](https://www.youtube.com/watch?v=Frr_OjTEPAM&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=4)


### The Elements Network Architecture

Elements is built upon the Bitcoin codebase, which means its fundamental architecture will feel immediately familiar to anyone who has worked with Bitcoin's software components. The core node software, called elementsd, operates as a daemon on a user's machine. A daemon is a program that runs as a background service without requiring direct control from a logged-in user, allowing the node to continuously participate in the network even when no one is actively interacting with it. While this course primarily references elementsd, all operations can alternatively be performed using elements-qt, the graphical interface version, provided the server option is enabled in its configuration.

The elements daemon connects to other nodes across the network to exchange transaction and block data, continuously validating new information and extending its local copy of the blockchain. Alongside the daemon, the Elements software includes a client program called elements-cli, which enables users to send Remote Procedure Call commands to elementsd directly from the command line. Through these RPC commands, users can query wallet balances, examine transaction or block data, broadcast new transactions, and perform numerous other operations essential to interacting with the network.

### The Elements Code Repository and Community Resources

Elements is an open-source project with its complete source code available in the Elements GitHub repository at github.com/ElementsProject/elements. This repository contains the source code for both elementsd and elements-cli, along with supporting installation and build tools, a comprehensive suite of tests, and instructional documentation to help developers get started. To run Elements on your machine, you will need to clone the source code repository, install any required dependencies, and then build the daemon and client executables from source.

Complementing the code repository is the elementsproject.org website, which serves as a community-focused resource explaining what Elements is and how it works. The site features a comprehensive tutorial section that teaches Elements concepts through command line examples and demonstrates how to build simple desktop and web applications on top of the platform. The website also lists popular community discussion forums and is itself hosted on GitHub, enabling community members to contribute improvements to the documentation and educational content.

### Nodes Configuration and Network Parameters

Configuration settings can be passed to an Elements node at startup to customize how it runs, validates data, connects to other nodes, and initializes its blockchain. These settings can be loaded from a designated elements.conf file or passed directly as command line parameters. The configurable options include the name of the default asset used in a standalone blockchain implementation, the initial quantity of assets created, which asset is used for paying transaction fees, and the storage location for blockchain data files.

Additional configuration parameters control RPC credentials for connecting to a Bitcoin node, the N-of-M threshold and valid public keys for block signing, and the script requirements for transferring assets in and out of a sidechain. Many of these parameters form part of the network's consensus rules, making it essential that they are applied consistently across all nodes at startup. While some settings can be modified after a chain has been initialized, others must remain fixed once they have been used to initialize the chain.

### Basic Operations Using the Command Line

This course demonstrates operations using the elements-cli program to make RPC calls to one or more Elements nodes from a terminal session. To make commands more concise and readable, the examples use aliases as a typographic shortcut. When you encounter commands using e1-dae and e1-cli, these aliases actually expand to full commands that specify the path to the Elements executables and include a datadir parameter pointing to the appropriate configuration and data directory.

The datadir parameter tells both the daemon and client where to locate their configuration files and, for the daemon specifically, where to store its copy of the blockchain. Because the daemon and client share a configuration file, the client can make RPC calls to the daemon when they reference the same datadir. By running the daemon with different datadir values, you can start multiple instances of Elements on a single machine, each maintaining its own separate copy of the blockchain and configuration settings. The course uses e2-dae and e2-cli to reference a second instance with its own distinct data directory, enabling demonstrations of multi-node operations such as transacting assets between nodes, issuing new assets, and exploring blinding and confidential transactions across a local network.

## RPC Tutorial, RPC Extensions
<chapterId>64b2d7f1-0170-4cf4-a9b9-eeb3de330de6</chapterId>

**No video -- TBD**

# Confidential Transactions & Issued Assets
<partId>458b7043-797c-49df-8618-78250849e7fb</partId>

## Creating Confidential Transactions
<chapterId>1ebf9044-f3ba-49db-9a7c-db01335dd94f</chapterId>

![video](https://www.youtube.com/watch?v=-by2xBtXQeE&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=5)

### Confidential Transactions in Elements

Every asset in the Elements blockchain benefits from confidential transactions by default, providing a powerful privacy layer that distinguishes it from many other blockchain implementations. This section explores how confidential transactions work, focusing on the creation of confidential addresses, the blinding mechanism that protects transaction details, and the process of selectively revealing transaction information when necessary. To follow along with these concepts practically, you will need two Elements nodes running, typically aliased as E1 CLI and E2 CLI to communicate with each respective node.

The fundamental principle behind confidential transactions is that transaction amounts and asset types remain hidden from parties not involved in the transaction. This privacy feature operates automatically when using confidential addresses, which Elements generates by default for all new addresses. The system achieves this through the use of blinding keys, which encrypt sensitive transaction details while still allowing the network to validate that transactions are legitimate and that no assets are being created or destroyed improperly.

### Confidential Addresses Creation 

When you generate a new address using an Elements node, the address is confidential by default. You can create one using the get new address command through your Elements CLI. These confidential addresses are immediately recognizable because they begin with the prefix "EL1," which serves as a visual indicator of their confidential nature. You will also notice that confidential addresses are significantly longer than standard blockchain addresses, and this additional length serves an important purpose.

Examining a confidential address using the get address info command reveals several important properties. The output includes a confidential key property, which confirms that this is indeed a confidential address. This confidential key is actually a public blinding key that gets embedded within the address itself, explaining why confidential addresses are so much longer than their non-confidential counterparts. The address information also reveals an associated unconfidential address, which you would use if you specifically wanted to conduct non-confidential transactions within Elements. This unconfidential address has a different prefix, making it easy to distinguish between the two types.

### How Blinding Protects Transaction Details

To understand how confidential transactions protect information, consider a scenario where one node sends funds to itself and another node attempts to view that transaction. When the sending node examines its own transaction using the getTransaction command, it can see all the details clearly, including the exact amount sent and received, the asset ID, and special properties called amountBlinder and assetBlinder. These blinder values are precisely what hide the transaction details from other nodes that were not involved in the transaction.

When a different node attempts to view the same transaction, the results are dramatically different. Using the getRawTransaction and decodeRawTransaction commands, the observing node can see that a transaction occurred, but the actual values appear only as ranges rather than specific amounts. Instead of seeing the asset ID, the node sees only an asset commitment. This means that while the transaction is visible on the blockchain, its meaningful details remain protected. The only exception is the fee output, which remains non-confidential since network fees must be verifiable by all participants.

What makes this privacy mechanism particularly robust is that importing the private key alone does not reveal the confidential information. Even after importing the sending node's private key into the observing node's wallet, the transaction amounts still appear as zeros and the values remain displayed as ranges. This demonstrates that private key ownership and transaction visibility are separate concerns in Elements. The private key controls spending authority, while the blinding key controls information visibility.

### Unblinding Transactions with Blinding Keys

To reveal confidential transaction details to a specific party, you must share the blinding key associated with the address. The DumpBlindingKey command exports this key from the node that owns the address. Once exported, the blinding key can be imported into another node using the ImportBlindingKey command, which requires both the address and the corresponding blinding key as parameters.

After importing the blinding key, running the getTransaction command produces completely different results. The previously hidden amount now displays correctly, showing the exact value that was transacted. The asset ID becomes visible in the transaction details, and all the information that was available to the original transacting party is now accessible to the node that received the blinding key. This selective disclosure mechanism has significant practical applications, such as providing transaction details to auditors who need to verify amounts and asset types held by a party without exposing that information to the entire network.

The confidential transactions feature also supports range proofs, which allow a party to prove that an asset amount falls within a certain range without revealing the exact amount. This capability enables compliance and verification scenarios where approximate values are sufficient, maintaining privacy while still satisfying regulatory or business requirements. Remember that while confidential transactions are enabled by default when generating new addresses, they remain optional, giving users flexibility in how they balance privacy with transparency in their blockchain operations.

## Issuing, Labeling and Sending Assets
<chapterId>b89e1a2c-b1f4-473c-b371-2dcfe842260c</chapterId>

![video](https://www.youtube.com/watch?v=XnY4WZUNSs4&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=6)


### Asset Issuance in Elements

One of the most powerful features of the Elements platform is the ability to issue your own custom assets on the blockchain. This capability opens up numerous possibilities for creating tokens, digital securities, or any other form of digital asset that can be tracked and transferred on a blockchain network. In this chapter, you will learn the complete workflow for issuing your own asset, assigning meaningful labels to it, making other nodes on the network aware of your issuance, and transferring portions of your asset to other participants.

To work through these concepts practically, you need access to two Elements nodes, which we will refer to as E1 and E2. These nodes operate on the same local network and maintain a connection to each other, meaning they share the same transactions in their mempool and will have identical blockchains once transactions are confirmed. Although both nodes may run on the same machine for testing purposes, each node manages its own local copy of the blockchain data. The consistency between them comes from their adherence to the same protocol rules and their consensus on the transaction history.

### Viewing Existing Issuances and Creating New Assets

Before issuing a new asset, it is helpful to examine the current state of asset issuances on the network. The `listissuances` command provides a view of all issuances that a particular node is aware of. When you run this command on both E1 and E2, you will typically see the same issuance history, including the initial Bitcoin issuance that was configured when the network was set up. Each asset on the network is identified by a unique hexadecimal string, and the default Bitcoin asset is automatically assigned the label "bitcoin" for convenience.

To issue your own asset, you use the `issueasset` command with several important parameters. The first parameter specifies the amount of the asset to create, such as 100 units. The second parameter determines how many reissuance tokens to generate, which are special tokens that grant the ability to create additional units of the asset in the future. The third parameter controls whether the issuance should be blinded or unblinded. Setting this to false creates an unblinded issuance, which allows other nodes to view the issuance amounts once they become aware of the transaction. After executing the command, you receive confirmation data including the transaction ID, the unique hex identifier of your new asset, and the hex value of any reissuance tokens created.

The issuance transaction initially resides in the mempool and must be confirmed by generating a block. Once confirmed, running `listissuances` again will show your new asset alongside the previously existing ones. You will notice that your new asset displays its hex identifier but lacks a human-readable label, unlike the default Bitcoin asset.

### Making Other Nodes Aware of Your Issuance

An interesting aspect of Elements is that asset issuance awareness does not automatically propagate to all nodes in the same way that transaction confirmations do. After confirming your issuance on E1, if you check the issuances visible to E2, you may find that E2 only sees the issuances it was previously aware of. This demonstrates that E2 is not automatically informed about the new asset issuance that E1 created, even though the underlying transaction has been confirmed on the shared blockchain.

It is worth noting that E1 could still send some of the new asset to E2 without E2 being aware of the original issuance. The asset would appear as an available balance in E2's wallet, functioning correctly for transfers and other operations. However, if you want E2 to see the actual issuance details, including the amount that was originally issued, you need to import the relevant address into E2 as a watched address. This involves retrieving the transaction information from E1 using the `gettransaction` command with the issuance transaction ID, identifying the output address that corresponds to the asset issuance, and then using the `importaddress` command on E2 to add that address. After completing this process, E2 will be able to see the issuance in its `listissuances` output, including the amount issued, provided the issuance was unblinded.

### Working with Asset Labels

Asset labels provide a convenient way to reference assets without needing to use their full hexadecimal identifiers. To assign a label to an asset, you must restart the Elements node with the appropriate configuration. This can be done by providing the `assetdir` argument when launching the node, specifying the asset hex followed by a colon and your desired label name. Alternatively, you can configure labels in the elements.conf file for persistence across restarts.

A crucial point to understand is that asset labels are entirely local to each node. When you assign a label like "jamestoken" on E1, that label exists only in E1's configuration. E2 can assign a completely different label, such as "strangetoken," to the exact same asset hex, and both labels will function correctly on their respective nodes. This local nature of labels means that nodes can customize their experience without affecting other participants on the network.

The practical benefit of labels becomes apparent when executing transactions. Instead of copying and pasting long hexadecimal asset identifiers, you can simply reference the asset by its label in commands like `sendtoaddress`. When sending assets from E1, you would use the label that E1 recognizes, regardless of what label E2 might have assigned to the same asset. After generating a block to confirm the transaction, you can verify the transfer by checking the wallet information on the receiving node, where the asset will appear under whatever label that node has assigned to it. This labeling system significantly simplifies day-to-day operations when working with multiple custom assets on an Elements network.

## Reissuing Assets, Destroying Amounts
<chapterId>e230bdc7-8c6b-4fad-8f7c-e07f4ee30f58</chapterId>

![video](https://www.youtube.com/watch?v=5em79YHtYk0&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=7)


### Asset Reissuance in Elements

One of the most powerful features of the Elements platform is the ability to issue your own custom assets on the blockchain. However, the initial issuance is just the beginning of what you can do with these assets. This section explores how to reissue additional amounts of an asset that has already been created, as well as how to destroy portions of an issued asset when needed. These capabilities provide essential flexibility for managing token supplies in real-world applications.

When creating more of an existing asset, it does not matter which node originally issued the asset. What matters is whether the node attempting the reissuance possesses what is commonly called the asset's reissuance token. This token acts as a permission mechanism, granting its holder the authority to mint additional units of the associated asset. Throughout this section, you will learn how to initially create a reissuance token during asset issuance, how to use that token to reissue additional amounts, and how to transfer the reissuance token to other nodes so they can also participate in reissuance operations.

### Creation of Assets with Reissuance Tokens

To issue a new asset along with its reissuance token, you use the issue asset command with specific parameters. The command takes three primary arguments: the amount of the asset to create, the number of reissuance tokens to generate, and whether the issuance should be blinded. For example, issuing 100 units of a new asset with one reissuance token in an unblinded format would involve setting the first argument to 100, the second to 1, and the third to false. The unblinded option simplifies the process for learning purposes, though blinded issuances offer enhanced privacy in production environments.

After executing the issuance command, the system returns important information including the asset ID and the transaction ID. The asset ID uniquely identifies your new asset on the blockchain, while the transaction ID references the specific issuance transaction. Both pieces of information prove useful for subsequent operations, particularly when reissuing from different nodes. Once the issuance transaction is confirmed by generating a block, you can examine the transaction details to see the outputs created, including both the asset amount and the reissuance token as separate outputs.

### Working with Reissuance Tokens

The reissuance token functions as a special permission asset that controls who can create additional units of the associated asset. When you check wallet information after an issuance, you will see the reissuance token listed as a separate asset alongside your newly created asset and any existing balances. Only wallets holding a reissuance token can successfully execute the reissue asset command for that particular asset. Attempting to reissue without holding the token results in an error indicating no available reissuance tokens exist in the wallet.

To reissue additional amounts of an asset, you use the reissue asset command with the asset ID and the desired amount. For instance, reissuing 100 more units of an asset doubles the supply from 100 to 200 after confirmation. The list issuances command reveals the complete history of issuances, distinguishing between original issuances and reissuances through the IsReissuance field. Original issuances show this field as false, while subsequent reissuances display it as true.

One particularly important characteristic of reissuance tokens is that they can be transferred and subdivided just like any other asset in Elements. You do not need to send a complete reissuance token to grant reissuance permissions to another party. Any fractional amount suffices to enable reissuance capabilities. This means you could send 0.1 of a reissuance token to another node, and that node would gain full authority to reissue any amount of the associated asset. The transfer process uses the standard send to address command, specifying the recipient address, the amount to send, and the reissuance token's asset ID.

### Destroying Asset Amounts

Beyond reissuance, Elements also supports destroying amounts of an asset through the destroy amount command. Unlike reissuance, destruction is not governed by the reissuance token. Any holder of an asset can destroy portions of their own holdings without needing special permissions. This capability proves useful for various scenarios such as token burns, supply reduction mechanisms, or correcting issuance errors.

To destroy an asset amount, you specify the asset ID and the quantity to destroy. After confirmation, the wallet balance reflects the reduction. For example, destroying 100 units from a balance of 500 leaves 400 remaining. This operation is irreversible, so careful consideration should precede any destruction commands.

Given the power that reissuance tokens represent, controlling access to them becomes critically important in any network deployment. Whoever holds a reissuance token can inflate the supply of the associated asset without limit. Therefore, proper security measures and governance policies around reissuance token distribution are essential considerations when designing asset-based systems on Elements.

# Creating an Elements Network
<partId>5a521cc2-f721-4d2e-a51b-1acb35dc4dd4</partId>

## Block Production, Node Signing, Signatures
<chapterId>da8a5e71-6032-45f1-985f-e8c630ba6d29</chapterId>

![video](https://www.youtube.com/watch?v=kxWX91fCnus&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=8)

### Federated Block Signing in Elements

The Elements blockchain takes a fundamentally different approach to block creation compared to Bitcoin. Rather than relying on the computationally intensive proof-of-work consensus mechanism, Elements employs a strong federation of designated signatories known as block signers. These trusted participants sign and create blocks in a reliable and timely manner, effectively eliminating the transaction latency that characterizes proof-of-work mining. This federated approach removes the large block time variances inherent in traditional mining while maintaining network security without introducing third-party trust requirements.

Throughout earlier tutorials in this series, the generate command has been used to create blocks, which bypasses the block signing model entirely for development and testing convenience. However, understanding the federated signing model is essential for deploying production Elements networks. This section covers how to configure Elements nodes to support federated signing, specifically implementing a 2-of-2 multi-signature block creation requirement where both designated signers must approve each new block.

### The Sign Block Script Configuration

The federated signing model is controlled through the signBlockScript parameter, which can be specified in the Elements configuration file or passed directly to the node at startup. This parameter defines the cryptographic conditions that must be satisfied for a block to be considered valid. Importantly, this script forms part of the network's consensus rules and must be established at chain initialization. You cannot add or modify this script on an already existing chain, which means any changes require wiping the existing blockchain data and restarting fresh with the new configuration.

To build the required script, you first need to generate addresses on each participating node and extract their public keys. Using the getaddressinfo RPC on each node's address reveals the associated public key, while the dumpprivkey RPC retrieves the private key needed for signing operations later. These cryptographic components form the foundation of the multi-signature arrangement. With the public keys from both nodes collected, the createmultisig command constructs a redeem script specifying that two signatures are required from the two provided public keys.

Before starting the chain with federated signing enabled, ensure that the con_max_block_sigsize parameter is set appropriately in each node's elements.conf file. A value of 2000 accommodates the larger signature data required for multi-signature blocks. Without this setting, the combined signatures may exceed the default size limit, causing blocks to be rejected as invalid despite having correct signatures.

### Chain Initialization and Key import

After generating the redeem script, the existing blockchain and wallet data must be cleared to start fresh with the new consensus rules. Stop both nodes using the stop RPC, then delete the elementsregtest directory from each node's data directory. This effectively removes all previous blockchain state while preserving the redeem script you generated earlier.

When restarting the nodes, pass the signblockscript argument with your 2-of-2 multi-signature redeem script. Additionally, include the evbparams parameter set to "dynafed:0:::" to disable Dynamic Federations, which would otherwise complicate the block creation process for this tutorial. Both nodes must be started with identical parameters to ensure they share the same consensus rules. Once running, create new wallets on each node since the previous wallet data was deleted along with the blockchain.

With the new chain initialized, attempting to use the standard generate command will fail, returning null for the blocks field. This confirms that the federated signing rules are being enforced. Before proceeding with block creation, import the previously saved private keys into each node using the importprivkey RPC. This step is necessary because the new wallets have no knowledge of the keys generated before the chain was reset, and these keys are required for signing blocks.

### Signed Blocks Creation and Submission

The block creation process under federated signing involves several distinct steps. First, use the getnewblockhex RPC to create a proposed block. This command generates a block candidate but does not submit it to the network. Running getblockcount confirms the chain height remains unchanged after this operation. Attempting to submit this unsigned block using submitblock results in a "block proof invalid" error, demonstrating that the consensus rules are actively enforcing the signature requirements.

Each node must sign the proposed block using the signblock RPC with the block hex as input. This returns a JSON object containing the public key used for signing and the corresponding signature. Verify that the returned public key matches the one originally extracted from that node's address to ensure the correct key is being used. Repeat this signing process on the second node to obtain both required signatures.

The combineblockssigs RPC merges the individual signatures into a single signed block. This command takes the original block hex and a list of public key and signature pairs from both nodes. The output includes a new hex representing the fully signed block and a complete field indicating whether all required signatures are present. If complete shows false, revisit the con_max_block_sigsize configuration setting, as insufficient size limits are a common cause of signature rejection.

Finally, submit the signed block hex using the submitblock RPC. A successful submission returns no error, and running getblockcount on both nodes should show the chain height has increased by one. Both nodes validate the block independently, verify that the signatures satisfy the redeem script threshold, and add the block to their local copy of the blockchain. This process demonstrates how a federation collaboratively creates blocks through cryptographic signing rather than competitive mining, enabling fast and predictable block times while maintaining decentralized validation across network participants.

## Fedpegscript, Initializing a New Chain, Mainchain-to-Sidechain Transfers, and Claims
<chapterId>74920e01-f371-4799-a4e0-bcc9cb4d98c3</chapterId>

![video](https://www.youtube.com/watch?v=egYzj4N8CB8&list=PLbgdHszjwqsZ7gtielvu3H7iSMViE7xKl&index=9)

### Elements as a Sidechain

Elements is an open-source, general-purpose blockchain platform that can operate independently or be pegged to an existing blockchain such as Bitcoin. When Elements is connected to another blockchain through this pegging mechanism, it functions as a sidechain. The fundamental purpose of sidechains is to enable the two-way transfer of assets between chains, allowing users to move value from one blockchain to another and back again. Implementing Elements as a sidechain provides a powerful way to work around some of the inherent limitations of the mainchain while still retaining a significant degree of the security that comes from having assets ultimately secured on the mainchain.

One of the most important architectural characteristics of this relationship is its asymmetric nature. While a sidechain maintains full awareness of the mainchain and its complete transaction history, the mainchain has absolutely no awareness of the sidechain, and none is required for its operation. This design enables sidechains to innovate freely without the restrictions or delays typically associated with mainchain protocol improvement proposals. Rather than attempting to alter the mainchain directly, extending its functionality through a sidechain allows the mainchain itself to remain secure and specialized, providing a stable foundation that underpins the smooth operation of the sidechain. By extending Bitcoin's functionality and leveraging its underlying security model, an Elements-based sidechain can deliver new capabilities that were previously unavailable to mainchain users. A prominent example of this approach in production is Blockstream's Liquid Network.

### The Federated Peg Script Configuration

To initialize an Elements blockchain as a sidechain, you must use the federated peg script parameter, which can be set either in a node's configuration file or passed as an argument during startup. This script defines which members of the strong federation are authorized to perform peg-in and peg-out functions. The functionaries responsible for these operations are called watchmen because they continuously monitor both the mainchain and sidechain for valid peg-in and peg-out transactions, taking action when valid transactions are detected.

Understanding the terminology is essential for working with federated pegs. Pegging out refers to moving pegged assets from the sidechain back to the mainchain, while pegging in means moving assets from the mainchain into the sidechain. When assets move into the sidechain, the funds are actually locked in a multi-signature address on the mainchain, and a corresponding amount of the asset is created on the Elements sidechain. Conversely, when assets move out of the sidechain, they are destroyed on the Elements chain, and the corresponding amount is released from the locked funds held on the mainchain. Permission to perform these functions requires that functionaries prove ownership of the public keys specified in the federated peg script by using their corresponding private keys.

Creating a federated peg script requires each participating node to generate a public key, with the associated private keys stored securely for later use. Because the federated peg script forms part of the consensus rules of a sidechain, it cannot be applied to an existing non-pegged blockchain after the fact. This means any existing chain data must be wiped before initializing a new chain with the federated peg script. The script itself is typically structured as a multi-signature requirement, specifying how many signatures from which keys are needed to authorize peg operations. For a two-node setup, this would be a two-of-two multi-signature script requiring signatures from both participating nodes.

### The Peg-In Process Execution

Before any pegging operations can occur, blocks must be matured on both chains. This maturity requirement protects against block reorganizations on the mainchain that could otherwise lead to inflation of the pegged asset supply within the sidechain. The goal is to ensure that mainchain blocks are sufficiently finalized before accepting pegging transactions, preventing situations where a reorganization removes a pegging transaction from the mainchain while the corresponding assets have already been issued on the sidechain. For Bitcoin, this typically requires at least 101 blocks before pegging operations can proceed.

The peg-in process begins by generating a special address using the getPeginAddress command. This command creates both a mainchain address and a script that must be satisfied to claim the peg-in funds on the sidechain. The mainchain address is a pay-to-script-hash address used by the functionaries performing the watchman role. It is important to note that peg-in addresses are not designed for long-term use and should not be reused, so the time between generating a peg-in address and claiming it should be minimized. Since getPeginAddress adds a new secret to the calling node's wallet, proper backup procedures for wallet files should be part of your node management process.

After generating the peg-in address, Bitcoin is sent from the mainchain to this address. Once the transaction is confirmed and buried under sufficient blocks (typically 101), the peg-in can be claimed on the sidechain using the claimPegin RPC. This command requires two pieces of information: the raw Bitcoin transaction containing the peg-in and a transaction output proof. After the claim transaction is confirmed on the sidechain by generating a new block, the pegged funds become available in the claiming node's wallet.

### The Peg-Out Process

The peg-out process follows a similar pattern to peg-in but operates in reverse. It begins by generating a Bitcoin address on the mainchain that will receive the peg-out funds. On the Elements sidechain, the sendToMainChain command is used, specifying the destination Bitcoin address and the amount to transfer. After generating a block to confirm this transaction on the sidechain, the balance decreases accordingly. The final step, which occurs on the mainchain side, involves claiming these funds once the sidechain transaction has been properly validated by the federation.

Through this complete workflow, Elements demonstrates its capability as a fully functional sidechain platform. The process encompasses generating a federated peg script, initializing a new chain that uses this script as a network consensus parameter, sending funds from the mainchain to the sidechain, claiming those funds within the Elements sidechain, and initiating the return of funds to the mainchain. This bidirectional asset transfer capability, combined with the security inherited from the mainchain and the flexibility to implement new features on the sidechain, makes Elements a powerful tool for extending blockchain functionality while maintaining robust security guarantees.

## Elements as Standalone Blockchain: Start-up Parameters, Default Asset, Reissuance Token
<chapterId>5ae2065a-ce4f-438f-9e79-b21e83b2f46b</chapterId>

![video](https://www.youtube.com/watch?v=u-3rV7DGtD0)

### Running Elements as a Standalone Blockchain

In the previous section, we explored how to run Elements as a sidechain connected to Bitcoin. This section takes a different approach by demonstrating how to operate Elements as a completely independent blockchain with no links or references to Bitcoin whatsoever. This standalone configuration is particularly useful when you want to leverage the powerful features of Elements, such as native asset issuance and confidential transactions, without requiring any connection to the Bitcoin network.

The process involves several key steps that we will work through systematically. First, we will initialize a new Elements blockchain with a default asset that we will name "NewAsset." During this initialization, we will specify that one million units of NewAsset should be created, along with two reissuance tokens that will allow us to mint additional units later. Since these initial coins are created as "anyone can spend" outputs, we will then claim them to a specific wallet. Finally, we will demonstrate the full functionality by sending assets between nodes and reissuing additional tokens from both nodes on the network.

### Standalone Network Initialization

To initialize an Elements network that operates as a standalone blockchain, each node must be started with specific parameters that configure its independent operation. These parameters serve two primary purposes: they instruct the node not to validate pegins from another blockchain, and they define the characteristics of the network's default asset, including its name and the initial supply to create.

The configuration can be applied either through the elements.conf file or by passing arguments directly through the command line. Command line arguments will override any values specified in the configuration file, which provides flexibility when testing different configurations. For our standalone setup, we need to set the validatePegin parameter to zero, which tells Elements to stop checking a Bitcoin chain for peg-in validation. We then set the default pegged asset name to "NewAsset" to give our native token a recognizable label.

When specifying the initial supply, it is important to understand that Elements follows Bitcoin's convention of denominating values in the smallest unit, similar to how Bitcoin uses satoshis. Since one Bitcoin equals one hundred million satoshis, all values in Elements are expressed with eight decimal places. Therefore, to create one million units of NewAsset, we must specify the value as one million followed by eight zeros. Similarly, when creating two reissuance tokens, we express this as two followed by eight zeros. Both nodes in our network must be started with identical parameters to ensure they recognize the same genesis state and can communicate properly.

### Initial Assets Claim and Wallets Management

After starting both nodes with the standalone configuration, we need to create wallets and rescan the blockchain before the initial coins become visible and claimable. The rescan process is necessary because the wallets were created after the chain was initialized, so they need to discover the existing unspent outputs. Once the rescan completes, both nodes will show the same balances in their wallet information: one million NewAsset and two reissuance tokens. This occurs because the initial coins are created as anyone-can-spend outputs, meaning any node on the network can claim them.

To establish proper ownership, we need to claim these assets by sending them to an address controlled by a specific wallet. Using the sendtoaddress RPC command, we can transfer the one million NewAsset to an address generated by the first node. Since NewAsset is the default asset on this chain, we do not need to specify the asset type explicitly in the command. The same address can receive multiple asset types in Elements, so we can reuse it to also claim the reissuance tokens by specifying the reissuance token's asset ID in the sendtoaddress command.

After generating blocks to confirm these transactions, the first node becomes the sole holder of all initial assets. The second node's wallet will show zero balances, confirming that the anyone-can-spend outputs have been successfully claimed. It is worth noting that when starting a fresh chain, you typically need to generate 101 blocks before normal operations proceed smoothly, due to the coinbase maturity requirements inherited from Bitcoin's design.

### Transferring Assets and Reissuing Tokens

With the assets now properly claimed, we can demonstrate standard transactional operations by sending portions of both NewAsset and the reissuance tokens to the second node. The process mirrors typical Bitcoin transactions but with the added capability of specifying different asset types. When sending NewAsset, we simply provide the destination address and amount, since it is the default asset. When sending reissuance tokens, we must include the asset ID as an additional parameter to identify which asset we are transferring.

After confirming these transfers, both nodes hold portions of the assets. The first node retains the majority of NewAsset along with one reissuance token, while the second node receives a smaller allocation plus one reissuance token. You may notice that balances are slightly less than expected due to transaction fees, which are paid in the default asset on this chain.

The reissuance tokens enable a powerful feature: the ability to mint additional units of the associated asset. Any node holding a reissuance token can create more NewAsset by calling the reissueasset command with the asset name and the desired quantity. This capability was enabled by the initial reissuance token parameter we specified during chain initialization. If that parameter had been omitted or set to zero, the default asset would have a fixed supply with no possibility of future issuance. Both nodes can successfully reissue NewAsset because each holds at least one reissuance token, demonstrating how token-based permissions can distribute minting authority across multiple parties.


# Liquid Network Operations & Security
<partId>9d32a87d-5451-4786-9a75-e76f5938c102</partId>

## Liquid vs Elements
<chapterId>96aaa5ae-cd19-43cf-ae29-ff5d7ffb6b40</chapterId>

**No video -- TBD**

## Creating a 'Liquid-like Network': Config Parameters, Functionary Code, Peg-in/out, PAK Keys, HSM Security, Disaster Recovery, DynaFed
<chapterId>7168c8e4-f612-4f5b-87b9-235082187c76</chapterId>

**No video -- TBD**

# Liquid Network Applications & Tools
<partId>6c1f6d87-9855-4b46-9f99-3f454fb5bd52</partId>

## Blockstream Explorer Services, Use Cases, and Demo
<chapterId>5b38e3a4-ad31-46a3-b07e-c1f003599792</chapterId>

**No video -- TBD**

## Asset Registry, AMP vs Non-AMP Assets, Blockstream AMP 3 Tutorial
<chapterId>12ace544-e785-461a-8416-d4abc055f50b</chapterId>

**No video -- TBD**

## Blockstream ECS and Custody Services
<chapterId>a699cfc9-6c3b-4c2c-9485-086976bbd3aa</chapterId>

**No video -- TBD**

# Final Section
<partId>25c221a3-ce9a-4e55-8e4a-7c905a1f0fdb</partId>


## Reviews & Ratings
<chapterId>a21d5257-4c91-4df8-9006-b7864419db17</chapterId>


<isCourseReview>true</isCourseReview>


## Conclusion
<chapterId>8cb06b89-9773-4672-aca6-957c1b89fe2a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
