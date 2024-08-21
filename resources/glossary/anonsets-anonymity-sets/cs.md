---
term: ANONSETY (SADY ANONYMNOSTI)
---

Anonsety slouží jako ukazatele pro posouzení úrovně soukromí konkrétního UTXO. Konkrétněji měří počet nerozlišitelných UTXO v sadě, která zahrnuje zkoumanou minci. Jelikož je vyžadována skupina identických UTXO, anonsety jsou obvykle počítány v rámci cyklu coinjoinů. Umožňují, je-li to vhodné, posoudit kvalitu coinjoinů. Velký anonset znamená zvýšenou úroveň anonymity, jelikož se stává obtížným rozlišit konkrétní UTXO v sadě. Existují dva typy anonsetů:
* Perspektivní sada anonymity;
* Retrospektivní sada anonymity.

První ukazuje velikost skupiny, mezi kterou je zkoumané UTXO skryto, s vědomím UTXO na vstupu. Tento ukazatel umožňuje měřit odolnost soukromí mince proti analýze od minulosti k přítomnosti (vstup k výstupu). V angličtině se název tohoto ukazatele označuje jako "*forward anonset*," nebo "*forward-looking metrics*."

![](../../dictionnaire/assets/39.png)

Druhý ukazuje počet možných zdrojů pro danou minci, s vědomím UTXO na výstupu. Tento ukazatel umožňuje měřit odolnost soukromí mince proti analýze od přítomnosti k minulosti (výstup k vstupu). V angličtině se název tohoto ukazatele označuje jako "*backward anonset*," nebo "*backward-looking metrics*."

![](../../dictionnaire/assets/40.png)

> ► *Ve francouzštině je obecně přijato používat termín “anonset.” Avšak mohl by být přeložen jako “ensemble d'anonymat” nebo “potentiel d'anonymat.” V angličtině i ve francouzštině se termín “score” také někdy používá pro označení anonsetů (perspektivní skóre a retrospektivní skóre).*