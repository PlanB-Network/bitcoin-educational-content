---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Způsobí, že transakce bude neplatná, pokud je pozorována kterákoli z těchto charakteristik:
* Zásobník je prázdný;
* Hodnota na vrcholu zásobníku je menší než `0`;
* Vypínací příznak pro hodnotu na vrcholu zásobníku není definován a; Verze transakce je menší než `2` nebo; Vypínací příznak pro pole `nSequence` vstupu je nastaven nebo; Typ časového zámku se neshoduje mezi polem `nSequence` a hodnotou na vrcholu zásobníku (reálný čas nebo počet bloků) nebo; Hodnota na vrcholu zásobníku je větší než hodnota pole `nSequence` vstupu.

Pokud je pozorována jedna nebo více těchto charakteristik, skript obsahující `OP_CHECKSEQUENCEVERIFY` nemůže být splněn. Pokud jsou všechny podmínky platné, pak `OP_CHECKSEQUENCEVERIFY` funguje jako `OP_NOP`, což znamená, že na skript neprovádí žádnou akci. Je to, jako by zmizel. `OP_CHECKSEQUENCEVERIFY` tak ukládá relativní časové omezení na vynaložení UTXO zajištěného skriptem, který jej obsahuje. Může to udělat buď ve formě reálného času nebo jako počet bloků. K tomu omezuje možné hodnoty pro pole `nSequence` vstupu, který jej vynakládá, a toto pole `nSequence` samo omezuje, kdy může být transakce obsahující tento vstup zařazena do bloku.

> ► *Tento operační kód je náhradou za `OP_NOP`. Byl umístěn na `OP_NOP3`. Často se odkazuje na něj zkratkou "CSV". Poznámka, `OP_CSV` by nemělo být zaměňováno s polem `nSequence` transakce. První využívá druhé, ale jejich povahy a akce jsou odlišné.*