---
term: BIP0381
definition: pk()-, pkh()- och sh()-funktioner för att beskriva Legacy-skript i deskriptorer.
---

Introducerar funktioner för beskrivningar, särskilt `pk(KEY)` (Pay-to-PubKey), `pkh(KEY)` (Pay-to-PubKey-Hash) och `sh(SCRIPT)` (Pay-to-Script-Hash). Dessa funktioner standardiserar sättet att beskriva Legacy-skriptyper i deskriptorer. BIP381 implementerades tillsammans med alla andra deskriptorrelaterade BIP:er (utom BIP386) i version 0.17 av Bitcoin Core.