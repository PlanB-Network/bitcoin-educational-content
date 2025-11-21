---
term: Merkle Tree
---

Merkle Tree je kriptografski akumulator. To je metoda za dokazivanje članstva određenog podatka unutar većeg skupa. To je struktura podataka koja omogućava verifikaciju informacija u kompaktnom formatu. U sistemu Bitcoin, Merkle stabla se koriste za grupisanje i kondenzovanje transakcija bloka u jedan Hash, nazvan Merkle Root (ili "*Root Hash*"). Svaka transakcija se hešira, zatim se susedni heševi hijerarhijski heširaju zajedno dok se ne dobije Merkle Root.


![](../../dictionnaire/assets/1.webp)


Ova struktura omogućava brzo proveravanje da li je određena transakcija uključena u dati blok bez potrebe za analizom svih transakcija. Na primer, ako imam samo Merkle Root i želim da proverim da li je `TX 7` zaista deo stabla, biće mi potrebni samo sledeći dokazi:


- `TX 7`;
- `Hash 8`;
- `Hash 5-6`;
- `Hash 1-2-3-4`.

Sa ovim informacijama, mogu da izračunam međučvorove do Merkle Root.


![](../../dictionnaire/assets/2.webp)


Merkle Trees su posebno korišćena za light nodove (poznate kao "SPV") koji čuvaju samo zaglavlja blokova, ali ne i transakcije. Ova struktura se takođe nalazi u UTREEXO protokolu, protokolu koji omogućava kondenzovanje UTXO skupa nodova, i u MAST Taproot.


> ► *Merkle Tree je nazvan po Ralphu Merkleu, kriptografu koji je dizajnirao ovu strukturu 1979. godine. Merkle Tree se takođe može nazvati "Hash stablo". Na francuskom se naziva "Arbre de Merkle" ili "arbre de hachage".*