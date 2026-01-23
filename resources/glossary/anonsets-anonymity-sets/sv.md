---
term: Anonsets (anonymitetsmängder)
definition: Indikatorer som mäter graden av integritet för en UTXO genom att räkna antalet ointegrerbara UTXO i en set, typiskt efter en coinjoin.
---
Anonsets fungerar som indikatorer för att bedöma graden av integritet för en viss UTXO. Mer specifikt mäter de antalet oskiljbara UTXO:er inom den mängd som inkluderar den studerade myntet. Eftersom det krävs en grupp identiska UTXO:er beräknas anonsets vanligtvis inom en coinjoin-cykel. De gör det möjligt, i förekommande fall, att bedöma kvaliteten på coinjoins. Ett anonset av stor storlek innebär en högre nivå av anonymitet, eftersom det blir svårt att urskilja en specifik UTXO inom mängden.

Det finns två typer av anonsets: forward anonset (forward-looking metrics); och backward anonset (backward-looking metrics). Termen "*score*" används ibland också för att beteckna anonsets.

Den första anger storleken på den grupp inom vilken den studerade utgående UTXO:n döljer sig, givet den ingående UTXO:n. Denna indikator gör det möjligt att mäta hur motståndskraftig myntets integritet är mot en analys från dåtid till nutid (från ingång till utgång). Den andra anger antalet möjliga källor för ett givet mynt, givet den utgående UTXO:n. Denna indikator gör det möjligt att mäta hur motståndskraftig myntets integritet är mot en analys från nutid till dåtid (från utgång till ingång).
















