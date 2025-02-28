---
term: PAYLOAD

---
Yleisessä tietojenkäsittelyn yhteydessä hyötykuormalla tarkoitetaan laajemman datapaketin sisältämiä olennaisia tietoja. Esimerkiksi Bitcoinin SegWit V0 -osoitteessa hyötykuorma vastaa julkisen avaimen hash-arvoa, lukuun ottamatta erilaisia metatietoja (HRP, erotin, SegWit-versio ja tarkistussumma). Esimerkiksi osoitteessa `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` on:


- `bc` : ihmisen luettavissa oleva osa (HRP);
- `1` : erotin;
- `q` : SegWit-versio. Tässä se on versio 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : hyötykuorma, tässä tapauksessa julkisen avaimen hash;
- `ys50gj` : tarkistussumma.