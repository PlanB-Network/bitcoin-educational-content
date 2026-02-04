---
term: OP_ENDIF (0X68)
definition: Opcode som markerar slutet på en villkorlig struktur i ett script.
---

Markerar slutet på en villkorlig kontrollstruktur som initieras av en `OP_IF` eller en `OP_NOTIF`, vanligtvis följt av en eller flera `OP_ELSE`. Det anger att exekveringen av skriptet ska fortsätta bortom den villkorliga strukturen, oavsett vilken gren som kördes. Med andra ord används `OP_ENDIF` för att markera slutet på villkorliga block i skript.