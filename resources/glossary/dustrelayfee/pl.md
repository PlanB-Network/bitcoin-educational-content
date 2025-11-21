---
term: DUSTRELAYFEE
---

Reguła standaryzacji używana przez węzły sieci do określenia tego, co uważają za "limit Dust" Ten parametr określa stawkę opłaty w Sats za wirtualny kilobajt (Sats/kvB), która służy jako odniesienie do obliczania, czy wartość UTXO jest mniejsza niż opłaty niezbędne do włączenia go do transakcji. Rzeczywiście, UTXO jest uważany za "Dust" na Bitcoin, jeśli wymaga więcej opłat do przeniesienia niż wartość, którą sam reprezentuje. Obliczenie tego limitu jest następujące:


```text
limit = (input size + output size) * fee rate
```


Ponieważ wymagana stawka opłaty za transakcję, która ma zostać uwzględniona w bloku Bitcoin, stale się zmienia, parametr `DustRelayFee` pozwala każdemu węzłowi zdefiniować stawkę opłaty używaną w tych obliczeniach. Domyślnie, na Bitcoin Core, wartość ta jest ustawiona na 3,000 Sats/kvB. Na przykład, aby obliczyć limit Dust dla wejścia i wyjścia P2PKH, które mierzą odpowiednio 148 i 34 bajty, obliczenia byłyby następujące:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


Oznacza to, że dany węzeł nie będzie przekazywał transakcji zawierających P2PKH zabezpieczony UTXO, którego wartość jest mniejsza niż 546 Sats.