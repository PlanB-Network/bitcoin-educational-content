---
term: TRANSAKCJA NIEPRZETWORZONA
---

Transakcja Bitcoin, która jest zbudowana i podpisana, istniejąca w formie binarnej. Surowa transakcja (*raw TX*) jest ostateczną reprezentacją transakcji, tuż przed jej emisją w sieci. Transakcja ta zawiera wszystkie informacje niezbędne do włączenia jej do bloku:


- Wersja;
- Flaga;
- Dane wejściowe;
- Wyniki;
- Czas blokady;
- Świadek.


To, co jest określane jako "*surowa transakcja*", reprezentuje surowe dane, które są dwukrotnie przekazywane przez funkcję SHA256 Hash do generate transakcji txid. Dane te są następnie wykorzystywane w Merkle Tree bloku w celu zintegrowania transakcji z Blockchain.


> koncepcja ta jest również czasami nazywana "serializowaną transakcją". W języku francuskim terminy te można przetłumaczyć odpowiednio jako "transaction brute" i "transaction sérialisée"