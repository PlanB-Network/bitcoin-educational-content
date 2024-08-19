---
term: NETWORK-ADJUSTED TIME (NAT)
---

Schätzung der universellen Zeit, die auf den Uhren der Netzwerkknoten basiert. Jeder Knoten berechnet seine NAT, indem er den Median der Zeitunterschiede zwischen seiner lokalen Uhr (UTC) und denen der Knoten, mit denen er verbunden ist, nimmt und dann seine lokale Uhrzeit zu dem Median dieser Unterschiede addiert, bis zu einem Maximum von 70 Minuten. Die netzwerkangepasste Zeit ist daher ein Median der lokal von jedem Knoten berechneten Knotenzeiten. Dieser Bezugsrahmen wird dann verwendet, um die Gültigkeit der Block-Zeitstempel zu überprüfen. Tatsächlich muss, damit ein Block von einem Knoten akzeptiert wird, sein Zeitstempel zwischen dem MTP (Medianzeit der letzten 11 abgebauten Blöcke) und der NAT plus 2 Stunden liegen:

```text
MTP < Gültiger Zeitstempel < (NAT + 2h)
```