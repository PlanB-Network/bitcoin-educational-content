---
term: Covenant
definition: Mekanism som ställer villkor för hur en bitcoin kan spenderas i framtida transaktioner.
---

En mekanism som gör det möjligt att införa specifika villkor för hur en viss valuta kan spenderas, inklusive i framtida transaktioner. Utöver de villkor som vanligtvis tillåts av skriptspråket på en UTXO, verkställer avtalet ytterligare begränsningar för hur denna Bitcoin kan spenderas i efterföljande transaktioner. Tekniskt sett uppstår en överenskommelse när `scriptPubKey` för en UTXO definierar restriktioner för `scriptPubKey` för utdata från en transaktion som spenderar nämnda UTXO. Genom att utvidga skriptets omfattning skulle avtal möjliggöra många utvecklingar på Bitcoin, såsom bilateral förankring av drivkedjor, implementering av valv eller förbättring av överlagringssystem som Lightning. Förslag till avtal differentieras baserat på tre kriterier:


- Deras omfattning;
- Deras genomförande;
- Deras återkommande.


Det finns många förslag som skulle göra det möjligt att använda avtal på Bitcoin. De mest avancerade i implementeringsprocessen är: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) och `OP_VAULT`. Bland andra förslag finns följande: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, etc.


För att bättre förstå vad ett avtal innebär kan man göra en liknelse: tänk dig ett kassaskåp som innehåller 500 euro i små sedlar. Om du lyckas låsa upp detta kassaskåp med rätt nyckel är du fri att använda dessa pengar som du vill. Detta är den normala situationen med Bitcoin. Föreställ dig nu att samma kassaskåp inte innehåller 500 euro i sedlar, utan måltidskuponger av motsvarande värde. Om du lyckas öppna kassaskåpet kan du använda denna summa. Din frihet att spendera är dock begränsad, eftersom du bara kan använda dessa kuponger för att betala på vissa restauranger. Det finns alltså ett första villkor för att få använda pengarna, nämligen att man lyckas öppna kassaskåpet med rätt nyckel. Men det finns också ett ytterligare villkor för den framtida användningen av denna summa: den måste spenderas uteslutande på partnerrestauranger, och inte fritt. Detta system av begränsningar för framtida transaktioner är vad som kallas ett avtal.


