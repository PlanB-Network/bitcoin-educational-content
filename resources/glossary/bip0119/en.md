---
term: BIP0119
definition: Proposal for the OP_CHECKTEMPLATEVERIFY (CTV) opcode allowing covenants to be created that impose conditions on future spending.
---

Introduces a new opcode named `OP_CHECKTEMPLATEVERIFY` (CTV). CTV would enable the creation of non-recursive covenants in transactions, allowing specific conditions to be imposed on how a coin can be spent, including in future transactions. 
More specifically, it would allow defining constraints on a transaction's output `scriptPubKey` based on the `scriptPubKey` of the UTXO being spent. 
CheckTemplateVerify is designed to be simple and without dynamic state. Its implementation aims to extend Bitcoin's scripting capabilities to facilitate various applications such as transaction congestion control, the creation of non-interactive payment channels, DLCs, payment pools... 
This new opcode would replace OP_NOP4 and would require a soft fork for activation.