---
term: BIP383
---

Tutvustab deskriptorites mitmeallkirjade skriptide kirjeldamiseks funktsioone `multi(NUM, KEY, ..., KEY)` ja `sortedmulti(NUM, KEY, ..., KEY)`. Need funktsioonid võimaldavad kirjeldada mitmeallkirjade skripte deskriptorites, kusjuures `sortedmulti` sorteerib avalikud võtmed leksikograafilises järjekorras, et tagada importimisel ühilduvus. BIP383 implementeeriti koos kõigi teiste deskriptoritega seotud BIP-dega (välja arvatud BIP386) Bitcoin Core versioonis 0.17.