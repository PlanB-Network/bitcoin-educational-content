---
term: nLockTime
definition: Transactieveld dat een absolute tijdsvoorwaarde definieert voordat deze in een blok wordt opgenomen.
---

Een ingebouwd veld in transacties dat een tijdsgebaseerde voorwaarde stelt voor wanneer de transactie niet kan worden toegevoegd aan een geldig blok. Met deze parameter kan een exacte tijd (Unix Timestamp) of een specifiek aantal blokken worden opgegeven als voorwaarde om de transactie als geldig te beschouwen. Het is dus een absoluut tijdslot (niet relatief). De `nLockTime` beïnvloedt de hele transactie en maakt tijdscontrole mogelijk, terwijl de opcode `OP_CHECKLOCKTIMEVERIFY` alleen de bovenste waarde van de stack vergelijkt met de `nLockTime` waarde.