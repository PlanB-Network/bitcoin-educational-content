---
term: BIP0143
---

Predstavlja novi način heširanja transakcije za verifikaciju potpisa u post-SegWit skriptama. Cilj je minimizirati redundantne operacije tokom verifikacije i uključiti vrednost UTXO-a u ulazu u potpis. Ovo rešava dva glavna problema sa originalnim algoritmom heširanja transakcija:


- Kvadratni rast heširanja podataka sa brojem potpisa;
- Odsustvo uključivanja ulazne vrednosti u potpis, što je predstavljalo rizik za hardverske novčanike, posebno u vezi sa saznanjem o nastalim transakcionim naknadama.

Od SegWit ažuriranja, objašnjenog u BIP141, uvodi se novi oblik transakcija čiji skript neće biti verifikovan od strane starih čvorova, BIP143 koristi ovu priliku da Address ovaj problem bez potrebe za Hard Fork. Stoga, BIP143 je deo SegWit Soft Fork.