---
term: BIP112
---

Zavádí operaci `OP_CHECKSEQUENCEVERIFY` (CSV) v jazyce Bitcoin Script. Tato operace umožňuje vytváření transakcí, jejichž platnost nabývá účinnosti až po určitém zpoždění vzhledem k předchozí transakci, definovaném buď počtem bloků nebo časovou délkou. `OP_CHECKSEQUENCEVERIFY` porovnává hodnotu na vrcholu zásobníku s hodnotou pole `nSequence` vstupu. Pokud je větší a jsou splněny všechny ostatní podmínky, skript je platný. Tím pádem `OP_CHECKSEQUENCEVERIFY` omezuje možné hodnoty pro pole `nSequence` vstupu, který jej utrácí, a toto pole `nSequence` samo omezuje, kdy může být transakce obsahující tento vstup zařazena do bloku. BIP112 byl zaveden prostřednictvím měkkého forku 4. července 2016 společně s BIP68 a BIP113, aktivovaný poprvé použitím metody BIP9.