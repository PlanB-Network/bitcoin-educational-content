---
term: BIP0017
definition: Alternative proposal to P2SH introducing the OP_CHECKHASHVERIFY opcode, ultimately not adopted in favor of BIP16.
---

Proposal by Luke Dashjr that competed with BIP12 and BIP16. BIP17 introduced a new opcode, `OP_CHECKHASHVERIFY`, designed to enable the verification of a script present in the `scriptSig` against its hash present in the `scriptPubKey` before unlocking the funds. BIP16 (P2SH) was eventually preferred over BIP17 (CHV) following a period of intense debates.