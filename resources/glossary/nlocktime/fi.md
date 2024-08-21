---
termi: NLOCKTIME
---

Sisäänrakennettu kenttä transaktioissa, joka asettaa aikapohjaisen ehdon, ennen kuin transaktio voidaan lisätä kelvolliseen lohkoon. Tämä parametri mahdollistaa tarkan ajan (Unix-aikaleima) tai tietyn määrän lohkoja ehtona transaktion katsomiselle kelvolliseksi. Näin ollen se on absoluuttinen aikalukko (ei suhteellinen). `nLockTime` vaikuttaa koko transaktioon ja mahdollistaa tehokkaasti ajan varmistamisen, kun taas operaatiokoodi `OP_CHECKLOCKTIMEVERIFY` sallii vain pinon päällimmäisen arvon vertaamisen `nLockTime`-arvoon.