---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Čini transakciju nevažećom osim ako svi ovi uslovi nisu ispunjeni:


- Stek nije prazan;
- Vrednost na vrhu steka je veća ili jednaka `0`;
- Tip vremenske brave je isti između polja `nLockTime` i vrednosti na vrhu steka (realno vreme ili broj bloka);
- Polje `nSequence` ulaza nije jednako `0xffffffff`;
- Vrednost na vrhu steka je veća ili jednaka vrednosti polja `nLockTime` transakcije.


Ako bilo koji od ovih uslova nije ispunjen, skripta koja sadrži `OP_CHECKLOCKTIMEVERIFY` ne može biti zadovoljena. Ako su svi ovi uslovi validni, tada `OP_CHECKLOCKTIMEVERIFY` deluje kao `OP_NOP`, što znači da ne vrši nikakvu akciju na skripti. Kao da nestaje. `OP_CHECKLOCKTIMEVERIFY` tako nameće vremensko ograničenje na trošenje UTXO osiguranog skriptom koji ga sadrži. To može učiniti bilo u obliku Unix vremenskog datuma ili kao broj bloka. Da bi to uradio, ograničava moguće vrednosti za polje `nLockTime` transakcije koja ga troši, a samo ovo polje `nLockTime` ograničava kada transakcija može biti uključena u blok.


> ► *Ovaj opcode je zamena za `OP_NOP`. Postavljen je na `OP_NOP2`. Često se naziva akronimom "CLTV". Napomena, `OP_CLTV` ne treba mešati sa `nLockTime` poljem transakcije. Prvi koristi drugi, ali njihove prirode i akcije su različite.*