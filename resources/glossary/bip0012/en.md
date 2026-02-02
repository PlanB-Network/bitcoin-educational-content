---
term: BIP0012
definition: Proposal introducing the OP_EVAL opcode for nested scripts, replaced by BIP16 (P2SH) for security reasons.
---

Proposal by Gavin Andresen to enhance the flexibility and privacy of Bitcoin transaction scripts. This BIP suggests implementing a new script opcode, named `OP_EVAL`, which would allow the evaluation of a script contained within the data of a `scriptSig` during transaction validation. 
The main modification of BIP12 is to allow the inclusion of one script inside another script. This technique enables the creation of more complex conditions that can be verified at the time of spending, without needing to reveal them to users sending bitcoins to the used address. BIP12 was later replaced by safer proposals, notably BIP16 (P2SH), which provided a different, more secure approach to achieving the same goals as `OP_EVAL`.