---
term: VIN
---

Określony element transakcji Bitcoin, który określa źródło funduszy wykorzystanych do zaspokojenia wyjść. Każdy `vin` odnosi się do niewydanych środków (UTXO) z poprzedniej transakcji. Transakcja może zawierać wiele wejść, każde identyfikowane przez kombinację `txid` (identyfikator oryginalnej transakcji) i `vout` (indeks wyjścia w tej transakcji).


Każdy `vin` zawiera następujące informacje:


- `txid`: identyfikator poprzedniej transakcji zawierającej dane wyjściowe użyte tutaj jako dane wejściowe;
- `vout`: indeks wyjścia w poprzedniej transakcji;
- `scriptSig` lub `scriptWitness`: skrypt odblokowujący, który dostarcza dane niezbędne do spełnienia warunków określonych przez `scriptPubKey` poprzedniej transakcji, której środki są wydawane, zazwyczaj poprzez dostarczenie podpisu kryptograficznego;
- `nSequence`: specyficzne pole używane do wskazania, w jaki sposób to wejście jest blokowane czasowo, a także innych opcji, takich jak RBF.