---
term: Nätverksjusterad tid (NAT)
definition: Uppskattning av universell tid baserad på medianen av klockorna hos nätverksnoderna.
---

Uppskattning av den universella tid som fastställts på nätverksnodernas klockor. Varje nod beräknar sin NAT genom att ta medianen av tidsskillnaderna mellan sin lokala klocka (UTC) och de noder som den är ansluten till, och sedan lägga till sin lokala klocka till medianen av dessa skillnader, upp till maximalt 70 minuter. Den nätverksjusterade tiden är därför en median av de nodtider som beräknas lokalt av varje nod. Denna referensram används sedan för att verifiera giltigheten hos blockens tidsstämplar. För att ett block ska accepteras av en nod måste dess Timestamp ligga mellan MTP (mediantiden för de senaste 11 blocken) och NAT plus 2 timmar:


```text
MTP < Valid Timestamp < (NAT + 2h)
```