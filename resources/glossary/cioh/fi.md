---
termi: CIOH
---

Lyhenne sanoista "*Common Input Ownership Heuristic*", suomeksi "Yhteisen syötteen omistajuuden heuristiikka". Kyseessä on heuristiikka, jota käytetään Bitcoinin ketjuanalyysin alalla ja joka olettaa, että kaikki transaktion syötteet kuuluvat samalle entiteetille tai käyttäjälle. Kun tarkastellaan Bitcoin-transaktion julkisia tietoja ja havaitaan useita syötteitä, niin, jos ei ole havaittavissa malleja tai muuta informaatiota, joka kumoaisi tämän oletuksen, voidaan arvioida, että kaikki tämän transaktion syötteet kuuluivat yhdelle henkilölle (tai entiteetille).

Tämän analyysiheuristiikan löysi itse Satoshi Nakamoto, joka keskustelee siitä White Paperin osassa 10:

> "Kuitenkin yhteys on väistämätön usean syötteen transaktioissa, jotka välttämättä paljastavat, että niiden syötteet omisti sama omistaja. Riskinä on, että jos avaimen omistaja paljastetaan, yhteydet voivat paljastaa muita transaktioita, jotka kuuluivat samalle omistajalle." - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Konsultoitu osoitteessa https://bitcoin.org/bitcoin.pdf.

Vielä tänä päivänäkin CIOH on pääasiallinen heuristiikka, jota ketjuanalyysiyhtiöt käyttävät, osoitteen uudelleenkäytön ohella.

![](../../dictionnaire/assets/13.png)

> ► *Englanniksi "CIOH" voidaan kääntää "Common Input Ownership Heuristic"ksi.*