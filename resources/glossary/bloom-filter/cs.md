---
term: BLOOM FILTER

---
Pravděpodobnostní datová struktura sloužící k testování, zda je prvek součástí množiny. Bloomovy filtry umožňují rychlou kontrolu příslušnosti bez nutnosti testovat celou množinu dat. Jsou obzvláště užitečné v kontextech, kde je kritický prostor a rychlost, ale kde je přijatelná nízká a kontrolovaná chybovost. Bloomovy filtry skutečně nevytvářejí falešně negativní výsledky, ale generují určité množství falešně pozitivních výsledků. Při přidání prvku do filtru generuje několik hashovacích funkcí pozice v bitovém poli. Pro kontrolu příslušnosti se používají stejné hashovací funkce. Pokud jsou všechny odpovídající bity nastaveny, prvek je pravděpodobně v množině, ale s rizikem falešných pozitivních výsledků. Bloomovy filtry se široce používají v oblastech databází a sítí. Zejména je známo, že je společnost Google používá pro svůj komprimovaný systém správy databází *BigTable*. V protokolu Bitcoin se používají zejména pro peněženky SPV podle BIP37.

> ► *Pokud se hovoří konkrétně o použití Bloomových filtrů v souvislosti s transakcemi Bitcoinu, někdy se setkáváme s pojmem "Transaction Bloom Filtering"