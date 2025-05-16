---
term: BATERIJA
---

U kontekstu skriptnog jezika koji se koristi za postavljanje uslova trošenja na Bitcoin UTXO-e, stek je LIFO (*Last In, First Out*) struktura podataka koja se koristi za privremeno skladištenje Elements tokom izvršavanja skripte. Svaka operacija u skripti manipuliše ovim stekovima, gde se Elements može dodati (*push*) ili ukloniti (*pop*). Skripte koriste stekove za evaluaciju izraza, skladištenje privremenih varijabli i upravljanje uslovima.


Kada se izvršava Bitcoin skripta, mogu se koristiti 2 steka: glavni stek i alt (alternativni) stek. Glavni stek se koristi za većinu operacija skripte. Na ovom steku operacije skripte dodaju, uklanjaju ili manipulišu podacima. Alternativni stek, s druge strane, koristi se za privremeno skladištenje podataka tokom izvršavanja skripte. Specifični opkodovi, kao što su `OP_TOALTSTACK` i `OP_FROMALTSTACK`, omogućavaju vam da prenesete Elements sa glavnog steka na alternativni stek i obrnuto.


Na primer, kada je transakcija validirana, potpisi i javni ključevi se postavljaju na glavnu stek i obrađuju sukcesivnim opkodovima kako bi se verifikovalo da potpisi odgovaraju ključevima i podacima transakcije.