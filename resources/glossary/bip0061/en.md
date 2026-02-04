---
term: BIP0061
definition: Reject message between nodes signaling why a transaction or block is invalid. Deprecated in Bitcoin Core 0.20.0.
---

Introduced a rejection message in the communication protocol between nodes. Its purpose was to provide a feedback mechanism so that when a node received a transaction or block it considered invalid, it could inform the sender of the reason for rejection. 
This type of communication was intended to improve interoperability among different clients and communications between full nodes and SPV clients. 
The functionalities brought by BIP61 were eventually abandoned starting from version 0.20.0 of Bitcoin Core, as they were considered unnecessary while they involved increased bandwidth needs.