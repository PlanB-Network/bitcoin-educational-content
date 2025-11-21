---
term: BIP0383
---

Predstavlja funkcije `multi(NUM, KEY, ..., KEY)` i `sortedmulti(NUM, KEY, ..., KEY)` za deskriptore. Ove funkcije omogućavaju opisivanje multisignature skripti u deskriptorima, pri čemu `sortedmulti` sortira javne ključeve po leksikografskom redosledu kako bi se osigurala kompatibilnost tokom uvoza. BIP383 je implementiran zajedno sa svim ostalim BIP-ovima vezanim za deskriptore (osim BIP386) u verziji 0.17 Bitcoin Core.