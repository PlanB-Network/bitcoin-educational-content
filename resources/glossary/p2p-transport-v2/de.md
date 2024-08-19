---
term: P2P TRANSPORT V2
---

Neue Version des Bitcoin P2P-Transportprotokolls, das opportunistische Verschlüsselung integriert, um die Privatsphäre und Sicherheit der Kommunikation zwischen Knoten zu verbessern. Diese Verbesserung zielt darauf ab, mehrere Probleme mit der Basisversion des P2P-Protokolls zu adressieren, insbesondere indem die ausgetauschten Daten für einen passiven Beobachter (wie einen Internetdienstanbieter) ununterscheidbar gemacht werden, wodurch die Risiken von Zensur und Angriffen durch die Erkennung spezifischer Muster in Datenpaketen reduziert werden.

Die implementierte Verschlüsselung beinhaltet keine Authentifizierung, um unnötige Komplexität zu vermeiden und die erlaubnisfreie Natur der Netzwerkverbindung nicht zu kompromittieren. Dieses neue P2P-Transportprotokoll bietet dennoch eine bessere Sicherheit gegen passive Angriffe und macht aktive Angriffe deutlich kostspieliger und erkennbarer (insbesondere MITM-Angriffe). Die Einführung eines pseudo-zufälligen Datenstroms erschwert Angreifern die Aufgabe, Kommunikation zu zensieren oder zu manipulieren.

Der P2P Transport V2 wurde als Option (standardmäßig deaktiviert) in Version 26.0 von Bitcoin Core, die im Dezember 2023 eingeführt wurde, inkludiert. Er kann mit der Option `v2transport=1` in der Konfigurationsdatei aktiviert werden.