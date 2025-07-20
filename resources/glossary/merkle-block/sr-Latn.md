---
term: MERKLE BLOK
---

Struktura podataka koja se koristi u kontekstu BIP37 (*Filtriranje transakcija pomoću Bloom filtera*) za pružanje kompaktnog dokaza o uključivanju specifičnih transakcija u blok. Posebno se koristi za SPV novčanike. Merkle blok sadrži zaglavlja blokova, filtrirane transakcije i delimičan Merkle Tree, omogućavajući lakim klijentima da brzo provere da li transakcija pripada bloku bez preuzimanja svih transakcija.