---
term: TRANSACTION FEES

---
Transaction fees represent a sum that aims to compensate miners for their participation in the proof of work mechanism. These fees encourage miners to include transactions in the blocks they create. They result from the difference between the total amount of inputs and the total amount of outputs in a transaction:

```text
fees = inputs - outputs
```

They are expressed in `sats/vBytes`, meaning that the fees do not depend on the amount of bitcoins sent, but on the weight of the transaction. They are freely chosen by the sender of a transaction and determine its speed of inclusion in a block through an auction mechanism. For example, let's say I make a transaction with an input of `100,000 sats`, an output of `40,000 sats`, and another output of `58,500 sats`. The total of the outputs is `98,500 sats`. The fees allocated to this transaction are `1,500 sats`. The miner who includes my transaction can create `1,500 sats` in their coinbase transaction in exchange for the `1,500 sats` that I did not recover in my outputs.

Transactions with higher fees, relative to their size, are treated as a priority by miners, which can speed up the confirmation process. Conversely, transactions with lower fees may be delayed during periods of high congestion. It is worth noting that Bitcoin transaction fees are distinct from the block subsidy, which is an additional incentive for miners. The block reward consists of new bitcoins created with each mined block (block subsidy), as well as the collected transaction fees. While the block subsidy decreases over time due to the total supply limit of bitcoins, transaction fees will continue to play a crucial role in encouraging miners to participate.

At the protocol level, nothing prevents users from including transactions without any fees in a block. In reality, this type of fee-less transaction is exceptional. By default, Bitcoin nodes do not relay transactions with fees lower than `1 sat/vBytes`. If some fee-less transactions have passed, it's because they were directly integrated by the winning miner, without traversing the network of nodes. For example, the following transaction includes no fees:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

In this specific example, it was a transaction initiated by the director of the F2Pool mining pool. As a regular user, the current lower limit is therefore `1 sat/vBytes`.

It is also necessary to consider the limits of purging. During periods of high congestion, the mempools of nodes purge their pending transactions below a certain threshold, in order to respect their allocated RAM limit. This limit is freely chosen by the user, but many leave the default value of Bitcoin Core at 300 MB. It can be modified in the `bitcoin.conf` file with the `maxmempool` parameter.

> ► *In English, we refer to it as "transaction fees".*