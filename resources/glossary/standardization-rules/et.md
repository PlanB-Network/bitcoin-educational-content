---
term: STANDARDISEERIMISE REEGLID
---

Standardiseerimise reeglid võetakse individuaalselt vastu iga Bitcoin'i sõlme poolt, lisaks konsensuse reeglitele, et määratleda kinnitamata tehingute struktuuri, mida see aktsepteerib oma mempool'i ja edastab oma eakaaslastele. Seega konfigureeritakse ja täidetakse neid reegleid kohalikult iga sõlme poolt ja need võivad erineda sõlmelt sõlmele. Need kehtivad ainult kinnitamata tehingutele. Seetõttu aktsepteerib sõlm tehingut, mida ta peab mittestandardseks, ainult juhul, kui see on juba kaasatud kehtivasse plokki.

On märgitud, et enamik sõlmi jätab vaikimisi konfiguratsioonid, nagu need on kehtestatud Bitcoin Core'is, luues seeläbi võrgus standardiseerimise reeglite ühtsuse. Tehing, mis kuigi on kooskõlas konsensuse reeglitega, ei järgi neid standardiseerimise reegleid, võib kogeda raskusi levimisel võrgus. Siiski võib see siiski olla kaasatud kehtivasse plokki, kui see jõuab kaevandajani. Praktikas edastatakse neid tehinguid, mida nimetatakse "mittestandardseteks", sageli otse kaevandajale välisvahendite kaudu, mis asuvad väljaspool Bitcoin'i võrdõigusvõrgustikku. See on sageli ainus viis sellist tüüpi tehingu kinnitamiseks.

Näiteks tehing, mis ei eralda tasusid, on nii kehtiv vastavalt konsensuse reeglitele kui ka mittestandardne, kuna Bitcoin Core'i vaikimisi poliitika `minRelayTxFee` parameetri jaoks on `0.00001` (BTC/kB kohta).

> ► *Terminit "mempooli reeglid" kasutatakse mõnikord ka standardiseerimise reeglitele viitamiseks.*