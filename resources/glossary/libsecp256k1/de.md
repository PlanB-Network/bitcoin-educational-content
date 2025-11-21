---
term: LIBSECP256K1
---

Leistungsstarke, hochsichere C-Bibliothek für digitale Signaturen und andere kryptographische Primitive auf der elliptischen Kurve `secp256k1`. Da diese Kurve außerhalb von Bitcoin nie weit verbreitet war (im Gegensatz zur oft bevorzugten `secp256r1`-Kurve), zielt diese Bibliothek darauf ab, die umfassendste Referenz für ihre Verwendung zu sein. Die Entwicklung von libsecp256k1 war in erster Linie auf die Bedürfnisse von Bitcoin ausgerichtet, und Funktionen, die für andere Anwendungen gedacht sind, wurden möglicherweise weniger getestet oder überprüft. Die angemessene Verwendung dieser Bibliothek erfordert sorgfältige Aufmerksamkeit, um sicherzustellen, dass sie für die spezifischen Zwecke anderer Anwendungen als Bitcoin geeignet ist.


Die libsecp256k1-Bibliothek bietet eine Vielzahl von Funktionen, darunter:




- ECDSA-secp256k1-Signatur und -Verifizierung sowie Erzeugung kryptografischer Schlüssel ;
- Additive und multiplikative Operationen mit geheimen und öffentlichen Schlüsseln ;
- Serialisierung und Analyse von geheimen Schlüsseln, öffentlichen Schlüsseln und Signaturen ;
- Signierung und Generierung öffentlicher Schlüssel in konstanter Zeit mit konstantem Speicherzugriff;
- Und eine Vielzahl anderer kryptographischer Primitive.