---
term: UTREEXO

---
Tadge Dryja loodud protokoll Bitcoini sõlmede UTXO-komplekti tihendamiseks, kasutades Merkle'i puudel põhinevat akumulaatorit. Erinevalt klassikalisest UTXO kogumist, mis nõuab märkimisväärset salvestusruumi, vähendab Utreexo drastiliselt mäluvajadust, salvestades ainult Merkle-puu juured. See võimaldab sõlme kontrollida tehingu sisendites kasutatavate UTXOde olemasolu, ilma et ta peaks säilitama kogu UTXOde kogumit. Utreexo abil säilitab iga sõlme ainult krüptograafilise sõrmejälje, mida nimetatakse Merkle'i juureks. Tehingu tegemisel esitab kasutaja UTXOde ja vastavate Merkle'i radade omanditõendid. Seega saab sõlm kontrollida tehinguid ilma kogu UTXO-kogumit säilitamata. Võtame selle mehhanismi mõistmiseks näite koos diagrammiga:

![](../../dictionnaire/assets/15.webp)

Selles näites vähendasin ma tahtlikult UTXO-de kogumit 4 UTXO-le, et hõlbustada arusaamist. Tegelikkuses on oluline ette kujutada, et nende ridade kirjutamise ajal on Bitcoinis peaaegu 140 miljonit UTXO-d. Sellel skeemil oleks Utreexo sõlme vaja hoida RAM-is ainult Merkle Root. Kui ta saab tehingu, mis kulutab UTXO nr 3 (mustas), siis koosneks tõestus järgmistest elementidest:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Selle tehingu saatja poolt edastatud teabe põhjal teostab Utreexo sõlmpunkt järgmised kontrollid:


- See arvutab UTXO 3 jäljendi, mis annab talle HASH 3;
- See ühendab HASH 3 ja HASH 4;
- See arvutab nende jäljendi, mis annab talle HASH 3-4;
- See ühendab HASH 3-4 ja HASH 1-2;
- See arvutab nende jäljendi, mis annab talle Merkle'i juure.

Kui Merkle'i juur, mille ta oma protsessi kaudu saab, on sama, mis Merkle'i juur, mille ta on salvestanud oma mällu, siis on ta veendunud, et UTXO nr 3 on tõepoolest osa UTXO kogumist.

See meetod vähendab täieliku sõlme operaatorite RAM-vajadust. Utreexol on siiski piirangud, sealhulgas täiendavate tõendite tõttu suurenev plokimaht ja Utreexo sõlmede võimalik sõltuvus sillasõlmedest, et saada puuduvaid tõendeid. Bridge Nodes on traditsioonilised täissõlmed, mis annavad Utreexo sõlmedele vajalikud tõendid, võimaldades seega täielikku verifitseerimist. See lähenemisviis pakub kompromissi tõhususe ja detsentraliseerituse vahel, muutes tehingu valideerimise kättesaadavamaks piiratud ressurssidega kasutajatele.