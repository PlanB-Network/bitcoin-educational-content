---
termi: MERKLE-JUURI
---

Tiivistelmä tai "päähajautus" Merkle-puusta, joka edustaa yhteenvetoa kaikista puussa olevista tiedoista. Merkle-puu on kryptografinen kumuloituva rakenne, jota joskus kutsutaan myös "hajautuspuuksi". Bitcoinin kontekstissa Merkle-puita käytetään järjestämään transaktioita lohkossa ja helpottamaan tietyn transaktion sisällyttämisen nopeaa varmistamista. Näin ollen Bitcoin-lohkoissa Merkle-juuri saadaan hajauttamalla transaktioita pareittain, kunnes jäljellä on vain yksi hajautus (Merkle-juuri). Tämä sisällytetään sitten vastaavan lohkon otsikkoon. Tämä hajautuspuu löytyy myös UTREEXO-rakenteesta, joka mahdollistaa solmujen UTXO-joukon tiivistämisen, sekä MAST Taprootissa.