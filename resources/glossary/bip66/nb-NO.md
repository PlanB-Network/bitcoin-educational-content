---
term: BIP66

---
Innførte en standardisering av signaturformatet i transaksjoner. Denne BIP-en ble foreslått som svar på at OpenSSL håndterte signaturkoding ulikt på tvers av ulike systemer. Denne heterogeniteten utgjorde en risiko for splitting av blokkjeden. BIP66 standardiserte signaturformatet for alle transaksjoner ved hjelp av streng DER-koding (*Distinguished Encoding Rules*). Denne endringen krevde en soft fork. For aktivering brukte BIP66 den samme mekanismen som BIP34, og krevde at `nVersion`-feltet ble økt til versjon 3, og avviste alle blokker med versjon 2 eller lavere når terskelen på 95 % gruvearbeidere var nådd. Denne terskelen ble overskredet ved blokk nummer 363 725 den 4. juli 2015.