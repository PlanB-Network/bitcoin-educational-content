---
termi: ASSUME UTXO
---

Konfiguraatioparametri johtavassa Bitcoin Core -asiakasohjelmassa, joka sallii juuri alustetun solmun (mutta joka ei ole vielä suorittanut IBD:tä) lykätä tapahtumien ja UTXO-joukon vahvistamista annettuun tilannevedokseen asti. Konsepti perustuu UTXO-joukon (luettelo kaikista olemassa olevista UTXO:ista tiettynä aikana) käyttöön, jonka Core tarjoaa ja oletetaan tarkaksi, mikä mahdollistaa solmun nopean synkronoinnin ketjuun, jolla on eniten kumuloitunutta työtä. Koska solmu jättää väliin pitkän IBD-vaiheen, se tulee nopeasti käyttövalmiiksi käyttäjälleen. Assume UTXO jakaa synkronoinnin (IBD) kahteen osaan:
* Ensin solmu suorittaa Header First Syncin (vain otsikoiden vahvistaminen) ja pitää Coren tarjoamaa UTXO-joukkoa kelvollisena;
* Sitten, kun se on toiminnallinen, solmu vahvistaa koko lohkoketjun historian taustalla, päivittäen uuden UTXO-joukon, jonka se on itse vahvistanut. Jos tämä uusi UTXO-joukko ei vastaa Coren tarjoamaa, se tuottaa virheviestin.

Näin ollen Assume UTXO nopeuttaa uuden Bitcoin-solmun valmistelua lykkäämällä tapahtumien vahvistusprosessia ja UTXO-joukkoa Coren tarjoaman päivitetyn tilannevedoksen kautta.