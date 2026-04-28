---
term: Hd (hierarchical-deterministic)
definition: Plånbok som genererar nycklar sekventiellt och reproducerbart från ett enda frö (seed).
---

Avser en Bitcoin Wallet som använder en unik bit information (seed) för att generate en mängd offentliga och privata nyckelpar på ett sekventiellt och reproducerbart sätt. Denna metod för att hantera nycklar definieras av BIP32-standarden. Den största fördelen med HD-plånböcker är att de gör det möjligt för användare att ha en mängd olika nyckelpar, särskilt för att undvika Address-återanvändning, samtidigt som de kan regenerera dem alla från en enda information. Den här strukturen beskrivs som hierarkisk eftersom den gör det möjligt att skapa en trädliknande organisation av flera nycklar och adresser från en enda seed. Och den är deterministisk i den meningen att varje seed alltid genererar samma sekvens av nycklar i varje Wallet som överensstämmer med detta system.