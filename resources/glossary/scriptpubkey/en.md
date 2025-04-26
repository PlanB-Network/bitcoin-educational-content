---
term: SCRIPTPUBKEY
---

A script located in the output part of a Bitcoin transaction that defines the conditions under which the associated UTXO can be spent. This script thus secures bitcoins. In its most common form, the `scriptPubKey` contains a condition that requires the next transaction to provide proof of possession of the private key corresponding to a specified Bitcoin address. This is often achieved by a script that demands a signature corresponding to the public key associated with the address used to secure these funds. When a transaction attempts to use this UTXO as an input, it must provide a `scriptSig` which, once combined with the `scriptPubKey`, meets the set conditions and produces a valid script.

For example, here is a classic P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

The corresponding `scriptSig` would be:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *This script is also sometimes referred to as a "locking script" in English.*