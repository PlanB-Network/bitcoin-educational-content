---
term: JEDNODUCHÁ PLATBA
---

Transakční vzor (nebo model) používaný v analýze řetězců, který se vyznačuje spotřebou jednoho nebo více UTXO na vstupu a vytvořením 2 UTXO na výstupu. Tento model bude tedy vypadat takto:

![](../../dictionnaire/assets/5.png)

Tento model jednoduché platby naznačuje, že jsme pravděpodobně přítomni transakci odesílání nebo platby. Uživatel spotřeboval své vlastní UTXO na vstupu, aby na výstupu uspokojil platbu UTXO a UTXO změny (změna vrácená stejnému uživateli). Proto víme, že pozorovaný uživatel pravděpodobně již není v držení jednoho ze dvou UTXO na výstupu (toho platícího), ale stále vlastní druhé UTXO (to změny).