---
term: HMAC-SHA512
---

`HMAC-SHA512` to skrót od "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Jest to algorytm kryptograficzny używany do weryfikacji integralności i autentyczności wiadomości wymienianych między dwiema stronami. Łączy on kryptograficzną funkcję Hash `SHA512` ze współdzielonym tajnym kluczem do generate unikalnego kodu uwierzytelniania wiadomości (MAC) dla każdej wiadomości.


W kontekście Bitcoin, naturalne użycie `HMAC-SHA512` jest nieco pochodne. Algorytm ten jest wykorzystywany w deterministycznym i hierarchicznym procesie wyprowadzania drzewa kluczy kryptograficznych Wallet. algorytm `HMAC-SHA512` jest w szczególności używany do przejścia od seed do klucza głównego, a następnie dla każdej derywacji od pary nadrzędnej do par podrzędnych. Algorytm ten znajduje się również w innym algorytmie derywacji o nazwie `PBKDF2`, używanym do przejścia od frazy odzyskiwania i passphrase do seed.