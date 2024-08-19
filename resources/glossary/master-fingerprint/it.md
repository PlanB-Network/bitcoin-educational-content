---
term: MASTER FINGERPRINT
---

Un'impronta digitale di 4 byte (32 bit) della chiave privata master in un portafoglio gerarchico deterministico (HD). Si ottiene calcolando l'hash `SHA256` della chiave privata master, seguito da un hash `RIPEMD160`, un processo noto come `HASH160` su Bitcoin. Il Master Fingerprint è utilizzato per identificare un portafoglio HD, indipendentemente dai percorsi di derivazione, ma tenendo conto della presenza o assenza di una passphrase. È un'informazione concisa che permette di fare riferimento all'origine di un insieme di chiavi, senza rivelare informazioni sensibili sul portafoglio.