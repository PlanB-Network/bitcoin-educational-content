---
term: BIP0386
definition: tr()-funktioner för att beskriva Taproot-utgångar i deskriptorer.
---

Introducerar deskriptorfunktioner för Taproot. Den definierar funktionerna `tr(KEY)` och `tr(KEY, TREE)` för att hitta Taproot-utdata, där `KEY` är den interna nyckeln och `TREE` är ett valfritt träd med skriptsökvägar. BIP386 implementerades i Bitcoin Core version 22.0.