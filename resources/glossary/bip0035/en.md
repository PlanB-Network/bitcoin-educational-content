---
term: BIP0035
---

Proposal that allows a Bitcoin node to share information about its mempool, the pool of transactions waiting for confirmation.
This feature enables other participants to receive real-time data on unconfirmed transactions by sending a specific request to the node. Before BIP35, nodes could only provide information on transactions that had already been confirmed.
This improvement benefits SPV wallets by giving them access to unconfirmed transaction data, helps miners avoid missing high-fee transactions after a restart, and facilitates mempool analysis by external services.