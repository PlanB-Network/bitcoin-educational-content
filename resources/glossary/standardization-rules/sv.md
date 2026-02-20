---
term: Standardiseringsregler
definition: Lokala regler som definierar strukturen för obekräftade transaktioner som en nod accepterar i sin mempool.
---

Standardiseringsregler antas individuellt av varje Bitcoin-nod, utöver konsensusreglerna, för att definiera strukturen för obekräftade transaktioner som den accepterar i sin Mempool och sänder till sina peers. Dessa regler konfigureras och verkställs således lokalt av varje nod och kan variera från en nod till en annan. De gäller uteslutande obekräftade transaktioner. Därför kommer en nod endast att acceptera en transaktion som den anser vara icke-standardiserad om den redan ingår i ett giltigt block.


Det noteras att majoriteten av noderna lämnar de standardkonfigurationer som fastställts i Bitcoin Core, vilket skapar en enhetlighet i standardiseringsreglerna över hela nätverket. En transaktion som, trots att den följer konsensusreglerna, inte följer dessa standardiseringsregler kommer att ha svårt att sändas över nätverket. Den kan dock fortfarande ingå i ett giltigt block om den når en Miner. I praktiken överförs dessa transaktioner, som kallas "icke-standard", ofta direkt till en Miner via externa medel utanför Bitcoin:s peer-to-peer-nätverk. Detta är ofta det enda sättet att bekräfta den här typen av transaktioner.


Till exempel är en transaktion som inte fördelar några avgifter både giltig enligt konsensusreglerna och icke-standard eftersom standardpolicyn för Bitcoin Core för parametern "minRelayTxFee" är "0,00001" (i BTC/kB).


> ► *Termen "Mempool-regler" används ibland också för att hänvisa till standardiseringsreglerna*