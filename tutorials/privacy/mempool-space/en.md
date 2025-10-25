---
name: Mempool
description: Explore the entire Bitcoin ecosystem.
---

![cover](assets/cover.webp)


The Bitcoin protocol is a pseudonymous, decentralized network open to consultation. Members (nodes), i.e. computers with an instance of the Bitcoin software, have unrestricted access to all data published on Bitcoin. However, in the early years of Bitcoin, the protocol was not as widely accessible as it is today.

In the early days of Bitcoin, it was necessary to run a Bitcoin node in order to access the appropriate tools (bitcoin-cli) to interrogate the network from command lines.


https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Projects have therefore been launched to expand the Bitcoin community, making it more accessible to anyone who doesn't own a node and/or doesn't have the required technical skills.


In this tutorial, we'll look at the **Mempool.space** project, its features and the impact it has had on the Bitcoin ecosystem.


## What is Mempool.space?


**Mempool.space** is an open-source explorer that provides useful information on transactions, transaction fees, blocks and miners on the various Bitcoin protocol networks. Launched in 2020, it brings a significant improvement in user experience through representative graphics, smooth animations and uncluttered interfaces.


To understand the project, a Mempool (memory pool) is a virtual space in which all transactions awaiting confirmation on the Bitcoin network are stored. A Mempool is like a "waiting room" where Bitcoin transactions wait to be confirmed. Each computer on the network (node) has its own waiting room, which explains why not all transactions are visible to everyone at the same time.


The main impact of the platform in the Bitcoin ecosystem is that it allows you to access the varied information in the memory areas of most of the nodes present on Bitcoin without needing to run one. Mempool.space is a repository for viewing and searching Bitcoin protocol networks.


Increasingly widespread use in the ecosystem and the fact that Mempool.space is open source have enabled it to be integrated into more and more personal hosting systems. You can now have your own instance of Mempool.space directly on your personal node. See our tutorial on configuring Mempool.space on your Umbrel node below.


https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## The basics of Mempool.space


As mentioned above, [Mempool.space](https://Mempool.space) is a Bitcoin protocol explorer that lets you monitor your transactions and their propagation on the chosen Bitcoin network in real time, from a graphical Interface.


Mempool.space supports many Bitcoin protocol networks.

In the menu bar, you will find the following networks:


- **Mainnet**: The main Bitcoin network where real Bitcoin transactions take place.
- **Signet**: A test network that uses digital signatures to validate blocks without requiring the resources required by the main network.
- **Testnet 3**: A risk-free test and development network on the Bitcoin protocol.
- **Testnet 4**: The new version of Testnet 3 brings greater stability and new consensus rules to the test environment.


![reseaux](assets/fr/01.webp)


On the home page, on the left in green, you'll see the possible future blocks (groups of transactions) ready to be validated and integrated (mined) into the Bitcoin network. On average, a block is mined every ten minutes: keep this information, as it will come in handy later in our development.

In purplish, on the right-hand side, you'll find the recent blocks mined on Bitcoin, with the number of the last block mined representing the current height of the network.


![blocs](assets/fr/02.webp)


The **Transaction Fees** section is a transaction fee estimator. The higher the fees allocated to your transaction, the more likely it is that your transaction will be added to the next block ready to be mined.

Transaction fees represent the cost a miner will take from you to insert your transaction into a candidate block for mining. It is defined by a ratio of sat/vB (Satoshi/Virtual Bytes) representing the number of satoshis you pay for the space your transaction will occupy in the candidate block.


⚠️ IMPORTANT: In the event of Mempool saturation, miners prioritize transactions offering the best Satoshi/vByte ratio. The heavier (larger) your transaction, the more satoshis it will need to be included quickly.


![fees-visualizer](assets/fr/03.webp)


The **Mempool Goggles** section lets you visualize the space occupied by a transaction.


![mempool](assets/fr/04.webp)


A block is mined approximately every ten minutes due to the difficulty of the proof of work that miners must provide to add their candidate block to the chain of mined blocks. This difficulty varies every **2016 blocks**, equivalent to about **2 weeks**. You can see the evolution of this difficulty here.


![difficulty](assets/fr/05.webp)


The addition of a new block to the main chain entitles the miner of the validated block to a reward made up of a fixed part (halved every 210,000 blocks**, equivalent to around 4 years** during halvings) and transaction fees.


![halving](assets/fr/06.webp)


## Access your transaction details


In the Mempool.space search bar, you can enter your Bitcoin address or your transaction ID to find out more about your history.


![search](assets/fr/07.webp)


On the transaction details page, you will find general information about your transaction:


- **Status**: Confirmed when added to a block, unconfirmed when waiting in a Mempool.
- **Transaction fees**.
- **Estimated time of arrival (ETA)**: The approximate time it will take for your transaction to be added to a block. It is calculated according to the ratio constituting the fees associated with this transaction.


![general-txinfo](assets/fr/08.webp)


The **Flow** section shows a graph of your transaction components.


Inputs (previous UTXO), used for your transaction, and outputs giving recipients the right to use the bitcoins from each output by presenting the signature required for their expenditure.


![flow](assets/fr/09.webp)


More details on the addresses used can be found in the **Inputs & Outputs** section.


![address](assets/fr/10.webp)


Discover the different Bitcoin transaction schemes to enhance your confidentiality.


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Speed up your transactions


In the Bitcoin ecosystem, the aspect of transaction validation by miners is intrinsically linked to the transaction fees associated with that transaction. Miners prioritize transactions with a higher fee ratio (satoshis/vBytes), which could affect the validity of your transaction if you don't pay reasonable fees accepted by miners. Your transaction would get stuck in Mempool waiting for a block that accepts its fee ratio.


Fortunately, there are two methods available on the Bitcoin network to speed up the confirmation of your transaction.



- **RBF** - Replacement By Fee: A method that allows you to spend the same entries as your low-fee transaction, but this time by increasing the transaction fee to speed up validation. Your new transaction will be validated more quickly and included in a block, invalidating the low-fee transaction.


You can carry out a fee replacement action with wallets that accept this mechanism. For example, see our article on the Blue Wallet wallet.


https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90


- **CPFP** - Child pay for parent: An approach inspired by RBF, but on the receiver's side. When the transaction in which you are the recipient is blocked in a Mempool, you have the option of spending the outputs (UTXOs) of this transaction, despite the fact that it has not yet been confirmed, by allocating more fees to this new transaction so that the average fees - of the transaction for which you are the recipient and the initiated transaction - encourage miners to include both transactions in a block.


⚠️ The first transaction must be included in a block to allow the second transaction to be confirmed.


If all these terms seem a little too technical, I recommend that you [consult our glossary](https://planb.network/resources/glossary), which contains definitions of all the technical terms related to Bitcoin and its ecosystem.


In addition to these methods, Mempool.space, thanks to its connections with over 80% of the miners present on the Bitcoin network, also allows you to accelerate any of your **unconfirmed** transactions, even those not activating RBF, by paying a consideration to the miners in exchange for inserting your low-cost transaction into the next block ready to be mined.


On the transaction details page, click on the **Accelerate** button, then proceed to pay your counterparty to the miners.


![accelerate-section](assets/fr/11.webp)

## Minors


A miner refers to a person who manages a mine, i.e. a computer engaged in the mining process, which consists of participating in Proof-of-Work. The miner groups the pending transactions in his Mempool to form a candidate block. It then searches for a valid hash, less than or equal to the target, for the header of this block by modifying the various nonces. If he finds a valid hash, he broadcasts his block to the Bitcoin network and pockets the associated pecuniary reward, made up of the block subsidy (creation of new bitcoins ex-nihilo), and the transaction fee.


https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Miners are like "validators" who verify and group transactions into blocks. To add a new block to the Bitcoin network, they have to solve a complex mathematical puzzle (the Proof-of-Work). The first miner to solve the puzzle wins a Bitcoin reward (block grant + fees for transactions included in the block).


The difficulty of this proof of work is monitored, allowing you to visualize the evolution of the computing power required for miners. You will find in the sections below :



- An estimate of the total rewards reaped by miners during the last difficulty adjustment, as well as estimates of the next halving of the block grant, which occurs every 210,000 blocks (approx. 04 years).


![rewards](assets/fr/12.webp)


This difficulty is adjusted every 2016 blocks (about two weeks). It is inversely proportional to the average time taken by miners to Miner every 2016 blocks.

When the average time taken by miners is less than 10 minutes, the difficulty increases, proving that it was easier for miners to validate Miner blocks. Conversely, when the average time taken is greater than 10 minutes, the difficulty decreases.


![mining-pool](assets/fr/13.webp)



- Groups of miners: In view of the difficulty involved, a group of miners collaborate to help find the proof of work on Bitcoin, in what we call a **pool**. When a block is mined by the group, the reward obtained is distributed according to the percentage of success in each miner's partial solution search, i.e. the contribution in computing power in the search for Proof-of-Work, or according to the remuneration method agreed upon by the cooperation.




![mining](assets/fr/14.webp)


## Lightning Network infrastructure


Mempool doesn't just provide information on Bitcoin's network infrastructure (main chain). It also integrates visualization and exploration tools for Bitcoin's Lightning overlay.


In the **Lightning** section, you can view all existing connections between Lightning nodes.


![network-stats](assets/fr/15.webp)


This Interface provides information on :



- Lightning network statistics.


![distribution](assets/fr/16.webp)



⚠️ **IMPORTANT**: The capacity of a payment channel designates the maximum amount that a node can send to another node during a Lightning transaction.



- Lightning nodes are allocated according to Internet service provider (hosting service) and optionally according to payment channel capacity.


![distribution](assets/fr/17.webp)



- The history of the Lightning network's overall capacity.

You'll also find a ranking of these nodes according to the capacity of their payment channels.


![ranking](assets/fr/18.webp)


## More graphics


Mempool.space is the ideal platform for enjoying interaction with Bitcoin protocol networks. The graphs not only provide visual data to help you decide when to make transactions, but also precise parameters enabling you to visualize, in real time, the strength and health of the Bitcoin network and associated Lightning infrastructures.


In the **Graphics** section, you can view essential data about the Bitcoin network:


- Mempool size evolution: You can observe how the size of the Mempool fluctuates, which can indicate periods of high or low activity on the network.


![graphs](assets/fr/19.webp)




- The evolution of transactions and transaction fees on the chosen network: By tracking variations in transactions per second, you can anticipate periods of congestion or low activity, and optimize your transaction fees. This graph gives you a perspective on the network's capacity to handle the volume of transactions.


![graphs](assets/fr/20.webp)


Now that you've reached the end of your journey on Mempool.space, become your own explorer and track your transactions in real time. Please find below our article on the Bitcoin **Public Pool** explorer.


https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1