---
term: DUSTRELAYFEE

---
A standardization rule used by network nodes to determine what they consider the "dust limit." This parameter sets a fee rate in sats per virtual kilobyte (sats/kvB) that serves as a reference for calculating if the value of a UTXO is less than the necessary fees to include it in a transaction. Indeed, a UTXO is considered "dust" on Bitcoin if it requires more in fees to be transferred than the value it represents itself. The calculation of this limit is as follows:

```text
limit = (input size + output size) * fee rate
```

As the required fee rate for a transaction to be included in a Bitcoin block constantly varies, the `DustRelayFee` parameter allows each node to define the fee rate used in this calculation. By default, on Bitcoin Core, this value is set to 3,000 sats/kvB. For example, to calculate the dust limit for a P2PKH input and output, which measure 148 and 34 bytes respectively, the calculation would be:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

This means that the node in question will not relay transactions including a P2PKH secured UTXO whose value is less than 546 sats.