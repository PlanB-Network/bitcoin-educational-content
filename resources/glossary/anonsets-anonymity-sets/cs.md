---
term: Anonsets (anonymity sets)

definition: Ukazatele měřící stupeň soukromí UTXO počítáním počtu nerozlišitelných UTXO v množině, obvykle po coinjoin.
---
Anonsety slouží jako ukazatele pro hodnocení míry soukromí konkrétního UTXO. Konkrétně měří počet nerozlišitelných UTXO v rámci množiny, která zahrnuje zkoumanou minci. Jelikož je nutné mít k dispozici skupinu identických UTXO, jsou anonsety obvykle počítány v rámci cyklu coinjoins. Umožňují tak v případě potřeby posoudit kvalitu coinjoins. Velký anonset znamená vyšší úroveň anonymity, protože je obtížné rozlišit konkrétní UTXO v rámci množiny.

Existují dva typy anonsetů: forward anonset (forward-looking metrics); a backward anonset (backward-looking metrics). Termín "*score*" se někdy také používá k označení anonsetů.

První ukazuje velikost skupiny, ve které se skrývá zkoumaný výstupní UTXO, při znalosti vstupního UTXO. Tento ukazatel umožňuje měřit odolnost soukromí mince vůči analýze z minulosti do současnosti (ze vstupu na výstup). Druhý ukazuje počet možných zdrojů pro danou minci při znalosti výstupního UTXO. Tento ukazatel umožňuje měřit odolnost soukromí mince vůči analýze ze současnosti do minulosti (z výstupu na vstup).










