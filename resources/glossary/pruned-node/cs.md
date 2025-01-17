---
term: PRUNED NODE

---
Ořezaný uzel, anglicky "Pruned Node", je úplný uzel, který provádí ořezávání blockchainu. Jedná se o postupné odstraňování nejstarších bloků po jejich řádném ověření tak, aby zůstaly zachovány pouze nejnovější bloky. Limit pro uchovávání je specifikován v souboru `bitcoin.conf` prostřednictvím parametru `prune=n`, kde `n` je maximální velikost zabraná bloky v megabajtech (MB). Pokud je za tímto parametrem uvedeno `0`, je pruning zakázán a uzel uchovává celý blockchain.

Ořezané uzly jsou někdy považovány za jiné typy uzlů než plné uzly. Použití ořezaného uzlu může být zajímavé zejména pro uživatele, kteří se potýkají s omezenou kapacitou úložiště. V současné době musí mít plný uzel téměř 600 GB jen pro uložení blockchainu. Ořezaný uzel může omezit potřebné úložiště až na 550 MB. Ačkoli využívá méně místa na disku, ořezaný uzel zachovává podobnou úroveň ověřování a validace jako plný uzel. Ořezané uzly proto nabízejí svým uživatelům větší důvěru ve srovnání s lehkými uzly (SPV).