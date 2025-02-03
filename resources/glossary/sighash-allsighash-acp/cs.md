---
term: SIGHASH_ALL/SIGHASH_ACP

---
Typ příznaku SigHash (`0x81`) v kombinaci s modifikátorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) používaným v podpisech transakcí Bitcoin. Tato kombinace určuje, že podpis se vztahuje na všechny výstupy a pouze na konkrétní vstup transakce. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` umožňuje ostatním účastníkům přidávat další vstupy transakce po jejím prvotním podpisu. To je užitečné zejména ve scénářích spolupráce, jako jsou transakce crowdfundingu, kdy mohou různí účastníci přidávat své vlastní vstupy při zachování integrity výstupů, které se zavázal podepsat původní účastník.