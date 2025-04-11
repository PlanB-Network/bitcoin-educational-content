---
term: COIN SELECTION

---
Proces, při kterém software bitcoinové peněženky vybírá, které UTXO použije jako vstupy k uspokojení výstupů transakce. Způsob výběru mincí je důležitý, protože má důsledky pro náklady transakce a soukromí uživatele. Často se snaží minimalizovat počet použitých vstupů, aby se snížila velikost transakce a související poplatky, a zároveň se snaží zachovat soukromí tím, že se vyhýbá slučování mincí z různých zdrojů (CIOH). Pro výběr mincí existuje několik metod, například *Knapsack Solver* nebo *Branch-and-Bound*. Pokud výběr mincí provádí uživatel ručně, označuje se jako "*Kontrola mincí*".

> ► V angličtině se označuje jako "Coin Selection".*