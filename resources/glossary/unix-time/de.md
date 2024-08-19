---
term: UNIX TIME
---

Unix-Zeit oder Unix-Zeitstempel repräsentiert die Anzahl der Sekunden, die seit dem 1. Januar 1970 um Mitternacht UTC (Unix-Epoche) vergangen sind. Dieses System wird in Unix-Betriebssystemen und deren Ablegern verwendet, um Zeit auf eine universelle und standardisierte Weise zu markieren. Es ermöglicht die Synchronisation von Uhren und die Verwaltung von zeitbasierten Ereignissen, unabhängig von Zeitzone.

Im Kontext von Bitcoin wird es für die lokale Uhr der Knoten verwendet und somit für die Berechnung der NAT (Network-Adjusted Time). Die netzwerkangepasste Zeit ist ein Median der lokal von jedem Knoten berechneten Zeiten, und dieser Bezugspunkt wird dann verwendet, um die Gültigkeit von Block-Zeitstempeln zu überprüfen. Tatsächlich muss für die Akzeptanz eines Blocks durch einen Knoten sein Zeitstempel zwischen dem MTP (Median Time Past der letzten 11 abgebauten Blöcke) und der NAT plus 2 Stunden liegen:

```text
MTP < Gültiger Zeitstempel < (NAT + 2h)
```

Unix-Zeit wird auch verwendet, um Zeitverriegelungen zu etablieren, wenn diese auf der realen Zeit basieren, anstatt auf einer Anzahl von Blöcken.