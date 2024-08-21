---
term: NODE
---

Bitcoin võrgustikus on node (või "node" inglise keeles) arvuti, mis käitab Bitcoin protokolli klienti (näiteks Bitcoin Core). See osaleb võrgustikus, hoides blockchaini koopiat, edastades ja kontrollides tehinguid ning uusi plokke ja vajadusel osaledes kaevandamisprotsessis. Kõikide Bitcoin node'ide summa esindab Bitcoin võrgustikku ennast.

Bitcoinis on mitut tüüpi node'e, sealhulgas täisnode'id ja kergnode'id. Täisnode'id hoiavad blockchaini täielikku koopiat, kontrollivad kõiki tehinguid ja plokke vastavalt konsensuse reeglitele ning osalevad aktiivselt tehingute ja plokkide levitamises võrgustikus. Teisest küljest, kergnode'id ehk SPV (*Simple Payment Verification*) node'id, hoiavad ainult plokkide päiseid ja sõltuvad täisnode'idest tehinguinfo saamiseks.

> ► *Mõned teevad vahet ka nn "kärbitud node'idel" ("pruned node" inglise keeles). Need on täisnode'id, mis laadivad alla ja kontrollivad kõiki plokke alates Genesis plokist, kuid hoiavad mälus ainult kõige uuemaid plokke.*