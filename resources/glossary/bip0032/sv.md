---
term: BIP0032
definition: Introduktion av HD-plånböcker (hierarchical deterministic) som gör det möjligt att generera alla nycklar i en plånbok från ett enda frö (seed).
---

I BIP32 introducerades begreppet hierarkisk deterministisk Wallet (HD Wallet). Detta förslag gör det möjligt att generera en hierarki av nyckelpar från en gemensam "master seed" med hjälp av enkelriktade härledningsfunktioner. Varje genererat nyckelpar kan i sig självt vara överordnat andra underordnade nycklar och på så sätt bilda en trädliknande (hierarkisk) struktur. Fördelen med BIP32 är att den gör det möjligt att hantera flera olika nyckelpar samtidigt som man bara behöver behålla en enda seed för att regenerera dem. Denna innovation har framför allt bidragit till att bekämpa problemet med återanvändning av Address, vilket är allvarligt för användarnas integritet. BIP32 gör det också möjligt att skapa undergrenar inom samma Wallet för att underlätta hanteringen av den.