---
term: TIMELOCK
---

Nutikas lepingu primitiiv, mis võimaldab seada aja-põhise tingimuse, mis peab olema täidetud, et tehingut saaks lisada plokki. Bitcoinis on kaks tüüpi ajalukke:
* Absoluutne ajalukk, mis määrab täpse hetke, enne mida tehingut ei saa plokki lisada;
* Suhteline ajalukk, mis seab viivituse eelmise tehingu aktsepteerimisest.
Ajalukk võib olla määratletud kas kuupäevana, mis on väljendatud Unixi ajas, või ploki numbrina. Lõpuks võib ajalukk kehtida tehingu väljundi suhtes, kasutades lukustusskriptis spetsiifilist operaatorit (`OP_CHECKLOCKTIMEVERIFY` või `OP_CHECKSEQUENCEVERIFY`), või tervele tehingule, kasutades spetsiifilisi tehinguvälju (`nLockTime` või `nSequence`).