---
term: ADDRESS REUSE
---

Address reuse refers to the practice of using the same receiving address to lock multiple UTXOs, sometimes across different transactions. Bitcoins are typically locked using a cryptographic key pair corresponding to a unique address. Since the blockchain is public, it is easy to see which addresses are associated with how many bitcoins. If the same address is reused for multiple payments, one can reasonably assume that all associated UTXOs belong to the same entity. This fact presents a privacy issue, as it allows deterministic links to be made between multiple transactions and UTXOs, enabling on-chain fund tracing. Satoshi Nakamoto already mentioned this problem in the Bitcoin White Paper:

> "*As an additional firewall, a new pair of keys could be used for each transaction to keep them from being linked to a common owner.*" - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Consulted at https://bitcoin.org/bitcoin.pdf.

To preserve user privacy, it is strongly recommended to use each receiving address only once. For each new payment, a new address should be generated. For change outputs, a fresh address should also be used. Fortunately, thanks to deterministic and hierarchical wallets, using many different addresses has become very easy. All key pairs associated with a wallet can be easily regenerated from a single seed. This is also why wallet software always generates a new, different address when you click on the “Receive” button.

> ► *In English, it is called "Address Reuse".*
