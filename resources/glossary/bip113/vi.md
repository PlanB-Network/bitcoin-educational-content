---
term: BIP113

---
Introduced a change in the calculation of all timelock operations (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, and `OP_CHECKSEQUENCEVERIFY`). It specifies that to evaluate the validity of timelocks, they must now be compared to the MTP (*Median Time Past*), which is the median of the timestamps of the last 11 blocks. Previously, only the timestamp of the previous block was used. This method makes the system more predictable and prevents the manipulation of the time reference by miners. BIP113 was introduced via a soft fork on July 4, 2016, alongside BIP68 and BIP112, activated for the first time using the BIP9 method.