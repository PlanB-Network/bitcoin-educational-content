---
term: Scriptwitness
definition: SegWit-element som innehåller signaturer och offentliga nycklar för att låsa upp bitcoins.
---

Ett element i SegWit-transaktionsposter som innehåller de signaturer och publika nycklar som krävs för att låsa upp de bitcoins som skickats i transaktionen. I likhet med `scriptSig` i Legacy-transaktioner är `scriptWitness` dock inte placerat på samma plats. Det är faktiskt denna del, som kallas "vittnet" (`*witness*` på engelska), som flyttas till en separat databas för att lösa problemet med transaktionens formbarhet. Varje SegWit-ingång har sitt eget `scriptWitness`, och alla `scriptWitness` Elements bildar tillsammans transaktionens `Witness`-fält.


> ► *Var försiktig så att du inte blandar ihop `scriptWitness` med `witnessScript`. Medan `scriptWitness` innehåller vittnesdata för alla SegWit-ingångar, definierar `witnessScript` utgiftsvillkoren för en P2WSH eller P2SH-P2WSH UTXO och utgör ett manus i sin egen rätt, liknande `redeemscript` för en P2SH-utgång*