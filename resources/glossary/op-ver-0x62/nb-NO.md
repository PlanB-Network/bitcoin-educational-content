---
term: OP_VER (0X62)

definition: Deaktivert opcode som skjøv klientversjonen, konvertert til OP_SUCCESS.
---
Tillot å skyve klientversjonen inn i stakken. Denne opkoden ble deaktivert fordi hvis den hadde blitt brukt, ville hver oppdatering ha ført til en hard fork. BIP342 endret denne opkoden til `OP_SUCCESS`.