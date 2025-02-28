---
term: KONSOLIDACE

---
Specifická transakce, při níž je více malých UTXO sloučeno do jednoho vstupu, aby na výstupu vznikl jeden větší UTXO. Tato operace je transakcí provedenou do vlastní peněženky. Cílem konsolidace je využít období, kdy jsou poplatky v síti Bitcoin nízké, ke sloučení několika malých UTXO do jednoho většího co do hodnoty. Předvídá tak povinné výdaje v případě zvýšení poplatků, což umožňuje ušetřit na budoucích transakčních poplatcích.

Transakce s mnoha vstupy jsou skutečně těžší, a tudíž dražší. Kromě úspor dosažitelných na transakčních poplatcích je konsolidace také formou dlouhodobého plánování. Pokud vaše peněženka obsahuje velmi malé UTXO, mohou se tyto stát nepoužitelnými, pokud síť Bitcoin vstoupí do delšího období vysokých poplatků. Pokud například potřebujete utratit UTXO o velikosti 10 000 sátů, ale minimální poplatky za těžbu činí 15 000 sátů, výdaje by přesáhly hodnotu samotného UTXO. Tyto malé UTXO se pak stávají ekonomicky neracionálními k používání a zůstávají nepoužitelné, dokud se poplatky nesníží. Tyto UTXO se běžně označují jako "prach" Pravidelnou konsolidací malých UTXO snižujete toto riziko spojené se zvyšováním poplatků.

Je však důležité poznamenat, že konsolidační transakce jsou při analýze řetězce rozpoznatelné. Taková transakce indikuje Heuristiku společného vlastnictví vstupů (CIOH), což znamená, že vstupy konsolidační transakce jsou ve vlastnictví jednoho subjektu. To může mít důsledky z hlediska ochrany soukromí uživatele.

![](../../dictionnaire/assets/7.webp)