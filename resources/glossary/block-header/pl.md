---
term: GŁOWICA BLOKU
---

Nagłówek bloku jest strukturą danych, która służy jako główny element w konstrukcji bloku Bitcoin. Każdy blok składa się z nagłówka i listy transakcji. Nagłówek bloku zawiera kluczowe informacje, które zapewniają integralność i ważność bloku w Blockchain. Nagłówek bloku zawiera 80 bajtów metadanych i składa się z następujących elementów Elements:


- Wersja blokowa;
- Hash poprzedniego bloku;
- Korzeń Merkle Tree transakcji;
- Blok Timestamp;
- Docelowy poziom trudności;
- Nonce.


Na przykład, oto nagłówek bloku numer 785,530 w formacie szesnastkowym, wydobytego przez Foundry USA 15 kwietnia 2023 roku:


```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```


Jeśli rozbijemy ten nagłówek, możemy rozpoznać:


- Wersja:


```text
00e0ff3f
```



- Poprzedni Hash:


```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```



- Merkle Root:


```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```



- Timestamp:


```text
bcb13a64
```



- Cel:


```text
b2e00517
```



- Nonce:


```text
43f09a40
```


Aby blok był ważny, musi mieć nagłówek, który po zaszyfrowaniu za pomocą `SHA256d` daje Hash, który jest mniejszy lub równy docelowemu poziomowi trudności.


> w języku angielskim jest on określany jako "Block Header"