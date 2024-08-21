---
term: PEER DISCOVERY
---

Protsess, mille käigus sõlmed Bitcoin'i võrgus ühenduvad teiste sõlmedega, et saada informatsiooni. Kui Bitcoin'i sõlm käivitatakse esimest korda, ei ole tal teavet teiste võrgus olevate sõlmede kohta. Siiski peab ta looma ühendused, et sünkroniseerida end blockchainiga, mis omab kõige rohkem kogunenud tööd. Selleks, et avastada neid partnereid, kasutatakse mitmeid mehhanisme, prioriteetsuse järjekorras:
* Sõlm alustab oma kohaliku `peers.dat` faili konsulteerimisest, mis salvestab informatsiooni sõlmede kohta, millega see on varem suhelnud. Kui sõlm on uus, siis see fail on tühi ja protsess liigub järgmise sammu juurde;
* Kui `peers.dat` failis informatsiooni ei ole (mis on tavaline äsja käivitatud sõlme puhul), teeb sõlm DNS päringuid DNS seemnetele. Need serverid pakuvad nimekirja IP aadressidest eeldatavalt aktiivsetest sõlmedest, et luua ühendusi. DNS seemnete aadressid on kõvakooditud Bitcoin Core koodi. See samm on tavaliselt piisav, et lõpetada partnerite avastamine;
* Kui DNS seemned ei vasta 60 sekundi jooksul, võib sõlm pöörduda seemnesõlmede poole. Need on avalikud Bitcoin'i sõlmed, mis on loetletud staatilises nimekirjas peaaegu tuhande kirjega, mis on otse integreeritud Bitcoin Core lähtekoodi. Uus sõlm kasutab seda nimekirja, et luua esimene ühendus võrguga ja saada teiste sõlmede IP aadresse;
* Väga ebatõenäolisel juhul, kui kõik eelnevad meetodid ebaõnnestuvad, on sõlmeoperaatoril alati võimalus käsitsi lisada sõlmede IP aadresse, et luua esimene ühendus.