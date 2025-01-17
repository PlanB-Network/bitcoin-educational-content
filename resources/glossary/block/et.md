---
term: BLOCK

---
Bitcoini süsteemi andmestruktuur. Plokk sisaldab kehtivate tehingute ja metaandmete kogumit, mis sisaldub selle päises. Iga plokk on seotud järgmise plokiga selle päise kaudu, moodustades seega plokiahelat. Plokiahel toimib ajamärgistusserverina, mis võimaldab igal kasutajal teada kõiki varasemaid tehinguid, et kontrollida tehingu mitteolemasolu ja vältida topeltkulutusi. Tehingud on korraldatud Merkle-puuna. See krüptograafiline akumulaator võimaldab koostada kõigi ploki tehingute digesti, mida nimetatakse "Merkle'i juureks" Ploki päis sisaldab 6 elementi:


- Ploki versioon;
- Eelmise ploki jäljend;
- Tehingute Merkle'i puu juur;
- Ploki ajatempel;
- Raskuse sihtmärk;
- Nonce.

Selleks, et plokk oleks kehtiv, peab sellel olema päis, mis pärast "SHA256d"-ga hashimist annab tulemuseks digesti, mis on väiksem või võrdne raskuse sihtarvuga.