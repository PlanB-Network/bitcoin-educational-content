---
term: LIBSECP256K1
---

Wysokowydajna i bezpieczna biblioteka C dla podpisów cyfrowych i innych prymitywów kryptograficznych na krzywej eliptycznej `secp256k1`. Ponieważ krzywa ta nigdy nie była szeroko używana poza Bitcoin (w przeciwieństwie do często preferowanej krzywej `secp256r1`), biblioteka ta ma być najbardziej wszechstronnym odniesieniem do jej użycia. Rozwój libsecp256k1 był przede wszystkim ukierunkowany na potrzeby Bitcoin, a funkcje przeznaczone dla innych aplikacji mogą być mniej przetestowane lub zweryfikowane. Odpowiednie wykorzystanie tej biblioteki wymaga starannej uwagi, aby zapewnić, że jest ona odpowiednia do konkretnych celów aplikacji innych niż Bitcoin.


Biblioteka libsecp256k1 oferuje szereg funkcji, w tym:




- Podpis i weryfikacja ECDSA-secp256k1 oraz generowanie kluczy kryptograficznych ;
- Operacje addytywne i multiplikatywne na kluczach tajnych i publicznych ;
- Serializacja i analiza kluczy tajnych, publicznych i podpisów ;
- Podpisywanie i generowanie kluczy publicznych w stałym czasie ze stałym dostępem do pamięci;
- I wiele innych prymitywów kryptograficznych.