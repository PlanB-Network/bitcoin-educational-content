---
term: OUTPUT SCRIPT DESCRIPTORS

---
Output script descriptors, or simply descriptors, are structured expressions that fully describe an output script (`scriptPubKey`) and provide all the necessary information to track transactions to or from a specific script. These descriptors facilitate the management of keys in HD wallets through a standard description of the structure and types of addresses used.

The main interest of descriptors lies in their ability to encapsulate all the essential information for restoring a wallet in a single string (in addition to the recovery phrase). By saving a descriptor with the corresponding mnemonic phrases, it is possible to restore not only the private keys but also the precise structure of the wallet and the associated script parameters. Indeed, recovering a wallet requires not only knowledge of the initial seed but also specific indexes for the derivation of child key pairs, as well as the `xpub` of each factor in the case of a multisig wallet. Previously, it was assumed that this information was implicitly known by all. However, with the diversification of scripts and the emergence of more complex configurations, this information could become difficult to extrapolate, thus turning these data into private and hard-to-bruteforce information. The use of descriptors greatly simplifies the process: it is enough to know the recovery phrase(s) and the corresponding descriptor to restore everything reliably and securely.

A descriptor consists of several elements:


- Script functions like `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature), and `sortedmulti` (Multisignature with sorted keys);
- Derivation paths, for example, `[d34db33f/44h/0h/0h]` indicating a derived path and a specific master key fingerprint;
- Keys in various formats such as hexadecimal public keys or extended public keys (`xpub`);
- A checksum, preceded by a hash, to verify the integrity of the descriptor.

For example, a descriptor for a P2WPKH wallet could look like:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

In this descriptor, the derivation function `wpkh` indicates a Pay-to-Witness-Public-Key-Hash script type. It is followed by the derivation path which contains:


- `cdeab12f`: the fingerprint of the master key;
- `84h`: which signifies the use of a BIP84 purpose, intended for SegWit v0 addresses;
- `0h`: which indicates that it is a BTC currency on the mainnet;
- `0h`: which refers to the specific account number used in the wallet.

The descriptor also includes the extended public key used in this wallet:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Next, the notation `/<0;1>/*` specifies that the descriptor can generate addresses from the external (`0`) and internal (`1`) chain, with a wildcard (`*`) allowing for the sequential derivation of multiple addresses in a configurable manner, similar to managing a "gap limit" on traditional wallet software.

Finally, `#jy0l7nr4` represents the checksum to verify the integrity of the descriptor.