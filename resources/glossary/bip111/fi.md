---
termi: BIP111
---

Ehdottaa palvelubitin, nimeltään `NODE_BLOOM`, lisäämistä, jotta solmut voivat nimenomaisesti ilmaista tukensa Bloom-suodattimille, kuten BIP37:ssä kuvataan. `NODE_BLOOM`in käyttöönotto mahdollistaa solmujen operaattoreille tämän palvelun poiskytkemisen, jotta voidaan vähentää DoS-hyökkäysten riskejä. BIP37-vaihtoehto on oletusarvoisesti pois käytöstä Bitcoin Core:ssa. Sen käyttöönottamiseksi konfiguraatiotiedostoon on syötettävä parametri `peerbloomfilters=1`.