---
term: NETZBEREINIGTE ZEIT (NAT)

---
Schätzung der Weltzeit, die anhand der Uhren der Netzknoten ermittelt wird. Jeder Knoten berechnet seine NAT, indem er den Median der Zeitdifferenzen zwischen seiner lokalen Uhr (UTC) und denen der Knoten, mit denen er verbunden ist, nimmt und dann seine lokale Uhr zum Median dieser Differenzen addiert, bis zu einem Maximum von 70 Minuten. Die netzbereinigte Zeit ist also ein Median der von jedem Knoten lokal berechneten Zeiten. Dieser Bezugsrahmen wird dann verwendet, um die Gültigkeit der Zeitstempel der Blöcke zu überprüfen. Damit ein Block von einem Knoten akzeptiert wird, muss sein Zeitstempel zwischen der MTP (Medianzeit der letzten 11 abgebauten Blöcke) und der NAT plus 2 Stunden liegen:

```text
MTP < Valid Timestamp < (NAT + 2h)
```