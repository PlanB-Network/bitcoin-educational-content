---
term: GAP LIMIT
---

Parametr používaný v softwaru Bitcoin peněženek k určení maximálního počtu po sobě jdoucích nepoužitých adres, které mají být generovány před zastavením hledání dalších transakcí. Úprava tohoto parametru je často nezbytná při obnově peněženky, aby se zajistilo, že jsou nalezeny všechny transakce. Nedostatečný Gap Limit by mohl vést k chybějícím některým transakcím, pokud byly adresy přeskočeny během fází derivace. Zvýšení Gap Limitu umožňuje peněžence hledat dále v sekvenci adres, aby mohla obnovit všechny přidružené transakce.

Skutečně, jediný `xpub` může teoreticky odvodit více než 4 miliardy přijímacích adres (jak interních, tak externích adres). Avšak softwarové peněženky nemohou odvodit a kontrolovat všechny tyto adresy na použití bez toho, aby vznikly obrovské provozní náklady. Proto postupují v pořadí indexů, jelikož to je obvykle pořadí, ve kterém všechny softwarové peněženky generují adresy. Software zaznamenává každou použitou adresu před přechodem na další a zastaví své hledání, když narazí na určitý počet po sobě jdoucích prázdných adres. Tento počet se nazývá Gap Limit.

Pokud je například Gap Limit nastaven na `20` a adresa `m/84'/0'/0'/0/15/` je prázdná, peněženka odvodí adresy až do `m/84'/0'/0'/0/34/`. Pokud tento rozsah adres zůstane nepoužitý, hledání se zde zastaví. V důsledku toho by transakce používající adresu `m/84'/0'/0'/0/40/` nebyla v tomto příkladu detekována.