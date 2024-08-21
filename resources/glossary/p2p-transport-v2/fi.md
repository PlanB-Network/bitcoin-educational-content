---
termi: P2P TRANSPORT V2
---

Bitcoinin P2P-siirtoprotokollan uusi versio, joka sisältää opportunistisen salauksen yksityisyyden ja kommunikaation turvallisuuden parantamiseksi solmujen välillä. Tämä parannus pyrkii puuttumaan useisiin perusversion P2P-protokollan ongelmiin, erityisesti tekemällä vaihdetun datan erottamattomaksi passiiviselle tarkkailijalle (kuten internet-palveluntarjoajalle), vähentäen näin sensuurin ja hyökkäysten riskejä, jotka perustuvat tiettyjen kuvioiden havaitsemiseen datapaketeissa.

Toteutettu salaus ei sisällä autentikointia välttääkseen tarpeettoman monimutkaisuuden lisäämisen ja ettei vaaranneta verkkoyhteyden luvattoman luonteen. Tämä uusi P2P-siirtoprotokolla tarjoaa kuitenkin paremman turvallisuuden passiivisia hyökkäyksiä vastaan ja tekee aktiiviset hyökkäykset huomattavasti kalliimmiksi ja havaittavammiksi (erityisesti MITM-hyökkäykset). Pseudo-satunnaisen datavirran käyttöönotto vaikeuttaa tehtävää hyökkääjille, jotka haluavat sensuroida tai manipuloida kommunikaatiota.

P2P Transport V2 sisällytettiin vaihtoehtona (oletuksena pois käytöstä) Bitcoin Coren versioon 26.0, joka otettiin käyttöön joulukuussa 2023. Sen voi aktivoida `v2transport=1`-vaihtoehdolla konfiguraatiotiedostossa.