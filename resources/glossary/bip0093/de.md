---
term: BIP0093
---

Informations-BIP, das einen Standard für die Speicherung und Wiederherstellung des seed eines hierarchischen deterministischen Portfolios (gemäß BIP32) unter Verwendung der geheimen gemeinsamen Nutzung von Schlüsseln nach Shamir vorschlägt. Dieses Protokoll definiert das "codex32"-Format, das vom bech32-Format inspiriert ist, indem es eine strukturierte Zeichenfolge einführt, die aus einem Präfix, einem Schwellenwertparameter, einem Bezeichner, einem Sharing-Index, einer Nutzlast und einer Prüfsumme (BCH) besteht. Die Methode ermöglicht die Aufteilung des seed in bis zu 31 Anteile, von denen ein bestimmter Schwellenwert (zwischen 1 und 9) für eine vollständige Wiederherstellung des seed erforderlich ist.