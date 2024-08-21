---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Způsobí, že transakce bude neplatná, pokud nejsou splněny všechny tyto podmínky:
* Zásobník není prázdný;
* Hodnota na vrcholu zásobníku je větší nebo rovna `0`;
* Typ časového zámku je stejný mezi polem `nLockTime` a hodnotou na vrcholu zásobníku (reálný čas nebo číslo bloku);
* Pole `nSequence` vstupu není rovno `0xffffffff`;
* Hodnota na vrcholu zásobníku je větší nebo rovna hodnotě pole `nLockTime` transakce.

Pokud některá z těchto podmínek není splněna, skript obsahující `OP_CHECKLOCKTIMEVERIFY` nemůže být splněn. Pokud jsou všechny tyto podmínky platné, pak `OP_CHECKLOCKTIMEVERIFY` funguje jako `OP_NOP`, což znamená, že na skript neprovádí žádnou akci. Je to, jako by zmizel. `OP_CHECKLOCKTIMEVERIFY` tak ukládá časové omezení na výdaje UTXO zajištěného skriptem, který jej obsahuje. Může to udělat buď ve formě data Unixového času nebo jako číslo bloku. To dělá tím, že omezuje možné hodnoty pro pole `nLockTime` transakce, která jej utrácí, a toto pole `nLockTime` samo omezuje, kdy může být transakce zařazena do bloku.

> ► *Tento operační kód je náhradou za `OP_NOP`. Byl umístěn na `OP_NOP2`. Často se odkazuje na něj zkratkou "CLTV". Poznámka, `OP_CLTV` by nemělo být zaměňováno s polem `nLockTime` transakce. První z nich používá druhé, ale jejich povaha a akce jsou odlišné.*