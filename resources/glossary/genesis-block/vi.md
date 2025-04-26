---
term: GENESIS BLOCK

---
The Genesis Block is the first block of the Bitcoin system. It signifies the concrete launch of Bitcoin. The Genesis Block was created by Bitcoin's anonymous founder, Satoshi Nakamoto, on January 3, 2009. Its hash is:

```text
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

This block contains only a coinbase transaction that generates 50 bitcoins as a reward for the miner (in this case, Satoshi Nakamoto himself). This block includes a message embedded in the coinbase transaction:

```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

This quote is a reference to an article from *The Times* newspaper. The message is interpreted as a critique of the traditional financial system and its excesses, which partly motivated the creation of Bitcoin as a monetary alternative.

Since it embodies the very first block of the Bitcoin blockchain, the Genesis Block obviously does not have a field containing the hash of the previous block (because there isn't one). Moreover, the 50 bitcoins generated as a reward in this block are not spendable at the protocol level.