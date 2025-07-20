---
term: TRANSAKCJA (TX)
---

W kontekście Bitcoin, transakcja (w skrócie "TX") jest operacją zarejestrowaną na Blockchain, która przenosi Ownership bitcoinów z jednego lub więcej wejść do jednego lub więcej wyjść. Każda transakcja zużywa niewydane wyjścia transakcji (UTXO) jako wejścia, które są wyjściami z poprzednich transakcji, i tworzy nowe UTXO jako wyjścia, które mogą być wykorzystane jako wejścia w przyszłych transakcjach.


Każde wejście zawiera odniesienie do istniejącego wyjścia wraz ze skryptem podpisu (`scriptSig`), który spełnia warunki wydawania (`scriptPubKey`) ustalone przez wyjście, do którego się odwołuje. To właśnie pozwala na odblokowanie bitcoinów. Wyjścia definiują nowe warunki wydawania (`scriptPubKey`) dla transferowanych bitcoinów, często w formie klucza publicznego lub Address, z którym bitcoiny są teraz powiązane.