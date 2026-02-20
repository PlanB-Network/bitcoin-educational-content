---
term: Witnessscript
definition: Skript som definierar spenderingsvillkor för P2WSH eller P2SH-P2WSH UTXOer, SegWit-motsvarigheten till redeemScript.
---

Ett skript som anger under vilka villkor bitcoins kan spenderas från P2WSH eller P2SH-P2WSH UTXO:er. Vanligtvis fastställer `witnessScript` villkoren för en multisignatur Wallet enligt SegWit-standarden. I dessa skriptstandarder innehåller `scriptPubKey` för UTXO (utdata) en Hash för `witnessScript`. För att använda denna UTXO som input i en ny transaktion måste innehavaren avslöja det ursprungliga `witnessScript` för att bevisa att det överensstämmer med fingeravtrycket i `scriptPubKey`. Vittnesskriften måste sedan ingå i transaktionens `scriptWitness`, som också innehåller de Elements som krävs för att validera skriften, t.ex. signaturer. Därför är `witnessScript` motsvarigheten för SegWit till `redeemscript` i en P2SH-transaktion, med den skillnaden att det placeras i transaktionens vittne och inte i `scriptSig`.


> ► *Försiktighet, `witnessScript` skall inte förväxlas med `scriptWitness`. Medan `witnessScript` definierar utgiftsvillkoren för en P2WSH eller P2SH-P2WSH UTXO och utgör ett manus i sin egen rätt, innehåller `scriptWitness` vittnesdata för alla SegWit-ingångar.*