---
term: UNIX ZEIT

---
Die Unix-Zeit oder der Unix-Zeitstempel gibt die Anzahl der Sekunden an, die seit dem 1. Januar 1970 um Mitternacht UTC (Unix-Epoche) verstrichen sind. Dieses System wird in Unix-Betriebssystemen und Derivaten verwendet, um die Zeit in einer universellen und standardisierten Weise zu kennzeichnen. Es ermöglicht die Synchronisierung von Uhren und die Verwaltung von zeitbasierten Ereignissen, unabhängig von Zeitzonen.

Im Kontext von Bitcoin wird sie für die lokale Uhr der Knoten und damit für die Berechnung der NAT (Network-Adjusted Time) verwendet. Die netzwerkbereinigte Zeit ist ein Median der von jedem Knoten lokal berechneten Knotenzeiten, und diese Referenz wird dann verwendet, um die Gültigkeit von Blockzeitstempeln zu überprüfen. Damit ein Block von einem Knoten akzeptiert wird, muss sein Zeitstempel zwischen der MTP (Median Time Past der letzten 11 geminten Blöcke) und der NAT plus 2 Stunden liegen:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time wird auch verwendet, um Timelocks zu erstellen, wenn diese auf Echtzeit und nicht auf einer Anzahl von Blöcken basieren.