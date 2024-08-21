---
term: MERKLE BLOCK
---

Datová struktura používaná v kontextu BIP37 (*Transaction Bloom Filtering*) k poskytnutí kompaktního důkazu o zařazení konkrétních transakcí do bloku. Je významně využívána pro SPV peněženky. MERKLE BLOCK obsahuje hlavičky bloků, filtrované transakce a částečný Merkle strom, což umožňuje lehkým klientům rychle ověřit, zda transakce patří do bloku, aniž by museli stahovat všechny transakce.