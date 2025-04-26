---
term: P2P TRANSPORT V2

---
Uusi versio Bitcoin P2P -kuljetusprotokollasta, joka sisältää opportunistisen salauksen solmujen välisen viestinnän yksityisyyden ja turvallisuuden parantamiseksi. Tällä parannuksella pyritään ratkaisemaan useita P2P-protokollan perusversioon liittyviä ongelmia, erityisesti tekemällä vaihdetuista tiedoista erottamattomia passiiviselle tarkkailijalle (kuten Internet-palveluntarjoajalle), mikä vähentää sensuurin ja hyökkäysten riskiä havaitsemalla tietopaketeissa tiettyjä malleja.

Toteutettuun salaukseen ei sisälly todennusta, jotta vältettäisiin tarpeettoman monimutkaisuuden lisääminen ja jotta verkkoyhteyden luvaton luonne ei vaarantuisi. Tämä uusi P2P-siirtoprotokolla tarjoaa kuitenkin paremman suojan passiivisia hyökkäyksiä vastaan ja tekee aktiivisista hyökkäyksistä huomattavasti kalliimpia ja helpommin havaittavia (erityisesti MITM-hyökkäykset). Pseudosattumanvaraisen tietovirran käyttöönotto vaikeuttaa niiden hyökkääjien työtä, jotka haluavat sensuroida tai manipuloida viestintää.

P2P Transport V2 sisällytettiin vaihtoehtona (oletusarvoisesti pois käytöstä) Bitcoin Coren versioon 26.0, joka otettiin käyttöön joulukuussa 2023. Se voidaan aktivoida konfiguraatiotiedoston `v2transport=1`-vaihtoehdolla.