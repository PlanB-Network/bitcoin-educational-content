---
term: FEE SNIPING

---
An attack scenario in which miners seek to rewrite a recently confirmed block in order to claim the transaction fees it contains, while adding high-fee transactions that have arrived in the meantime in the mempool. The ultimate goal of this attack for the miner is to increase their profitability. Fee sniping can become increasingly profitable as the block reward decreases and transaction fees represent a larger part of miners' revenue. It can also be advantageous when the fees contained in the previous block are significantly higher than those in the next best candidate block. To simplify, the miner is faced with this choice in terms of incentives:


- Mine in a normal manner following the last block, with a high probability of winning a low reward;
- Attempt to mine a previous block (fee sniping), with a low probability of winning a high reward.

This attack poses a risk to the Bitcoin system, as the more miners adopt it, the more other miners, initially honest, are incentivized to do the same. Indeed, each time a new miner joins those attempting fee sniping, the probability that one of the attacking miners succeeds increases, and the probability that one of the honest miners extends the chain decreases in return. If this attack is carried out massively and sustained over time, block confirmations would no longer be a reliable indicator of the immutability of a Bitcoin transaction. This could potentially render the system unusable.

To counter this risk, most wallet software automatically fills in the `nLocktime` field so that it conditions the validation of the transaction to inclusion in the next block height. Thus, it becomes impossible to include the transaction in a rewrite of the previous block. If the widespread use of `nLocktime` is adopted by Bitcoin users, it significantly reduces the incentives for fee sniping. Indeed, it encourages the progression of the blockchain rather than its rewriting by reducing the potential profits from it. For Taproot transactions, BIP326 proposes using the `nSequence` field in a similar way to achieve the equivalent effect of the `nLocktime` field for other types of transactions. This usage would kill two birds with one stone by also improving the privacy of second-layer protocols that use the same field.