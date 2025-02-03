---
term: OP_ENDIF (0X68)

---
Markerer slutten på en betinget kontrollstruktur som er initiert av en `OP_IF` eller en `OP_NOTIF`, vanligvis etterfulgt av en eller flere `OP_ELSE`. Det indikerer at kjøringen av skriptet skal fortsette utover den betingede strukturen, uavhengig av hvilken forgrening som ble utført. Med andre ord brukes `OP_ENDIF` til å markere slutten på betingede blokker i skript.