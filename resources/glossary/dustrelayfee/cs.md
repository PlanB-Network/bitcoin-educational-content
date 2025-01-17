---
term: DUSTRELAYFEE

---
Standardizační pravidlo, které uzly sítě používají k určení toho, co považují za "hranici prašnosti" Tento parametr nastavuje sazbu poplatků v satech za virtuální kilobajt (saty/kvB), která slouží jako referenční hodnota pro výpočet, zda je hodnota UTXO nižší než poplatky nutné k jeho zahrnutí do transakce. UTXO je totiž v Bitcoinu považováno za "prach", pokud k převodu vyžaduje více poplatků, než je hodnota, kterou samo představuje. Výpočet tohoto limitu je následující:

```text
limit = (input size + output size) * fee rate
```

Protože se požadovaná sazba poplatku za transakci, která má být zahrnuta do bloku Bitcoinu, neustále mění, parametr `DustRelayFee` umožňuje každému uzlu definovat sazbu poplatku použitou při tomto výpočtu. Ve výchozím nastavení je v jádře bitcoinu tato hodnota nastavena na 3 000 sátů/kvB. Například pro výpočet limitu prachu pro vstup P2PKH a výstup, které měří 148 a 34 bajtů, by výpočet vypadal takto:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

To znamená, že dotyčný uzel nebude předávat transakce včetně zabezpečeného UTXO P2PKH, jehož hodnota je nižší než 546 sats.