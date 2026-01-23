---
term: BIP0382
definition: wpkh()- och wsh()-funktioner för att beskriva SegWit-skript i deskriptorer.
---

Introducerar funktionerna `wpkh(KEY)` (Pay-to-Witness-PubKey-Hash) och `wsh(SCRIPT)` (Pay-to-Witness-Script-Hash) för descriptors. Dessa funktioner standardiserar sättet att beskriva SegWit-skriptyper i deskriptorer. BIP382 implementerades tillsammans med alla andra deskriptorrelaterade BIP:er (utom BIP386) i version 0.17 av Bitcoin Core.