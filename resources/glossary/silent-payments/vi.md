---
term: SILENT PAYMENTS

---
Method for using static Bitcoin addresses to receive payments without address reuse, without interaction, and without a visible on-chain link between the different payments and the static address. This technique eliminates the need to generate new, unused receiving addresses for each transaction, thus avoiding the usual interactions in Bitcoin where the recipient must provide a new address to the payer.

With Silent Payments, the payer uses the recipient's public keys (spend public key and scan public key) and the sum of their own private keys as input to generate a fresh address for each payment. Only the recipient, with their private keys, can compute the private key corresponding to this payment address. ECDH (*Elliptic-Curve Diffie-Hellman*), a cryptographic key exchange algorithm, is used to establish a shared secret which is then used to derive the receiving address and the private key (on the recipient's side only). To identify the Silent Payments intended for them, recipients must scan the blockchain and examine each transaction matching the protocol's criteria. Unlike BIP47, which uses a notification transaction to establish the payment channel, Silent Payments eliminate this step, saving a transaction. However, the compromise is that the recipient must scan all potential transactions to determine, by applying ECDH, if they are addressed to them.

For example, Bob's static address $B$ represents the concatenation of his scan public key and his spend public key:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

These keys are simply derived from the following path:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

This static address is published by Bob. Alice retrieves it to make a Silent Payment to Bob. She calculates Bob's payment address $P_0$ in this way:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Where:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

With:


- $B_{\text{scan}}$: Bob's scan public key (static address);
- $B_{\text{spend}}$: Bob's spend public key (static address);
- $A$: The sum of the public keys in input (tweak);
- $a$: The private key of the tweak, that is, the sum of all key pairs used in the `scriptPubKey` of the UTXOs consumed as inputs in Alice's transaction;
- $\text{outpoint}_L$: The smallest UTXO (lexicographically) used as an input in Alice's transaction;
- $\text{ ‖ }$: Concatenation (the operation of joining operands end-to-end);
- $G$: The generator point of the elliptical curve `secp256k1`;
- $\text{hash}$: The SHA256 hash function tagged with `BIP0352/SharedSecret`;
- $P_0$: The first public key / unique address for payment to Bob;
- $0$: An integer used to generate multiple unique payment addresses.

Bob scans the blockchain to find his Silent Payment in this way:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

With:


- $b_{\text{scan}}$: Bob's private scan key.

If he finds $P_0$ as an address containing a Silent Payment addressed to him, he calculates $p_0$, the private key allowing him to spend the funds sent by Alice to $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

With:


- $b_{\text{spend}}$: Bob's private spending key;
- $n$: the order of the elliptical curve `secp256k1`.

In addition to this basic version, labels can also be used to generate several different static addresses from the same basic static address, with the aim of separating multiple uses without unreasonably multiplying the work required during scanning.