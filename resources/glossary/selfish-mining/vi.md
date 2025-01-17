---
term: SELFISH MINING

---
Strategy (or attack) in mining, where a miner or a group of miners intentionally keeps blocks with a valid proof of work without immediately broadcasting them to the network. The goal is to maintain a lead over other miners in terms of proof of work, which potentially allows them to mine several blocks in a row and publish them all at once, thus maximizing their gains.

In other words, the attacking group of miners does not mine on the last block validated by the entire network, but rather on a block they have created themselves, which differs from the one validated by the network. This process generates a kind of secret fork of the blockchain, which remains unknown to the entire network until this alternative chain potentially surpasses the honest blockchain. Once the secret chain of the attacking miners becomes longer (i.e., it contains more accumulated work) than the honest and public chain, it is then broadcast to the entire network. At that point, the network nodes, which follow the longest chain (with the most accumulated work), will synchronize with this new chain. This results in a reorganization.

Selfish mining is problematic because it decreases the security of the system by wasting part of the network's computational power. If successful, it also leads to blockchain reorganizations, thus affecting the reliability of transaction confirmations for users. This practice remains risky for the attacking group of miners, as it is often more profitable to mine normally on the last block known publicly rather than allocating computational power to a secret fork that will probably never surpass the honest blockchain. The greater the number of blocks in the reorganization, the lower the probability of the attack's success.

> ► *The English translation of "minage égoïste" is "selfish mining". Note, a selfish mining attack should not be confused with a block withholding attack.*