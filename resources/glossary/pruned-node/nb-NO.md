---
term: PRUNED NODE

---
En beskåret node, på engelsk "Pruned Node", er en full node som utfører beskjæring av blokkjeden. Dette innebærer at de eldste blokkene fjernes gradvis, etter at de er behørig verifisert, slik at bare de nyeste blokkene beholdes. Oppbevaringsgrensen spesifiseres i filen `bitcoin.conf` via parameteren `prune=n`, der `n` er den maksimale størrelsen på blokkene i megabyte (MB). Hvis `0` er angitt etter denne parameteren, er beskjæring deaktivert, og noden beholder blokkjeden i sin helhet.

Beskårne noder betraktes noen ganger som en annen type noder enn fullstendige noder. Bruken av en beskåret node kan være spesielt interessant for brukere som har begrenset lagringskapasitet. I dag må en full node ha nesten 600 GB bare for å lagre blokkjeden. En beskåret node kan begrense lagringsbehovet til opptil 550 MB. Selv om den bruker mindre diskplass, opprettholder en beskåret node et verifiserings- og valideringsnivå som tilsvarer det en full node har. Beskårne noder gir derfor brukerne mer tillit sammenlignet med lette noder (SPV).