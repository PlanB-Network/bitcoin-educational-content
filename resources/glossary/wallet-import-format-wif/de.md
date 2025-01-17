---
term: BRIEFTASCHEN-IMPORTFORMAT (WIF)

---
Eine Methode, um einen privaten Bitcoin-Schlüssel so zu kodieren, dass er leichter zwischen verschiedenen Wallets importiert oder exportiert werden kann. Die WIF basiert auf der `Base58Check`-Kodierung, die Informationen über die Version, die Kompression des entsprechenden öffentlichen Schlüssels und eine Prüfsumme zur Fehlererkennung bei der Eingabe enthält. Ein privater WIF-Schlüssel beginnt mit den Zeichen "5" für unkomprimierte Schlüssel bzw. "K" und "L" für komprimierte Schlüssel und enthält alle Zeichen, die zur Rekonstruktion des ursprünglichen privaten Schlüssels erforderlich sind. Das WIF-Format bietet ein standardisiertes Mittel zur Übertragung eines privaten Schlüssels zwischen verschiedener Wallet-Software.