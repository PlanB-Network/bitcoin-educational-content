---
term: P2P TRANSPORT V2

---
Neue Version des Bitcoin-P2P-Transportprotokolls mit opportunistischer Verschlüsselung zur Verbesserung der Privatsphäre und der Sicherheit der Kommunikation zwischen den Knotenpunkten. Diese Verbesserung zielt darauf ab, mehrere Probleme mit der Basisversion des P2P-Protokolls zu beheben, insbesondere indem die ausgetauschten Daten für einen passiven Beobachter (z. B. einen Internetdienstanbieter) ununterscheidbar gemacht werden, wodurch die Risiken von Zensur und Angriffen durch die Erkennung bestimmter Muster in Datenpaketen verringert werden.

Die implementierte Verschlüsselung beinhaltet keine Authentifizierung, um unnötige Komplexität zu vermeiden und den erlaubnisfreien Charakter der Netzverbindung nicht zu gefährden. Dieses neue P2P-Transportprotokoll bietet dennoch eine bessere Sicherheit gegen passive Angriffe und macht aktive Angriffe deutlich kostspieliger und aufspürbarer (insbesondere MITM-Angriffe). Die Einführung eines pseudozufälligen Datenstroms erschwert Angreifern, die die Kommunikation zensieren oder manipulieren wollen, die Arbeit.

Der P2P-Transport V2 wurde als Option (standardmäßig deaktiviert) in Version 26.0 von Bitcoin Core aufgenommen, die im Dezember 2023 bereitgestellt wurde. Er kann mit der Option `v2transport=1` in der Konfigurationsdatei aktiviert werden.