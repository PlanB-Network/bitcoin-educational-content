---
name: BLOCKSTREAM Explorer
description: Explore the main layer of Bitcoin and Liquid Network
---

![cover](assets/cover.webp)


The BLOCKSTREAM Explorer is a project that facilitates the exploration of transactions and the global state of the Bitcoin protocol, as well as the [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid developed by the BLOCKSTREAM company.


Initiated in 2014 by BLOCKSTREAM, a company founded by Adam Back, the [BLOCKSTREAM.info](https://BLOCKSTREAM.info) explorer aims to provide a robust infrastructure for Bitcoin, guaranteeing interoperability and transaction tracking between layers (On-Chain and Liquid), while enhancing user security and privacy.


In this tutorial, we present what makes it different, its services, and how it offers seamless monitoring of the operations and status of Bitcoin's On-Chain and Liquid layers.


## Getting started with BLOCKSTREAM


### Navigate the main channel


When you go to the BLOCKSTREAM.info explorer, on the "**Dashboard**", the main Bitcoin protocol channel is selected by default. From this Interface, you have an overview of :



- Main chain size: Recently mined blocks.


![blocks](assets/fr/01.webp)


This section provides information on recent blocks mined, the timestamp, the number of transactions included in each block, the size in kilobytes (kB) and the measurement of each block in weight units (**WU** = *Weight Units*). This last measurement is of interest, as it enables us to evaluate the optimization of the block, given that each block of the main chain is limited to `4,000,000 WU`, or `4,000 kWU`.



- Recent transactions.


![transactions](assets/fr/02.webp)


The transaction section provides information on the transaction's unique identifier, the Bitcoin value involved, the size in virtual bytes (vB) - which represents the sum of all data (input and output) - and the associated charge rate. For example, a transaction with a size of `153 vB` at a rate of `2 sat/vB` will incur a charge of `306 satoshis`.


### Fluid exploration


From the "**Blocks**" menu, you can trace the history of the entire main chain back to the last block mined.


![blocs](assets/fr/03.webp)


By clicking on a specific block, you can obtain more details about the information and transactions included in it. For example, for block 919330: you have the Hash of the block. You can also navigate to the previous block, as each mined block (apart from Genesis) is linked to the previous one, retaining the Hash of its predecessor.


![metadata](assets/fr/04.webp)


By clicking on the **"Details "** button, you can obtain more information about this block, such as its status, which confirms that it has been added to the retained and propagated main chain. You also have the difficulty at which this block is mined: this difficulty represents the computing power required to solve the cryptographic problem of mining and is adjusted every 2016 blocks (about 2 weeks).


![details](assets/fr/05.webp)


Below this details section, we find all the transactions included in this block.


The very first transaction in the block is called the **transaction coinbase**. It is used to allocate the miner's mining reward (all fees associated with the transactions included in the block and the block grant). The bitcoins created by this transaction can only be spent once another 100 consecutive blocks have been mined. In other words, to be able to use them, the miner will have to wait for the production of block **919430**. This is known as the [*"maturity period "*](https://planb.network/fr/resources/glossary/maturity-period).


The coinbase is a special transaction: it's the only one with no real input, as it doesn't spend any bitcoins from a previous transaction.



![coinbase](assets/fr/06.webp)


All other transactions are divided into two sections: inputs and outputs.


For bitcoins to be used as inputs in a new transaction, the initiator of the transaction must prove his or her possession by providing a signature that corresponds to a specific script. Each piece of bitcoins (UTXO) contains a script generally requiring a specific signature that only the holder's private key can provide. These scripts are ***scriptSig*** (in ASM), written in Bitcoin Script, and can be of various types. In this example, we can see that the UTXOs used were of type P2SH to an output of type P2WPKH (*Pay-to-Witness-Public-Key-Hash*).


You can trace the history of a specific UTXO using heuristics. We invite you to discover the different Bitcoin heuristics and how to strengthen the confidentiality of your Bitcoin transactions:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)


Let's take the example of this transaction's outgoing expense. By clicking on the transaction identifier, we are redirected to the **Transactions** section on the transaction details page.


![transaction](assets/fr/08.webp)


From this page, you can find out which block the transaction was included in. Depending on the type of address used, the transaction can optimize its data (*virtual bytes*) and therefore pay less transaction fees. This transaction, for example, saved 53% in fees by using a native SegWit BECH32 address format starting with `bc1q`.


![trx_details](assets/fr/09.webp)


## Liquid coating


Liquid Network is a [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) and a level 2 open source solution for the Bitcoin protocol. In particular, it enables faster and more confidential bitcoin transactions.


On the BLOCKSTREAM.info explorer, click on the **"Liquid"** button to switch to the Liquid network.


![liquid](assets/fr/10.webp)


Clicking on one of the transactions we wish to follow, we see that the amounts of the Bitcoin pieces are replaced by the words "**Confidential**". On this network, transactions can be confidential, so we can't see the amounts of each UTXO, either in or out of the transaction.


![liquid_trx](assets/fr/11.webp)


However, we note that the principles and mechanisms present on the main layer of the Bitcoin protocol are the same: bitcoin locking scripts and UTXO traceability.


![liquid_details](assets/fr/12.webp)


The Liquid Network also provides non-depository digital assets that can be used by organizations. In the **"Assets "** menu, you'll find a list of registered assets, their total and the domain to which they relate.


![assets](assets/fr/13.webp)


For each asset, you can trace the history of issue and burn transactions (deleting the total in circulation).


![assets_trxs](assets/fr/14.webp)



## More options


The BLOCKSTREAM.info explorer also includes visualizations and tracking of transactions on Testnet, Bitcoin, On-Chain and Liquid Network.


![testnet](assets/fr/15.webp)


When you go to the Testnet network, you don't use real bitcoins, but you do have all the features described above.


![liquid_testnet](assets/fr/16.webp)


This network features a different chain length, to which you can connect and test the operation of the Bitcoin and Liquid mechanisms.



- The API section is dedicated to anyone wishing to integrate certain Explorer functions into their own application. Through this API you can interrogate the main chain of the different layers (On-Chain and Liquid), track transactions and find out the average fees for transactions in a block, for example.


![api](assets/fr/17.webp)


You're now ready to exploit the full potential of BLOCKSTREAM Explorer to query blockchains on the On-Chain and Liquid layers. We hope you've found this tutorial informative, and recommend our tutorial on another Bitcoin Explorer:


https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f