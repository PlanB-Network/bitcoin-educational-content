---
termi: SIGHASH_ANYPREVOUT
---

Ehdotus uuden SigHash-lipun muokkaimen käyttöönotosta Bitcoinissa, joka esiteltiin BIP118:n yhteydessä. `SIGHASH_ANYPREVOUT` mahdollistaa suuremman joustavuuden transaktioiden hallinnassa, erityisesti edistyneissä sovelluksissa kuten Lightning Networkin maksukanavissa ja Eltoo-päivityksessä. `SIGHASH_ANYPREVOUT` mahdollistaa sen, että allekirjoitus ei ole sidottu mihinkään tiettyyn aiempaan UTXO:oon (*Mikä Tahansa Edellinen Lähtö*). Käytettynä yhdessä `SIGHASH_ALL` kanssa, se sallisi kaikkien transaktion lähtöjen allekirjoittamisen, mutta ei yhdenkään syötteen. Tämä mahdollistaisi allekirjoituksen uudelleenkäytön eri transaktioissa, kunhan tietyt määritellyt ehdot täyttyvät.

> ► *Tämä SigHash-muokkain SIGHASH_ANYPREVOUT on johdettu Joseph Poonin vuonna 2016 esittämästä SIGHASH_NOINPUT-ideasta, jonka tarkoituksena oli parantaa hänen konseptiaan Lightning Networkista.*