---
term: ASSUME UTXO
---

Ein Konfigurationsparameter im führenden Bitcoin Core Client, der es einem Knoten, der gerade initialisiert wurde (aber noch nicht den IBD durchlaufen hat), ermöglicht, die Verifizierung von Transaktionen und des UTXO-Sets bis zu einem gegebenen Snapshot aufzuschieben. Das Konzept stützt sich auf die Verwendung eines UTXO-Sets (eine Liste aller existierenden UTXOs zu einem bestimmten Zeitpunkt), das von Core bereitgestellt und als korrekt angenommen wird, was dem Knoten ermöglicht, sehr schnell mit der Kette mit der meisten angesammelten Arbeit synchronisiert zu werden. Da der Knoten den langwierigen IBD-Schritt überspringt, wird er sehr schnell betriebsbereit für seinen Benutzer. Assume UTXO teilt die Synchronisation (IBD) in zwei Teile:
* Zuerst führt der Knoten die Header First Sync durch (Verifizierung nur der Header) und betrachtet das von Core bereitgestellte UTXO-Set als gültig;
* Sobald er betriebsbereit ist, wird der Knoten die komplette Blockhistorie im Hintergrund verifizieren und ein neues UTXO-Set aktualisieren, das er selbst verifiziert hat. Stimmt dieses neue UTXO-Set nicht mit dem von Core bereitgestellten überein, wird eine Fehlermeldung erzeugt.

Daher beschleunigt Assume UTXO die Vorbereitung eines neuen Bitcoin-Knotens, indem es den Prozess der Transaktionsverifizierung und des UTXO-Sets durch einen aktualisierten Snapshot, der in Core bereitgestellt wird, aufschiebt.