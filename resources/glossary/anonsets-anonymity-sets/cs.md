---
term: ANONSETS (SADY ANONYMITY)

---
Anonce slouží jako indikátory pro posouzení úrovně soukromí konkrétního UTXO. Konkrétně měří počet nerozlišitelných UTXO v souboru, který zahrnuje zkoumanou minci. Protože je vyžadována skupina identických UTXO, anonsety se obvykle počítají v rámci cyklu spojování mincí. Umožňují případně posoudit kvalitu spojování mincí. Velký anonset znamená zvýšenou úroveň anonymity, protože je obtížné rozlišit konkrétní UTXO v rámci souboru. Existují dva typy anonsetů:


- Soubor perspektivní anonymity;
- Retrospektivní soubor anonymity.

První udává velikost skupiny, mezi níž je zkoumaný UTXO skryt, přičemž zná UTXO na vstupu. Tento ukazatel umožňuje měřit odolnost soukromí mince proti analýze z minulosti do současnosti (ze vstupu na výstup). V angličtině je název tohoto ukazatele "*forward anonset*" nebo "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

Druhá udává počet možných zdrojů pro danou minci, přičemž zná UTXO na výstupu. Tento ukazatel umožňuje měřit odolnost soukromí mince proti analýze od současnosti do minulosti (od výstupu ke vstupu). V angličtině je název tohoto ukazatele "*backward anonset*" nebo "*backward-looking metrics*"

![](../../dictionnaire/assets/40.webp)

> ► *Ve francouzštině je obecně přijato používat termín "anonset" Lze jej však přeložit jako "ensemble d'anonymat" nebo "potentiel d'anonymat" V angličtině i ve francouzštině se někdy pro anonsety používá také termín "score" (prospektivní skóre a retrospektivní skóre).*