---
term: CURRENCY TYPE
---

In the context of deterministic and hierarchical (HD) wallets, the currency type (*coin type* in English) is a level of derivation that allows for differentiating the branches of the wallet based on the various cryptocurrencies used. This layer of derivation, defined by BIP 44, is located at depth 2 of the derivation structure, following the master key and the purpose. For example, for Bitcoin, the assigned index is `0x80000000`, noted as `/0'/` in the derivation path. This means that all addresses and accounts derived from this path are associated with Bitcoin. This layer of derivation enables a clear separation of different assets in a multi-currency wallet. Here are the indexes used for various cryptocurrencies:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)

