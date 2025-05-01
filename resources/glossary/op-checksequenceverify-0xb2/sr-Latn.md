---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Čini transakciju nevažećom ako je bilo koja od ovih karakteristika primećena:


- Stek je prazan;
- Vrednost na vrhu steka je manja od `0`;
- Zastavica onemogućavanja za vrednost na vrhu steka je nedefinisana i; Verzija transakcije je manja od `2` ili; Zastavica onemogućavanja za polje `nSequence` ulaza je postavljena ili; Tip vremenske brave nije isti između polja `nSequence` i vrednosti na vrhu steka (realno vreme ili broj blokova) ili; Vrednost na vrhu steka je veća od vrednosti polja `nSequence` ulaza.


Ako se uoči jedna ili više ovih karakteristika, skripta koja sadrži `OP_CHECKSEQUENCEVERIFY` ne može biti zadovoljena. Ako su svi uslovi ispravni, tada `OP_CHECKSEQUENCEVERIFY` deluje kao `OP_NOP`, što znači da ne vrši nikakvu akciju na skripti. Kao da nestaje. `OP_CHECKSEQUENCEVERIFY` tako nameće relativno vremensko ograničenje na trošenje UTXO osiguranog skriptom koji ga sadrži. To može učiniti bilo u obliku stvarnog vremena ili kao broj blokova. Da bi to uradio, ograničava moguće vrednosti za polje `nSequence` ulaza koji ga troši, a samo ovo polje `nSequence` ograničava kada transakcija koja uključuje ovaj ulaz može biti uključena u blok.


> ► *Ovaj opcode je zamena za `OP_NOP`. Postavljen je na `OP_NOP3`. Često se naziva akronimom "CSV". Napomena, `OP_CSV` ne treba mešati sa `nSequence` poljem transakcije. Prvi koristi drugi, ali njihove prirode i akcije su različite.*