---
term: SIGHASH FLAG
---

Parametr v Bitcoinové transakci, který určuje, které komponenty transakce (vstupy a výstupy) jsou pokryty přidruženým podpisem, čímž se stávají neměnnými. SigHash Flag je bajt přidaný k digitálnímu podpisu každého vstupu. Volba SigHash Flag tedy přímo ovlivňuje, které části transakce jsou podpisem zmrazeny a které je možné po podpisu ještě upravit. Tento mechanismus zajišťuje, že podpisy přesně a bezpečně zavazují data transakce podle záměru podepisujícího. Existují tři hlavní SigHash Flagy:

- `SIGHASH_ALL` (`0x01`): Podpis se vztahuje na všechny vstupy a výstupy transakce, čímž je úplně uzamčené;

- `SIGHASH_NONE` (`0x02`): Podpis se vztahuje na všechny vstupy, ale na žádný z výstupů, což umožňuje výstupy po podpisu upravit;

- `SIGHASH_SINGLE` (`0x03`): Podpis pokrývá všechny vstupy a pouze jeden výstup odpovídající indexu podepsaného vstupu.

Kromě těchto tří SigHash Flagů lze použít modifikátor `SIGHASH_ANYONECANPAY` (`0x80`), který lze kombinovat s každým z předchozích typů. Když se použije tento modifikátor, je podepsána pouze část vstupů, zatímco ostatní zůstávají otevřené pro úpravy. Zde jsou existující kombinace s modifikátorem:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Podpis se vztahuje na jeden vstup a zároveň pokrývá všechny výstupy transakce;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Podpis pokrývá jeden vstup, aniž by se zavazoval k jakémukoli výstupu;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Podpis se vztahuje na jeden vstup a pouze na výstup, který má stejný index jako tento vstup.

> ► *Synonymem, které se někdy používá pro "SigHash", jsou "Typy Hash Podpisu".*