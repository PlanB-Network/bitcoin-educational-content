---
term: PÄÄSORMENJÄLKI

---
Hierarkkisen deterministisen (HD) lompakon yksityisen pääavaimen 4 tavun (32-bittinen) sormenjälki. Se saadaan laskemalla yksityisen pääavaimen `SHA256`-hash, jota seuraa `RIPEMD160`-hash, prosessia kutsutaan Bitcoinissa nimellä `HASH160`. Master Fingerprintin avulla HD-lompakko tunnistetaan johdannaispoluista riippumatta, mutta ottaen huomioon tunnuslauseen olemassaolo tai puuttuminen. Se on tiivis tieto, jonka avulla voidaan viitata avainsarjan alkuperään paljastamatta lompakon arkaluonteisia tietoja.