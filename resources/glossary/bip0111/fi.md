---
term: BIP0111

definition: NODE_BLOOM-palvelubitin lisäys, jonka avulla solmut voivat ilmoittaa tuestaan Bloom-suodattimille (BIP37).
---
Ehdotetaan lisättäväksi palvelubitti nimeltä `NODE_BLOOM`, jotta solmut voivat nimenomaisesti ilmoittaa tukevansa Bloom-suodattimia BIP37:ssä kuvatulla tavalla. NODE_BLOOM`:n käyttöönotto antaa solmujen operaattoreille mahdollisuuden poistaa tämä palvelu käytöstä DoS-riskien vähentämiseksi. BIP37-vaihtoehto on oletusarvoisesti poistettu käytöstä Bitcoin Coressa. Sen ottamiseksi käyttöön parametri `peerbloomfilters=1` on syötettävä konfiguraatiotiedostoon.