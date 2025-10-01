---
term: BIP0147
---

Proposal included in the SegWit soft fork aimed at resolving a malleability vector related to the dummy element consumed by the `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` operations. Due to a historical off-by-one bug (unit shift error), these 2 opcodes remove an additional element from the stack in addition to their intended function. 
To prevent script failure, a dummy value must therefore be placed at the beginning of the `scriptSig`. While this value serves no functional purpose, it is required for the script to be considered valid. 
BIP11, which introduced the P2MS standard, recommended using `OP_0` as the dummy element but this was never enforced at the consensus level, meaning any value could be used, thus introducing a malleability vector. 
This is how `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` contained a malleability vector. BIP147 introduces a new consensus rule, named `NULLDUMMY`, requiring that this dummy element be an empty byte array (`OP_0`). Any other value results in the immediate failure of the script evaluation. This change applies to pre-SegWit scripts as well as P2WSH scripts and required a soft fork.

