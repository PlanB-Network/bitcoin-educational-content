---
term: BIP44
---

A proposal for improvement that introduces a standard hierarchical derivation structure for HD wallets. BIP44 builds on the principles established by BIP32 for key derivation and on BIP43 for the use of the “purpose” field. It introduces a five-level derivation structure: `m / purpose' / coin_type' / account' / change / address_index`. Here are the details of each depth:
* `m /` indicates the master private key. It is unique to a wallet and cannot have siblings at the same depth. The master key is directly derived from the wallet's seed;
* `m / purpose' /` indicates the derivation purpose which helps identify the followed standard. This field is described in BIP43. For example, if the wallet follows the BIP84 (SegWit V0) standard, the index would then be `84'`;
* `m / purpose' / coin-type' /` indicates the type of cryptocurrency. This allows for clear differentiation between branches dedicated to one cryptocurrency and those dedicated to another cryptocurrency in a multi-coin wallet. The index dedicated to Bitcoin is `0'`;
* `m / purpose' / coin-type' / account' /` indicates the account number. This depth allows for easy differentiation and organization of a wallet into different accounts. These accounts are numbered starting from `0'`. Extended keys (`xpub`, `xprv`...) are found at this depth;
* `m / purpose' / coin-type' / account' / change /` indicates the chain. Each account as defined in depth 3 has two chains at depth 4: an external chain and an internal chain (also called “change”). The external chain derives addresses intended to be communicated publicly, i.e., the addresses offered to us when we click on “receive” in our wallet software. The internal chain derives addresses not intended to be exchanged publicly, i.e., primarily change addresses. The external chain is identified with the index `0` and the internal chain is identified with the index `1`. You will notice that from this depth, we no longer perform a hardened derivation, but a normal derivation (there is no apostrophe). It is thanks to this mechanism that we are capable of deriving all the child public keys from their `xpub`;
* `m / purpose' / coin-type' / account' / change / address-index` simply indicates the number of the receiving address and its pair of keys, in order to differentiate it from its siblings at the same depth on the same branch. For example, the first derived address has the index `0`, the second address has the index `1`, and so on...
For instance, if my receiving address has the derivation path `m / 86' / 0' / 0' / 0 / 5`, we can deduce the following information:
* `86'` indicates that we are following the derivation standard of BIP86 (Taproot or SegWitV1);
* `0'` indicates that it is a Bitcoin address;
* `0'` indicates that we are on the first account of the wallet;
* `0` indicates that it is an external address;
* `5` indicates that it is the sixth external address of this account.

![](../../dictionnaire/assets/18.webp)