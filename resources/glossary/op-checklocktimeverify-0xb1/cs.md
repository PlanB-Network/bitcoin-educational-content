---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Transakce je neplatná, pokud nejsou splněny všechny tyto podmínky:


- Zásobník není prázdný;
- Hodnota na vrcholu zásobníku je větší nebo rovna `0`;
- Typ časového zámku je stejný jako u pole `nLockTime` a hodnoty na vrcholu zásobníku (reálný čas nebo číslo bloku);
- Pole `nSequence` na vstupu se nerovná `0xffffffff`;
- Hodnota na vrcholu zásobníku je větší nebo rovna hodnotě pole `nLockTime` transakce.

Pokud některá z těchto podmínek není splněna, skript obsahující `OP_CHECKLOCKTIMEVERIFY` nemůže být splněn. Pokud jsou všechny tyto podmínky splněny, pak se `OP_CHECKLOCKTIMEVERIFY` chová jako `OP_NOP`, což znamená, že se skriptem neprovede žádnou akci. Je to, jako by zmizel. `OP_CHECKLOCKTIMEVERIFY` tedy ukládá časové omezení na utrácení UTXO zajištěného skriptem, který ho obsahuje. Může tak učinit buď ve formě unixového časového data, nebo jako číslo bloku. Za tímto účelem omezuje možné hodnoty pole `nLockTime` transakce, která jej vynakládá, a toto pole `nLockTime` samo omezuje, kdy může být transakce zařazena do bloku.

> ► *Tento opkód nahrazuje `OP_NOP`. Byl umístěn na `OP_NOP2`. Často se označuje zkratkou "CLTV". Poznámka: `OP_CLTV` by se neměl zaměňovat s polem `nLockTime` transakce. První z nich používá druhé, ale jejich povaha a působení jsou odlišné.*