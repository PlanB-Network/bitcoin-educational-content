---
term: GAP LIMIT

---
Parametr používaný v softwaru peněženky Bitcoin k určení maximálního počtu po sobě jdoucích nepoužitých adres, které se mají vygenerovat před zastavením vyhledávání dalších transakcí. Úprava tohoto parametru je často nutná při obnově peněženky, aby se zajistilo nalezení všech transakcí. Nedostatečný Gap Limit by mohl vést k vynechání některých transakcí, pokud by byly adresy během fází odvozování přeskočeny. Zvýšení parametru Gap Limit umožní peněžence prohledávat dále v posloupnosti adres, aby bylo možné obnovit všechny související transakce.

Z jednoho `xpubu` lze teoreticky odvodit více než 4 miliardy přijímacích adres (interních i externích). Software peněženky však nemůže všechny tyto adresy odvodit a zkontrolovat, zda jsou používány, aniž by tím vznikly obrovské provozní náklady. Proto postupují v indexovém pořadí, protože v tomto pořadí obvykle generují adresy všechny softwary peněženek. Software zaznamená každou použitou adresu, než přejde k další, a zastaví hledání, když narazí na několik po sobě jdoucích prázdných adres. Tomuto číslu se říká mezera.

Pokud je například limit mezery nastaven na `20` a adresa `m/84'/0'/0'/0/15/` je prázdná, peněženka odvodí adresy až do `m/84'/0'/0'/0/34/`. Pokud tento rozsah adres zůstane nevyužitý, hledání se zde zastaví. V důsledku toho by transakce používající adresu `m/84'/0'/0'/0/40/` nebyla v tomto příkladu detekována.