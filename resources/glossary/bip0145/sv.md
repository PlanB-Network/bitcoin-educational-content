---
term: BIP0145
definition: Uppdatering av JSON-RPC-anropet getblocktemplate för att integrera SegWit-stöd och beräkning av transaktionsvikt.
---

Uppdaterar JSON-RPC-anropet `getblocktemplate` för att inkludera stöd för SegWit, i enlighet med BIP141. Denna uppdatering gör det möjligt för miners att konstruera block genom att ta hänsyn till den nya "vikt"-mätningen av transaktioner och block som infördes av SegWit, och andra parametrar såsom beräkningen av sigopsgränsen.