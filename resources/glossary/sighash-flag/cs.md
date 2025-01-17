---
term: SIGHASH FLAG

---
Parametr v transakci Bitcoin, který určuje, na které součásti transakce (vstupy a výstupy) se vztahuje příslušný podpis, čímž se transakce stává neměnnou. Příznak SigHash je bajt přidaný k digitálnímu podpisu každého vstupu. Volba příznaku SigHash Flag tedy přímo ovlivňuje, které části transakce jsou zmrazeny podpisem a které lze ještě dodatečně upravovat. Tento mechanismus zajišťuje, že podpisy přesně a bezpečně zavazují data transakce v souladu se záměrem podepisujícího. Existují tři hlavní příznaky SigHash:


- `SIGHASH_ALL` (`0x01`): Podpis se vztahuje na všechny vstupy a výstupy transakce, čímž je zcela uzamkne;
- `SIGHASH_NONE` (`0x02`): Signatura se vztahuje na všechny vstupy, ale na žádný z výstupů, takže výstupy mohou být upraveny až po signatuře;
- `SIGHASH_SINGLE` (`0x03`): Signatura pokrývá všechny vstupy a pouze jeden výstup odpovídající indexu podepsaného vstupu.

Kromě těchto tří příznaků SigHash lze s každým z předchozích typů kombinovat modifikátor `SIGHASH_ANYONECANPAY` (`0x80`). Při použití tohoto modifikátoru se podepisuje pouze část vstupů, ostatní vstupy zůstávají otevřené pro modifikaci. Zde jsou uvedeny existující kombinace s tímto modifikátorem:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Signatura se vztahuje na jediný vstup a zároveň pokrývá všechny výstupy transakce;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Signatura pokrývá jediný vstup, aniž by se zavázala k jakémukoli výstupu;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Signatura se vztahuje na jediný vstup a pouze na výstup se stejným indexem jako tento vstup.

> ► *Synonymem pro "SigHash" je někdy "Signature Hash Types".*