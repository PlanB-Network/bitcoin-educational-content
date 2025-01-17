---
term: TIMELOCK

---
Aruka lepingu primitiiv, mis võimaldab määrata ajapõhise tingimuse, mis peab olema täidetud, et tehing saaks plokki lisada. Bitcoinis on kahte tüüpi ajamääranguid:


- Absoluutne ajalukk, mis määrab täpse hetke, enne mida tehingut ei saa blokki lisada;
- Suhteline ajalukk, mis määrab viivituse eelmise tehingu aktsepteerimisest.

Ajaluku saab määratleda kas Unixi ajas väljendatud kuupäevana või plokkide numbrina. Lõpuks võib ajalukk kehtida tehingu väljundile, kasutades lukustusskriptis konkreetset opkoodi (`OP_CHECKLOCKTIMEVERIFY` või `OP_CHECKSEQUENCEVERIFY`) või kogu tehingule, kasutades konkreetseid tehinguvälju (`nLockTime` või `nSequence`).