---
term: PEER DISCOVERY

---
Protsess, mille abil Bitcoini võrgu sõlmed ühenduvad teiste sõlmedega, et saada teavet. Kui Bitcoini sõlme esimest korda käivitatakse, ei ole tal teavet teiste võrgus olevate sõlmede kohta. Siiski peab ta looma ühendusi, et sünkroniseerida end selle plokiahelaga, millel on kõige rohkem kogunenud tööd. Nende eakaaslaste avastamiseks kasutatakse mitmeid mehhanisme, mis on järjestatud tähtsuse järjekorras:


- Sõlm alustab oma kohalikku faili `peers.dat`, mis sisaldab teavet sõlmede kohta, millega ta on varem suhelnud. Kui sõlm on uus, on see fail tühi ja protsess liigub järgmise sammu juurde;
- Kui failis `peers.dat` puudub teave (mis on äsja käivitatud sõlme puhul tavaline), teeb sõlme DNS päringuid DNS-seemnetele. Need serverid annavad ühenduse loomiseks eeldatavalt aktiivsete sõlmede IP-aadresside nimekirja. DNS-seemnete aadressid on Bitcoin Core'i koodis kõvakooditud. Sellest sammust piisab tavaliselt, et lõpetada partnerite leidmine;
- Kui DNS-seemned ei reageeri 60 sekundi jooksul, võib sõlme pöörduda seemnesõlmede poole. Need on avalikud Bitcoini sõlmed, mis on loetletud peaaegu tuhandest kirjest koosnevas staatilises nimekirjas, mis on integreeritud otse Bitcoin Core'i lähtekoodi. Uus sõlme kasutab seda nimekirja, et luua esimene ühendus võrguga ja saada teiste sõlmede IP-aadressid;
- Väga ebatõenäolisel juhul, kui kõik eelnevad meetodid ebaõnnestuvad, on sõlmeoperaatoril alati võimalus lisada sõlmede IP-aadressid käsitsi, et luua esimene ühendus.