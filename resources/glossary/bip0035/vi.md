---
term: BIP0035

definition: Đề xuất cho phép các nút chia sẻ thông tin mempool của họ (các giao dịch đang chờ xử lý) với các tác nhân khác trong mạng.
---
Proposal allowing a Bitcoin node to open up information about its mempool, meaning the transactions waiting for confirmation. Thanks to this, other participants can receive real-time data on unconfirmed transactions by sending a specific message to a node. Before the adoption of BIP35, nodes could only access information about already confirmed transactions. This improvement offers SPV wallets the ability to receive information on unconfirmed transactions, allows a miner to avoid missing transactions with high fees during a restart, and facilitates the analysis of mempool information by external services.