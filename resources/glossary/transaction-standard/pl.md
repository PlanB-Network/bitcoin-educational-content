---
term: STANDARD TRANSAKCJI
---

Transakcja Bitcoin, która oprócz przestrzegania zasad konsensusu, podlega również zasadom standaryzacji ustawionym domyślnie na węzłach Bitcoin Core. Te zasady standaryzacji są narzucane indywidualnie przez każdy węzeł Bitcoin, oprócz zasad konsensusu, w celu zdefiniowania struktury niepotwierdzonych transakcji, które akceptuje w swoim Mempool i transmituje do swoich rówieśników.


Reguły te są zatem konfigurowane i wykonywane lokalnie przez każdy węzeł i mogą się różnić w zależności od węzła. Mają one zastosowanie wyłącznie do niepotwierdzonych transakcji. Dlatego węzeł zaakceptuje transakcję, którą uzna za niestandardową, tylko wtedy, gdy jest już zawarta w ważnym bloku.


Należy zauważyć, że większość węzłów pozostawia domyślne konfiguracje ustalone w Bitcoin Core, tworząc w ten sposób jednolitość zasad standaryzacji w całej sieci. Transakcja, która, choć zgodna z zasadami konsensusu, nie przestrzega tych zasad standaryzacji, będzie miała trudności z propagacją w sieci. Nadal jednak może zostać włączona do ważnego bloku, jeśli dotrze do Miner. W praktyce transakcje te, zakwalifikowane jako niestandardowe, są często przesyłane bezpośrednio do Miner za pośrednictwem zewnętrznych środków do sieci peer-to-peer Bitcoin. Jest to często jedyny sposób na potwierdzenie takiej transakcji. Na przykład transakcja, która nie przydziela żadnych opłat, jest zarówno ważna zgodnie z zasadami konsensusu, jak i niestandardowa, ponieważ domyślna polityka Bitcoin Core dla parametru `minRelayTxFee` wynosi `0,00001` (w BTC/kB).