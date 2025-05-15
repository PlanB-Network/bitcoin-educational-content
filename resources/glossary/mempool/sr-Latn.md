---
term: Mempool
---

Kontrakcija termina "memorija" i "bazen". Ovo se odnosi na virtuelni prostor u kojem se Bitcoin transakcije koje čekaju uključivanje u blok grupišu zajedno. Kada se transakcija kreira i emituje na Bitcoin mreži, prvo je verifikuju čvorovi mreže. Ako se smatra validnom, zatim se smešta u Mempool svakog čvora, gde ostaje dok je ne odabere Miner za uključivanje u blok.


Važno je napomenuti da svaki čvor u Bitcoin mreži održava svoj sopstveni Mempool, te stoga može doći do varijacija u sadržaju Mempool između različitih čvorova u bilo kom trenutku. Posebno, parametar `maxmempool` u `Bitcoin.conf` fajlu svakog čvora omogućava operaterima da kontrolišu količinu RAM-a (memorije sa slučajnim pristupom) koju će njihov čvor koristiti za skladištenje transakcija na čekanju u Mempool. Ograničavanjem veličine Mempool, operateri čvorova mogu sprečiti da on troši previše resursa na njihovom sistemu. Ovaj parametar je specificiran u megabajtima (MB). Podrazumevana vrednost za Bitcoin Core do danas je 300 MB.


Transakcije prisutne u Mempool su privremene. Ne treba ih smatrati nepromenljivim dok ne budu uključene u blok i nakon određenog broja potvrda. One često mogu biti zamenjene ili uklonjene.