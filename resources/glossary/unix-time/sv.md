---
term: Unixtid
definition: Antal sekunder som förflutit sedan den 1 januari 1970 vid midnatt UTC, används för tidshantering på Bitcoin.
---

Unix Time eller Unix Timestamp representerar antalet sekunder som har förflutit sedan den 1 januari 1970 vid midnatt UTC (Unix Epoch). Detta system används i Unix operativsystem och derivat för att markera tid på ett universellt och standardiserat sätt. Det möjliggör synkronisering av klockor och hantering av tidsbaserade händelser, oberoende av tidszoner.


I samband med Bitcoin används den för nodernas lokala klocka och därmed för beräkning av NAT (Network-Adjusted Time). Den nätverksjusterade tiden är en median av de nodtider som beräknas lokalt av varje nod, och denna referens används sedan för att verifiera giltigheten hos blockets tidsstämplar. För att ett block ska accepteras av en nod måste dess Timestamp ligga mellan MTP (Median Time Past för de senaste 11 minade blocken) och NAT plus 2 timmar:


```text
MTP < Valid Timestamp < (NAT + 2h)
```


Unix Time används också för att skapa tidslås när de baseras på realtid, snarare än på ett antal block.