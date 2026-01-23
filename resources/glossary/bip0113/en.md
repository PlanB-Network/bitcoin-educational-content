---
term: BIP0113
definition: Modification of timelocks to use Median Time Past (median of the last 11 blocks) instead of the previous block's timestamp.
---

Introduced a change in how all timelock operations (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, and `OP_CHECKSEQUENCEVERIFY`) are evaluated. 
It specifies that timelocks must now be compared to the Median Time Past (MTP), which is the median of the timestamps of the last 11 blocks, rather than to the timestamp of the previous block. 
This change makes the system more predictable and prevents miners from manipulating the time reference. 
BIP113 was introduced via a soft fork on July 4, 2016, alongside BIP68 and BIP112, activated for the first time using the BIP9 method.