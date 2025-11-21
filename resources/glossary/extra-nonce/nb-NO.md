---
term: EXTRA-Nonce
---

Felt som brukes i `scriptSig` for en blokks Coinbase Transaction, noe som gjør det mulig å teste et større antall muligheter for å få en Hash som er lavere enn vanskelighetsmålet, i tillegg til den klassiske Nonce, som finnes direkte i overskriften til hver blokk.


Ved å endre ekstra-Nonce i Coinbase Transaction endres identifikatoren for denne transaksjonen, og dermed Merkle Root for alle transaksjonene i blokken, noe som også endrer blokkoverskriften. Dette gjør at Miner kan fortsette å søke etter hashes når rekkevidden til den klassiske Nonce allerede er brukt opp, uten å endre strukturen til kandidatblokken.


I Mining-pooler er ekstra-Nonce ofte delt inn i to deler: én som genereres av poolen for å identifisere hver chopper, og en annen som modifiseres av chopperen i søken etter en gyldig share. På denne måten kan de ulike chopperne i poolen arbeide samtidig på den samme kandidatblokken med hele nonces-utvalget, uten å duplisere det samme arbeidet på poolnivå.