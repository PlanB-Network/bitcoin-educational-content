---
term: P2PKH
definition: Skript som låser bitcoin till hashen av en publik nyckel, adresser börjar på 1.
---

P2PKH står för *Pay to Public Key Hash*. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor på en UTXO. Det gör det möjligt att låsa bitcoins på en Hash av en publik nyckel, det vill säga på en mottagande Address. Detta skript är associerat med Legacy-standarden och introducerades i de tidiga versionerna av Bitcoin av Satoshi Nakamoto.


Till skillnad från P2PK, där den publika nyckeln uttryckligen ingår i skriptet, använder P2PKH ett kryptografiskt fingeravtryck av den publika nyckeln. Detta skript innehåller `RIPEMD160` Hash av `SHA256` för den publika nyckeln och föreskriver att mottagaren, för att få tillgång till pengarna, måste tillhandahålla en publik nyckel som matchar denna Hash, samt en giltig digital signatur som genererats från den tillhörande privata nyckeln. P2PKH-adresser kodas med hjälp av formatet `Base58Check`, vilket ger dem robusthet mot typografiska fel genom användning av en kontrollsumma. Dessa adresser börjar alltid med siffran "1".