---
term: Klucz główny
definition: Klucz prywatny wyprowadzony z seeda, służący jako punkt wyjścia dla wszystkich kluczy w portfelu HD.
---

W kontekście portfeli HD (Hierarchical Deterministic) główny klucz prywatny jest unikalnym kluczem prywatnym pochodzącym z Wallet seed. Aby uzyskać klucz główny, funkcja `HMAC-SHA512` jest stosowana do seed, używając słów "*Bitcoin seed*" dosłownie jako klucza. Wynikiem tej operacji jest 512-bitowy wynik, przy czym pierwsze 256 bitów stanowi klucz główny, a pozostałe 256 bitów tworzy kod łańcucha głównego. Klucz główny i kod łańcucha głównego służą jako punkt wyjścia do wyprowadzenia wszystkich podrzędnych kluczy prywatnych i publicznych w strukturze drzewa HD Wallet. Dlatego główny klucz prywatny znajduje się na głębokości 0 wyprowadzania.


