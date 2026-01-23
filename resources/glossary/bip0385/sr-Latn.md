---
term: BIP0385
definition: Funkcije addr() i raw() za opisivanje izlaznih skripti prema adresi ili u heksadecimalnom formatu u deskriptorima.
---

Predstavlja funkcije deskriptora `addr(ADDR)` i `raw(HEX)`. Funkcija `addr(ADDR)` omogućava opisivanje izlaznog skripta koristeći primajući Address, dok funkcija `raw(HEX)` omogućava specificiranje izlaznog skripta koristeći sirovu heksadecimalnu reprezentaciju tog skripta. BIP385 je implementiran zajedno sa svim ostalim BIP-ovima vezanim za deskriptore (osim BIP386) u verziji 0.17 Bitcoin Core.