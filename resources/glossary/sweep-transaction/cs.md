---
term: SWEEP TRANSACTION
---

Model transakce nebo vzor používaný při analýze řetězce k určení povahy transakce. Tento model je charakterizován spotřebou jediného UTXO jako vstupu a produkcí jediného UTXO jako výstupu. Interpretace tohoto modelu je, že jsme svědky samopřevodu. Uživatel převedl své bitcoiny sám sobě, na jinou adresu, kterou vlastní. Jelikož v transakci nedochází ke změně, je velmi nepravděpodobné, že bychom měli co do činění s platbou. Skutečně, když je provedena platba, je téměř nemožné, aby plátce měl UTXO, které přesně odpovídá částce požadované prodávajícím, navíc k transakčním poplatkům. Obvykle je tedy plátce nucen vyprodukovat výstup změny. Poté víme, že pozorovaný uživatel pravděpodobně stále vlastní toto UTXO. V kontextu analýzy řetězce, pokud víme, že UTXO použité jako vstup v transakci patří Alici, můžeme předpokládat, že UTXO na výstupu také patří jí.

![](../../dictionnaire/assets/6.png)

> ► *Ve francouzštině by se "sweep transaction" dalo přeložit jako "transaction de balayage".*