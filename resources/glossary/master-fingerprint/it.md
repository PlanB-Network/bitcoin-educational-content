---
term: IMPRONTA DIGITALE MASTER

---
Impronta digitale a 4 byte (32 bit) della chiave privata principale in un portafoglio deterministico gerarchico (HD). Si ottiene calcolando l'hash `SHA256` della chiave privata principale, seguito da un hash `RIPEMD160`, un processo indicato come `HASH160` su Bitcoin. L'impronta digitale master viene utilizzata per identificare un portafoglio HD, indipendentemente dai percorsi di derivazione, ma tenendo conto della presenza o meno di una passphrase. Si tratta di un'informazione concisa che consente di fare riferimento all'origine di un insieme di chiavi, senza rivelare informazioni sensibili sul portafoglio.