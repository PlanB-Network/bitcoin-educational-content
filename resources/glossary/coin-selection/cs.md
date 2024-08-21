---
term: VÝBĚR MINCÍ
---

Proces, při kterém software Bitcoin peněženky vybírá, které UTXO použít jako vstupy pro pokrytí výstupů transakce. Metoda výběru mincí je důležitá, protože má důsledky na cenu transakce a soukromí uživatele. Často si klade za cíl minimalizovat počet použitých vstupů, aby se snížila velikost transakce a s ní spojené poplatky, zatímco se snaží zachovat soukromí tím, že se vyhýbá sloučení mincí z různých zdrojů (CIOH). Existuje několik metod pro výběr mincí, jako je *Knapsack Solver* nebo *Branch-and-Bound*. Když uživatel provádí výběr mincí ručně, označuje se to jako "*Coin Control*".

> ► *V angličtině se tomu říká "Coin Selection".*