---
term: DERIVATION

---
Viitab protsessile, mille käigus genereeritakse lapsvõtmepaarid vanemvõtmepaarist (isiklik võti ja avalik võti) ja ahelakoodist deterministlikus ja hierarhilises (HD) rahakotis. See protsess võimaldab harude segmenteerimist ja rahakoti organiseerimist eri tasanditeks koos arvukate lapsvõtmepaaridega, mida kõiki saab taastada, teades ainult põhilist taastamisinfot (mnemofraasi ja võimalikku salasõna). Lapsvõtme tuletamiseks kasutatakse funktsiooni `HMAC-SHA512` koos vanemvõtme ahelakoodi ja vanemvõtme ja 32-bitise indeksi ahelaga. On olemas kahte tüüpi tuletusi:


- Tavaline tuletamine, mis kasutab vanemate avalikku võtit `HMAC-SHA512`-funktsiooni alusena;
- Karastatud tuletamine, mis kasutab vanemate privaatvõtit `HMAC-SHA512`-funktsiooni alusena;

HMAC-SHA512 tulemus jagatakse kaheks: esimesed 256 bitti saavad lapsvõtmeks (privaatne või avalik pärast ECDSA töötlemist) ja ülejäänud 256 bitti saavad lapsahela koodiks.