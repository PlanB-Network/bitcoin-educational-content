---
term: Standardtransaktion
definition: Transaktion som respekterar både konsensusregler och de förinställda standardiseringsreglerna för Bitcoin Core-noder.
---

En Bitcoin-transaktion som, utöver att följa konsensusreglerna, även faller inom standardiseringsreglerna som är standardinställda på Bitcoin Core-noder. Dessa standardiseringsregler införs individuellt av varje Bitcoin-nod, utöver konsensusreglerna, för att definiera strukturen för obekräftade transaktioner som den accepterar i sin Mempool och sänder till sina peers.


Dessa regler konfigureras och verkställs således lokalt av varje nod och kan variera från en nod till en annan. De gäller uteslutande obekräftade transaktioner. En nod kommer därför endast att acceptera en transaktion som den anser vara icke-standardiserad om den redan ingår i ett giltigt block.


Det noteras att majoriteten av noderna lämnar de standardkonfigurationer som fastställts i Bitcoin Core, vilket skapar en enhetlighet i standardiseringsreglerna över hela nätverket. En transaktion som, trots att den följer konsensusreglerna, inte respekterar dessa standardiseringsregler kommer att ha svårt att spridas genom nätverket. Den kan dock fortfarande ingå i ett giltigt block om den når en Miner. I praktiken överförs dessa transaktioner, som kvalificeras som icke-standardiserade, ofta direkt till en Miner via externa medel till Bitcoin:s peer-to-peer-nätverk. Detta är ofta det enda sättet att bekräfta en sådan transaktion. Till exempel är en transaktion som inte tilldelar några avgifter både giltig enligt konsensusreglerna och icke-standard, eftersom standardpolicyn för Bitcoin Core för parametern "minRelayTxFee" är "0,00001" (i BTC/kB).