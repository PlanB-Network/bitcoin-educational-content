---
term: UNIX TIME

---
Unix Time eller Unix Timestamp representerer antall sekunder som har gått siden 1. januar 1970, ved midnatt UTC (Unix Epoch). Dette systemet brukes i Unix-operativsystemer og -derivater for å markere tid på en universell og standardisert måte. Det gjør det mulig å synkronisere klokker og administrere tidsbaserte hendelser, uavhengig av tidssoner.

I Bitcoin-sammenheng brukes den til nodenes lokale klokke, og dermed til beregning av NAT (Network-Adjusted Time). Den nettverksjusterte tiden er en median av node-tidene som beregnes lokalt av hver node, og denne referansen brukes deretter til å verifisere gyldigheten av blokkenes tidsstempler. For at en blokk skal bli akseptert av en node, må tidsstempelet ligge mellom MTP (Median Time Past for de siste 11 utvunnede blokkene) og NAT pluss 2 timer:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time brukes også til å etablere tidslåser når de er basert på sanntid, i stedet for på et antall blokker.