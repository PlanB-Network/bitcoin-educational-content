---
term: BIP0090
definition: Proposal simplifying the activation verification of old soft forks by using block height rather than miner signaling.
---

BIP90 proposes simplifying the activation of previous soft forks by replacing miner signaling via block version numbers with simple block height checks. 
This change removes the need to scan the previous 1,000 blocks when activating consensus rules, thereby reducing the technical debt associated with implementing these soft forks.