---
term: SIGHASH_NONE/SIGHASH_ACP

definition: Kombinace SigHash podepisující pouze jeden konkrétní vstup bez závazku k jakémukoli výstupu.
---
Typ příznaku SigHash (`0x82`) v kombinaci s modifikátorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) používaným v podpisech transakcí Bitcoin. Tato kombinace označuje, že podpis se vztahuje pouze na konkrétní vstup, aniž by se závazně vztahoval na jakýkoli výstup. To umožňuje ostatním účastníkům volně přidávat další vstupy a měnit všechny výstupy transakce.