---
term: ŚWIADEK TRANSAKCJI
---

Odnosi się do składnika transakcji Bitcoin, który został przeniesiony wraz z SegWit Soft Fork do Address w kwestii podatności transakcji. Świadek zawiera podpisy i klucze publiczne niezbędne do odblokowania bitcoinów wydanych w transakcji. W starszych transakcjach świadek reprezentował sumę `scriptSig` ze wszystkich danych wejściowych. W transakcjach SegWit świadek reprezentuje sumę `scriptWitness` dla każdego wejścia, a ta część transakcji jest teraz przenoszona do oddzielnego Merkle Tree w bloku.


Przed SegWit podpisy mogły być nieznacznie zmieniane bez unieważnienia przed potwierdzeniem transakcji, co zmieniało identyfikator transakcji. Utrudniało to tworzenie różnych protokołów, ponieważ niepotwierdzona transakcja mogła zobaczyć zmianę swojego identyfikatora. Oddzielając świadków, SegWit sprawia, że transakcje są nieciągliwe, ponieważ wszelkie zmiany w podpisach nie wpływają już na identyfikator transakcji (txid), a jedynie na identyfikator świadka (WTXID). Oprócz rozwiązania problemu podatności na zmiany, separacja ta pozwala na zwiększenie pojemności każdego bloku.


> w języku angielskim "témoin" jest tłumaczone jako "świadek"