---
term: ASSUME UTXO

---
Ein Konfigurationsparameter im führenden Bitcoin Core Client, der es einem Node, der gerade initialisiert wurde (aber noch nicht die IBD durchlaufen hat), erlaubt, die Verifizierung von Transaktionen und des UTXO-Sets bis zu einem bestimmten Snapshot aufzuschieben. Das Konzept beruht auf der Verwendung eines UTXO-Satzes (einer Liste aller zu einem bestimmten Zeitpunkt existierenden UTXOs), der von Core bereitgestellt wird und als korrekt gilt, wodurch der Knoten sehr schnell mit der Kette mit der meisten angesammelten Arbeit synchronisiert werden kann. Da der Knoten den langwierigen IBD-Schritt überspringt, ist er für seinen Benutzer sehr schnell einsatzbereit. Angenommen, UTXO unterteilt die Synchronisierung (IBD) in zwei Teile:


- Zunächst führt der Knoten die Header-First-Sync durch (nur Überprüfung der Header) und betrachtet den vom Kern bereitgestellten UTXO-Satz als gültig;
- Sobald er betriebsbereit ist, prüft der Knoten die gesamte Blockhistorie im Hintergrund und aktualisiert einen neuen UTXO-Satz, den er selbst geprüft hat. Wenn dieser neue UTXO-Satz nicht mit dem von Core bereitgestellten Satz übereinstimmt, gibt er eine Fehlermeldung aus.

Daher beschleunigt Assume UTXO die Vorbereitung eines neuen Bitcoin-Knotens, indem der Transaktionsverifizierungsprozess verschoben und der UTXO-Satz durch einen aktualisierten Snapshot in Core bereitgestellt wird.