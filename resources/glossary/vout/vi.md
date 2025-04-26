---
term: VOUT

---
A specific element of a Bitcoin transaction that determines the destination of the sent funds. A transaction can include multiple outputs, each uniquely identified by the combination of the transaction identifier (`txid`) and an index called `vout`. This index, starting at `0`, marks the position of the output in the sequence of transaction outputs. Thus, the first output will be designated by `"vout": 0`, the second by `"vout": 1`, and so on.

Each `vout` primarily encapsulates two pieces of information:


- the value, expressed in bitcoins, which represents the amount sent;
- a locking script (`scriptPubKey`) that stipulates the conditions required for the funds to be spent again in a future transaction.

The combination of the `txid` and the `vout` of a specific piece forms what is called a UTXO, for example:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```