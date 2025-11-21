---
term: txid (IDENTIFIKATOR TRANSAKCIJE)
---

Jedinstveni identifikator povezan sa svakom Bitcoin transakcijom. Generiše se izračunavanjem `SHA256d` Hash podataka transakcije. txid služi kao referenca za pronalaženje određene transakcije unutar Blockchain. Takođe se koristi za referenciranje UTXO, što je u suštini konkatenacija txid prethodne transakcije i indeksa određenog izlaza (takođe nazvanog "vout"). Za post-SegWit transakcije, txid više ne uzima u obzir svedoka transakcije, što eliminiše promenljivost.