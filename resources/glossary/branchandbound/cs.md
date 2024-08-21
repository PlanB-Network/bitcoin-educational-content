---
term: BRANCH-AND-BOUND
---

Metoda používaná pro výběr vstupů v peněžence Bitcoin Core od verze 0.17, kterou vynalezl Murch. Branch-and-Bound (BnB) je vyhledávací metoda, která se snaží najít sadu UTXO, která přesně odpovídá požadované částce výstupů transakce, aby se minimalizovaly změny a s nimi spojené poplatky. Jejím cílem je snížit kritérium plýtvání, které zohledňuje jak okamžité náklady, tak očekávané budoucí náklady na změnu. Tato metoda je přesnější z hlediska poplatků ve srovnání s předchozími heuristikami, jako je *Knapsack Solver*. *Branch-and-Bound* je inspirována metodou řešení problémů stejného názvu, kterou v roce 1960 vynalezly Ailsa Land a Alison Harcourt.

> ► *Tato metoda je také někdy nazývána "Murchův algoritmus" na počest jejího vynálezce.*