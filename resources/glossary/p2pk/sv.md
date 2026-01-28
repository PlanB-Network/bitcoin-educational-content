---
term: P2PK
definition: Skript som låser bitcoin direkt till en publik nyckel utan hashning.
---

P2PK står för *Pay to Public Key* (betala till offentlig nyckel). Det är en standardskriptmodell som används på Bitcoin för att fastställa utgiftsvillkor på en UTXO. Det gör det möjligt att låsa bitcoins direkt på en publik nyckel, snarare än en Address.

Tekniskt sett innehåller P2PK-skriptet en offentlig nyckel och en instruktion som kräver en motsvarande digital signatur för att låsa upp pengarna. När ägaren vill spendera bitcoins måste de tillhandahålla en signatur som produceras med den tillhörande privata nyckeln. Signaturen verifieras med hjälp av ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK användes ofta i de tidiga versionerna av Bitcoin, framför allt av Satoshi Nakamoto. Det används nästan inte längre idag.