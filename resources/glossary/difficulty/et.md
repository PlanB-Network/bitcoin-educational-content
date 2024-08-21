---
term: RASKUSASTE
---

Reguleeritav parameeter, mis määrab töötõendi (proof of work) keerukuse, mis on vajalik uue ploki lisamiseks plokiahelasse ja sellega seotud tasu teenimiseks. See raskusaste esindab raskustaset, 256-bitist väärtust, mis seab ülemise piiri, millele ploki päise räsi peab vastama, et seda kehtivaks pidada. Eesmärk on, et räsi, mis saavutatakse SHA256 topeltrakendusega (SHA256d), oleks väiksem või võrdne selle sihtmärgiga. Selle räsi saavutamiseks manipuleerivad kaevurid ploki päises oleva `nonce` väärtusega. Raskusastme kohandamine toimub iga 2016 ploki järel, või umbes iga kahe nädala tagant, et hoida keskmist ploki loomise aega umbes 10 minuti juures.