---
term: HORODATAGE
---

Zeitstempeln, oder "Timestamp" auf Englisch, ist ein Mechanismus, um ein Ereignis, Daten oder eine Nachricht mit einer genauen Zeitmarke zu versehen. Im allgemeinen Kontext von Computersystemen wird Zeitstempelung verwendet, um die chronologische Reihenfolge von Operationen zu bestimmen und die Integrität von Daten im Laufe der Zeit zu überprüfen.


Im speziellen Fall von Bitcoin werden Zeitstempel verwendet, um die Chronologie von Transaktionen und Blöcken zu erstellen. Jeder Block in Blockchain enthält einen Timestamp, der den ungefähren Zeitpunkt seiner Erstellung angibt. Satoshi Nakamoto spricht in seinem Weißbuch sogar von einem "Timestamp-Server", um zu beschreiben, was wir heute als "Blockchain" bezeichnen würden. Die Aufgabe des Zeitstempels auf Bitcoin besteht darin, die Chronologie der Transaktionen zu bestimmen, so dass ohne das Eingreifen einer zentralen Behörde festgestellt werden kann, welche Transaktion zuerst eingetroffen ist. Dieser Mechanismus ermöglicht es jedem Nutzer, das Nichtvorhandensein einer Transaktion in der Vergangenheit zu überprüfen und somit zu verhindern, dass ein böswilliger Nutzer eine doppelte Ausgabe tätigt. Dieser Mechanismus wird von Satoshi Nakamoto in seinem White Paper mit dem berühmten Satz begründet: "*Dieser Standard basiert auf der Unix-Zeit, die die Gesamtzahl der seit dem 1. Januar 1970 vergangenen Sekunden darstellt.


> ► *Die Zeitstempel der Blöcke sind bei Bitcoin relativ flexibel, da ein Timestamp nur dann als gültig angesehen wird, wenn er größer ist als der Median der 11 vorangegangenen Blöcke (MTP) und kleiner als der Median der von den Knoten zurückgegebenen Zeiten (netzbereinigte Zeit) plus 2 Stunden