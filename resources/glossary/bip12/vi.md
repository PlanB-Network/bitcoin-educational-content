---
term: BIP12

---
Proposal by Gavin Andresen to enhance the flexibility and privacy of Bitcoin transaction scripts. This BIP suggests implementing a new script opcode, named `OP_EVAL`, which allows for the evaluation of a script contained within the data of a `scriptSig` during the transaction validation process. The main modification of BIP12 is to allow the inclusion of one script inside another script. This technique enables the creation of more complex conditions that can be verified at the time of spending, without needing to reveal them to users sending bitcoins to the used address. BIP12 was later replaced by safer proposals, notably BIP16 (P2SH), which offers a different method to achieve the same objectives as `OP_EVAL`.