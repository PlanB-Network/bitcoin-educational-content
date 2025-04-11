---
term: PEER DISCOVERY

---
Der Prozess, durch den sich Knoten im Bitcoin-Netzwerk mit anderen Knoten verbinden, um Informationen zu erhalten. Wenn ein Bitcoin-Knotenpunkt zum ersten Mal gestartet wird, hat er keine Informationen über andere Knotenpunkte im Netzwerk. Dennoch muss er Verbindungen herstellen, um sich mit der Blockchain zu synchronisieren, die die meiste Arbeit angesammelt hat. Es werden mehrere Mechanismen verwendet, um diese Peers in der Reihenfolge ihrer Priorität zu finden:


- Der Knoten beginnt, indem er seine lokale Datei "peers.dat" konsultiert, in der Informationen über die Knoten gespeichert sind, mit denen er zuvor interagiert hat. Wenn der Knoten neu ist, ist diese Datei leer, und der Prozess geht zum nächsten Schritt über;
- In Ermangelung von Informationen in der Datei `peers.dat` (was bei einem neu gestarteten Knoten normal ist), führt der Knoten DNS-Anfragen an die DNS-Seeds durch. Diese Server liefern eine Liste von IP-Adressen vermutlich aktiver Knoten, um Verbindungen herzustellen. Die Adressen der DNS Seeds sind im Bitcoin Core Code fest einkodiert. Dieser Schritt ist in der Regel ausreichend, um die Suche nach Peers abzuschließen;
- Wenn die DNS Seeds nicht innerhalb von 60 Sekunden antworten, kann sich der Knoten an die Seed Nodes wenden. Dies sind öffentliche Bitcoin-Knoten, die in einer statischen Liste mit fast tausend Einträgen aufgeführt sind, die direkt in den Quellcode von Bitcoin Core integriert ist. Der neue Knoten nutzt diese Liste, um eine erste Verbindung zum Netzwerk herzustellen und IP-Adressen anderer Knoten zu erhalten;
- In dem sehr unwahrscheinlichen Fall, dass alle vorherigen Methoden fehlschlagen, hat der Knotenbetreiber immer die Möglichkeit, IP-Adressen von Knoten manuell hinzuzufügen, um eine erste Verbindung herzustellen.