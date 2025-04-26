---
term: OP_NOP (0X61)

---
Nemá žádný vliv na zásobník ani na stav skriptu. Neprovádí žádné přesuny, kontroly ani úpravy. Prostě nedělá nic, pokud není rozhodnuto jinak prostřednictvím soft fork. Příkazy `OP_NOP` (`OP_NOP1` (`0XB0`) až `OP_NOP10` (`0XB9`)) se totiž od jejich úpravy Satoshim Nakamotem v roce 2010 používají k přidávání nových opkódů formou soft forku.

Proto již byly `OP_NOP2` (`0XB1`) a `OP_NOP3` (`0XB2`) použity k implementaci `OP_CHECKLOCKTIMEVERIFY`, respektive `OP_CHECKSEQUENCEVERIFY`. Používají se v kombinaci s `OP_DROP` k odstranění přidružených časových hodnot ze zásobníku, čímž umožňují pokračovat ve vykonávání skriptu bez ohledu na to, zda je uzel aktuální, nebo ne. Příkazy `OP_NOP` tedy umožňují vložit do skriptu bod přerušení, aby bylo možné zkontrolovat další podmínky, které již existují nebo mohou být přidány s budoucími soft forky. Od verze Tapscript bylo použití příkazu `OP_NOP` nahrazeno efektivnějším příkazem `OP_SUCCESS`.