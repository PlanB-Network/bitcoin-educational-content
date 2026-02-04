---
term: P2SH
definition: Skript som tillåter godtyckliga utgiftsvillkor via hashen av ett redeemScript.
---

P2SH står för *Pay to Script Hash*. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO. Till skillnad från P2PK- och P2PKH-skript, där utgiftsvillkoren är fördefinierade, gör P2SH det möjligt att integrera godtyckliga utgiftsvillkor och ytterligare funktioner i ett transaktionsskript.


Tekniskt sett innehåller `scriptPubKey` i en P2SH-transaktion den kryptografiska Hash för en `redeemscript`, snarare än uttryckliga utgiftsvillkor. Denna Hash erhålls med hjälp av en `SHA256` Hash. När bitcoins skickas till en P2SH Address avslöjas inte den underliggande `redeemscript`. Endast dess Hash ingår i transaktionen. P2SH-adresser är kodade i `Base58Check` och börjar med siffran `3`. När mottagaren vill spendera de mottagna bitcoins måste de tillhandahålla en `redeemscript` som matchar den Hash som finns i `scriptPubKey`, tillsammans med nödvändiga data för att uppfylla villkoren för denna `redeemscript`. I ett P2SH-skript med flera signaturer kan skriptet t.ex. kräva signaturer från flera privata nycklar.


Användningen av P2SH ger större flexibilitet, eftersom det gör det möjligt att skapa godtyckliga skript utan att avsändaren känner till detaljerna. P2SH introducerades 2012 med BIP16.