---
term: BRANCH-AND-BOUND

---
Metoda používaná pro výběr vstupů v peněžence Bitcoin Core od verze 0.17, kterou vymyslel Murch. Branch-and-Bound (BnB) je hledání množiny UTXO, která přesně odpovídá množství výstupů, jež mají být v transakci splněny, aby se minimalizovaly změny a související poplatky. Jeho cílem je snížit kritérium plýtvání, které zohledňuje jak okamžité náklady, tak budoucí náklady očekávané na změnu. Tato metoda je z hlediska poplatků přesnější ve srovnání s předchozími heuristikami, jako je *Knapsack Solver*. Metoda *Branch-and-Bound* je inspirována stejnojmennou metodou řešení problémů, kterou v roce 1960 vynalezly Ailsa Landová a Alison Harcourtová.

> ► *Tato metoda se také někdy nazývá "Murchův algoritmus", což odkazuje na jejího vynálezce.*