---
term: SWEEP TRANSAKCE

---
Vzor nebo model transakce používaný při analýze řetězce k určení povahy transakce. Tento model je charakterizován spotřebou jednoho UTXO jako vstupu a výrobou jednoho UTXO jako výstupu. Interpretace tohoto modelu je taková, že se nacházíme v přítomnosti samopřevodu. Uživatel převedl své bitcoiny na sebe, na jinou adresu, kterou vlastní. Vzhledem k tomu, že v transakci nedochází k žádné změně, je velmi nepravděpodobné, že bychom měli co do činění s platbou. Při platbě je totiž téměř nemožné, aby měl plátce kromě transakčních poplatků UTXO, které přesně odpovídá částce požadované prodávajícím. Obecně je tedy plátce nucen vytvořit výstupní změnu. Pak víme, že sledovaný uživatel pravděpodobně stále disponuje tímto UTXO. V kontextu řetězové analýzy, pokud víme, že UTXO použité jako vstup v transakci patří Alici, můžeme předpokládat, že UTXO na výstupu jí také patří.

![](../../dictionnaire/assets/6.webp)

> ► *Ve francouzštině by se "sweep transaction" dalo přeložit jako "transaction de balayage".*