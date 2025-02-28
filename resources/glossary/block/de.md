---
term: BLOCK

---
Datenstruktur im Bitcoin-System. Ein Block enthält eine Reihe von gültigen Transaktionen und Metadaten, die in seinem Header enthalten sind. Jeder Block ist durch den Hash seines Headers mit dem nächsten verknüpft und bildet so die Blockchain. Die Blockchain fungiert als Zeitstempel-Server, der es jedem Nutzer ermöglicht, alle vergangenen Transaktionen zu kennen, um die Nichtexistenz einer Transaktion zu überprüfen und Doppelausgaben zu verhindern. Die Transaktionen sind in einem Merkle-Baum organisiert. Dieser kryptografische Akkumulator ermöglicht die Erstellung einer Zusammenfassung aller Transaktionen in einem Block, der so genannten "Merkle-Wurzel" Der Kopf eines Blocks besteht aus 6 Elementen:


- Die Version des Blocks;
- Das Impressum des vorherigen Blocks;
- Die Wurzel des Merkle-Baums der Transaktionen;
- Der Zeitstempel des Blocks;
- Das Schwierigkeitsziel;
- Die Nonce.

Damit ein Block gültig ist, muss er einen Header haben, der, nachdem er mit `SHA256d` gehasht wurde, einen Digest ergibt, der kleiner oder gleich dem Schwierigkeitsziel ist.