---
term: UTREEXO
---

Protokoll, mille on välja töötanud Tadge Dryja, et tihendada Bitcoin'i sõlmede UTXO komplekti, kasutades akumulaatorit, mis põhineb Merkle'i puudel. Erinevalt klassikalisest UTXO komplektist, mis nõuab olulist salvestusruumi, vähendab Utreexo mälu vajadust drastiliselt, säilitades ainult Merkle'i puude juured. See võimaldab sõlmel kontrollida tehingu sisendites kasutatavate UTXO-de olemasolu, ilma et peaks hoidma kogu UTXO komplekti. Utreexo kasutamisel säilitab iga sõlm ainult krüptograafilist sõrmejälge, mida nimetatakse Merkle'i juureks. Kui tehing tehakse, esitab kasutaja UTXO-de omandiõiguse tõendid ja vastavad Merkle'i teed. Seega saab sõlm tehinguid kontrollida, ilma et peaks säilitama terve UTXO komplekti. Vaatame näidet diagrammiga, et mõista seda mehhanismi:

![](../../dictionnaire/assets/15.png)

Selles näites vähendasin ma tahtlikult UTXO komplekti 4 UTXO-le, et hõlbustada mõistmist. Tegelikkuses on oluline ette kujutada, et kirjutamise hetkel on Bitcoinis peaaegu 140 miljonit UTXO-d. Selles diagrammis peaks Utreexo sõlm säilitama ainult Merkle'i juure RAM-is. Kui see saab tehingu, mis kulutab UTXO nr 3 (mustas), koosneks tõend järgmistest elementidest:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Selle tehingu saatja poolt edastatud teabega teostab Utreexo sõlm järgmised kontrollid:
* See arvutab UTXO 3 jäljendi, mis annab talle HASH 3;
* See ühendab HASH 3 HASH 4-ga;
* See arvutab nende jäljendi, mis annab talle HASH 3-4;
* See ühendab HASH 3-4 HASH 1-2-ga;
* See arvutab nende jäljendi, mis annab talle Merkle'i juure.

Kui Merkle'i juur, mille ta oma protsessi kaudu saab, on sama mis Merkle'i juur, mille ta on oma RAM-is säilitanud, siis on ta veendunud, et UTXO nr 3 on tõepoolest osa UTXO komplektist.
See meetod vähendab täissõlme operaatorite RAM-i nõudmisi. Siiski on Utreexol piiranguid, sealhulgas bloki suuruse suurenemine täiendavate tõendite tõttu ja Utreexo sõlmede potentsiaalne sõltuvus Bridge Nodes'ist, et saada puuduvaid tõendeid. Bridge Nodes on traditsioonilised täissõlmed, mis pakuvad vajalikke tõendeid Utreexo sõlmedele, võimaldades seeläbi täielikku kontrolli. See lähenemine pakub kompromissi efektiivsuse ja detsentraliseerituse vahel, muutes tehingute valideerimise kättesaadavamaks piiratud ressurssidega kasutajatele.