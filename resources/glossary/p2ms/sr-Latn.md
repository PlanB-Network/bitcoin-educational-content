---
term: P2MS
---

P2MS označava *Pay to Multisig*, što se prevodi kao "plaćanje na više potpisa". To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. Omogućava zaključavanje bitkoina sa više javnih ključeva. Da bi se ovi bitkoini potrošili, potreban je potpis sa unapred definisanim brojem povezanih privatnih ključeva. Na primer, `P2MS 2/3` uključuje `3` javna ključa sa `3` povezana tajna privatna ključa. Da bi se potrošili bitkoini zaključani ovom P2MS skriptom, potreban je potpis sa najmanje `2` od `3` privatna ključa. Ovo je sistem sigurnosti sa pragom.


Ovo pismo je izumio Gavin Andresen 2011. godine kada je preuzeo održavanje glavnog Bitcoin klijenta. Danas, P2MS se koristi samo marginalno od strane nekih aplikacija. Velika većina modernih multisignatura koristi druge skripte kao što su P2SH ili P2WSH. U poređenju sa njima, P2MS je izuzetno trivijalan. Javni ključevi koje sadrži otkrivaju se prilikom primanja transakcije. Korišćenje P2MS-a je takođe skuplje od drugih multisignature skripti.


> ► *P2MS se često nazivaju "bare-Multisig", što bi se moglo prevesti kao "gola višestruka potpisivanja" ili "sirova višestruka potpisivanja". Početkom 2023. godine, P2MS skripte su bile u centru kontroverze zbog njihove zloupotrebe unutar Stamps protokola. Njihov uticaj na UTXO set je posebno istaknut.*