---
term: P2SH

---
P2SH stands for *Pay to Script Hash*. It is a standard script model used to establish spending conditions on a UTXO. Unlike P2PK and P2PKH scripts, where spending conditions are predefined, P2SH allows for the integration of arbitrary spending conditions and additional functionalities within a transaction script.

Technically, in a P2SH transaction, the `scriptPubKey` contains the cryptographic hash of a `redeemScript`, rather than explicit spending conditions. This hash is obtained using a `SHA256` hash. When sending bitcoins to a P2SH address, the underlying `redeemScript` is not revealed. Only its hash is included in the transaction. P2SH addresses are encoded in `Base58Check` and start with the number `3`. When the recipient wishes to spend the received bitcoins, they must provide a `redeemScript` that matches the hash present in the `scriptPubKey`, along with the necessary data to satisfy the conditions of this `redeemScript`. For example, in a P2SH multisignature script, the script could require signatures from multiple private keys.

The use of P2SH offers more flexibility, as it allows for the construction of arbitrary scripts without the sender knowing the details. P2SH was introduced in 2012 with BIP16.