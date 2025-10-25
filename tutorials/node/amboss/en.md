---
name: Amboss
description: Explore and analyze Lightning Network
---

![cover](assets/cover.webp)


Lightning Network is a layer of the Bitcoin protocol, which was primarily developed to promote the adoption of Bitcoin payments on a day-to-day basis by increasing the processing speed of each transaction. Based on the principle of decentralization, Lightning Network consists of nodes (computers running a Lightning implementation) communicating peer-to-peer, relaying data (payments and payment verification) to each other.


https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Just as on the main chain, it has become essential to enable users to know the information and status of the network, in order to facilitate connections between nodes and minimize the liquidity problem that generally arises in the network. Indeed, on Lightning Network, we recommend micro-payments of relatively smaller amounts than those for transactions on the Bitcoin main chain.


It's important to note that not all Lightning nodes are available on the Amboss platform.


Like [Mempool Space](https://Mempool.space), which provides useful information on the Bitcoin protocol's main chain, since 2022 [Amboss](https://amboss.space) provides information on :



- Nodes on the Lightning Network
- Payment channels and their payment capacity
- Lightning Network evolution over time
- Statistics on charges to relay nodes for your payments.


https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In this tutorial, we'll take you on a tour of this platform, which is an essential resource for Lightning Network users, those who want to connect their node to expand the network, etc.



## Find pairs


One of the aims of the Amboss platform is to enable the various nodes in the network to connect and communicate information with each other. On the platform's home page, you can directly search for the name of a node you already know, or find nodes from the most popular Lightning wallets you use.


![home](assets/fr/01.webp)


![wallet](assets/fr/02.webp)


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

On the home page, you'll also find nodes classified according to :


- Capacity evolution: the quantity of Bitcoin associated with the node's public key and the total available in all its channels.
- Channel evolution: the number of new connections to other nodes in the network.
- Node popularity: how often the node is used.


![nodes](assets/fr/03.webp)


Choosing the right node to connect to therefore comes down to checking the following criteria:



- Ensure that the node has a sufficient quantity of bitcoins; the greater the capacity of the node, the greater the amount of bitcoins you can pay.



- Ensure that the node has a large number of connections and open channels with other nodes in the network.



- Make sure the node is active and still appreciated by its peers by checking the number of new channels; the more new channels this node has open, the more it is appreciated by the other nodes in the network.


Once you've found the right node, click on its name to be redirected to the node information page.


On this Interface, by checking the timestamp of the newly created channel, you'll get a clue to the activity of this node. You'll also find information on the capacity of this node's channels: this information is vital if you want to actively use this node to make your payments.



![node_info](assets/fr/04.webp)


In the left-hand section, you'll find more details about the location of this node. For example, you can view :


- The public key: the identifier just below the node name.
- The geographical position of this node.



![channels](assets/fr/05.webp)


This Interface tells you the connection address for this node: it takes the form `pubkey@ip:port`. In our example, we want to connect to the node whose :


- the public key `pubkey` is: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP address: `170.75.163.209`
- The port: `9735`


![geoinfo](assets/fr/06.webp)


In the **Channels** section, you'll see the list of open channels and the node's connections to other nodes in the network. On this Interface, several pieces of information are vital to confirm that this node corresponds to our needs or is reliable:



- Incoming ratio**: The amount the node will charge you for every million Satoshi it receives, depending on the channel chosen.
- The ratio (parts per million)** : which represents the number of Satoshi per million units that the node will charge you when you decide to make a payment via one of its channels. Let's say you decide to make a payment of `10_000 Sats` via a channel whose ppm ratio is `500 Sats`, you'll have to pay the node `10_000 * 500 / 1_000_000` satoshis, equivalent to `5 Sats`.
- The [HTLC](https://planb.network/resources/glossary/htlc) maximum** : The maximum amount this node allows you to transit via one of these channels.


By consulting the table in this Interface, you can also find all this information on the node it is matched to.


![channels_info](assets/fr/07.webp)


In the **Channel maps** section, you can see the distribution and capacity of the various channels on this node. You can change the distribution criteria displayed by selecting one of the options in the drop-down list on the right.


![cha_maps](assets/fr/08.webp)


The **Closed channels** section groups all the node's former channels according to the type of closure:


- Mutual closing**: represents the agreement of both parties, who use their private key to sign the transaction marking the closing of the channel and the distribution of balances within it
- A **forced closure**: represents the abrupt, unilateral closure of one part of the channel. This type of closure is not recommended, as Lightning Network is a punishment-based protocol: when you try to defraud the balance of a channel, you risk losing all your available balance in that channel.


![closed](assets/fr/09.webp)


Get information on transit fees for routing your payments through a channel on the node you use


![fees](assets/fr/10.webp)


## Network information


Amboss focuses not only on network member information, but also on the state of the network itself.


In the **Statistics** section, under the left-hand "Simulations" menu, you'll find a graph showing the probability of a successful payment as a function of the payment amount.


In fact, you'll notice that the curve is decreasing because, as the amount of your payment increases, you have less chance of seeing that payment go through. This reflects the real liquidity problem on Lightning Network. For example, your payment of `10_000` satoshis has a `79%` chance of being made. On the other hand, for a payment of `3_000_000` satoshis you have less than `13%` chance of success.


![network](assets/fr/11.webp)


The **Network statistics** menu allows you to graphically display statistics for :


- Payment channels
- Nodes
- Capacity
- Fees
- Channel evolution.


![network_stat](assets/fr/12.webp)


In the **Market statistics** menu, the **Order details** option allows you to view the demand for liquidity on the Lightning Network. This graph can also show which channels are the most in demand and/or which have considerable capacity.


![markets](assets/fr/13.webp)



## Tools


Amboss offers a number of tools to help you optimize your searches and actions.


### Lightning Network decoder


This tool is mainly responsible for giving you details of the structure of a Lightning invoice, Lightning address or Lightning URL.


On the home page, in the **Tools** section, submit your Lightning address, for example.


![decoder](assets/fr/14.webp)


From this decoder, you can obtain information such as :


- the node's public key associated with your Lightning address;
- The expiration time of an invoice from your address;
- The minimum and maximum you can send;
- The Nostr node associated with your address, if Nostr is enabled on this node.


![decode](assets/fr/15.webp)


### Magma IA


Discover the latest tool unveiled by Amboss to efficiently manage your connections to Lightning Network nodes. Magma AI uses dedicated artificial intelligence to focus on an important problem: making a good selection of nodes to connect to.


![magma](assets/fr/16.webp)


### Satoshi calculator


Find out the current price of Bitcoin in your local currency (EUR / USD). On the home page, use the satoshis calculator to find out the current market price.


![calculator](assets/fr/17.webp)



You've now taken a complete tour of the platform's features and analysis tools. Please find below our article on the Bitcoin **Mempool.space** explorer.


https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f