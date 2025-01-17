---
term: SPV NODE (LIGHT NODE)

---
An SPV (*Simple Payment Verification*) node, sometimes called a "light node," is a lightweight client of a Bitcoin node that allows users to validate transactions without having to store the entire blockchain. Instead, an SPV node only stores the block headers and obtains information about specific transactions by querying full nodes when necessary. This verification principle is made possible by the structure of transactions in Bitcoin blocks, which are organized within a cryptographic accumulator (Merkle Tree).

This approach is advantageous for devices with limited resources, such as mobile phones. However, SPV nodes rely on full nodes for the availability of information, which implies an additional level of trust and, consequently, less security compared to full nodes. SPV nodes cannot validate transactions autonomously, but they can verify if a transaction is included in a block by consulting Merkle proofs.