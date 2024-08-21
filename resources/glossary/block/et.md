---
term: BLOKK
---

Andmestruktuur Bitcoin süsteemis. Blokk sisaldab kehtivate tehingute kogumit ja metateavet, mis on sisaldunud selle päises. Iga blokk on järgmisega ühendatud oma päise räsi kaudu, moodustades seeläbi plokiahela. Plokiahel toimib ajatempli serverina, mis võimaldab igal kasutajal teada kõiki minevikutehinguid, et kontrollida tehingu puudumist ja vältida topeltkulutamist. Tehingud on organiseeritud Merkle puusse. See krüptograafiline akumulaator võimaldab toota kõikide bloki tehingute kokkuvõtte, mida nimetatakse "Merkle juureks". Bloki päis sisaldab 6 elementi:
* Bloki versioon;
* Eelmise bloki jäljend;
* Tehingute Merkle puu juur;
* Bloki ajatempel;
* Raskusaste;
* Nonce.

Bloki kehtivuseks peab sellel olema päis, mis, kui seda räsida `SHA256d` abil, toodab kokkuvõtte, mis on väiksem või võrdne raskusastmega.