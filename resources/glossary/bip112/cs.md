---
term: BIP112

---
Zavádí opkód `OP_CHECKSEQUENCEVERIFY` (CSV) v jazyce Bitcoin Script. Tato operace umožňuje vytvářet transakce, jejichž platnost začne platit až po určitém zpoždění vzhledem k předchozí transakci, definovaném buď počtem bloků, nebo délkou trvání. `OP_CHECKSEQUENCEVERIFY` porovnává hodnotu na vrcholu zásobníku s hodnotou pole `nSequence` na vstupu. Pokud je větší a všechny ostatní podmínky jsou splněny, je skript platný. Funkce `OP_CHECKSEQUENCEVERIFY` tedy omezuje možné hodnoty pole `nSequence` vstupu, který ji vydává, a toto pole `nSequence` samo omezuje, kdy může být transakce, která obsahuje tento vstup, zařazena do bloku. BIP112 byl zaveden prostřednictvím soft forku 4. července 2016 spolu s BIP68 a BIP113, poprvé aktivovanými metodou BIP9.