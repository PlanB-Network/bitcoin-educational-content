---
term: BLK*.DAT

---
Name der Dateien in Bitcoin Core, die die rohen Blockdaten der Blockchain speichern. Jede Datei wird durch eine eindeutige Nummer in ihrem Namen identifiziert. Die Blöcke werden also in chronologischer Reihenfolge aufgezeichnet, beginnend mit der Datei blk00000.dat. Wenn diese Datei ihre maximale Kapazität erreicht hat, werden die folgenden Blöcke in blk00001.dat, dann blk00002.dat und so weiter aufgezeichnet. Jede blk-Datei hat eine maximale Kapazität von 128 Megabyte (MiB), was etwas mehr als 134 Megabyte (MB) entspricht. Diese Dateien sind seit Version 0.8.0 in den Ordner `/blocks` verschoben worden.