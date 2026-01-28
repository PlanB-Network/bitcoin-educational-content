---
term: Nulldummy
definition: Rule requiring the dummy element in OP_CHECKMULTISIG to be an empty byte array.
---

Consensus rule introduced with BIP147 in the SegWit soft fork that requires the dummy element used in the `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` opcodes to be an empty byte array (`OP_0`). This measure was implemented to eliminate a malleability vector by prohibiting any value other than `OP_0` for this element.

