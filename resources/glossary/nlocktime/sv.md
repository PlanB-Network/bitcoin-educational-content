---
term: nLockTime
definition: Transaktionsfält som definierar ett absolut tidsvillkor innan inkludering i ett block.
---

Ett inbäddat fält i transaktioner som anger ett tidsbaserat villkor före vilket transaktionen inte kan läggas till i ett giltigt block. Denna parameter gör det möjligt att ange en exakt tid (Unix Timestamp) eller ett specifikt antal block som ett villkor för att transaktionen ska anses vara giltig. Det är alltså en absolut tidslåsning (inte relativ). `nLockTime` påverkar hela transaktionen och möjliggör i praktiken tidsverifiering, medan opkoden `OP_CHECKLOCKTIMEVERIFY` endast gör det möjligt att jämföra det översta värdet i stacken med värdet för `nLockTime`.