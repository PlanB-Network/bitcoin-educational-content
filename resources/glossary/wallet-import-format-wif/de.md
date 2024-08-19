---
term: WALLET IMPORT FORMAT (WIF)
---

Eine Methode zur Kodierung eines Bitcoin-Privatschlüssels, sodass er einfacher zwischen verschiedenen Wallets importiert oder exportiert werden kann. Der WIF basiert auf der `Base58Check`-Kodierung, die Informationen über die Version, die Kompression des entsprechenden öffentlichen Schlüssels und eine Prüfsumme zur Fehlererkennung bei der Eingabe enthält. Ein WIF-Privatschlüssel beginnt mit den Zeichen `5` für unkomprimierte Schlüssel oder `K` und `L` für komprimierte Schlüssel und enthält alle Zeichen, die notwendig sind, um den ursprünglichen Privatschlüssel zu rekonstruieren. Das WIF-Format bietet ein standardisiertes Mittel, um einen Privatschlüssel zwischen unterschiedlicher Wallet-Software zu übertragen.