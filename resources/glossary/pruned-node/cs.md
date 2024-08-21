---
term: PRUNED NODE
---

Pruned node, v češtině "prořezaný uzel", je plný uzel, který provádí prořezávání blockchainu. To zahrnuje postupné odstraňování nejstarších bloků, po jejichž řádném ověření, aby byly ponechány pouze nejnovější bloky. Limit uchovávání je specifikován v souboru `bitcoin.conf` prostřednictvím parametru `prune=n`, kde `n` je maximální velikost, kterou bloky zaberou v megabytech (MB). Pokud je po tomto parametru uvedena hodnota `0`, prořezávání je vypnuto a uzel si uchovává blockchain v celé jeho rozsáhlosti.

Prořezané uzly jsou někdy považovány za odlišné typy uzlů od plných uzlů. Použití prořezaného uzlu může být zvláště zajímavé pro uživatele čelící omezením kapacity úložiště. V současnosti musí mít plný uzel téměř 600 GB jen pro ukládání blockchainu. Prořezaný uzel může omezit požadované úložiště až na 550 MB. Přestože využívá méně místa na disku, prořezaný uzel udržuje úroveň ověřování a validace podobnou té u plného uzlu. Prořezané uzly tedy nabízejí svým uživatelům větší důvěru ve srovnání s lehkými uzly (SPV).