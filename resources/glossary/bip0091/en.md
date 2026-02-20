---
term: BIP0091
definition: Mechanism that allowed the activation of SegWit in 2017 with an 80% threshold, avoiding the UASF conflict of BIP148.
---

Proposal by James Hilliard (engineer at Bitmain) to facilitate the activation of the SegWit soft fork, defined in BIP141, BIP143, and BIP147, through a MASF without directly reaching the required threshold of 95% of computing power signaling support via bit 1. 
Instead, BIP91 allowed miners to indirectly signal support for SegWit by setting bit 4 in their mined blocks. 
Once 269 blocks out of a 336‑block window (80% of hash power) signaled using bit 4, BIP91 would lock in. After lock‑in, all compatible nodes would reject blocks not signaling SegWit using bit 1.
This method aimed to make BIP148 (UASF) obsolete and to avoid a potential split of the blockchain on August 1, 2017. 
BIP91 was eventually activated on July 23, 2017 (at block 477,120), just before the critical date of August 1 imposed in BIP148. 
This forced miners to signal for SegWit, which was eventually locked in on August 9 at block 479,808, and then activated on August 24 at block 481,824. 
In summary, BIP148 (UASF) was created in response to miners not signaling SegWit sufficiently, but was ultimately never implemented. 
BIP91 (MASF) was created in response to BIP148 to force miners' hands, without risking the UASF of BIP148. BIP91 itself represents a soft fork, which will eventually force miners to lock in the SegWit soft fork via the base method (MASF BIP9).

