---
term: DUSTRELAYFEE
---

Standardizační pravidlo používané uzly sítě k určení toho, co považují za "limit prachu". Tento parametr nastavuje sazbu poplatku v sats za virtuální kilobajt (sats/kvB), která slouží jako referenční bod pro výpočet, zda je hodnota UTXO menší než nezbytné poplatky pro její zahrnutí do transakce. Skutečně, UTXO je na Bitcoinu považováno za "prach", pokud vyžaduje více na poplatcích pro převod, než jakou hodnotu samo představuje. Výpočet tohoto limitu je následující:

```text
limit = (velikost vstupu + velikost výstupu) * sazba poplatku
```

Jelikož požadovaná sazba poplatku pro zahrnutí transakce do bloku Bitcoinu se neustále mění, parametr `DustRelayFee` umožňuje každému uzlu definovat sazbu poplatku použitou v tomto výpočtu. Ve výchozím nastavení na Bitcoin Core je tato hodnota nastavena na 3 000 sats/kvB. Například pro výpočet limitu prachu pro vstup a výstup P2PKH, které mají velikost 148 a 34 bajtů, by výpočet byl:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

To znamená, že dotčený uzel nebude přeposílat transakce obsahující UTXO zabezpečené P2PKH, jehož hodnota je menší než 546 sats.