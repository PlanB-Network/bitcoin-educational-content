---
term: Blocks Index

definition: LevelDB-Struktur in Bitcoin Core, die die Metadaten und Speicherorte der Blöcke katalogisiert.
---
Eine LevelDB-Datenstruktur in Bitcoin Core, die Metadaten über alle Blöcke katalogisiert. Jeder Eintrag in diesem Index enthält Details wie die Kennung des Blocks, seine Höhe in der Blockchain, den Zeiger auf den Block in der Datenbank und andere Metadaten. Diese Indexierung ermöglicht das schnelle Auffinden eines gespeicherten Blocks im Speicher.