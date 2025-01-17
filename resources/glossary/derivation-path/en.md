---
term: DERIVATION PATH
---

In the context of Hierarchical Deterministic (HD) wallets, a derivation path refers to the sequence of indices used to derive child keys from a master key. Described in BIP32, this path identifies the tree structure for deriving child keys. A derivation path is represented by a series of indices separated by slashes, and always starts with the master key (denoted as `m/`). For example, a typical path might be `m/84'/0'/0'/0/0`. Each level of derivation is associated with a specific depth:
* `m /` indicates the master private key. It is unique to a wallet and cannot have siblings at the same depth. The master key is derived directly from the seed;
* `m / purpose' /` indicates the derivation purpose which helps to identify the followed standard. This field is described in BIP43. For example, if the wallet adheres to the BIP84 standard (SegWit V0), the index would then be `84'`;
* `m / purpose' / coin-type' /` indicates the type of cryptocurrency. This allows for clear differentiation between branches dedicated to one cryptocurrency and those dedicated to another in a multi-coin wallet. The index dedicated to Bitcoin is `0'`;
* `m / purpose' / coin-type' / account' /` indicates the account number. This depth makes it easy to differentiate and organize a wallet into different accounts. These accounts are numbered starting from `0'`. Extended keys (`xpub`, `xprv`...) are found at this level of depth;
* `m / purpose' / coin-type' / account' / change /` indicates the path. Each account as defined at depth 3 has two paths at depth 4: an external chain and an internal chain (also called "change"). The external chain derives addresses intended to be shared publicly, that is, the addresses that are offered to us when we click on "receive" in our wallet software. The internal chain derives addresses not intended to be exchanged publicly, mainly change addresses. The external chain is identified with the index `0` and the internal chain is identified with the index `1`. You will notice that from this depth, we no longer perform a hardened derivation, but a normal derivation (there is no apostrophe). It is thanks to this mechanism that we are able to derive all the child public keys from their `xpub`;

* `m / purpose' / coin-type' / account' / change / address-index` simply indicates the number of the receiving address and its pair of keys, in order to differentiate it from its siblings at the same depth on the same branch. For example, the first derived address has the index `0`, the second address has the index `1`, and so on...

For example, if my receiving address has the derivation path `m / 86' / 0' / 0' / 0 / 5`, we can deduce the following information:
* `86'` indicates that we are following the derivation standard of BIP86 (Taproot / SegWit V1);
* `0'` indicates that it is a Bitcoin address;
* `0'` indicates that we are on the first account of the wallet;
* `0` indicates that it is an external address;
* `5` indicates that it is the sixth external address of this account.

![](../../dictionnaire/assets/18.webp)