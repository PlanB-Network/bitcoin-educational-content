---
term: Schnorr-protokoll
definition: Elektronisk signaturalgoritm på elliptiska kurvor, implementerad på Bitcoin sedan Taproot.
---

Schnorr-protokollet är en elektronisk signaturalgoritm baserad på elliptisk kurvkryptografi (ECC). Det används i Bitcoin för att härleda en publik nyckel från en privat nyckel och för att signera en transaktion med en privat nyckel. I Bitcoin, precis som ECDSA, baseras Schnorr på användningen av den elliptiska kurvan `secp256k1`, som kännetecknas av ekvationen: $y^2 = x^3 + 7$. Schnorr-signaturprotokollet har implementerats i Bitcoin-protokollet sedan november 2021 med aktiveringen av Taproot-uppdateringen.