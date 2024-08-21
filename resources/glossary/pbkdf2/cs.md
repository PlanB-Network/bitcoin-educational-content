---
term: PBKDF2
---

`PBKDF2` je zkratka pro *Password-Based Key Derivation Function 2* (Funkce pro odvození klíče založená na heslu 2). Jedná se o metodu vytváření kryptografických klíčů z hesla pomocí odvozovací funkce. Jako vstup bere heslo, kryptografickou sůl a iterativně aplikuje předem určenou funkci (často hashovací funkci jako `SHA256` nebo `HMAC`) na tato data. Tento proces je opakován mnohokrát, aby se vygeneroval kryptografický klíč.

V kontextu Bitcoinu se `PBKDF2` používá ve spojení s funkcí `HMAC-SHA512` k vytvoření seedu deterministické a hierarchické peněženky (seed) z obnovovací fráze o 12 nebo 24 slovech. Kryptografická sůl použitá v tomto případě je heslo BIP39 a počet iterací je `2048`.