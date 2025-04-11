---
term: DIFFICULTY

---
Reguleeritav parameeter, mis määrab uue ploki lisamiseks plokiahelasse ja sellega seotud tasu teenimiseks vajaliku töö tõestamise keerukuse. Seda raskust esindab raskuse sihtmärk, mis on 256-bitine väärtus, mis määrab ülemise piiri, millele ploki päise hash peab vastama, et seda saaks pidada kehtivaks. Eesmärk on, et SHA256 (SHA256d) kahekordse täitmisega saavutatud hash oleks väiksem või võrdne selle sihtarvuga. Selle hashi saavutamiseks manipuleerivad kaevandajad ploki päises olevat `nonce`. Raskusastet kohandatakse iga 2016 ploki järel ehk umbes iga kahe nädala tagant, et keskmine ploki loomise aeg oleks umbes 10 minutit.