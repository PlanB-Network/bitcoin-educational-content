---
term: ROZWÓJ
---

Odnosi się do procesu generowania par kluczy podrzędnych z pary kluczy nadrzędnych (klucz prywatny i klucz publiczny) oraz kodu łańcuchowego w ramach deterministycznego i hierarchicznego (HD) Wallet. Proces ten pozwala na segmentację gałęzi i organizację Wallet na różnych poziomach z licznymi parami kluczy podrzędnych, które można odzyskać, znając tylko podstawowe informacje o odzyskiwaniu (fraza Mnemonic i wszelkie potencjalne passphrase). Aby wyprowadzić klucz potomny, używana jest funkcja `HMAC-SHA512` z kodem łańcucha nadrzędnego i konkatenacją klucza nadrzędnego i 32-bitowego indeksu. Istnieją dwa rodzaje pochodnych:


- Normalna derywacja, która wykorzystuje macierzysty klucz publiczny jako podstawę funkcji `HMAC-SHA512`;
- Wzmocniona derywacja, która wykorzystuje macierzysty klucz prywatny jako podstawę funkcji `HMAC-SHA512`;


Wynik HMAC-SHA512 jest dzielony na dwie części: pierwsze 256 bitów staje się kluczem podrzędnym (prywatnym lub publicznym po przetworzeniu przez ECDSA), a pozostałe 256 bitów staje się kodem łańcucha podrzędnego.