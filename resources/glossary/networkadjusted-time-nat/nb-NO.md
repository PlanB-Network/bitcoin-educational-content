---
term: NETTVERKSJUSTERT TID (NAT)

---
Estimering av universell tid basert på klokkene til nettverksnodene. Hver node beregner sin NAT ved å ta medianen av tidsforskjellene mellom sin lokale klokke (UTC) og klokkene til nodene den er koblet til, og deretter legge sin lokale klokke til medianen av disse forskjellene, opp til maksimalt 70 minutter. Den nettverksjusterte tiden er derfor en median av node-tidene som beregnes lokalt av hver node. Denne referanserammen brukes deretter til å verifisere gyldigheten av blokkenes tidsstempler. For at en blokk skal bli akseptert av en node, må tidsstempelet ligge mellom MTP (mediantiden for de siste 11 utvunnede blokkene) og NAT pluss 2 timer:

```text
MTP < Valid Timestamp < (NAT + 2h)
```