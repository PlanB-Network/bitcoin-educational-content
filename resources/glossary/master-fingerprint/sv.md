---
term: Master fingerprint
definition: 4-byte fingeravtryck som identifierar en HD-plånbok, härlett från masternyckeln.
---

Ett fingeravtryck på 4 byte (32 bitar) av den privata huvudnyckeln i en hierarkisk deterministisk (HD) Wallet. Det erhålls genom att beräkna `SHA256` Hash för den privata huvudnyckeln, följt av en `RIPEMD160` Hash, en process som kallas `HASH160` på Bitcoin. Masterfingeravtrycket används för att identifiera en HD Wallet, oberoende av härledningsvägarna, men med hänsyn tagen till förekomsten eller frånvaron av en passphrase. Det är kortfattad information som gör det möjligt att hänvisa till ursprunget för en uppsättning nycklar utan att avslöja känslig information om Wallet.