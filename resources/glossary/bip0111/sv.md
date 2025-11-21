---
term: BIP0111
---

Föreslår tillägg av en tjänstebit med namnet `NODE_BLOOM` för att noder uttryckligen ska kunna signalera sitt stöd för Bloomfilter enligt beskrivningen i BIP37. Införandet av `NODE_BLOOM` gör det möjligt för nodoperatörer att inaktivera denna tjänst för att minska riskerna för DoS. Alternativet BIP37 är inaktiverat som standard i Bitcoin Core. För att aktivera det måste parametern `peerbloomfilters=1` anges i konfigurationsfilen.