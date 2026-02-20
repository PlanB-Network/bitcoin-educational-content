---
term: RPC (lời gọi thủ tục từ xa)

definition: Giao thức cho phép thực thi các lệnh từ xa trên một nút Bitcoin.
---
A computer protocol that allows a program to execute a procedure on another remote computer as if it were executed locally. Specifically, in the context of Bitcoin, it is used to enable applications to interact with bitcoind. It can be used to execute commands on a Bitcoin node, such as sending transactions, managing wallets, or accessing information on the blockchain. The security of this interaction is ensured through authentication via a `.cookie` file or credentials, so that only authorized clients can perform RPCs on the node.

