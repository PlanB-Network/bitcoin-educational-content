---
term: PBKDF2

---
`PBKDF2` znamená *Password-Based Key Derivation Function 2*. Jedná se o metodu vytváření kryptografických klíčů z hesla pomocí derivační funkce. Jako vstup přijímá heslo, kryptografickou sůl a na tato data iterativně aplikuje předem určenou funkci (často hashovací funkci jako `SHA256` nebo `HMAC`). Tento proces se mnohokrát opakuje, aby se vygeneroval kryptografický klíč.

V kontextu Bitcoinu se `PBKDF2` používá ve spojení s funkcí `HMAC-SHA512` k vytvoření semínka deterministické a hierarchické peněženky (seed) z obnovovací fráze o 12 nebo 24 slovech. Kryptografickou solí použitou v tomto případě je heslová fráze BIP39 a počet iterací je `2048`.