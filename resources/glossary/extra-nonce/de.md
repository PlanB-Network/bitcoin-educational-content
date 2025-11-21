---
term: EXTRA-Nonce
---

Feld, das in der `scriptSig` des Coinbase Transaction eines Blocks verwendet wird und das es ermöglicht, eine größere Anzahl von Möglichkeiten zu testen, um einen Hash zu erhalten, der niedriger ist als der angestrebte Schwierigkeitsgrad, zusätzlich zum klassischen Nonce, der direkt in der Kopfzeile eines jeden Blocks zu finden ist.


Durch die Änderung der Extra-Nonce in der Coinbase Transaction wird die Kennung dieser Transaktion und damit die Merkle Root aller Transaktionen im Block geändert, wodurch auch der Blockkopf geändert wird. Dadurch kann die Miner weiterhin nach Hashes suchen, wenn der Bereich der klassischen Nonce bereits erschöpft ist, ohne die Struktur ihres Kandidatenblocks zu ändern.


In Mining-Pools wird der Extra-Nonce oft in zwei Teile aufgeteilt: einen, der vom Pool zur Identifizierung jedes Choppers erzeugt wird, und einen weiteren, der vom Chopper auf der Suche nach einem gültigen Anteil modifiziert wird. Auf diese Weise können die verschiedenen Chopper im Pool gleichzeitig an demselben Kandidatenblock mit dem gesamten Nonces-Bereich arbeiten, ohne die gleiche Arbeit auf Pool-Ebene zu duplizieren.