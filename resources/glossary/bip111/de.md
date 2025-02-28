---
term: BIP111

---
Schlägt die Hinzufügung eines Dienstbits mit dem Namen `NODE_BLOOM` vor, um Knoten zu ermöglichen, ihre Unterstützung für Bloom-Filter, wie in BIP37 beschrieben, explizit zu signalisieren. Die Einführung von `NODE_BLOOM` ermöglicht es Knotenbetreibern, diesen Dienst zu deaktivieren, um die Risiken von DoS zu reduzieren. Die BIP37 Option ist in Bitcoin Core standardmäßig deaktiviert. Um sie zu aktivieren, muss der Parameter `peerbloomfilters=1` in der Konfigurationsdatei eingetragen werden.