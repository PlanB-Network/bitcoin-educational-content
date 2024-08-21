---
term: TEHINGUSTANDARD
---

Bitcoin'i tehing, mis lisaks konsensuse reeglitele järgimisele kuulub ka Bitcoin Core sõlmede vaikimisi seatud standardiseerimisreeglite alla. Need standardiseerimisreeglid kehtestatakse individuaalselt iga Bitcoin'i sõlme poolt, lisaks konsensuse reeglitele, et määratleda kinnitamata tehingute struktuuri, mida see oma mempool'is aktsepteerib ja oma eakaaslastele edastab.

Need reeglid seega konfigureeritakse ja täidetakse lokaalselt iga sõlme poolt ning võivad ühest sõlmest teise erineda. Need kehtivad ainult kinnitamata tehingutele. Seetõttu aktsepteerib sõlm tehingut, mida ta peab mittestandardseks, ainult siis, kui see on juba kehtivas plokis.

On märgitud, et enamik sõlmi jätab vaikeseaded nii, nagu need on Bitcoin Core'is kehtestatud, luues seeläbi võrgus standardiseerimisreeglite ühtsuse. Tehing, mis kuigi on kooskõlas konsensuse reeglitega, ei austata neid standardiseerimisreegleid, võib võrgus levimisel raskusi kohata. Siiski võib see siiski olla kaasatud kehtivasse plokki, kui see jõuab kaevandajani. Praktikas edastatakse sellised tehingud, mida kvalifitseeritakse mittestandardsetena, sageli otse kaevandajale välisvahendite kaudu, mis on väljaspool Bitcoin'i võrdõiguslikku võrku. See on sageli ainus viis sellise tehingu kinnitamiseks. Näiteks tehing, mis ei eralda tasusid, on nii konsensuse reeglite kohaselt kehtiv kui ka mittestandardne, kuna Bitcoin Core'i vaikimisi poliitika `minRelayTxFee` parameetri jaoks on `0.00001` (BTC/kB kohta).