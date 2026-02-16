---
term: BIP0149
definition: Alternative to BIP148 proposing SegWit activation via BIP8 with a more gradual and less confrontational approach.
---

Proposal by Shaolin Fry for a new deployment of SegWit (BIP141, BIP143, and BIP147) using the BIP8 activation method with `LOT=true`, if the initial deployment of SegWit via BIP9 failed to activate before November 15, 2017. 
Unlike the BIP9 method, where a signaling failure results in the abandonment of activation, BIP149 aimed to activate SegWit on July 4, 2018, whether miners reached the 95% signaling threshold or not. 
During the eight-month period between November and July, nodes would have had the opportunity to implement BIP149, to ensure a SegWit activation by the economic majority of the network if miner activation did not occur (UASF). 
Once the first difficulty adjustment was reached after July 4, 2018, the activation would move to `LOCKED_IN`, and SegWit would have been activated in the next adjustment cycle. 
Unlike BIP148, which enforced SegWit activation via users or a majority of miners, BIP149 suggested a more gradual and measured activation method, though it remained decidedly offensive, following the principles of BIP8. 
Whereas BIP148 risked a blockchain split, BIP149 avoided this by accepting blocks not signaling SegWit (unless a miner deliberately acted otherwise). 
Therefore, BIP149 was a less conflictual SegWit activation mechanism than BIP148, favoring a more gradual and lower-risk adoption. 
Neither BIP148 nor BIP149 were ultimately implemented, with SegWit being activated through a MASF, notably under the impulse of BIP91.

