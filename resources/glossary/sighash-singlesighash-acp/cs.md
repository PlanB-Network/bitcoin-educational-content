---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

Typ SigHash příznaku (`0x83`) kombinovaný s modifikátorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) používaný v podpisech Bitcoinových transakcí. Tato kombinace specifikuje, že podpis se vztahuje pouze na konkrétní jednotlivý vstup a pouze na výstup, který má stejný index jako tento vstup. Ostatní vstupy a výstupy mohou být přidány nebo modifikovány jinými stranami. Tato konfigurace je užitečná pro kolaborativní transakce, kde účastníci mohou přidat své vlastní vstupy k financování konkrétního výstupu.