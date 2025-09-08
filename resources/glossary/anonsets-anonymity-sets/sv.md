---
term: ANONSETS (ANONYMITETSUPPSÄTTNINGAR)
---

Anonsets fungerar som indikatorer för att bedöma sekretessnivån för en viss UTXO. Mer specifikt mäter de antalet oskiljbara UTXO:er inom den uppsättning som inkluderar myntet som studeras. Eftersom det krävs en grupp av identiska UTXO:er beräknas anonsets i allmänhet inom en cykel av coinjoins. De gör det möjligt att i tillämpliga fall bedöma kvaliteten på coinjoins. En stor anonset innebär en ökad nivå av anonymitet, eftersom det blir svårt att urskilja en specifik UTXO inom uppsättningen. Det finns två typer av anonset:


- Den potentiella anonymitetsuppsättningen;
- Den retrospektiva anonymitetsuppsättningen.


Den första anger storleken på den grupp bland vilka den studerade UTXO är dold, med kännedom om UTXO vid inmatningen. Denna indikator gör det möjligt att mäta motståndet hos myntets integritet mot en analys från det förflutna till nutid (input till output). På engelska är namnet på denna indikator "*forward anonset*" eller "*forward-looking metrics*"


![](../../dictionnaire/assets/39.webp)


Den andra anger antalet möjliga källor för ett visst mynt, med kännedom om UTXO vid utmatningen. Denna indikator gör det möjligt att mäta motståndet hos myntets integritet mot en analys från nutid till förflutet (utgång till ingång). På engelska kallas denna indikator för "*backward anonset*" eller "*backward-looking metrics*"


![](../../dictionnaire/assets/40.webp)


> ► *På franska är det allmänt accepterat att använda termen "anonset" Det kan dock översättas med "ensemble d'anonymat" eller "potentiel d'anonymat" På både engelska och franska används ibland också termen "score" för att hänvisa till anonset (prospective score och retrospective score).*