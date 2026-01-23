---
term: BIP0380
definition: Output Script Descriptors, ett standardspråk för att beskriva utgångsskripten för HD-plånböcker.
---

Ett förbättringsförslag som introducerar ett standardspråk för att beskriva samlingarna av utdataskript för HD Bitcoin-plånböcker. Detta språk kallas "Output Script Descriptors" Det syftar till att standardisera sättet att representera och hantera utdataskript, för att underlätta säkerhetskopiering, export och import av plånböcker. Förutom privata data som återställningsfrasen ger deskriptorerna all nödvändig information för att hämta de nyckelpar som används i en HD Wallet. BIP380 beskriver den allmänna funktionen för deskriptorer, medan BIP381, BIP382, BIP383, BIP384, BIP385 och BIP386 specificerar de uttryck som används. BIP380 implementerades tillsammans med alla andra deskriptorrelaterade BIP:er (utom BIP386) i version 0.17 av Bitcoin Core.