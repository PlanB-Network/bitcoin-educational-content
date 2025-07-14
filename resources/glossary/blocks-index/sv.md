---
term: BLOCKS INDEX
---

En LevelDB-datastruktur i Bitcoin Core som katalogiserar metadata om alla block. Varje post i detta index innehåller detaljer som blockets identifierare, dess höjd i Blockchain, pekaren till blocket i databasen och andra metadata. Denna indexering gör det möjligt att snabbt hämta ett lagrat block i minnet.