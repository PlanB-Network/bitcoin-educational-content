---
term: PBKDF2
---

pBKDF2 to skrót od *Password-Based Key Derivation Function 2*. Jest to metoda tworzenia kluczy kryptograficznych z hasła przy użyciu funkcji derywacyjnej. Przyjmuje jako dane wejściowe hasło, sól kryptograficzną i iteracyjnie stosuje z góry określoną funkcję (często funkcję Hash, taką jak `SHA256` lub `HMAC`) do tych danych. Proces ten jest powtarzany wiele razy do generate klucza kryptograficznego.


W kontekście Bitcoin, `PBKDF2` jest używany w połączeniu z funkcją `HMAC-SHA512` w celu utworzenia seed deterministycznego i hierarchicznego Wallet (seed) z frazy odzyskiwania składającej się z 12 lub 24 słów. Sól kryptograficzna użyta w tym przypadku to BIP39 passphrase, a liczba iteracji to `2048`.