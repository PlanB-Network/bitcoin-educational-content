---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Typ příznaku SigHash (`0x83`) v kombinaci s modifikátorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) používaným v podpisech transakcí Bitcoin. Tato kombinace určuje, že podpis se vztahuje pouze na konkrétní jediný vstup a pouze na výstup, který má stejný index jako tento vstup. Ostatní vstupy a výstupy mohou být přidány nebo upraveny jinými stranami. Tato konfigurace je užitečná pro kolaborativní transakce, kdy účastníci mohou přidávat své vlastní vstupy k financování konkrétního výstupu.