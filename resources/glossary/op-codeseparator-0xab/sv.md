---
term: OP_CODESEPARATOR (0XAB)
definition: Opcode som segmenterar ett skript för att tillåta oberoende signaturer för varje del.
---

Ändrar det aktuella utdataskriptet och anger att endast de operationer som följer efter denna opcode kommer att beaktas vid verifieringen av signaturerna för motsvarande inmatningar. Detta gör det möjligt att segmentera ett komplext skript i flera delar, där varje segment kan signeras oberoende av varandra.