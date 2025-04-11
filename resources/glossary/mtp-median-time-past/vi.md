---
term: MTP (MEDIAN TIME PAST)

---
This concept is used in the Bitcoin protocol to determine a margin on the network's consensus timestamp. MTP is defined as the median of the timestamps of the last 11 mined blocks. The use of this indicator helps to avoid disagreements among nodes about the exact time in case of discrepancies. MTP was initially used to verify the validity of block timestamps against the past. Since BIP113, it has also been used as a reference for network time to verify the validity of time-lock transactions (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, and `OP_CHECKSEQUENCEVERIFY`).