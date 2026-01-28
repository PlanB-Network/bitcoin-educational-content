---
term: Gossip
definition: P2P protokol za širenje informacija između čvorova na epidemičan način.
---

Trač je peer-to-peer (P2P) distribuirani algoritam za širenje informacija epidemijski svim agentima mreže. Za Bitcoin, Lightning i druge distribuirane sisteme, ovaj protokol omogućava Global State čvorova da budu razmenjeni i sinhronizovani u samo nekoliko ciklusa. Svaki čvor propagira informacije jednom ili više slučajnih ili neslučajnih suseda, koji zatim propagiraju informacije drugim susedima, i tako dalje, dok se ne postigne globalno sinhronizovano stanje.


U Lightning-u, trač je komunikacioni protokol između čvorova za deljenje informacija o trenutnom stanju i topologiji mreže. Protokol trača omogućava čvorovima da znaju dinamičko stanje kanala plaćanja i drugih čvorova, kako bi olakšali rutiranje transakcija preko mreže bez potrebe za direktnim vezama između svih čvorova.


