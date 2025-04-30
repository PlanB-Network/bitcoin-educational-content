---
term: NVERSION
---

Polje `nVersion` u transakciji Bitcoin koristi se za označavanje verzije formata transakcije koja se koristi. Omogućava mreži da razlikuje različite evolucije formata transakcije tokom vremena i da primeni odgovarajuća pravila. Ovo polje nema uticaj na pravila konsenzusa. To znači da bilo koja vrednost dodeljena ovom polju ne dovodi do poništavanja transakcije. Međutim, polje `nVersion` ima pravila standardizacije koja trenutno prihvataju samo vrednosti `1` i `2`. Za sada, ovo polje je korisno samo za aktivaciju polja `nSequence`.