---
term: BIP0009
---

Method for activating soft forks on Bitcoin proposed in 2015. It introduced a mechanism in which miners signal their support for a soft fork by setting a specific bit in the block version field. 
A soft fork proposed under BIP9 is activated if 95% of blocks within a 2016-block period (approximately two weeks, matching each difficulty adjustment period) signal approval. After this lock-in period, an additional grace period allows miners to prepare for the update before it activates. If the 95% threshold is not reached within the maximum allotted time, the soft fork is abandoned. 
BIP9 allows multiple soft forks to be signaled simultaneously but grants considerable influence to miners: if the threshold is not met, the proposed soft fork simply fails to activate. This method was initially used for SegWit until BIP148 (a User-Activated Soft Fork) shifted the dynamics and forced activation through BIP91.
