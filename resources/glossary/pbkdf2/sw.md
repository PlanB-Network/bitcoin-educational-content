---
term: PBKDF2
---

`PBKDF2` inawakilisha *Utoaji wa Ufunguo Unaotegemea Nenosiri 2*. Ni njia ya kuunda funguo za kriptografia kutoka kwa nenosiri kwa kutumia kitendakazi cha derivation. Inachukua kuweka nenosiri, chumvi ya kriptografia, na kutumia mara kwa mara utendaji uliobainishwa (mara nyingi ni chaguo la kukokotoa la Hash kama `SHA256` au `HMAC`) kwa data hizi. Mchakato huu unarudiwa mara nyingi kwa generate ufunguo wa kriptografia.


Katika muktadha wa Bitcoin, `PBKDF2` inatumika pamoja na chaguo za kukokotoa za `HMAC-SHA512` ili kuunda seed ya kibainishi na kidaraja cha Wallet (seed) kutoka kwa kifungu cha maneno cha urejeshaji cha maneno 12 au 24. Chumvi ya kriptografia inayotumika katika kesi hii ni BIP39 passphrase, na idadi ya marudio ni `2048`.