---
term: OP_NOP (0X61)
---

Nemá žádný vliv na zásobník ani na stav skriptu. Neprovádí žádné pohyby, kontroly nebo úpravy. Jednoduše nedělá nic, pokud není rozhodnuto jinak prostřednictvím měkkého forku. Skutečně, od jejich úpravy Satoshi Nakamotem v roce 2010, jsou příkazy `OP_NOP` (`OP_NOP1` (`0XB0`) až `OP_NOP10` (`0XB9`)) používány k přidání nových operací ve formě měkkého forku.

Takto `OP_NOP2` (`0XB1`) a `OP_NOP3` (`0XB2`) byly již použity k implementaci `OP_CHECKLOCKTIMEVERIFY` a `OP_CHECKSEQUENCEVERIFY` respektive. Používají se ve spojení s `OP_DROP` k odstranění přidružených časových hodnot ze zásobníku, čímž umožňují pokračování v provádění skriptu, ať už je uzel aktualizován nebo ne. Příkazy `OP_NOP` tedy umožňují vložení bodu přerušení do skriptu pro kontrolu dodatečných podmínek, které již existují nebo mohou být přidány s budoucími měkkými forky. Od Tapscriptu bylo použití `OP_NOP` nahrazeno efektivnějším `OP_SUCCESS`.