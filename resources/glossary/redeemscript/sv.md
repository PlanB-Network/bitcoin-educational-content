---
term: Redeemscript
definition: Skript som definierar utgiftsvillkoren för en P2SH UTXO, avslöjad vid utgiftstillfället.
---

Ett skript som definierar de specifika villkor som ingångar måste uppfylla för att låsa upp de medel som är associerade med en P2SH-utgång. I en P2SH UTXO innehåller `scriptPubKey` Hash för `redeemscript`. När en transaktion vill spendera denna UTXO som en input, måste den tillhandahålla den tydliga `redeemscript` som matchar Hash i `scriptPubKey`. `redeemscript` ges således i `scriptSig` för inmatningen, tillsammans med andra Elements som är nödvändiga för att uppfylla skriptets villkor, t.ex. signaturer eller publika nycklar. Denna inkapslade struktur säkerställer att detaljerna i utgiftsvillkoren förblir dolda tills bitcoins faktiskt spenderas. Den används framför allt för Legacy P2SH-plånböcker med flera signaturer.