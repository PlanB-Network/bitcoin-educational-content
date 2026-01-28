---
term: Mempool
definition: Utrymme där transaktioner som väntar på att inkluderas i ett block lagras av varje nod.
---

En sammandragning av termerna "memory" och "pool". Detta hänvisar till ett virtuellt utrymme där Bitcoin-transaktioner som väntar på att inkluderas i ett block grupperas tillsammans. När en transaktion skapas och sänds ut i Bitcoin-nätverket verifieras den först av nätverkets noder. Om den anses giltig placeras den sedan i Mempool i varje nod, där den ligger kvar tills den väljs av en Miner för att ingå i ett block.


Det är viktigt att notera att varje nod i Bitcoin-nätverket upprätthåller sin egen Mempool, och därför kan det finnas variationer i innehållet i Mempool mellan olika noder vid varje given tidpunkt. Parametern `maxmempool` i filen `Bitcoin.conf` för varje nod gör det möjligt för operatörerna att kontrollera mängden RAM (random access memory) som deras nod kommer att använda för att lagra väntande transaktioner i Mempool. Genom att begränsa storleken på Mempool kan nodoperatörer förhindra att den förbrukar för mycket resurser i systemet. Denna parameter anges i megabyte (MB). Standardvärdet för Bitcoin Core hittills är 300 MB.


Transaktioner som finns i Mempool är preliminära. De bör inte betraktas som oföränderliga förrän de ingår i ett block och efter ett visst antal bekräftelser. Dessa kan ofta ersättas eller rensas bort.