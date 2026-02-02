---
term: Assume utxo

definition: Ein Bitcoin Core-Parameter, der schnelle Synchronisierung eines neuen Knotens durch Verwendung eines Snapshots des UTXO-Satzes ermöglicht, der als gültig angenommen wird, bevor die Historie im Hintergrund überprüft wird.
---
Konfigurationsparameter im Mehrheitsclient Bitcoin Core, der es einem gerade initialisierten Knoten (der aber das IBD noch nicht durchgeführt hat) ermöglicht, die Überprüfung von Transaktionen und dem UTXO-Set vor einem bestimmten Snapshot aufzuschieben. Das Konzept beruht auf der Verwendung eines von Core bereitgestellten und als korrekt angenommenen UTXO-Sets (Liste aller zu einem bestimmten Zeitpunkt existierenden UTXOs), wodurch der Knoten sehr schnell mit der Kette mit der meisten akkumulierten Arbeit synchronisiert werden kann. Da der Knoten den langen Schritt des IBD überspringt, ist er für seinen Benutzer sehr schnell einsatzbereit.

Assume UTXO unterteilt die Synchronisation (IBD) in zwei Teile: Zuerst führt der Knoten den Header First Sync (nur Überprüfung der Header) durch und betrachtet das von Core bereitgestellte UTXO-Set als gültig; sobald er funktionsfähig ist, überprüft der Knoten dann den vollständigen Blockverlauf im Hintergrund und aktualisiert ein neues UTXO-Set, das er selbst überprüft hat. Wenn letzteres nicht mit dem von Core bereitgestellten UTXO-Set übereinstimmt, wird eine Fehlermeldung ausgegeben.

Assume UTXO ermöglicht es somit, die Vorbereitung eines neuen Bitcoin-Knotens zu beschleunigen, indem der Verifizierungsprozess von Transaktionen und dem UTXO-Set dank eines in Core bereitgestellten aktualisierten Snapshots aufgeschoben wird.





