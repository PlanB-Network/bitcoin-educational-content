---
term: BLOCK
---

Datenstruktur im Bitcoin-System. Ein Block enthält eine Reihe gültiger Transaktionen und Metadaten, die in seinem Header enthalten sind. Jeder Block ist durch den Hash seines Headers mit dem nächsten verbunden und bildet so die Blockchain. Die Blockchain fungiert als Zeitstempel-Server, der es jedem Benutzer ermöglicht, alle vergangenen Transaktionen zu kennen, um die Nichtexistenz einer Transaktion zu überprüfen und Doppelausgaben zu verhindern. Transaktionen werden in einem Merkle-Baum organisiert. Dieser kryptographische Akkumulator ermöglicht die Erstellung eines Digests aller Transaktionen in einem Block, genannt der "Merkle-Root". Der Header eines Blocks enthält 6 Elemente:
* Die Version des Blocks;
* Der Abdruck des vorherigen Blocks;
* Die Wurzel des Merkle-Baums der Transaktionen;
* Der Zeitstempel des Blocks;
* Das Schwierigkeitsziel;
* Der Nonce.

Damit ein Block gültig ist, muss er einen Header haben, der, einmal mit `SHA256d` gehasht, einen Digest produziert, der kleiner oder gleich dem Schwierigkeitsziel ist.