---
term: MTP (MEDIAN TIME PAST)
---

See kontseptsioon on kasutusel Bitcoin'i protokollis, et määrata võrgu konsensuse ajatemplile marginaal. MTP on defineeritud kui viimase 11 kaevandatud ploki ajatemplite mediaan. Selle näitaja kasutamine aitab vältida erimeelsusi sõlmede vahel täpse aja osas, kui esineb lahknevusi. MTP-d kasutati algselt plokkide ajatemplite kehtivuse kontrollimiseks minevikuga võrreldes. Alates BIP113-st on seda kasutatud ka võrgu aja referentsina, et kontrollida ajalukkudega tehingute (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ja `OP_CHECKSEQUENCEVERIFY`) kehtivust.