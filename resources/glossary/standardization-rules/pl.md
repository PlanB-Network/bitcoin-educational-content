---
term: ZASADY STANDARYZACJI
---

Reguły standaryzacji są indywidualnie przyjmowane przez każdy węzeł Bitcoin, oprócz reguł konsensusu, w celu zdefiniowania struktury niepotwierdzonych transakcji, które akceptuje do swojego Mempool i transmituje do swoich rówieśników. Zasady te są zatem konfigurowane i wykonywane lokalnie przez każdy węzeł i mogą się różnić w zależności od węzła. Mają one zastosowanie wyłącznie do niepotwierdzonych transakcji. Dlatego węzeł zaakceptuje transakcję, którą uzna za niestandardową, tylko wtedy, gdy jest już zawarta w ważnym bloku.


Należy zauważyć, że większość węzłów pozostawia domyślne konfiguracje ustalone w Bitcoin Core, tworząc w ten sposób jednolitość zasad standaryzacji w całej sieci. Transakcja, która, choć zgodna z zasadami konsensusu, nie przestrzega tych zasad standaryzacji, będzie miała trudności z rozgłaszaniem w całej sieci. Nadal jednak może zostać uwzględniona w ważnym bloku, jeśli dotrze do Miner. W praktyce transakcje te, określane jako "niestandardowe", są często przesyłane bezpośrednio do Miner za pośrednictwem zewnętrznych środków poza siecią peer-to-peer Bitcoin. Jest to często jedyny sposób na potwierdzenie tego typu transakcji.


Na przykład transakcja, która nie przydziela żadnych opłat, jest zarówno ważna zgodnie z zasadami konsensusu, jak i niestandardowa, ponieważ domyślna polityka Bitcoin Core dla parametru `minRelayTxFee` wynosi `0,00001` (w BTC/kB).


> termin "zasady Mempool" jest również czasami używany w odniesieniu do zasad standaryzacji