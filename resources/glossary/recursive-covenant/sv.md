---
term: Rekursiv (covenant)
definition: Covenant som ställer villkor för den aktuella transaktionen och alla efterföljande transaktioner på obestämd tid.
---

Ett rekursivt avtal på Bitcoin är en typ av Smart contract som ställer villkor inte bara på den aktuella transaktionen utan även på framtida transaktioner som spenderar utdata från denna transaktion. Detta gör det möjligt att skapa transaktionskedjor där varje transaktion måste följa vissa regler som definieras av den första i kedjan. Rekursivitet skapar en sekvens av transaktioner där var och en ärver restriktionerna från sin föräldratransaktion. Detta skulle möjliggöra komplex och långsiktig kontroll över hur bitcoins kan spenderas, men det skulle också medföra risker avseende spenderingsfrihet och fungibilitet.


Sammanfattningsvis skulle ett icke-rekursivt avtal endast begränsa sig till den transaktion som omedelbart följer på den som fastställde reglerna. Omvänt har ett rekursivt avtal möjlighet att införa specifika villkor för en Bitcoin på obestämd tid. Transaktioner kan följa på varandra, men Bitcoin i fråga kommer alltid att behålla de ursprungliga villkor som är knutna till den. Tekniskt sett uppstår ett icke-recursivt avtal när `scriptPubKey` i en UTXO definierar restriktioner för `scriptPubKey` i utdata från en transaktion som spenderar nämnda UTXO. Å andra sidan sker upprättandet av ett rekursivt avtal när `scriptPubKey` i en UTXO definierar restriktioner för `scriptPubKey` i resultatet av en transaktion som spenderar nämnda UTXO, och för alla de `scriptPubKey` som kommer att följa på spenderingen av denna UTXO.


Mer allmänt, inom databehandling, är det som kallas "rekursivitet" förmågan hos en funktion att anropa sig själv, vilket skapar en slags loop.