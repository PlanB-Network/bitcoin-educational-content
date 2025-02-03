---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Transakce je neplatná, pokud je zjištěn některý z těchto znaků:


- Zásobník je prázdný;
- Hodnota na vrcholu zásobníku je menší než `0`;
- Příznak zakázání pro hodnotu na vrcholu zásobníku je nedefinovaný a; Verze transakce je menší než `2` nebo; Příznak zakázání pro pole `nSequence` vstupu je nastaven nebo; Typ časového zámku není stejný mezi polem `nSequence` a hodnotou na vrcholu zásobníku (reálný čas nebo počet bloků) nebo; Hodnota na vrcholu zásobníku je větší než hodnota pole `nSequence` vstupu.

Pokud je pozorována jedna nebo více těchto vlastností, skript obsahující `OP_CHECKSEQUENCEVERIFY` nemůže být splněn. Pokud jsou všechny podmínky platné, pak se `OP_CHECKSEQUENCEVERIFY` chová jako `OP_NOP`, což znamená, že se skriptem neprovede žádnou akci. Je to, jako by zmizel. `OP_CHECKSEQUENCEVERIFY` tedy ukládá relativní časové omezení na utrácení UTXO zajištěného skriptem, který ho obsahuje. Může tak učinit buď ve formě reálného času, nebo jako počet bloků. Za tímto účelem omezuje možné hodnoty pole `nSequence` vstupního výdaje a toto pole `nSequence` samo omezuje, kdy může být transakce, která obsahuje tento vstup, zařazena do bloku.

> ► *Tento opkód nahrazuje `OP_NOP`. Byl umístěn na `OP_NOP3`. Často se označuje zkratkou "CSV". Všimněte si, že `OP_CSV` by se neměl zaměňovat s polem `nSequence` transakce. První z nich využívá druhé, ale jejich povaha a činnost se liší.*