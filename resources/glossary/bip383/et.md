---
term: BIP383

---
Võtab kasutusele funktsioonid `multi(NUM, KEY, ..., KEY)` ja `sortedmulti(NUM, KEY, ..., KEY)` kirjeldajate jaoks. Need funktsioonid võimaldavad kirjeldustes kirjeldada mitme allkirjaga skripte, kusjuures `sortedmulti` sorteerib avalikud võtmed leksikograafilises järjekorras, et tagada ühilduvus importimisel. BIP383 rakendati koos kõigi teiste deskriptoritega seotud BIP-dega (välja arvatud BIP386) Bitcoin Core'i versioonis 0.17.