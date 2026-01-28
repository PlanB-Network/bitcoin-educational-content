---
term: Blocks/rev*.dat
definition: Fajlovi koji skladište podatke za poništavanje (undo data) kako bi se omogućio povratak na prethodno stanje UTXO seta.
---

Nazivi datoteka u Bitcoin Core koje čuvaju informacije potrebne za potencijalno poništavanje promena napravljenih u UTXO setu od strane prethodno dodatih blokova. Svaka datoteka je identifikovana jedinstvenim brojem koji je isti kao i odgovarajuća blk*.dat datoteka. rev*.dat datoteke sadrže podatke za poništavanje koji odgovaraju blokovima sačuvanim u blk*.dat datotekama. Ovi podaci su u suštini lista svih UTXO-a potrošenih kao ulazi u bloku. Ove datoteke za poništavanje omogućavaju čvoru da se vrati na prethodno stanje u slučaju Blockchain reorganizacije koja uzrokuje odbacivanje prethodno validiranih blokova.