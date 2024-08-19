---
term: BLK*.DAT
---

Name der Dateien in Bitcoin Core, die die rohen Blockdaten der Blockchain speichern. Jede Datei wird durch eine einzigartige Nummer in ihrem Namen identifiziert. Somit werden die Blöcke in chronologischer Reihenfolge aufgezeichnet, beginnend mit der Datei blk00000.dat. Wenn diese Datei ihre maximale Kapazität erreicht, werden die folgenden Blöcke in blk00001.dat aufgezeichnet, dann in blk00002.dat und so weiter. Jede blk-Datei hat eine maximale Kapazität von 128 Mebibyte (MiB), was etwas mehr als 134 Megabyte (MB) entspricht. Diese Dateien wurden seit der Version 0.8.0 in den Ordner `/blocks` verschoben.