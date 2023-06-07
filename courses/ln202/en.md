---
name: Setting up a Bitcoin & Lightning Node
goal: Deploying a Bitcoin and Lightning node via Umbrel
objectives:
  - Installing a Bitcoin node
  - Managing a Bitcoin node
  - Using a Lightning Network node
---

# A journey to the technical side of Bitcoin

![Course poster](Formation\courses\btc101\assets\affiche\BTC101_vignette-presentation-front.png)

This training is more technical and will be even more beneficial if you have a basic understanding of Bitcoin, including how Bitcoin wallets work and the principles of transactions, mining, and blockchain. You don't need to know how to code, your curiosity and willingness to learn are the only skills required. Remember, every expert was once a beginner. So take a deep breath and dive into the exciting world of Bitcoin. You are about to embark on an exciting and rewarding journey. Good luck!

+++

# Becoming a Sovereign Bitcoiner

![Course launch](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

To fully embrace the philosophy of Bitcoin and embody the adage "Don't Trust, Verify," we aim to become sovereign users of Bitcoin nodes. In this process, we will rely on the Umbrel interface to set up our own node. The tools needed for this task include a Raspberry Pi, an external hard drive, an SD card, a fan, and a case, for an estimated total investment of around €200.

By adopting Umbrel as our operational base, we will be able to integrate the Lightning Network, explore the mempool, and discover multisig solutions. At the end of this journey, not only will we have asserted ourselves as sovereign Bitcoiners, but we will also have the satisfaction of having actively contributed to the Bitcoin network.

# What is a Bitcoin node?

![What is a node?](https://youtu.be/19YgL9vkHh4)

A Bitcoin node is simply a device running Bitcoin software, the cornerstone of the network's existence and communication. These nodes form the foundation of Bitcoin's decentralization, taking on different forms and responsibilities. Among them are receiving and transmitting transactions, displaying outgoing transactions, and establishing connections with other nodes.
Three main roles are assigned to these nodes: establishing Bitcoin consensus, validating transactions, and interacting with the network. Thanks to this decentralization, Bitcoin benefits from increased resilience, with privacy strengthened by not relying on a third-party server. According to [Bitnodes](https://bitnodes.io/nodes/all/), approximately 43,000 nodes around the world form the Bitcoin network.

Let's now explore the specific functions of these nodes within the Bitcoin network. A node is not just software; it is also a gateway to the Bitcoin network consensus and access to the blockchain history. For example, merchants operate their own node to validate incoming and outgoing transactions.

The advantage of managing your own node lies in improving privacy and achieving financial sovereignty. Indeed, running your own node strengthens your contribution to the network and makes you your own bank. This allows you to verify transactions in real-time, giving you better decision-making power over your finances.

In conclusion, running your own node in the Bitcoin network offers many advantages. Not only does it contribute to the decentralization of the network, thus strengthening the resilience of the system, but it also ensures greater privacy and financial autonomy. By taking this step, you can authenticate transactions in real-time, make informed financial decisions, and avoid dependence on a third-party server, thus ensuring your privacy. Beyond all this, running your own node is a concrete way to contribute to the Bitcoin ecosystem and truly embody the role of your own bank.

# Bitcoin Node Tutorial via Umbrel

![Umbrel Tutorial](https://youtu.be/mr4iTzdTczI)

In this chapter, we will deploy our own Bitcoin node, open lightning channels, and try a multi-signature wallet. This has a significant hardware cost for some people. Know that the entire training can be followed WITHOUT the hardware. You will not be lost if you do not have your own node.
If you want to get started, here are the products (affiliate link):

- 16GB SD Card - https://amzn.to/3Qi2Opm
- Raspberry Pi 4 - https://amzn.to/3qoSUYl
- 1TB SSD - https://amzn.to/3jSvjLC​
- External Hard Drive Case - https://amzn.to/3x5R02S
- RASPBERRY Power Supply - https://amzn.to/3D36zvM
- Raspberry Pi FLIRC Case - https://amzn.to/3TNllgi
  If you have used affiliate links, thank you for your support! You are helping this project survive and offer even more training and educational content.

What do you need to run your Bitcoin node?

- The blockchain is about 500GB, so you need to plan for space.
- The internet connection must be constant with about 5GB of bandwidth per month.
- You need RAM to run BTC Core.
- You need more RAM if you run Umbrel and an LN node (minimum 4GB).

You can run your Bitcoin node directly on your computer or use a system like the one in the video with a Raspberry Pi.

Other ready-made solutions already exist!

Follow these steps to create a full node with a Raspberry Pi and Umbrel. Before you start, please note that you will need about 200 euros to purchase the necessary hardware, although the software is free.

1. **Preparing the tools**: Go to Umbrel, a well-known open-source solution for its excellent user interface and good service, to download the necessary software. Additionally, you will need Benella Itcher to flash the SD card.
2. **Assembling the Raspberry Pi**: Assemble your Raspberry Pi. Make sure to install the fan and small cooling components included in the kit.
3. **Flashing the SD card**: Use the device provided in the kit to flash the SD card. If you encounter difficulties, try reformatting the card or unplugging/replugging the device.
4. **Connecting the hardware**: Once the SD card is flashed, connect the SSD to the Raspberry Pi via a 3.0 port. Then, connect the Raspberry Pi to your router and a power source.
5. **Configuring Umbrel**: After about 5 minutes, you will be able to access the Umbrel interface on your computer. It is recommended to use a password manager to create and save a secure password for accessing your Umbrel node.
6. **Securing your seed (mnemonic phrase)**: Your seed is the private key that gives you access to your bitcoins. Therefore, be sure to keep it safe. Avoid taking photos or screenshots of your seed. It is also recommended to save the TOR link in your password manager for easy future access.
7. **Exploring the Umbrel dashboard**: Umbrel has a clear dashboard and an innovative App Store for downloading other applications. The Umbrel tutorial is accessible to everyone, you just need to buy the hardware and follow the steps.

# Overview of Umbrel

![umbrel overview](https://youtu.be/cwEa61BgemM)

In this comprehensive review, we will examine the interface that facilitates the management of your Bitcoin and Lightning Network wallet.

To begin, we will log in to the account using a secure password and a dedicated password manager. Then, we will undertake a thorough exploration of the interface, familiarizing ourselves with the distinctive features of the Bitcoin wallet and the Lightning Network.

The node will communicate with other nodes on the Bitcoin peer-to-peer network randomly and under a pseudonym. This essential feature allows you to download the entire blockchain (also known as the timechain) without relying on a central entity. However, it should be noted that the initial download of the timechain can take several days, as it represents a volume of over 500 GB to receive.

We will then carry out transactions within the Bitcoin wallet, including a test transfer to a multisig wallet. Afterwards, we will open Lightning Network channels and use active connections in the Lightning Network wallet. Opening channels requires some visual exploration.

After completing these operations, Bitcoin Core becomes operational. You can then connect some of your wallets to your node to check the status of your accounts.

It is possible to link your Bitcoin wallets such as [Green Wallet](https://blockstream.com/green/), [Samouraï](https://samouraiwallet.com/), [Spectre](https://specter.solutions/), [Sparrow](https://sparrowwallet.com/) to your Bitcoin node via a dedicated interface. By connecting your wallet to your own node, you can confirm the receipt of funds without relying on an external server, which is particularly recommended for merchants.

By following these steps, you can contribute to the decentralization of the Bitcoin network, increase your financial privacy and autonomy, and actively participate in the evolution of the traditional banking system. So, don't hesitate to get started and become a true sovereign Bitcoiner.
Umbrel also offers an App Store that includes Explorers, multiple other services related to Bitcoin, Lightning, or hosting your own data. New applications are regularly added to their [appstore](https://apps.umbrel.com/).

For more information and support, do not hesitate to visit their website, Telegram chat, Discord, Github, and Reddit. In summary, with Umbrel, you have the opportunity to regain control of your financial sovereignty through Bitcoin and become your own bank while contributing to the network. We strongly encourage you to delve deeper and learn this technology to integrate it into your store, e-commerce, personal life, or simply out of curiosity.

# Mempool Analysis

![mempool](https://youtu.be/0xS859IoMh8)

The Mempool essentially functions as a transit space for Bitcoin transactions waiting to be validated in the blockchain. To effectively examine the Mempool, Umbrel serves as the tool of choice. The [Mempool.space](https://mempool.space/) application, accessible through the Umbrel interface, provides a clear representation of pending transactions, associated costs, and various other relevant features.

The Bitcoin blockchain is essentially a database that incorporates blocks of transactions at regular intervals of about 10 minutes. After each series of 2016 blocks, the mining difficulty adjusts to maintain this average interval. If miners decide to withdraw their energy from the Bitcoin network, the average time required to find new blocks increases, leading to a decrease in mining difficulty and allowing other miners to become competitive again.

In addition to mining difficulty, the current cost of a Bitcoin transaction is visible on the dashboard, as well as the blockchain with its chain of blocks. The fees for a Bitcoin transaction are currently 40 sats/vbytes. Transaction fees on Bitcoin are based on the complexity of the transaction, which is considered proportional to the virtual weight (vbytes) of the transaction. Vbytes, or virtual bytes, are a unit of measurement used in Bitcoin to evaluate the size of a transaction, taking into account SegWit technology. Thus, the use of vbytes allows for a more precise measure of space efficiency in a block.

Each user is free to determine the fees associated with their transaction, which tend to reflect the urgency of transaction validation: the more the user wants their transaction to be validated quickly, the higher the fees. Thus, as the volume of a block is limited to 4 MB (although the average block size is about 1.5 MB), when demand increases, fees to increase the probability that our transaction will be included in the next block can increase significantly.

# Bitcoin Layers

Bitcoin has several layers: the Mainnet (the main chain), the Testnet and the Signet (dedicated chains for experimentation and validation of new features), the Lightning Network (a payment network), and Liquid (a sidechain where blocks are validated every minute). Each of these layers has its own usefulness and specific use cases.

The blocks that contain transactions are built by mining pools, and their fill level varies depending on demand and time elapsed since the last block was mined. Upper layers, such as the Lightning Network, allow for faster and cheaper transactions than on the main blockchain, but they still rely on Bitcoin for their security model.

In conclusion, block explorers allow for real-time tracking of transactions or retracing them in the past. These transactions can have varying levels of complexity. Mempool offers an effective solution for visualizing the blockchain, tracking transactions, and analyzing fees and network congestion.

# Block Explorer & Analyze Stats

![block explorer and analyze stats](https://youtu.be/Qe9VaUhUS0E)

We will embark on an exploration journey through the Bitcoin blockchain, using powerful tools such as Block Explorers and the BTC Explorer application on the Umbrel node. Block Explorers give us the ability to analyze the Bitcoin blockchain in detail. With BTC Explorer, an application on Umbrel, you can check all the information related to the Bitcoin blockchain that is on your hard drive, allowing you to no longer rely on third-party trust.

We refer to a specific transaction, the same one examined in the previous course, to demonstrate the features and importance of these tools. We will also illustrate the latest mined blocks and detail information about their content. Then, we will make a thorough comparison between two distinct blocks, analyzing their content and the time it took to mine them.

The Block Explorer allows us to view the details of a mined block, such as the hash, summary, outputs, fees, time, and transactions. As for Bitcoin Explorer, it offers more sophisticated tools for blockchain analysis. The first tool, for example, allows for a detailed examination of your node (synchronization, indexing, blockchain size, accepted BIPs).

Bitcoin Improvement Proposals (BIPs) are proposals for improving the Bitcoin protocol. We can observe the activation of Segwit and the number of network connections. In addition, Blockstats provide detailed statistics on fees, transactions, inputs, and outputs.
The analysis of Segwit data provides an overview of Bitcoin's evolution over the years. Transaction statistics, volumes, blocks, UTXOs, and timestamps are available for free. Interpreting this data is crucial for financial research and verifying Bitcoin adoption.

It is important to take control of one's financial sovereignty and seek out data oneself. Block analysis allows for the study of data from a specific block, such as the first block mined by Satoshi in 2009, where he intentionally destroyed his first 50 bitcoins for an honest launch.

Bitcoin transaction data is transparent and accessible to everyone, including analysts and industry professionals. This information is vital as it provides valuable insights into Bitcoin network activity, market dynamics, and current trends, which is essential for informed decision-making and the implementation of strong financial strategies. Additionally, this data is used for transaction tracking, ensuring the traceability and transparency of the Bitcoin network.

A "heavy" Bitcoin transaction, such as one containing 673 inputs and 1 output, illustrates the trade-off between the number of UTXOs (Unspent Transaction Outputs) and the amount of Bitcoin in an address. UTXOs represent the unspent funds from a previous transaction, which become the inputs for future transactions. Increasing the number of UTXOs in a transaction makes it more complex and costly. Therefore, it is essential to consolidate UTXOs to minimize transaction fees and optimize the use of space in a Bitcoin blockchain block.

Mining, the central pivot of the Bitcoin protocol, plays a fundamental role in securing transactions. The process is regulated by a difficulty adjustment every 2016 blocks to maintain an average interval of 10 minutes between blocks. At the same time, the hash rate, reflecting the network's computing power, is constantly increasing.

Within the network, miners gather in mining pools. These entities do not have the power to control the entire network as miners have the privilege of being able to switch between pools at their convenience. Innovative technologies like Stratum V2 give more power to miners within mining pools. Additionally, technical solutions such as MimbleWimble and Dandelion present themselves as promising improvements for transactions.
Furthermore, the historical wealth of the blockchain lies in the fact that it archives all transactions, from the genesis block to the most recent transactions. It includes the first Bitcoin transaction made by Satoshi to Hal Finney in block 170 and the famous transaction of 10,000 bitcoins for two pizzas in block 57043, an event that gave rise to the annual celebration of "Pizza Day" on May 22.

To strengthen your financial sovereignty and avoid dependence on a third party for receiving and sending your bitcoins, it is crucial to connect your wallets to your own Bitcoin node. Transactions are first validated by the network nodes during their propagation, and then a second time when they are incorporated into a block.

In conclusion, sharing and introducing Bitcoin to your circle is a commendable step. By running your own node and contributing to the network, you can become your own bank. The ultimate goal is to become fully autonomous.

# Connecting your wallet to your node

![connecting your wallet to your node](https://youtu.be/HOV3bVcram4)

In today's digital world, protecting your cryptocurrencies and your privacy is essential. In this context, I will guide you through the process of connecting your mobile and desktop wallets to our Bitcoin node. This procedure significantly increases your security while increasing your control over your assets.

There are many wallets available: Bitbox App, Blue Wallet, Blockstream Green, Samouraï, Phoenix, Sparrow, Wasabi, Electrum, and many others. Each has its own specificities, strengths, and weaknesses. For today, our focus will be on Sparrow, an interesting alternative to Ledger Live, known for its ease of management and wallet creation.

In terms of security and privacy, an additional step can be taken: the use of a private server rather than a public server. This approach, although more complex, ensures a higher level of control and protection. You will find the necessary information for connecting to a private server on Umbrel.

Remember, keeping your wallets up to date is an essential gesture. Updates fix bugs, combat vulnerabilities, improve the product, and sometimes add useful new features. Umbrel, in particular, ensures the automatic update of all its applications. It is therefore wise to keep your Umbrel up to date.
To conclude, connecting your wallets directly to our Bitcoin node is a step towards financial independence. This gives you a higher level of privacy and security while allowing you to maintain full control over your digital assets. Financial sovereignty means having full ownership and control of your money, without intermediaries. By diversifying your wallets and keeping them up to date, you are taking one step closer to this autonomy.

# Multi-Sig Wallets via Specter

![multi-sig wallets](https://youtu.be/mV1KS-Uwjew)

We propose taking a new step towards financial autonomy. Our goal is to set up a multisig wallet with the Specter application, integrated into Umbrel. We will connect the Desktop application to our node, making this tutorial accessible to everyone.

The concept of multisig is simple: to ensure exceptional security for large amounts. To do this, we will use three private keys to secure our new Bitcoin wallet. Several levels of security exist: mobile wallet, physical wallet, passphrase, 2-of-3 multisig, 3-of-5 multisig, or even a combination of all these elements with open dimes. You don't need to be a technology expert to follow this tutorial, but some familiarity with the system of private and public keys is required.

Get ready, because the tutorial is quick. With the devices already initialized, it should take us about 15 minutes. To follow along, you will need three initialized devices, a node to connect the Specter application, as well as a USB key and a printer. We will use the Specter application for our multisig solution. You can download it via Umbrel or directly from the Specter Solutions website. Don't forget to check the signature before downloading. You can also do your multisig with Sparrow or Electrum. Feel free to do your research and take the time to familiarize yourself with these tools before using them to manage large amounts.

Now let's get practical. Here, we have done a 2-of-3 with a ledger and 2 trezors (white and black) and Specter Desktop, which is the wallet interface that allows us to interact with our wallets and is connected to Bitcoin Core via Umbrel.
We will first create a simple wallet to interact with Ledger without Ledger Live. This will allow us to generate new addresses and send Bitcoins. We will then add other devices (treasures) to create the multisig. Let's start by choosing the second device (the white Treasure) that we will connect via USB. After using the PIN to activate it, we will extract the public keys and create a second wallet. We will then add a third device (the Black Trezor) and use it to create a multisig wallet. We will create a multisig wallet by choosing the three devices, using Signet to test and not lose funds in case of mishandling (however, the process is the same for the mainnet).

We will then create the wallet by combining the public keys. The backup of a multisig wallet contains several elements. Indeed, to recreate the wallet, we will need the three public keys and two private keys to spend the money. It is therefore crucial to store the public keys with the backup of each private key in a safe place.

It is recommended to write down the mnemonic phrases (list of 24 words) of the 3 private keys on paper or metal in several copies (at least 2). In addition, it is advisable to write precise and detailed information that allows you to recover your money in case of problems or for an inheritance plan. These instructions must also be stored in a safe place.

Thus, you will have taken another step towards Bitcoin sovereignty. By mastering your security and using tools such as multisig, you strengthen your financial autonomy and optimally protect your assets. Remember, continuous caution and learning are the keys to success in the world of Bitcoin.
If you want to practice with Testnet bitcoins, you can get them through this [faucet](https://bitcoinfaucet.uo1.net/).

# Opening Lightning Channels

![opening channels](https://youtu.be/bAZJn0AH1yU)

Let's now move on to the Lightning part of the Umbrel node. We will use ThunderHub, an application among several that serve as a Lightning node manager, such as Lightning Terminal and RideTheLightning (RTL). These applications give us a precise overview of the state of our channels, serving as an interface between us and our Lightning Network (LN) channels.
At this stage, our main goal is to open a new channel. When you download ThunderHub, a default password is provided, which you can find directly in the app store. It is essential to change it and keep this new password in a dedicated password manager.

When considering opening a channel with another Lightning node on the network, some questions arise. For example, how much liquidity do you want to allocate in a channel? With which parties do you want to open a channel? The answers to these questions are crucial to optimize your transactions and avoid potential problems.

Let's talk about channel size. It would not be wise to start by opening channels with a low amount, such as 20k, 50k, or 100k sats. This would be insufficient, and the opening and closing fees of the channel would not be covered. A low amount channel would be more harmful than useful for you and the rest of the network. For example, if you have a 20k channel open with my node, it would barely cover the opening and closing fees (+ reserve). You would only have crumbs left to spend.

That's why it is recommended to open channels of at least 500k-1M sats. This would offer better routing, beneficial for you and everyone else who routes transactions through your node. It is important to note that the idea of "the bigger, the better" does not apply here. It would be better to have 5-6 outgoing channels, each containing between 500k and 1M sats, and, depending on your needs, 4-5 incoming channels of similar capacity.

Now that you are familiar with channel size, let's move on to their management. Regarding outgoing liquidity (on your side), your LN node allows you to make LN payments, buy things, send money to friends, pay for services, etc. Try to open LN channels with merchants you plan to exchange with. Regarding incoming liquidity (on your peers' side), find peers willing to open channels to your node. This incoming liquidity is necessary to receive payments on the LN.
The question of who to open channels with is crucial. Firstly, with merchants with whom you plan to transact, you can benefit from direct routing and avoid fees. Secondly, consider friends and experienced LN users you know who can create a ring of fire with a certain amount of sats for these channels. This is perfect for balancing liquidity while reducing fees between ring nodes. Thirdly, your ring of nodes can have "external" connections or channels with other good nodes, making routing to any recipient easier and faster.

To establish these connections, you will need to retrieve the public addresses of the other parties. You can do this by asking them directly or via sites like [1ML](https://1ml.com/) or [Amboss](https://amboss.space/). Opening a channel involves chain transaction fees, so take advantage of times when the Mempool is empty to open channels. Once a channel is open, liquidity is locked on one side of the channel. To move it to the other side, transactions for payments must be made, or what is called a "submarine swap" (we will see this in the next part). It should be noted that in the Lightning Network, there are routing fees. If a channel empties too quickly due to routing, you can increase these fees.

Before concluding, it is important to note that there is another crucial decision to make when opening Lightning channels: choosing between a public channel or a private channel. Each has its advantages and disadvantages, depending on your needs and preferences.

A public channel is announced to the entire Lightning network and can be used for payment routing. This is an excellent option if you want to actively participate in the network and help facilitate transactions for other users. It can also generate (very low) income through routing fees that you can collect. However, keep in mind that since a public channel is visible to everyone, it is not suitable if you are looking to maintain a high level of privacy.

On the other hand, a private channel is not announced to the network and will not be used for payment routing. This is a good option if you prioritize privacy and plan to use the channel mainly for your own transactions. It should be noted that even though a private channel does not offer the same routing fee income opportunities as a public channel, it can offer increased peace of mind in terms of security and privacy.
In the end, the choice between a public channel and a private channel depends on your own situation and priorities. Carefully evaluate your needs and goals before making a decision.

In conclusion, opening channels in the Lightning Network is an essential technical step to optimize your transactions. The choice of channel size, the choice between a public or private channel, and the careful selection of parties with whom to open channels are determining factors for efficient and economical routing. In our next section, we will focus on the effective management of these channels. So, move on to the next section for more details on this important facet of the Lightning Network.

# LN Channel Management

![LN Channel Management](https://youtu.be/CgBnGQLar4o)

Now that we have covered the opening of Lightning Network channels, let's turn our attention to their management. Effective channel management can make a big difference in optimizing your Lightning Network experience.

The first essential element of channel management is balancing. Lightning Network channels have what is called "liquidity," which is distributed between the two parties of the channel. Balancing this liquidity is crucial to ensure that transactions can be efficiently routed by your node. Too much liquidity on one side or the other can make the channel less useful for routing. Fortunately, there are several strategies for balancing channels, including using services like Lightning Loop from Lightning Labs, which allows you to move liquidity in and out of the Bitcoin network.

The second element to consider is monitoring your channels. It is important to regularly check the status of your channels and monitor the performance of your node. Tools like ThunderHub and RTL offer great features to help monitor your node and manage your channels. They provide you with information about the status of your channels, including their liquidity, fees, and capacity. Additionally, they offer features to close channels, open new channels, and rebalance liquidity between channels.

Thirdly, channel closure must be taken into account. Sometimes, you may end up with a channel that is no longer useful or performing well. In this case, you will want to close the channel. However, it is important to note that closing a channel results in a transaction on the Bitcoin blockchain, which can incur fees. Therefore, it is wise to close channels during periods of low congestion on the blockchain to minimize fees.
In conclusion, managing Lightning Network channels is an important element in maintaining a performant and economical Lightning node. With a good balancing strategy, regular monitoring, and intelligent management of channel opening and closing, you can optimize your experience with the Lightning Network. In the next segment, we will address another crucial aspect of the Lightning Network: security.

# Renaming your LN node

![rename your LN node](https://youtu.be/HnK1_TDYXsY)

Customizing the alias of your Lightning Network node is an excellent way to distinguish yourself on the network. It is not only practical, but it is also a way to personalize your experience. To change the alias of your node, we will use the command-line interface. For those less familiar with this interface, don't worry, this guide will help you step by step.

To begin, you need to open your system's terminal. The terminal is a command interface that allows you to interact directly with your operating system. Once the terminal is open, type the command `ssh -t umbrel@umbrel.local` and press Enter. This command will establish a secure connection with your Umbrel.

Next, you will be asked to enter your Umbrel password. Note that for security reasons, the password does not appear on the screen when typing. After entering your password, you will access your Umbrel interface.

Once connected, enter the command `sudo nano umbrel/lnd/lnd.conf` in the terminal and press Enter. This will take you to a text editor called Nano where you can modify your Lightning node's configuration file.

Again, you will need to type your password. Then, navigate to the section titled "Application Options". In this section, add the line `alias=SOMENAME`, replacing "SOMENAME" with the alias you want for your node. Note that using the mouse is useless in this interface, so use the arrows to navigate instead.

To save the changes, press `Ctrl-X`, then `Y`, and finally `Enter`. This will close the editor and save your changes. To make these changes take effect, you need to restart your Umbrel. To do this, access the settings menu of the Umbrel interface and choose the restart option.

And there you have it, you have successfully changed the alias of your Lightning Network node! You can now claim your node on sites like 1ML or Amboss. In the next section, we will discuss other methods to customize and optimize your Lightning Network node.

### Support us

This course, as well as all the content available on this university, has been offered to you for free by our community. To support us, you can share it with others, become a member of the university, and even contribute to its development via GitHub. On behalf of the entire team, thank you!

### Course Rating

A rating system for the course will soon be integrated into this new E-learning platform! In the meantime, thank you very much for taking the course and if you enjoyed it, please consider sharing it with others.

# Fun Use of LN

![LN usage](https://youtu.be/6yekAvH13E0)

Now that you have set up your node, it's time to use it. For this first use, we will focus on [Satoshi's Place](https://satoshis.place/), a fascinating service that allows you to spend satoshis, the smallest unit of bitcoin, to create pixel art on a public online space. Each pixel changes color for one satoshi. You are free to unleash your creativity, for my part, I created a pokeball for 166 satoshis! Payments are made through "invoices" on the Lightning network. These invoices can be represented as QR codes, making payment easy and instant.

When a transaction goes through multiple nodes, routing fees are usually involved. It is therefore crucial to be well connected to the center of the network to reduce these costs. An alternative would be to open a channel directly with the merchant. This has several advantages, including lower transaction fees and faster transaction speeds.

As an example, we will create a channel with Satoshi's Place for future payments. After creating the channel, a wait of about 30 minutes is necessary for the channel to become operational. Once the channel is created, you can make direct payments. For example, you can send one satoshi for free via the Lightning network without a trusted intermediary.

The Lightning network has several advantages, including its low cost and the ability to make regular payments. To get started, it is recommended to use wallets such as Wallet of Satoshi or Alby. These wallets allow you to pay invoices using the Lightning network. To learn more, you can read this [article](https://asi0.substack.com/p/comparatif-des-portefeuilles-ln) by Darthcoin.

In conclusion, the Lightning network proves Bitcoin's ability to evolve. Not only does it allow for low-cost transactions, but it also offers a solution to the scaling problems that Bitcoin has faced in the past.

# Accepting Bitcoin with BTCpay server

![accepting bitcoin in your business](https://youtu.be/zpCMlLfiRgg)
In this final chapter, we will explore the different ways to accept Bitcoin for your business. We will review three main options, namely BTCPay Server via your Umbrel node, BTCPay via an external Luna node, and finally via OpenNode. It is essential to note that each option has its nuances, and it is crucial to choose the one that best suits your specific needs.

Let's imagine that you own a restaurant and have an Umbrel node in your establishment. In this case, you can use BTCpay directly under Tor. This is an ideal solution for physical operations where customers pay in person.

However, for an e-commerce, using BTCPay under Tor from its Umbrel node is not feasible. In this case, using an external node in clearnet, such as Luna Node, is preferable. This offers more flexibility and allows for smoother integration with your online commerce platform.

For those looking for an all-in-one and easy-to-manage solution, OpenNode is an excellent option. However, its configuration and use can be quite complex. That is why we plan to cover this solution in more detail in a dedicated training.

Below are the links to the different services mentioned:

- OpenNode
- BTCPay Server
- Luna Node and the guide on BTCPay Server with Luna Node

In addition, I had the opportunity to interview Nicolas Dorier, the creator of BTCPay Server. If you are interested, feel free to watch our conversation by clicking here. You will discover many interesting information and valuable tips to optimize the use of BTCPay Server in your business.

In summary, accepting Bitcoin can offer a multitude of advantages for your business. Whether you are a local restaurant or a global e-commerce, there is a solution that suits your needs. Take the time to examine the different options, and do not hesitate to embark on this new Bitcoin adventure.

# Training Summary

![conclusion](https://youtu.be/QrKbagtUE1s)
Here we are at the conclusion of our in-depth exploration of the Bitcoin Lightning Network. We have traveled a complex path, populated with technological innovations and new perspectives on how we interact with our digital money. From the initial exploration of Umbrel to the opening and management of Lightning channels, each step has been a move towards a better understanding and greater mastery of this revolutionary technology.

We began with an overview of Umbrel, familiarizing ourselves with the interface and key features. We then delved into the Mempool, learning to analyze pending transactions for a deeper insight into the Bitcoin network. Next, we explored block explorers and network statistics, essential tools for monitoring the network's status.

We then tackled the most personal aspect of the Bitcoin network: the wallet. We learned to connect our wallet to our node, and then discovered the importance and security of multisig wallets through Specter.

Next, we dove into the world of the Lightning Network. We explored the opening and management of Lightning channels, two crucial aspects for optimal node operation. We also learned how to rename our node to facilitate its identification on the network.

We also had a playful glimpse into the use of the Lightning Network through Satoshi's Place, a concrete example of how LN can be used for low-cost microtransactions.

Finally, we addressed the commercial aspect of Bitcoin. We explored how to accept Bitcoin in one's business via BTCpay server, taking into account different configurations depending on the needs.

That being said, mastering the Lightning Network is not a task that can be done in a day. It is a constantly evolving, complex, and nuanced technology. It will take time, practice, and a willingness to learn to truly master this tool. Just like Bitcoin itself, the Lightning Network is an adventure, an exploration of what is possible in the field of digital finance. But with patience, perseverance, and a willingness to learn, you will soon be able to navigate the Lightning Network with ease and confidence.

In summary, the journey we have undertaken together through the Lightning Network is only the beginning. Mastering this technology offers many opportunities and advantages. So keep exploring, learning, and experimenting with the Lightning Network. The future of finance is within reach.
To conclude, it is important to emphasize that this training, like the others we offer, is completely free. We firmly believe in the importance of sharing knowledge and making access to information as free and open as possible. It is in this spirit that we have decided to share with you everything we have learned about the Lightning network.

However, if you have found value in this training and would like to support us, we invite you to visit our e-commerce site at the following address: https://thebitcoinrabbithole.myshopify.com/. By making purchases on our site, you not only contribute to supporting our work, but you also help us to continue providing free and high-quality training.

Thank you for taking the time to follow this training. Your support and interest in our work mean a lot to us.

# Acknowledgments and keep digging the rabbit hole

Congratulations on completing this LN 202 training! I sincerely hope you enjoyed it and opened doors. Your discovery of bitcoin is just beginning and I invite you to discover all the other training courses available at the university.

- ECON 201 will cover Austrian economics
- SECU 101 will allow you to update your security
- MINING 201 to learn more about mining
- (and many more)

Kisses and see you soon!
