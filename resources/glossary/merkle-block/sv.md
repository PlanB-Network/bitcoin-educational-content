---
term: Merkle-block
definition: Struktur som ger ett kompakt bevis på att en transaktion ingår i ett block för lättklienter.
---

En datastruktur som används i samband med BIP37 (*Transaction Bloom Filtering*) för att ge ett kompakt bevis på att specifika transaktioner ingår i ett block. Den används framför allt för SPV-plånböcker. Merkle-blocket innehåller blockhuvuden, filtrerade transaktioner och en partiell Merkle Tree, vilket gör det möjligt för lätta klienter att snabbt verifiera om en transaktion tillhör ett block utan att ladda ner alla transaktioner.