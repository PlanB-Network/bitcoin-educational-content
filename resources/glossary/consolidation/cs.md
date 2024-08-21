---
term: KONZOLIDACE
---

Specifická transakce, při které jsou několik malých UTXO sloučeny do jednoho vstupu, aby vytvořily jeden, větší UTXO jako výstup. Tato operace je transakcí provedenou do vlastní peněženky. Cílem konzolidace je využít období, kdy jsou poplatky v síti Bitcoin nízké, aby sloučila několik malých UTXO do jednoho většího hodnotově. Tím předvídá povinné výdaje v případě zvýšení poplatků, což umožňuje ušetřit na budoucích transakčních poplatcích.

Skutečně, transakce s mnoha vstupy jsou těžší a tudíž dražší. Kromě úspor dosažitelných na transakčních poplatcích je konzolidace také formou dlouhodobého plánování. Pokud vaše peněženka obsahuje velmi malé UTXO, tyto se mohou stát nepoužitelnými, pokud síť Bitcoin vstoupí do prodlouženého období vysokých poplatků. Například, pokud potřebujete utratit UTXO 10 000 sats, ale minimální poplatky za těžbu činí 15 000 sats, výdaje by překročily hodnotu samotného UTXO. Tyto malé UTXO se pak stávají ekonomicky neracionálními k použití a zůstávají nepoužitelné, dokud se poplatky nesníží. Tato UTXO se běžně označují jako "prach". Pravidelnou konzolidací vašich malých UTXO snižujete toto riziko spojené se zvýšením poplatků.

Je však důležité poznamenat, že transakce konzolidace jsou rozpoznatelné během analýzy řetězce. Taková transakce ukazuje na heuristiku společného vlastnictví vstupu (CIOH), což znamená, že vstupy transakce konzolidace jsou vlastněny jednou entitou. To může mít důsledky z hlediska soukromí pro uživatele.

![](../../dictionnaire/assets/7.png)