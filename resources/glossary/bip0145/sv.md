---
term: BIP0145
---

Uppdaterar JSON-RPC-anropet `getblocktemplate` för att inkludera stöd för SegWit, i enlighet med BIP141. Denna uppdatering gör det möjligt för miners att konstruera block genom att ta hänsyn till den nya "vikt"-mätningen av transaktioner och block som infördes av SegWit, och andra parametrar såsom beräkningen av sigopsgränsen.