---
term: SIGHASH_ALL/SIGHASH_ACP
---

Typ příznaku SigHash (`0x81`) kombinovaný s modifikátorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`), používaný v podpisech transakcí Bitcoinu. Tato kombinace specifikuje, že podpis se vztahuje na všechny výstupy a pouze na konkrétní vstup transakce. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` umožňuje ostatním účastníkům přidávat další vstupy do transakce po jejím počátečním podepsání. Je to zvláště užitečné ve spolupracujících scénářích, jako jsou transakce pro crowdfunding, kde různí přispěvatelé mohou přidávat své vlastní vstupy, přičemž zachovávají integritu výstupů zavázaných počátečním signatářem.