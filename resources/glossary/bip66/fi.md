---
termi: BIP66
---

Otti käyttöön transaktioiden allekirjoitusmuodon standardisoinnin. Tämä BIP ehdotettiin vastauksena OpenSSL:n allekirjoitusten koodauksen käsittelyn eroavaisuuksiin eri järjestelmissä. Tämä heterogeenisyys aiheutti riskin lohkoketjun jakautumisesta. BIP66 standardisoi kaikkien transaktioiden allekirjoitusmuodon käyttäen tiukkaa DER-koodausta (*Distinguished Encoding Rules*). Tämä muutos vaati pehmeän haarautumisen (soft fork). Aktivointiinsa BIP66 käytti samaa mekanismia kuin BIP34, vaatien `nVersion` kentän nostamista versioon 3 ja hyläten kaikki versio 2 tai sitä alempien versioiden lohkot, kun 95% louhijoiden kynnys saavutettiin. Tämä kynnys ylitettiin lohkonumerossa 363,725 heinäkuun 4. päivänä 2015.