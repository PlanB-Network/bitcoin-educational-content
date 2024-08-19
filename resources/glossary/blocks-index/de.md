---
term: BLOCKS INDEX
---

Eine LevelDB-Datenstruktur in Bitcoin Core, die Metadaten über alle Blöcke katalogisiert. Jeder Eintrag in diesem Index liefert Details wie den Identifikator des Blocks, seine Höhe in der Blockchain, den Zeiger auf den Block in der Datenbank und andere Metadaten. Diese Indizierung ermöglicht die schnelle Wiederherstellung eines gespeicherten Blocks im Speicher.