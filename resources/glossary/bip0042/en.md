---
term: BIP0042
---

A Bitcoin Core improvement proposal that fixed a minor bug in the block reward halving schedule. If left uncorrected, this bug would have resulted in the creation of more than the intended 21 million bitcoins.
Specifically, after all halvings were completed, a new cycle of bitcoin creation could theoretically have been triggered around the year 2214. 
The Core code in question used a right binary shift operation on the value of the miner's reward. The bug stemmed from the use of this shift operation in a context where the behavior was undefined according to C++ language standards. Shifting a 64-bit integer (`int64_t`) more than 63 bits to the right falls into this category of undefined behavior. 
In the Bitcoin Core code, this could have occurred after 64 halvings, at block height no. 13,440,000. Beyond this limit, the behavior of the bit shift was not defined, meaning different compilations could interpret the code differently. This could have led to unpredictable outcomes, including the possibility of creating infinite bitcoin inflation. BIP42 corrected this problem by mandating that the block reward be set to zero after 64 halvings, thus avoiding the use of a right shift operation in a context of undefined behavior. 
This modification, which was a soft fork, clarified the behavior of the Bitcoin Core code. Although quite serious, this bug corrected by BIP42 was not immediately critical, as it would not have manifested until around the year 2214. Published on April 1, 2014, by Pieter Wuille, BIP42 is distinguished by its humorous tone.