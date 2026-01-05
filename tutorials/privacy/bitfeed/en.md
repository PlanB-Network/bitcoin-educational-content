---
name: Bitfeed
description: Explore the main Bitcoin protocol chain.
---

![cover](assets/cover.webp)


Bitfeed is a platform for visualizing the onchain layer of the Bitcoin protocol. It was initiated by one of the contributors to the Mempool.space project and stands out mainly for its minimalist appearance and ease of use.


https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In this tutorial, we'll take a look at this tool, which lets you explore all the transactions and blocks on the network.


## Getting started with Bitfeed


Bitfeed is a platform that focuses on three main points:



- Blockchain consultation**,
- Transaction search**,
- Visualizing the mempool**.


### Consulting the blockchain


On the Bitfeed home page, you'll mainly find :



- The search bar: This section is the entry point for blockchain queries. Here you can search for a specific block by its number or hash. You can also search for specific transactions and Bitcoin addresses to verify certain transaction information on the network.


![searchBar](assets/fr/01.webp)


In the top left-hand corner, you can see the current price of bitcoin, estimated in US dollars (USD).


![price](assets/fr/02.webp)


On the right-hand sidebar is the platform menu. From this menu you can customize the platform interface to your liking, add or remove items and customize viewing filters. For example, view the size of each block by value or by weight in virtual bytes (vBytes).


![menu](assets/fr/03.webp)


In the center of the page is the last block mined, with a view of all the transactions included in that block. This section provides information on the timestamp, the total number of bitcoins involved in the block, the size of the block in bytes, the number of transactions and the average transaction cost ratio per virtual byte in the block.


![block](assets/fr/04.webp)


You can go back through the channel's history by searching for a specific block in the search bar, and view it according to your criteria.


For example, we want to view the transactions in block `879488`.


![bloc](assets/fr/05.webp)


The first transaction of this block represents the **coinbase** transaction which enables the miner of this block to earn the mining reward, which can only be spent after 100 blocks have been mined, made up of the included transaction fees and the block grant. This transaction is the one that enables new bitcoins to be issued on the system.


![coinbase](assets/fr/06.webp)


https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

By default, transactions in a block are represented according to two criteria:


- The size, which can vary between the value and the weight (vBytes) ;
- The color can vary between age and the ratio of transaction fees per virtual byte.


![options](assets/fr/07.webp)


We can therefore conclude that all transactions included in the same block have the same number of confirmations in the blockchain. The largest cubes represent the transactions containing the highest amount of bitcoins.


This interpretation is further confirmed by the **"Info "** menu option, which informs us of the translation of the color and size of the block's transactions.


![infos](assets/fr/08.webp)


You can also view a block's transactions by virtual bytes and fee ratio. This view may differ from the previous one, as the bitcoin value included in a transaction does not define its size.


![visualisation](assets/fr/09.webp)


### Viewing transactions


You can search for a transaction using its identifier via the search bar. You can also click on a cube to see the information related to that transaction.


In our case, let's take the transaction occupying the largest space in block `879488`.


![biggest](assets/fr/10.webp)


You'll see that this transaction has `42,989`, which represents the difference between the last block being mined and our chosen block. These confirmations help strengthen the security of the Bitcoin network, because to modify this transaction maliciously, attackers would need to possess the equivalent computing power to rewrite the entire main block chain.


The size of this transaction is `57,088 vBytes`, mainly due to the large number of UTXOs used in its construction (842 entries). Surprisingly, the fee ratio applied remains relatively low (only 4 sats/vByte) compared to the overall block average of 5.82 sats/vByte.


The transaction taking up the most space is therefore not necessarily the transaction with the highest transaction cost ratio.


![transaction](assets/fr/11.webp)


If you follow the scale in the **Info** menu, the transaction with the highest transaction cost ratio is the purple one. This is the transaction [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) with a transaction cost ratio of `147.49 sats/vBytes`.


![mostfeerate](assets/fr/12.webp)


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool visualization


The mempool is the virtual location where Bitcoin transactions waiting to be included in a block are grouped together. Bitfeed allows consultation of the [mempool](https://planb.academy/resources/glossary/mempool) of several Bitcoin miners, offering a wide range of transaction tracking.


![mempool](assets/fr/13.webp)


In this section, you can track all valid and as yet unconfirmed transactions on the Bitcoin network's main chain.


![unconfirmed](assets/fr/14.webp)


You now have a guide to using the Bitfeed platform to analyze blocks and transactions in order to visualize the information available on the Bitcoin network's main chain, while benefiting from a minimalist, easy-to-use interface. If you enjoyed this tutorial, we recommend that you take the next step: discover Lightning Network via the Amboss project.


https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017