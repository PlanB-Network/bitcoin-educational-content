---
term: MERKLE BLOK
---

Een gegevensstructuur die wordt gebruikt in de context van BIP37 (*Transaction Bloom Filtering*) om een compact bewijs te leveren van de opname van specifieke transacties in een blok. Het wordt met name gebruikt voor SPV wallets. Het Merkle Block bevat de block headers, gefilterde transacties en een gedeeltelijke Merkle Tree, waardoor light clients snel kunnen verifiëren of een transactie bij een blok hoort zonder alle transacties te downloaden.