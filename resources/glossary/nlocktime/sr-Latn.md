---
term: NLOCKTIME
---

Ugrađeno polje u transakcijama koje postavlja vremenski uslov pre kojeg transakcija ne može biti dodata u važeći blok. Ovaj parametar omogućava specificiranje tačnog vremena (Unix Timestamp) ili određenog broja blokova kao uslov za validnost transakcije. Dakle, to je apsolutni vremenski zaključ (nije relativan). `nLockTime` utiče na celu transakciju i efektivno omogućava vremensku verifikaciju, dok opcode `OP_CHECKLOCKTIMEVERIFY` omogućava samo poređenje gornje vrednosti steka sa `nLockTime` vrednošću.