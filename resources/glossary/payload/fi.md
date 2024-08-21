---
termi: PAYLOAD
---

Yleisessä tietotekniikan kontekstissa payload viittaa olennaiseen dataan, joka kuljetetaan suuremman datan paketin sisällä. Esimerkiksi SegWit V0 -osoitteessa Bitcoinissa payload vastaa julkisen avaimen hashia, jättäen erilaiset metadatat huomiotta (HRP, erotin, SegWit-versio ja tarkistussumma). Esimerkiksi osoitteessa `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` meillä on:
* `bc` : ihmisen luettava osa (HRP);
* `1` : erotin;
* `q` : SegWit-versio. Tässä se on versio 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : payload, tässä julkisen avaimen hash;
* `ys50gj` : tarkistussumma.