---
term: Branch-and-bound
definition: Algoritm för myntval i Bitcoin Core för att minimera växel och transaktionsavgifter.
---

Metod som används för att välja inputs i Bitcoin Core Wallet sedan version 0.17 och uppfanns av Murch. Branch-and-Bound (BnB) är en sökning för att hitta en uppsättning UTXO som matchar den exakta mängden output som ska uppfyllas i en transaktion, för att minimera förändringar och tillhörande avgifter. Målet är att minska ett avfallskriterium som tar hänsyn till både den omedelbara kostnaden och de framtida kostnader som förväntas för förändringen. Denna metod är mer exakt när det gäller avgifter jämfört med tidigare heuristiker som *Knapsack Solver*. *Branch-and-Bound* är inspirerad av problemlösningsmetoden med samma namn, som uppfanns 1960 av Ailsa Land och Alison Harcourt.


> ► *Den här metoden kallas ibland också "Murch's Algorithm" med hänvisning till dess uppfinnare*