---
term: MERKLE BLOCK

---
Datová struktura používaná v kontextu BIP37 (*Transaction Bloom Filtering*) k poskytnutí kompaktního důkazu o zařazení konkrétních transakcí do bloku. Používá se zejména pro peněženky SPV. Blok Merkle obsahuje hlavičky bloků, filtrované transakce a částečný strom Merkle, což umožňuje lehkým klientům rychle ověřit, zda transakce patří do bloku, aniž by museli stahovat všechny transakce.